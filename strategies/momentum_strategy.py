import backtrader as bt

class MomentumStrategy(bt.Strategy):
    params = (("momentum_period", 10),)

    def __init__(self):
        self.momentum = bt.indicators.Momentum(period=self.params.momentum_period)

    def next(self):
        if not self.position:
            if self.momentum[0] > 100:
                self.buy()
        elif self.momentum[0] < 100:
            self.close()
