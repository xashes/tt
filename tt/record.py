import os
import datetime as dt

import pandas as pd

from . import util

class Position(object):
    def __init__(self, sid):
        self.sid = sid
        self.amount = 0

    def __repr__(self):
        return "Position({})".format(self.__dict__)


def positions(path):
    """
    Return: DataFrame
    """
    files = os.listdir(path)
    positions = pd.DataFrame()

def records(base_dir='./data'):
    """
    Return: DataFrame
    """
    files = os.listdir(base_dir)
    records = pd.DataFrame()

    for fname in files:
        sid = fname.split('.')[0]
        df = pd.read_csv(os.path.join(base_dir, fname), index_col='date', parse_dates=True)
        df['sid'] = sid
        records = records.append(df)

    records = records.reset_index()
    return records


def position(end_date=dt.datetime.today()):
    # rd = records()
    # pt = {}
    # grp = rd.groupby('sid')
    pass

print('-'*60)
# print(position().tail(10))
