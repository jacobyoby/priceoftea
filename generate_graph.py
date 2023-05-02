import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os


def read_stock_data_from_csv(file_name: str):
    """
    This function reads stock data from a CSV file and returns a tuple containing the times, USD prices
    and CNY prices as three separate lists.
    """
    try:
        df = pd.read_csv(os.path.join(os.getcwd(), "data", file_name))
    except FileNotFoundError:
        print(f"{file_name} not found!")
        return [], [], []
    return [datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f") for t in df["Time"]], list(df["Price in USD"]), list(df["Price in CNY"])


def plot_stock_data(times: list, usd_prices: list, cny_prices: list):
    """
    This function generates a plot of the stock prices over time and saves it to a file.
    """
    file_path = os.path.join(os.getcwd(), "data", "stock_price_chart.png")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(times, usd_prices, label="Price in USD")
    ax.plot(times, cny_prices, label="Price in CNY")
    ax.set(title="T Stock Price",
           xlabel="Time",
           ylabel="Stock Price")
    ax.legend()
    ax.grid()
    fig.savefig(file_path)
    plt.close()


def main():
    """
    This is the main function that reads the stock data and plots a graph using the data.
    """
    times, usd_prices, cny_prices = read_stock_data_from_csv("stock_data.csv")
    if not all([times, usd_prices, cny_prices]):
        return
    plot_stock_data(times, usd_prices, cny_prices)


if __name__ == "__main__":
    main()
