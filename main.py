import os
import requests
from forex_python.converter import CurrencyRates
import urllib
import datetime
import csv
import generate_graph

# Define the Alpha Vantage API URL
ALPHAVANTAGE_API_URL = "https://www.alphavantage.co/query"

# Function to fetch the stock price
def fetch_stock_price():
    # Replace YOUR_API_KEY with your actual API key
    api_key = "4TRT8KNTAO3IEB5H"
    stock_symbol = "TSE"

    # Set up the API request parameters
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock_symbol,
        "apikey": api_key
    }

    # Generate the URL with the request parameters
    url = f"{ALPHAVANTAGE_API_URL}?{urllib.parse.urlencode(params)}"

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

# Function to save the stock data to a CSV file
def save_stock_data_to_csv(time, usd_price, cny_price):
    file_name = "stock_data.csv"
    headers = ["Time", "Price in USD", "Price in CNY"]

    # Check if the CSV file exists
    file_exists = os.path.isfile(file_name)

    # Open the CSV file in append mode
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        # If the CSV file does not exist, write the headers
        if not file_exists:
            writer.writerow(headers)

        # Write the stock data
        writer.writerow([time, usd_price, cny_price])

def main():
    # Fetch the stock price and convert it to CNY
    stock_price_usd = fetch_stock_price()

    if stock_price_usd is not None:
        stock_price_cny = convert_usd_to_cny(stock_price_usd)

        print(f"Current price of TSE stock in USD: {stock_price_usd}")
        print(f"Current price of TSE stock in CNY: {stock_price_cny}")

        # Store the stock data to the CSV file
        current_time = datetime.datetime.now()
        save_stock_data_to_csv(current_time, stock_price_usd, stock_price_cny)
        
    


if __name__ == "__main__":
    main()
    generate_graph.main()

