# pylint: disable=missing-module-docstring

# database.py

import psycopg2
from project.config import *
from project.logger import logger

class Database:  # pylint: disable=missing-class-docstring

    def __init__(self):
        self.connection = None

    def connect(self):    # pylint: disable=missing-function-docstring
        try:
            self.connection = psycopg2.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                database=DB_NAME  
            )
            logger.info('Connection to PostgreSQL database successful!')
        except psycopg2.Error as e:
            logger.error(e)


    def store_data(self, data): # pylint: disable=missing-function-docstring
        
        if not self.connection:
            logger.info("Database conenction is not established")
            return
        #
        try:
            cursor = self.connection.cursor()
            for recipe in data['recipes']:
                recipe_id = recipe['id']
                recipe_name=recipe['title']
                ingredients = recipe['extendedIngredients']
                logger.info(ingredients)
                ### Transform data if needed

                #Check if any recipe with the same id already exists in the DB
                cursor.execute('select recipe_id from recipes where recipe_id = %s', (recipe_id,))
                existing_recipe = cursor.fetchone()

                #Srore recipe
                if not existing_recipe:
                    cursor.execute('INSERT INTO recipes (recipe_id,recipe_name) VALUES (%s,%s) RETURNING recipe_id', (recipe_id,recipe_name))

                #Check if ingredient with the same id already exists
                for ingredient in ingredients:
                    ingredient_id = ingredient['id']
                    ingredient_name = ingredient['name']
                    amount = ingredient['amount']
                    unit = ingredient['unit']
                    cursor.execute('select ingredient_id from ingredients where ingredient_id = %s', (ingredient_id,))
                    existing_ingredient = cursor.fetchone()
                    if not existing_ingredient:
                        cursor.execute('insert into ingredients (ingredient_id, ingredient_name) values (%s,%s)', (ingredient_id,ingredient_name))
                        cursor.execute('insert into recipe_ingredients (recipe_id,ingredient_id,amount,unit) values (%s,%s,%s,%s)', (recipe_id,ingredient_id,amount,unit))

            self.cleanup()

        except psycopg2.Error as e:
            self.cancel_transaction()
            logger.error(e)                        

    def cleanup(self): # pylint: disable=missing-function-docstring
        self.connection.commit()


    def cancel_transaction(self): # pylint: disable=missing-function-docstring
        self.connection.rollback()

    def close(self):   # pylint: disable=missing-function-docstring
        if self.connection:
            self.connection.close()
            logger.info("Connection closed")
