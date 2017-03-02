import pandas as pd

from tt.blotter import Blotter

class Position:

    def __init__(self, sid):
        self.sid = sid
        self.bought_value = 0
        self.sold_value = 0
        self.total_trades = 0
        self.sellable = 0
        self.average_cost = 0
        self.market_value = 0
        self.value_percent = 0

    def __repr__(self):
        return "Position({})".format(self.__dict__)

    @property
    def records(self):
        blotters = Blotter().get_data()
        return blotters[blotters['sid']==self.sid]

    @property
    def quantity(self):
        return self.records.quantity.sum()

    @property
    def bought_quantity(self):
        return self.records[self.records['type']=='buy'].quantity.sum()

    @property
    def sold_quantity(self):
        return -self.records[self.records['type']=='sell'].quantity.sum()
