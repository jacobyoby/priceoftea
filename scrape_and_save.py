import os
import requests
from bs4 import BeautifulSoup
import datetime


def scrape_data():
    """
    Scrape the first product's name and price in Chinese Yen (CNY) from the specified webpage.

    Returns:
        str: A string containing the product's name, original price, and discounted price, separated by commas.
    """
    # Replace with the URL of the webpage you want to scrape
    example_url = 'https://www.rt-mart.com.tw/direct/index.php?action=prod_search&prod_keyword=tea'

    # Bypass SSL certificate verification (use with caution)
    response = requests.get(example_url, verify=False)

    if response.status_code != 200:
        return f"Failed to fetch the webpage. Status code: {response.status_code}\n"
    soup = BeautifulSoup(response.text, 'html.parser')
    product_name = soup.find('h5', class_='for_proname')
    product_price_container = soup.find('div', class_='for_pricebox')

    if product_name and product_price_container:
        name = product_name.text.strip()
        product_prices = product_price_container.find_all('span')
        if len(product_prices) >= 2:
            original_price = product_prices[0].text.strip()
            discounted_price = product_prices[1].text.strip()

            return (
                f"{name},{original_price},{discounted_price}\n"
                if '¥' not in original_price and '$' in original_price
                else "The first price found is not in Chinese Yen (CNY).\n"
            )
        else:
            return "Price not found in the container.\n"
    else:
        return "Product name or price container not found.\n"


def save_data_to_file(data):
    """
    Save the given data to the 'data.csv' file with a timestamp, if the data for the current hour doesn't exist.

    Args:
        data (str): The data to be saved.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_hour = datetime.datetime.now().strftime('%Y-%m-%d %H')

    # Check if the data.csv file exists
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if data for the current hour exists
        if current_hour in content:
            print(f"Data for the current hour ({current_hour}) already exists.")
            return

    # Save the data to the file
    with open('data.csv', 'a', encoding='utf-8') as f:
        f.write(f"{timestamp},{data}")


if __name__ == "__main__":
    data = scrape_data()
    save_data_to_file(data)