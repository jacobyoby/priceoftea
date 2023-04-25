The Price of T(itatnium) in China

## Description

This repository contains a script to check the current price of titanium on the US stock exchange, convert it to Chinese Yuan, and display it in a chart over time. The script runs every 5 minutes using GitHub Actions.

## Features

1. Fetches the current price of titanium on the US stock exchange
2. Converts the price to Chinese Yuan
3. Visualizes the data in a chart over time
4. Uses GitHub Actions to run the script every 5 minutes

## Requirements

To set up the project, you'll need to install the following Python libraries:

- `requests`
- `beautifulsoup4`
- `pandas`
- `matplotlib`
- `forex-python`

You can install these libraries using the following command:

```
pip install requests beautifulsoup4 pandas matplotlib forex-python
```

## How to Use

1. Clone this repository or download the source code.
2. Run the `main.py` script to fetch the current price of titanium, convert it to Chinese Yuan, and save the data to a CSV file.
3. Run the `generate_graph.py` script to create a chart of the titanium prices over time.
4. Set up a GitHub Action to run the `main.py` script every 5 minutes. See the `main.yml` file for the GitHub Action configuration.

## File Structure

- `main.py`: Contains the main script to fetch the titanium price, convert it to Yuan, and save the data to a CSV file.
- `generate_graph.py`: Contains the script to generate a chart of titanium prices over time.
- `main.yml`: Contains the GitHub Action configuration to run the `main.py` script every 5 minutes.
- `requirements.txt`: Contains the required Python libraries for this project.
