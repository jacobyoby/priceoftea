import csv
import os
import datetime
import urllib.parse
from typing import Union

import requests
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates
from generate_graph import main as generate_graph_main


# Load the .env file
load_dotenv()

ALPHAVANTAGE_API_URL = "https://www.alphavantage.co/query"
STOCK_SYMBOL: str = os.getenv("STOCK_SYMBOL", None)
API_KEY: str = os.getenv("API_KEY", None)

file_name: str = "stock_data.csv"


def fetch_stock_price() -> Union[None, float]:
    """
    This function fetches the current stock price for a given symbol and returns it as a float.
    """
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": STOCK_SYMBOL,
        "apikey": API_KEY,
    }
    
    print(f"API_KEY: {API_KEY}")
    print(f"STOCK_SYMBOL: {STOCK_SYMBOL}")
    url: str = f"{ALPHAVANTAGE_API_URL}?{urllib.parse.urlencode(params)}"
    response = requests.get(url)
    json_data = response.json()
    current_price = json_data.get("Global Quote", {}).get("05. price")
    if current_price is not None:
        return float(current_price)
    print(f"Unable to fetch the stock price. JSON data: {json_data}")
    return None


def convert_usd_to_cny(usd_amount: float) -> float:
    """
    This function converts an amount in USD to CNY and returns it as a float.
    """
    currency_rates = CurrencyRates()
    return currency_rates.convert("USD", "CNY", usd_amount)


def save_stock_data_to_csv(time: datetime.datetime, usd_price: float, cny_price: float):
    """
    This function saves the time, USD price and CNY price to a CSV file.
    """
    headers = ["Time", "Price in USD", "Price in CNY"]
    file_path: str = f"app/data/{file_name}"
    if not os.path.exists("app/data"):
        os.makedirs("app/data")
    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow([time, usd_price, cny_price])


def main():
    """
    This is the main function that fetches the stock price, converts it to CNY, saves it to a CSV file
    and generates a graph using the saved data.
    """
    stock_price_usd: Union[None, float] = fetch_stock_price()
    if stock_price_usd is not None:
        stock_price_cny: float = convert_usd_to_cny(stock_price_usd)
        print(f"Current price of TSE stock in USD: {stock_price_usd}")
        print(f"Current price of TSE stock in CNY: {stock_price_cny}")
        current_time = datetime.datetime.now()
        save_stock_data_to_csv(current_time, stock_price_usd, stock_price_cny)
        generate_graph_main(input_file='app/data/stock_data.csv', output_file='app/data/stock_price_chart.png')



if __name__ == "__main__":
    main()
