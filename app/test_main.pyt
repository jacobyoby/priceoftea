import unittest
import os
import tempfile
from dotenv import load_dotenv
from main import fetch_stock_price, convert_usd_to_cny, save_stock_data_to_csv
from unittest.mock import patch

class TestStockPrice(unittest.TestCase):
    """
    This class contains unit tests to test the fetch_stock_price(), 
    convert_usd_to_cny() and save_stock_data_to_csv() functions 
    in the main module.
    """

    def setUp(self):
        # Mock the STOCK_SYMBOL and API_KEY environment variables
        os.environ["STOCK_SYMBOL"] = "Test Symbol"
        os.environ["API_KEY"] = "Test Key"
        # Load the .env file
        load_dotenv()

    def tearDown(self):
        # Delete the mocked environment variables
        del os.environ["STOCK_SYMBOL"]
        del os.environ["API_KEY"]

    @patch("requests.get")
    def test_fetch_stock_price(self, mock_get):
        # Mock the API response
        mock_get.return_value.json.return_value = {
            "Global Quote": {
                "05. price": "123.45"
            }
        }
        self.assertIsInstance(fetch_stock_price(stock_symbol="Test Symbol", api_key="Test Key"), (int, float))

    def test_convert_usd_to_cny(self):
        self.assertIsInstance(convert_usd_to_cny(price=100.0), float)

    def test_save_stock_data_to_csv(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            save_stock_data_to_csv(file_path=temp_file.name, time="Test Time", usd_price=1.0, cny_price=2.0)
            self.assertTrue(os.path.isfile(temp_file.name))
        # Clean up the temporary file
        os.remove(temp_file.name)



if __name__ == "__main__":
    unittest.main()
