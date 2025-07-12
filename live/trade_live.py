from alpaca_trade_api.rest import REST, TimeFrame
from config.config import ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL, SYMBOL, RISK_PER_TRADE
from utils.logger import log
import time

api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL)

def get_price(symbol):
    barset = api.get_bars(symbol, TimeFrame.Minute, limit=1)
    return barset[0].c if barset else None

def check_momentum(symbol, period=10):
    bars = api.get_bars(symbol, TimeFrame.Minute, limit=period).df
    bars["momentum"] = bars["close"].diff(period)
    return bars["momentum"].iloc[-1]

def trade():
    price = get_price(SYMBOL)
    momentum = check_momentum(SYMBOL)
    position = api.get_position(SYMBOL) if SYMBOL in [p.symbol for p in api.list_positions()] else None

    log(f"Price: {price}, Momentum: {momentum}")

    if not position and momentum > 0:
        api.submit_order(symbol=SYMBOL, qty=1, side='buy', type='market', time_in_force='gtc')
        log(f"BUY {SYMBOL}")
    elif position and momentum < 0:
        api.submit_order(symbol=SYMBOL, qty=1, side='sell', type='market', time_in_force='gtc')
        log(f"SELL {SYMBOL}")

if __name__ == "__main__":
    while True:
        try:
            trade()
            time.sleep(60)
        except Exception as e:
            log(f"Error: {str(e)}")
