import os
import requests
from forex_python.converter import CurrencyRates
import urllib

# Define the Alpha Vantage API URL
ALPHAVANTAGE_API_URL = "https://www.alphavantage.co/query"

# Function to fetch the stock price
def fetch_stock_price():
    # Replace YOUR_API_KEY with your actual API key
    api_key = "4TRT8KNTAO3IEB5H"
    stock_symbol = "ibm"

    # Set up the API request parameters
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock_symbol,
        "apikey": api_key
    }

    # Generate the URL with the request parameters
    url = f"{ALPHAVANTAGE_API_URL}?{urllib.parse.urlencode(params)}"
    print(url)

    # Send a request to the API
    response = requests.get(url)
    json_data = response.json()

    try:
        current_price = json_data["Global Quote"]["05. price"]
        return float(current_price)
    except KeyError:
        print(f"Unable to fetch the stock price. JSON data: {json_data}")
        return None

# Function to convert USD to CNY
def convert_usd_to_cny(usd_amount):
    currency_rates = CurrencyRates()
    return currency_rates.convert("USD", "CNY", usd_amount)

def main():
    # Fetch the stock price and convert it to CNY
    stock_price = fetch_stock_price()
    if stock_price is not None:
        stock_price_cny = convert_usd_to_cny(stock_price)
        print(f"Current price of IBM stock in USD: {stock_price}")
        print(f"Current price of IBM stock in CNY: {stock_price_cny}")

if __name__ == "__main__":
    main()
