import csv
import matplotlib.pyplot as plt
import datetime

def read_stock_data_from_csv(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the headers

        times = []
        usd_prices = []
        cny_prices = []

        for row in reader:
            times.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f"))
            usd_prices.append(float(row[1]))
            cny_prices.append(float(row[2]))

        return times, usd_prices, cny_prices

def plot_stock_data(times, usd_prices, cny_prices):
    plt.figure(figsize=(12, 6))

    plt.plot(times, usd_prices, label="Price in USD")
    plt.plot(times, cny_prices, label="Price in CNY")

    plt.title("T Stock Price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price")

    plt.legend()
    plt.grid()
    plt.savefig("stock_price_chart.png")

def main():
    times, usd_prices, cny_prices = read_stock_data_from_csv("stock_data.csv")
    plot_stock_data(times, usd_prices, cny_prices)

if __name__ == "__main__":
    main()
