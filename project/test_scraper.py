# pylint: disable=missing-module-docstring

from scraper import Scraper
import unittest


class TestScraper(unittest.TestCase): # pylint: disable=missing-class-docstring
    def test_status_code(self):   # pylint: disable=missing-function-docstring

        scraper = Scraper()
        response = scraper.scrape_data()
        
        # check status_code
        self.assertEqual(response.status_code, 200)

    def test_response_format(self):   # pylint: disable=missing-function-docstring

        scraper = Scraper()
        response = scraper.scrape_data()

        # check if the response is in JSON format
        content_type = response.headers.get("Content-Type")
        self.assertTrue(content_type and "application/json" in content_type)

        # check if the response is not empty
        data = scraper.parse_response(response)
        self.assertIsNotNone(data)



if __name__ == '__main__':
    unittest.main()
