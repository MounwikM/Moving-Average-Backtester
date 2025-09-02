import pandas as pan
import yfinance as yf
from backtesting import Strategy, Backtest

data = yf.download("GOOGL", start="2020-01-01", end="2025-02-28", interval="1d")

if isinstance(data.columns, pan.MultiIndex):
    data.columns = [col[0] for col in data.columns]

class OpeningRangeBreakout(Strategy):

    def init(self):
        self.sma_short = self.I(lambda x: pan.Series(x).rolling(10).mean(), self.data.Close)
        self.sma_long = self.I(lambda x: pan.Series(x).rolling(50).mean(), self.data.Close)

    def next(self):
        if self.position:
            return  # already in position, wait

        # Buy signal
        if self.sma_short[-2] < self.sma_long[-2] and self.sma_short[-1] > self.sma_long[-1]:
            # Enter with stop loss 5% below entry, take profit 10% above
            self.buy()

        # Sell signal (for shorting if desired)
        elif self.sma_short[-2] > self.sma_long[-2] and self.sma_short[-1] < self.sma_long[-1]:
            self.sell()
            
bt = Backtest(data, OpeningRangeBreakout, cash=25000, commission= 0.002)
stats = bt.run()
print(stats)
bt.plot()
