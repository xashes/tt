import pandas as pd

from tt.blotter import Blotter


class Portfolio(object):
    def __init__(self):
        self.starting_cash = 0.

    @property
    def value(self):
        return self.cash + self.market_value

    @property
    def cash(self):
        pass

    @property
    def market_value(self):
        pass

    @property
    def positions(self):
        grp = self.blotter.groupby('sid')
        quantities = grp.agg({'quantity': sum})
        holding = quantities[quantities>0].index.values
        return holding

    @property
    def blotter(self):
        return Blotter().data_frame
