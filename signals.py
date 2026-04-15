import pandas as pd

def sma_crossover_signals(df):
    """
    BUY: SMA20 crosses above SMA50 (golden cross)
    SELL: SMA20 crosses below SMA50 (death cross)
    """
    df = df.copy() # makes a copy so it does not alter original data
    df["Signal"] = 0 # Adds column signal and fills it with value 0

    for i in range(1, len(df)): # loops through rows starting at index 1(needs to start at 1 so you can compare)
        # Golden cross: SMA20 just crossed above SMA50
        if df["SMA20"].iloc[i] > df["SMA50"].iloc[i] and \
           df["SMA20"].iloc[i-1] <= df["SMA50"].iloc[i-1]: # if the SMA20 value is > SMA50 for today AND if SMA20 is <= SMA50 yesterday
            df.iloc[i, df.columns.get_loc("Signal")] = 1  # if both are true then puts 1 in signal and is a good indicator to buy
        # Death cross: SMA20 just crossed below SMA50
        elif df["SMA20"].iloc[i] < df["SMA50"].loc[i] and \
           df["SMA20"].iloc[i-1] >= df["SMA50"].iloc[i-1]: # if the SMA20 value is < SMA50 for today AND if SMA20 is >= SMA50 yesterday
            df.iloc[i, df.columns.get_loc("Signal")] = -1 # if both are true then puts -1 in signal column and indicates to sell
        
    return df 

def rsi_macd_signals(df):
    """
    BUY: RSI < 35 AND MACD line crosses above signal line
    SELL: RSI > 65 AND MACD line crosses below signal line
    """
    df = df.copy()
    df["Signal"] = 0

    for i in range(1, len(df)):
        macd_cross_up = (df["MACD"].iloc[i] > df["MACD_signal"].iloc[i] and
                         df["MACD"].iloc[i-1] <= df["MACD_signal"].iloc[i-1]) # Checks if the MACD is above signal today and was below or equal to yesterday
        
        macd_cross_down = (df["MACD"].iloc[i] < df["MACD_signal"].iloc[i] and
                         df["MACD"].iloc[i-1] >= df["MACD_signal"].iloc[i-1]) # Checks if the MACD is below signal today and was above or equal to yesterday
        
        rsi_oversold = df["RSI"].iloc[i] < 35 # RSI is oversold if below 35
        rsi_overbought = df["RSI"].iloc[i] > 65 # RSI is overbought if above 65

        if macd_cross_up and rsi_oversold: # if rsi is low and macd crosses up then buy
            df.iloc[i, df.columns.get_loc("Signal")] = 1 # BUY

        elif macd_cross_down and rsi_overbought: # if rsi is high and macd crosses below then sell
            df.iloc[i, df.columns.get_loc("Signal")] = -1 # SELL

    return df

def bollinger_signals(df):
    """
    BUY: Price touches/crosses lower Bollinger Band
    SELL: Price touches/crosses upper Bollinger Band
    """
    df = df.copy()
    df["Signal"] = 0

    df.loc[df["Close"] <= df["BB_lower"], "Signal"] = 1 # BUY if close price is less than or equal to the lower band, signal set to 1
    df.loc[df["Close"] >= df["BB_upper"], "Signal"] = -1 # SELL if close price is greater than or equal to the upper band, signal set to -1

    return df

if __name__ == "__main__":
    from data import get_data # allows us to get data
    from indicators import add_all_indicators # imports all indicators used in indicators

    df = get_data("AAPL") # downloads stock data
    df = add_all_indicators(df) # adds indicators in dataframe
    df = rsi_macd_signals(df) # runs the one of the indicators

    buys = df[df["Signal"] == 1] # Creates a new dataframe that keeps rows with signal val 1
    sells = df[df["Signal"] == -1] # Creates a new dataframe that keeps rows with signal val -1

    print(f"Buy signals:     {len(buys)}") # Prints the number of rows wiht buy signals
    print(f"Sell signals:    {len(sells)}") # Prints the number of rows wiht buy signals