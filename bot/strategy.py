def trading_signal(df):

    last = df.iloc[-1]

    if last["ema_9"] > last["ema_21"] and last["rsi"] < 70:
        return "buy"

    if last["ema_9"] < last["ema_21"] and last["rsi"] > 30:
        return "sell"

    return "hold"
