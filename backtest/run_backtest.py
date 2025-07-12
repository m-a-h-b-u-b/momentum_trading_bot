import backtrader as bt
from datetime import datetime
from strategies.momentum_strategy import MomentumStrategy
from data.data_loader import fetch_data

def run():
    cerebro = bt.Cerebro()
    df = fetch_data()
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(MomentumStrategy)
    cerebro.broker.set_cash(10000)
    print("Starting Portfolio Value:", cerebro.broker.getvalue())
    cerebro.run()
    print("Final Portfolio Value:", cerebro.broker.getvalue())
    cerebro.plot()

if __name__ == "__main__":
    run()
