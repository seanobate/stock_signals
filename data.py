import yfinance as yf # downloads data from yahoo
import pandas as pd # allows you to edit and manipulate data
import matplotlib.pyplot as plt #allows for charting and visuals


def get_data(ticker="AAPL", start="2020-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end) # downloads data from single stock from a certain time range.
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.dropna(inplace=True) #dropna drops missing vals & inplace saves these changes
    print(f"Downloaded {len(df)} rows for {ticker}")
    print(df.head()) # prints the top 5 rows
    return df # allows you to use the dataframe later in my code

def plot_price(df, ticker="AAPL"):
    df["Close"].plot(figsize=(14, 5), 
                     title=f"{ticker} Closing Price", 
                     color="steelblue")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    df = get_data("AAPL") # download Apple data
    plot_price(df, "AAPL") # displays data in a graph