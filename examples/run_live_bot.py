from bot.api import initialize_binance

exchange = initialize_binance("API_KEY", "SECRET")

ticker = exchange.fetch_ticker("BTC/USDT")

print(ticker)
