# main.py

from scraper import Scraper
from database import Database


def main():
    """
    main function
    """
    #Initialize the scraper
    scraper = Scraper()

    #Get the data
    response = scraper.scrape_data()
    
    data = scraper.parse_response(response)

    #Connect to the database
    db = Database()
    db.connect()

    #Store the data
    db.store_data(data)

    #Close connection
    db.close()


if __name__ == "__main__":
    main()
