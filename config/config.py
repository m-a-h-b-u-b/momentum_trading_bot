import os
from dotenv import load_dotenv

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("BASE_URL", "https://paper-api.alpaca.markets")
SYMBOL = "AAPL"
RISK_PER_TRADE = 0.01
