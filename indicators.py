import pandas_ta as ta # allows you to use technical indicators 

def add_sma(df):
    df["SMA20"] = ta.sma(df["Close"], length=20) # Simple moving average over last 20 days
    df["SMA50"] = ta.sma(df["Close"], length=50) # Simple moving average over last 50 days
    df["SMA200"] = ta.sma(df["Close"], length=200) # Simple moving average over last 200 days
    return df

def add_rsi(df):    
    df["RSI"] = ta.rsi(df["Close"], length=14) # calcs rsi over 14 days
    return df

def add_macd(df):
    macd = ta.macd(df["Close"], fast=12, slow=26, signal=9) # fast moving average, slow moving average, signal line period
    df["MACD"] = macd["MACD_12_26_9"] # stores the macd values
    df["MACD_signal"] = macd["MACDs_12_26_9"] # stores the signal vals in a new column
    df["MACD_hist"] = macd["MACDh_12_26_9"] # stores histogram values in a new column
    return df

def add_bollinger(df):
    bb = ta.bbands(df["Close"], length=20, std=2)
    df["BB_upper"] = bb["BBU_20_2.0_2.0"]
    df["BB_mid"] = bb["BBM_20_2.0_2.0"]
    df["BB_lower"] = bb["BBL_20_2.0_2.0"]
    return df

def add_all_indicators(df):
    df = add_sma(df)
    df = add_rsi(df)
    df = add_macd(df)
    df = add_bollinger(df)
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    from data import get_data
    df = get_data("AAPL")
    df = add_all_indicators(df)
    print(df[["Close",
              "SMA20",
              "SMA50", 
              "RSI", 
              "MACD"
              ]].tail(10))