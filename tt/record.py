import os

import pandas as pd


def records(base_dir='./data'):
    """
    Return: DataFrame
    """
    files = os.listdir(base_dir)
    records = pd.DataFrame()

    for fname in files:
        sid = fname.split('.')[0]
        df = pd.read_csv(
            os.path.join(base_dir, fname), index_col='date', parse_dates=True)
        df['sid'] = sid
        records = records.append(df)

    records = records.reset_index()
    return records


print('-' * 60)
