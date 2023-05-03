import pandas as pd #Importing the pandas library for data manipulation
import datetime #Importing the datetime module for date-time operations
import matplotlib.pyplot as plt #Importing matplotlib to plot the data
from typing import List, Tuple #Importing the list and tuple functions from the typing module
import os #Importing the operating system module to handle file paths

def read_stock_data_from_csv(file_path: str) -> Tuple[List[datetime.datetime], List[float], List[float]]:
    """
    This function reads stock data from a CSV file and returns a tuple containing the times, USD prices
    and CNY prices as three separate lists.
    """
    try: #Using a try-except statement to read the file and handle errors
        df = pd.read_csv(file_path)  #Reading the file into a pandas DataFrame
        if not {"Time", "Price in USD", "Price in CNY"}.issubset(set(df.columns)): #Checking for valid column names
            raise ValueError("Invalid input file format!")
    except (FileNotFoundError, ValueError) as e: #Handling FileNotFoundError or ValueError exceptions
        print(f"{e}")
        return [], [], []

    times = [datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f") for t in df["Time"]] #Converting strings to datetime objects
    usd_prices = list(df["Price in USD"]) #Creating a list of USD prices
    cny_prices = list(df["Price in CNY"]) #Creating a list of CNY prices
    return times, usd_prices, cny_prices  #Returning the three lists


def plot_stock_data(times: List[datetime.datetime], usd_prices: List[float], cny_prices: List[float], title: str,
                     xlabel: str, ylabel: str, save_path: str):
    """
    This function generates a plot of the stock prices over time and saves it to a file.
    """
    fig, ax = plt.subplots(figsize=(12, 6)) #Creating a basic plot with labels
    ax.plot(times, usd_prices, label="Price in USD") #Plotting the USD prices
    ax.plot(times, cny_prices, label="Price in CNY") #Plotting the CNY prices
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel) #Setting the plot labels
    ax.legend() #Adding the legend
    ax.grid() #Creating a grid
    fig.savefig(save_path) #Saving the plot to a file
    plt.close(fig) #Closing the figure


def main(input_file: str, output_file: str, title: str = "Stock Price Chart", xlabel: str = "Time",
         ylabel: str = "Stock Price") -> None:
    """
    This is the main function that reads the stock data and plots a graph using the data.
    """
    times, usd_prices, cny_prices = read_stock_data_from_csv(input_file) #Retrieving the stock data
    if not all([times, usd_prices, cny_prices]): #Checking that all data has been successfully loaded
        return
    plot_stock_data(times, usd_prices, cny_prices, title, xlabel, ylabel, output_file) #Generating the plot


if __name__ == "__main__":
    input_file = os.path.join("app", "data", "stock_data.csv")  #Setting the path of the input file
    output_file = os.path.join("app", "data", "stock_price_chart.png") #Setting the path of the output file
    main(input_file, output_file) #Running the main function