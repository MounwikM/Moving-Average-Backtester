# Moving-Average-Backtester
Python project for back testing stock trading strategies using simple moving average crossovers. 

A moving average is a trend following indicator that helps traders determine whether the average price of a stock is going up or down. Traders can see the movement of stock prices over time in relation to the actual stock price. 

To find the 50-day moving average, add the stock’s closing price from the last 50 days and divide the total by 50. Everyday the average changes because the oldest day is subtracted, while current day is added. 

In this code the stock will be bought if the short moving average crosses the long moving average, and will sell if the long moving average crosses the short moving average. 

**Remember to download pandas, yfinance and backtesting into your terminal**



