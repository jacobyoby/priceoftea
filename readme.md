# Price of T(itanium) in China 🇨🇳

This Python application fetches the price of TSE (Taiwan Semiconductor Manufacturing Company Limited) stock in the US market, converts it to Chinese Yuan (CNY), and generates a line chart to visualize the stock price in both currencies over time. The application also stores the price data in a CSV file. 📈

![Fetch TSE Stock Price and Generate Chart](https://github.com/jacobyoby/priceoftea/actions/workflows/main.yml/badge.svg?branch=master)
![TSE Stock Price Chart](https://github.com/jacobyoby/priceoftea/blob/master/data/stock_price_chart.png?raw=true)

## Prerequisites

1. Register for an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
2. Install Python 3.x with pip.
3. Install required modules using `pip install -r requirements.txt`.

## Features

- Fetches current stock prices from the Alpha Vantage API for a given symbol.
- Converts the stock price from USD to Chinese Yuan (CNY).
- Saves the fetched data (time, price in USD, price in CNY) to a CSV file.
- Generates a line chart using the saved data to visualize the stock price in USD and CNY over time.

## Running the Application

### Using Python

1. Create a `.env` file in the same directory as the `main.py` file with the following contents:

   ```
   STOCK_SYMBOL={symbol}
   API_KEY={your-alphavantage-API-key}
   ```

   Replace `{symbol}` with the stock symbol you want to fetch the data for and `{your-alphavantage-API-key}` with your Alpha Vantage API key.

2. Run the script using `python main.py`.

The script will now fetch the data, store it in the CSV file, and generate a graph using the fetched data.

### Using Docker

1. Install Docker on your machine if you haven't already. You can download Docker from the official website: https://www.docker.com/get-started
2. Clone the application's repository or download the source code, ensuring the Dockerfile, Python script, and `.env` file are in the same directory.
3. Open a terminal or command prompt and navigate to the directory containing the Dockerfile.
4. Build the Docker image by running the following command:

   ```
   docker build -t jacobedurham/priceoftea-python .
   ```

5. After the build is successful, run the Docker container with the following command:

   ```
   docker run -p 8000:8000 jacobedurham/priceoftea-python
   ```

The application should now be running inside the Docker container, and you can interact with it through the exposed port 8000.