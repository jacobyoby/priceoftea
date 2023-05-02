# The Price of T(itanium) in China 🇨🇳 

This Python script fetches the price of TSE (Taiwan Semiconductor Manufacturing Company Limited) stock in the US market and converts it to Chinese Yuan (CNY). It generates a CSV file to store the price data and creates a line chart to visualize the stock price in USD and CNY over time. 📈  

[![Fetch TSE Stock Price and Generate Chart](https://github.com/jacobyoby/priceoftea/actions/workflows/main.yml/badge.svg?branch=master)][def]  
![TSE Stock Price Chart](https://github.com/jacobyoby/priceoftea/blob/master/data/stock_price_chart.png?raw=true)  

## Prerequisites
1. Register for an API key from [alphavantage](https://www.alphavantage.co/support/#api-key)
2. Install Python 3.x with pip.
3. Install required modules using `pip install -r requirements.txt`.

## Features:
- Fetches current stock prices from Alphavantage API for a given symbol.
- Converts the stock price from USD to Chinese Yuan (CNY).
- Saves the fetched data (time, price in USD, price in CNY) to a CSV file.
- Generates a line chart using the saved data to visualize the stock price in USD and CNY over time.

## Running the script

1. Create `.env` file in the same directory as main.py file with the following contents: 
	```
	STOCK_SYMBOL={symbol}
	API_KEY={your-alphavantage-API-key}
	``` 
	where `{symbol}` is the stock symbol you want to fetch the data for.
2. Run the script using `python main.py`

That's it! The script will now fetch the data and generate a graph using the fetched data stored in the CSV file.
