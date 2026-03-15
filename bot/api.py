import ccxt

def initialize_binance(api_key, secret):
    exchange = ccxt.binance({
        "apiKey": api_key,
        "secret": secret,
        "enableRateLimit": True
    })
    return exchange
