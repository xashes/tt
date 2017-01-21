import os

import pandas as pd


def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbol):
    """Read stock data for given symbol from CSV file."""
    df = pd.read_csv(
        symbol_to_path(symbol), index_col='date', parse_dates=True)
    return df


def position_list(path='data'):
    files = os.listdir(path)
    position = [s.split('.')[0] for s in files]
    return position


def profit(file='data/profit.csv'):
    profit_df = pd.read_csv(file, index_col='date', parse_dates=True)
    return profit_df

def latest_date():
    latest_date = []
    files = os.listdir()

def latest_date():
    latest_date = []
    files = os.listdir('data')
    for f in files:
        df = pd.read_csv('data/{}'.format(f), index_col='date', parse_dates=True)
        latest_date.append(df.index[-1])
    return latest_date


def test():
    print(60 * '-')
    print(latest_date())
    print(max(latest_date()))
