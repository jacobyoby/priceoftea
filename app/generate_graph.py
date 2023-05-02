import pandas as pd
import datetime
import matplotlib.pyplot as plt
from typing import List, Tuple
import os


def read_stock_data_from_csv(file_path: str) -> Tuple[List[datetime.datetime], List[float], List[float]]:
    """
    This function reads stock data from a CSV file and returns a tuple containing the times, USD prices
    and CNY prices as three separate lists.
    """
    try:
        df = pd.read_csv(file_path)
        if not {"Time", "Price in USD", "Price in CNY"}.issubset(set(df.columns)):
            raise ValueError("Invalid input file format!")
    except (FileNotFoundError, ValueError) as e:
        print(f"{e}")
        return [], [], []

    times = [datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f") for t in df["Time"]]
    usd_prices = list(df["Price in USD"])
    cny_prices = list(df["Price in CNY"])
    return times, usd_prices, cny_prices


def plot_stock_data(times: List[datetime.datetime], usd_prices: List[float], cny_prices: List[float], title: str,
                     xlabel: str, ylabel: str, save_path: str):
    """
    This function generates a plot of the stock prices over time and saves it to a file.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(times, usd_prices, label="Price in USD")
    ax.plot(times, cny_prices, label="Price in CNY")
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid()
    fig.savefig(save_path)
    plt.close()


def main(input_file: str, output_file: str, title: str = "Stock Price Chart", xlabel: str = "Time",
         ylabel: str = "Stock Price") -> None:
    """
    This is the main function that reads the stock data and plots a graph using the data.
    """
    times, usd_prices, cny_prices = read_stock_data_from_csv(input_file)
    if not all([times, usd_prices, cny_prices]):
        return
    plot_stock_data(times, usd_prices, cny_prices, title, xlabel, ylabel, output_file)


if __name__ == "__main__":
    input_file = "app/data/stock_data.csv"
    output_file = "app/data/stock_price_chart.png"
    main(input_file, output_file)
