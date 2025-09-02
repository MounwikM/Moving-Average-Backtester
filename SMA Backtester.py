# Import pandas, yfinance, and backtesting
import pandas as pan
import yfinance as yf
from backtesting import Strategy, Backtest

# This is the data for the stock GOOGL from 01/01/2020 to 02/28/2025 in one day intervals
data = yf.download("GOOGL", start="2020-01-01", end="2025-02-28", interval="1d")

# This gives the data in format of backtesting
if isinstance(data.columns, pan.MultiIndex):
    data.columns = [col[0] for col in data.columns]

# Start of backtesting class
class OpeningRangeBreakout(Strategy):

    # This is where the data for the short and long averages will store.
    def init(self):
        self.sma_short = self.I(lambda x: pan.Series(x).rolling(10).mean(), self.data.Close)
        self.sma_long = self.I(lambda x: pan.Series(x).rolling(50).mean(), self.data.Close)

    # logic for the selling and buying of shares.
    def next(self):
        if self.position:
            return  # already in position, wait

        # Buy signal
        if self.sma_short[-2] < self.sma_long[-2] and self.sma_short[-1] > self.sma_long[-1]:
            self.buy()

        # Sell signal (for shorting if desired)
        elif self.sma_short[-2] > self.sma_long[-2] and self.sma_short[-1] < self.sma_long[-1]:
            self.sell()

# To show the results and the starting cash and commision. 
bt = Backtest(data, OpeningRangeBreakout, cash=25000, commission= 0.002)
stats = bt.run()
print(stats)
bt.plot()
