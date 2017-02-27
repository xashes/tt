import os
import pandas as pd
import numpy as np


class Blotter:

    def __init__(self, data_file='~/Dropbox/Apps/tt/blotter.csv'):
        self.data_file = data_file

    def get_data(self):
        data = pd.read_csv(
            self.data_file,
            index_col='date',
            parse_dates=True,
            dtype={'sid': object})
        data.sort_index(inplace=True)
        return data

    def add_record(self, date, sid, price=np.nan, quantity=np.nan):
        # TODO make backup file before write record
        pass

    def check_data(self):
        """
        Check data's potential mistakes
        Return True if there's no mistake be found
        """
        pass
