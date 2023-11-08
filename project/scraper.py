# pylint: disable=missing-module-docstring

import requests
from project.config import KEY_API
from project.logger import logger

class Scraper:  # pylint: disable=missing-class-docstring

    def __init__(self):
        self.url = "https://api.spoonacular.com/recipes/random?number=20"
        self.headers = {
            "User-Agent":
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
            }
        self.params = {'apiKey' : KEY_API}

    def scrape_data(self):

        try:
            response = requests.get(url=self.url, params=self.params, headers=self.headers, timeout=10)
            if response.status_code == 200:
                logger.info(response.status_code)
                return response
            else:
                logger.info('API request failed with status code: %s',response.status_code)

        except requests.exceptions.RequestException as e:
            logger.error(e)
    
    def parse_response(self,response):
        try:
            data = response.json()
            return data
        except ValueError as e:
            data = None
            logger.error(e)
    