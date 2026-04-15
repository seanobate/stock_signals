import matplotlib.pyplot as plt # imports library used for graphing

def plot_signals(df, ticker="AAPL"): # This function takes the stock data and the ticker
    # alpha changes the transparency
    # s changes the size of the scatter marker
    # zorder 1=bottom, 3=middle, 5=top, this is like the layer

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 12),
                                          gridspec_kw={"height_ratios": [3, 1, 1]}) # creates 3 graphs; (3,1) 3 rows 1 col; ratios top is bigger than middle and bottom
    fig.suptitle(f"{ticker} — Buy/Sell Signals", fontsize=16) # Adds title to top of the page

    # --- Top chart: Price + signals ---
    ax1.plot(df.index, df["Close"], label="Close", color="steelblue", linewidth=1.5) # plots the close price, df.index shows the dates
    ax1.plot(df.index, df["SMA20"], label="SMA20", color="orange", linewidth=1, alpha=0.7)
    ax1.plot(df.index, df["SMA50"], label="SMA50", color="purple", linewidth=1, alpha=0.7)
    ax1.plot(df.index, df["BB_upper"], "--", color="gray", linewidth=0.8, alpha=0.5) # -- means dashed lines
    ax1.plot(df.index, df["BB_lower"], "--", color="gray", linewidth=0.8, alpha=0.5)

    # Plot buy signals (green triangles up)
    buys = df[df["Signal"] == 1] # keeps only rows where signal is 1
    ax1.scatter(buys.index, buys["Close"], marker="^", color="green",
                s=100, zorder=5, label="BUY") # puts a green triangle pointing up on the buy points

    # Plot sell signals (red triangles down)
    sells = df[df["Signal"] == -1] # keeps the sell rows
    ax1.scatter(sells.index, sells["Close"], marker="v", color="red",
                s=100, zorder=5, label="SELL") # puts a red triangle pointing down on the sell points

    ax1.set_ylabel("Price (USD)") # labels y axis
    ax1.legend(loc="upper left") # adds a legend
    ax1.grid(True, alpha=0.3) # adds grid lines

    # --- Middle chart: RSI ---
    ax2.plot(df.index, df["RSI"], color="darkorange", linewidth=1) # plots the RSI line
    ax2.axhline(70, color="red", linestyle="--", linewidth=0.8) # draws horizontal line at 70
    ax2.axhline(30, color="green", linestyle="--", linewidth=0.8) # draws horizontal line at 30
    ax2.fill_between(df.index, df["RSI"], 70, where=(df["RSI"] >= 70),
                     alpha=0.3, color="red") # Shades the area red when RSI is above 70
    ax2.fill_between(df.index, df["RSI"], 30, where=(df["RSI"] <= 30),
                     alpha=0.3, color="green") # shades the area green when RSI is below 30
    
    ax2.set_ylabel("RSI") # Labels RSI axis
    ax2.set_ylim(0, 100) # RSI stays between 0 to 100
    ax2.grid(True, alpha=0.3) # adds grid lines

    # --- Bottom chart: MACD ---
    ax3.plot(df.index, df["MACD"], label="MACD", color="blue", linewidth=1) # plots MACD line
    ax3.plot(df.index, df["MACD_signal"], label="Signal", color="red", linewidth=1) # plots MACD signal line
    ax3.bar(df.index, df["MACD_hist"], color="gray", alpha=0.5, label="Histogram") # This makes bars for the MACD histogram
    ax3.axhline(0, color="black", linewidth=0.5) # draws a horizontal line at 0 because MACD gets analyzed around zero.

    ax3.set_ylabel("MACD") # Adds labels
    ax3.legend(loc="upper left") # Adds legend
    ax3.grid(True, alpha=0.3) # Adds grid

    plt.tight_layout() # makes spacing nicer
    plt.show() # dsiplays the chart

if __name__ == "__main__":
    from data import get_data # imports the data
    from indicators import add_all_indicators # imports the indicators
    from signals import rsi_macd_signals # imports the rsi + macd signal

    df = get_data("AAPL") # downloads apples data
    df = add_all_indicators(df) # adds all the indicators
    df = rsi_macd_signals(df) # adds rsi + macd signal
    plot_signals(df, "AAPL") # plots the rsi + macd of the apple data 