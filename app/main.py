import csv
import datetime
import os
import urllib.parse
from typing import Union

import requests
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates
from generate_graph import main as generate_graph_main

# Load the .env file
load_dotenv()

# Set constant values
ALPHAVANTAGE_API_URL = "https://www.alphavantage.co/query"
STOCK_SYMBOL: str = os.getenv("STOCK_SYMBOL", None)
API_KEY: str = os.getenv("API_KEY", None)
file_name: str = "stock_data.csv"

def fetch_stock_price(stock_symbol: str, api_key: str) -> Union[None, float]:
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock_symbol,
        "apikey": api_key,
    }
    url: str = f"{ALPHAVANTAGE_API_URL}?{urllib.parse.urlencode(params)}"

    response = requests.get(url)
    json_data = response.json()

    current_price = json_data.get("Global Quote", {}).get("05. price")

    if current_price is not None:
        return float(current_price)
    print(f"Unable to fetch the stock price. JSON data: {json_data}")
    return None

def convert_usd_to_cny(price: float) -> float:
    currency_rates = CurrencyRates()
    return currency_rates.convert("USD", "CNY", price)

def save_stock_data_to_csv(file_path: str, time: datetime.datetime, usd_price: float, cny_price: float):
    """
    This function saves the time, USD price and CNY price to a CSV file.
    """
    # Define CSV headers
    headers = ["Time", "Price in USD", "Price in CNY"]

    # Create directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Check if file exists and write data to the file
    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow([time, usd_price, cny_price])


def main():
    stock_price_usd: Union[None, float] = fetch_stock_price(stock_symbol=STOCK_SYMBOL, api_key=API_KEY)

    if stock_price_usd is not None:
        stock_price_cny: float = convert_usd_to_cny(price=stock_price_usd)
        print(f"Current price of TSE stock in USD: {stock_price_usd}")
        print(f"Current price of TSE stock in CNY: {stock_price_cny}")
        current_time = datetime.datetime.now()
        save_stock_data_to_csv(file_path=f"app/data/{file_name}", time=current_time, usd_price=stock_price_usd, cny_price=stock_price_cny)
        
        generate_graph_main(input_file='app/data/stock_data.csv',
                            output_file='app/data/stock_price_chart.png')

if __name__ == "__main__":
    main()
