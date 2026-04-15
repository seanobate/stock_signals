from backtesting import Backtest, Strategy 
from backtesting.lib import crossover
import pandas as pd

# Backtest= runs the strategy on historical data
# Strategy= base class you build your strategy from
# crossover= checks if one line crossed above another

# lambda means take some input x and do something with it like a super simple fuction

# This code is taking your stock strategy and tests whether it would have made money in the past


# ---- Import your own functions ----
from data import get_data 
from indicators import add_all_indicators

class RSI_MACD_Strategy(Strategy): # sets buy and sell rules
    rsi_buy  = 35   # RSI threshold for buy
    rsi_sell = 65   # RSI threshold for sell

    def init(self): # sets up indicators
        close = self.data.Close # gets the Close prices from backtest data.

        # Register indicators (backtesting.py needs them wrapped)
        import pandas_ta as ta
        import pandas as pd

        closes = pd.Series(self.data.Close) # takes all the closing prices and makes them a pandas series
        self.rsi = self.I(lambda x: ta.rsi(pd.Series(x), length=14), closes) # uses the close price to calculate a 14-day RSI, and register it as an indicator

        macd_df = ta.macd(closes, fast=12, slow=26, signal=9) # gives back a small line with MACD line, signal lines, and histogram
        self.macd   = self.I(lambda x: macd_df["MACD_12_26_9"].values, closes) # takes the main MACD line and registers as an indicator
        self.macd_s = self.I(lambda x: macd_df["MACDs_12_26_9"].values, closes) # takes MACD signal line and is stored as an indicator 

    def next(self): # checks the rules every new day
        # BUY condition
        if (self.rsi[-1] < self.rsi_buy and
            crossover(self.macd, self.macd_s)): # takes most recent RSI value is less then 35 and if there is a crossover with MACD and signal line.
            self.buy() # if both are true then buy

        # SELL condition
        elif (self.rsi[-1] > self.rsi_sell and
              crossover(self.macd_s, self.macd)): # takes most recent RSI value and checks if val is greater than 65 and if there is a cross oveer
            self.sell() # if both are true then sell.
 

if __name__ == "__main__":
    df = get_data("AAPL", start="2018-01-01", end="2024-01-01") # downloads stock data from date range

    bt = Backtest(df, RSI_MACD_Strategy,
                  cash=10_000,
                  commission=0.002)  # 0.2% commission per trade
# tests df, uses RSI_MACD_strategy, starts with $10,000, 0.2% charge per trade
    results = bt.run() # simulates everything
    print(results) # prints return %, number of trades, win rate, max drawdown, final equity
    bt.plot() # plots everything