import os
import pandas as pd


class Blotter:

    @property
    def data_frame(self, base_dir='data'):
        """
        Return: DataFrame
        """
        files = os.listdir(base_dir)
        data = pd.DataFrame()

        for fname in files:
            sid = fname.split('.')[0]
            df = pd.read_csv(
                os.path.join(base_dir, fname), index_col='date', parse_dates=True)
            df['sid'] = sid
            data = data.append(df)

        return data
