import matplotlib.pyplot as plt

def plot_signals(df, ticker="AAPL"):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 12),
                                          gridspec_kw={"height_ratios": [3, 1, 1]})
    fig.suptitle(f"{ticker} — Buy/Sell Signals", fontsize=16)

    # --- Top chart: Price + signals ---
    ax1.plot(df.index, df["Close"], label="Close", color="steelblue", linewidth=1.5)
    ax1.plot(df.index, df["SMA20"], label="SMA20", color="orange", linewidth=1, alpha=0.7)
    ax1.plot(df.index, df["SMA50"], label="SMA50", color="purple", linewidth=1, alpha=0.7)
    ax1.plot(df.index, df["BB_upper"], "--", color="gray", linewidth=0.8, alpha=0.5)
    ax1.plot(df.index, df["BB_lower"], "--", color="gray", linewidth=0.8, alpha=0.5)

    # Plot buy signals (green triangles up)
    buys = df[df["Signal"] == 1]
    ax1.scatter(buys.index, buys["Close"], marker="^", color="green",
                s=100, zorder=5, label="BUY")

    # Plot sell signals (red triangles down)
    sells = df[df["Signal"] == -1]
    ax1.scatter(sells.index, sells["Close"], marker="v", color="red",
                s=100, zorder=5, label="SELL")

    ax1.set_ylabel("Price (USD)")
    ax1.legend(loc="upper left")
    ax1.grid(True, alpha=0.3)

    # --- Middle chart: RSI ---
    ax2.plot(df.index, df["RSI"], color="darkorange", linewidth=1)
    ax2.axhline(70, color="red", linestyle="--", linewidth=0.8)
    ax2.axhline(30, color="green", linestyle="--", linewidth=0.8)
    ax2.fill_between(df.index, df["RSI"], 70, where=(df["RSI"] >= 70),
                     alpha=0.3, color="red")
    ax2.fill_between(df.index, df["RSI"], 30, where=(df["RSI"] <= 30),
                     alpha=0.3, color="green")
    ax2.set_ylabel("RSI")
    ax2.set_ylim(0, 100)
    ax2.grid(True, alpha=0.3)

    # --- Bottom chart: MACD ---
    ax3.plot(df.index, df["MACD"], label="MACD", color="blue", linewidth=1)
    ax3.plot(df.index, df["MACD_signal"], label="Signal", color="red", linewidth=1)
    ax3.bar(df.index, df["MACD_hist"], color="gray", alpha=0.5, label="Histogram")
    ax3.axhline(0, color="black", linewidth=0.5)
    ax3.set_ylabel("MACD")
    ax3.legend(loc="upper left")
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    from data import get_data
    from indicators import add_all_indicators
    from signals import rsi_macd_signals

    df = get_data("AAPL")
    df = add_all_indicators(df)
    df = rsi_macd_signals(df)
    plot_signals(df, "AAPL")