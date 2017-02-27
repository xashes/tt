class Position:

    def __init__(self, sid):
        self.sid = sid
        self.quantity = 0
        self.bought_quantity = 0
        self.sold_quantity = 0
        self.bought_value = 0
        self.sold_value = 0
        self.total_trades = 0
        self.sellable = 0
        self.average_cost = 0
        self.market_value = 0
        self.value_percent = 0

    def __repr__(self):
        return "Position({})".format(self.__dict__)
