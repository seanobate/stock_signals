from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

# ---- Import your own functions ----
from data import get_data
from indicators import add_all_indicators

class RSI_MACD_Strategy(Strategy):
    rsi_buy  = 35   # RSI threshold for buy
    rsi_sell = 65   # RSI threshold for sell

    def init(self):
        close = self.data.Close

        # Register indicators (backtesting.py needs them wrapped)
        import pandas_ta as ta
        import pandas as pd

        closes = pd.Series(self.data.Close)
        self.rsi = self.I(lambda x: ta.rsi(pd.Series(x), length=14), closes)

        macd_df = ta.macd(closes, fast=12, slow=26, signal=9)
        self.macd   = self.I(lambda x: macd_df["MACD_12_26_9"].values, closes)
        self.macd_s = self.I(lambda x: macd_df["MACDs_12_26_9"].values, closes)

    def next(self):
        # BUY condition
        if (self.rsi[-1] < self.rsi_buy and
            crossover(self.macd, self.macd_s)):
            self.buy()

        # SELL condition
        elif (self.rsi[-1] > self.rsi_sell and
              crossover(self.macd_s, self.macd)):
            self.sell()


if __name__ == "__main__":
    df = get_data("AAPL", start="2018-01-01", end="2024-01-01")

    bt = Backtest(df, RSI_MACD_Strategy,
                  cash=10_000,
                  commission=0.002)  # 0.2% commission per trade

    results = bt.run()
    print(results)
    bt.plot()