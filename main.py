# Import the backtest runner function (aliased as run_backtest)
from backtest.run_backtest import run as run_backtest  

# Import the live trading function
from live.trade_live import trade  

if __name__ == "__main__":
    # Call this to run backtest mode
    # run_backtest()   # Uncomment to backtest
    
    # Call this to run live trading mode
    trade()           # Uncomment to go live
