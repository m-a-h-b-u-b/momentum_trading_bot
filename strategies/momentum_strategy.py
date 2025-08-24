# Import the Backtrader library, which is used for backtesting trading strategies
import backtrader as bt  # powerful Python backtesting framework


# Define a trading strategy by creating a class that inherits from bt.Strategy
class MomentumStrategy(bt.Strategy):  # Every strategy must subclass bt.Strategy
    
    # Define configurable parameters for the strategy
    # Here, "momentum_period" means how many bars/candles to use in momentum calculation
    params = (("momentum_period", 10),)  # Default momentum lookback = 10 periods


    # __init__ is called once when the strategy is initialized
    def __init__(self):
        # Create a Momentum indicator using Backtrader's built-in indicators
        # Momentum = (current price / price N periods ago) * 100
        self.momentum = bt.indicators.Momentum(period=self.params.momentum_period)  # attach momentum indicator


    # The next() method runs once per bar (candle) of data
    # This is where you define the trading logic
    def next(self):
        # Check if we are currently NOT holding any position
        if not self.position:  # no active trades yet
            # If momentum is greater than 100 → bullish signal (price increasing)
            if self.momentum[0] > 100:  # Momentum crossing above 100
                self.buy()  # open a long position
        else:
            # If we already have a position and momentum falls below 100 → bearish signal
            if self.momentum[0] < 100:  # Momentum dropping below 100
                self.close()  # exit the trade (close position)
