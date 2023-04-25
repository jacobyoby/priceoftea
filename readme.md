# The Price of T(itanium) in China 🇨🇳

This Python script fetches the price of Titanium in the US stock market and converts it to Chinese Yuan (CNY). It generates a CSV file to store the price data and creates a line chart to visualize the stock price in USD and CNY over time. 📈

[![Fetch Titanium Stock Price and Generate Chart](https://github.com/jacobyoby/priceoftea/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/jacobyoby/priceoftea/actions/workflows/main.yml)

![Titanium Stock Price Chart](https://github.com/jacobyoby/priceoftea/blob/master/stock_price_chart.png?raw=true)


## Features

- 🪙 Fetch the current price of Titanium in the US stock market
- 💱 Convert the price to Chinese Yuan (CNY) using real-time exchange rates
- 📊 Generate a line chart to visualize the stock price in USD and CNY over time
- 📝 Store the time, price in USD, and price in CNY in a CSV file

## Prerequisites

Before running the script, make sure you have the following Python packages installed:

- `requests`: To make API calls
- `matplotlib`: To create the line chart

You can install them using the following command:

```bash
pip install requests matplotlib
```

## Usage

1. First, run `main.py` to fetch the current price of Titanium in the US stock market and convert it to Chinese Yuan (CNY). The script will store the time, price in USD, and price in CNY in a CSV file named `stock_data.csv`.

```bash
python main.py
```

2. Next, run `generate_graph.py` to create a line chart using the data from `stock_data.csv` and save the chart as a PNG image named `stock_price_chart.png`.

```bash
python generate_graph.py
```

## Notes

- 🌐 The script uses the Alpha Vantage API to fetch stock prices and exchange rates. You'll need to obtain an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and set it as an environment variable named `ALPHAVANTAGE_API_KEY` before running the script.

- ⏲️ The data is fetched and stored in real-time. To track the stock price over time, you can set up a scheduled job (e.g., using cron or Task Scheduler) to run the script periodically.

- 🎨 Customize the line chart's appearance by modifying the `plot_stock_data` function in `generate_graph.py`.

## License

This project is licensed under the MIT License.
