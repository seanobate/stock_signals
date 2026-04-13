# stock_signals
## Summary:
- A data pipeline that pulls real stock data
- Technical indicator (RSI, MACD, SMA, Bollinger Bands)
- Clear buy/sell signal rules
- A backtester to measure ral performance
- Charts to visualize everything

## Prerequisites:
- Python 3
- Concepts(loops, functions, pandas, DataFrames)
- Code editor

## Phase 0 Setting Up Project:
1. Create Project Folder
2. Install Libaries:
   - yfinance (Real stock data from Yahoo Fincance)
   - pandas (Data manipulation and analysis)
   - pandas-ta [Technical indicators (RSI, MACD, etc.)]
   - matplotlib (Charting and visualization)
   - backtesting (Simulate strategy performance on historical data)
     
## Phase 1 Pull & Explore Stock Data: 
1. Download stock data
   - Create data.py
2. Plot the closing price
   - add to data.py

## Phase 2 Add Technical Indicators:
1. Simple Moving Averages (SMA)
   - Create indicators.py file
   - Smooths Price over N days.
   - Crossovers signal trend changes.
2. RSI (Relative Strength Index)
   - Measires momentum. Below 30 = oversold (potential buy). Above 70 = overbought (potential sell).
3. MACD (Moving Average Convergence Divergence)
   - Trend + Momentum Indicator.
   - Signal line crossovers are key events.
4. Bollinger Bands
   - Price envelope that shows volatility. Price touching lower band = potential buy.
   - Upper band = potential sell.
5. Combine all indicators

## Phase 3 Define Buy/Sell Signal Rules
- Write explicit rules that trigger buy and sell signals.
- Creat signals.py
1. Understand the approach
   - This part can use AI but this project uses if/else logic.
   - Buy when multiple bullish conditions align
   - Sell when multiple bearish conditions align
2. SMA Crossover
3. RSI + MACD Combined
4. Bollinger Band Bounce
5. Preview Signals
   - You should see a count of buy and sell signals generated.
## Phase 4 Visualize Your Signals
- See exactly where your buy/sell signals appear on price chart.
- Create chart.py
- A 3-panel chart should appear with price, buy/sell markers, RSI, and MACD
## Phase 5 Backtest Your Strategy
- Simulate trading your signal on historical data to measure real performance.
1. Build the backtester
2. Run the backtest
3. Understand the key metrics
   - Return = Total profit/loss % -> >Buy & Hold return
   - Sharpe Ratio = Return per unit of risk -> >1.0
   - Max Drawdown = Worst peak-to-trough loss -> <20%
   - Win Rate = % of trades that were profitable -> >50%
   - Number of trades = Total trade executed -> Not too high (overtrading)
- You should see a performance summary table and an interactive chart
## Phase 6 Tune & Improve
- Improve your strategy's performance by adjusting rules and thresholds.
1. Optimize parameters automatically
2. Common improvement ideas
   - Add volume confirmation: only take signals when volume is above average.
   - Use trend filter: Only buy when price is above SMA 200.
   - Add stop loss: Exit trade if price falls 5% from entry.
   - Combine strategies: REquire 2+ indicators to agree before signaling
   - etc.
