import pandas as pd
import os

def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbol):
    """Read stock data for given symbol from CSV file."""
    df = pd.read_csv(symbol_to_path(symbol),
                     index_col='date',
                     parse_dates=True)
    return df

def position_list(path='data'):
    files = os.listdir(path)
    position = [s.split('.')[0] for s in files]
    return position

def profit(file='data/profit.csv'):
    profit_df = pd.read_csv(file,
                            index_col='date',
                            parse_dates=True)
    return profit_df


def test():
    df = get_data(601989)
    print(60*'-')
    print(df)

    def total_share(symbol):
        df = get_data(symbol)
        return df['quantity'].sum()

    share = total_share(601989)
    print(share)
    print(position_list())
    print(profit())

test()
