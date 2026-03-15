# AI Crypto Trading Bot

An open-source cryptocurrency trading bot powered by **AI and technical indicators**.
This project provides a modular framework for building automated crypto trading systems using **machine learning, reinforcement learning, and traditional trading strategies**.

---

## Features

* Binance API trading
* Reinforcement learning training
* Multiple technical indicators
* Risk management
* Backtesting support
* Modular architecture
* Configurable trading settings
* Example scripts for training and live trading

---

## Tech Stack

* Python
* TensorFlow
* Gymnasium
* TensorTrade
* CCXT
* Pandas
* TA (Technical Analysis Library)

---

## Project Structure

ai-crypto-trading-bot/

├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── config.example.yaml      # Example configuration file
├── .gitignore               # Ignored files for Git

├── bot/                     # Core trading bot modules
│   ├── api.py               # Exchange API connection
│   ├── indicators.py        # Technical indicators
│   ├── strategy.py          # Trading signal logic
│   ├── risk_management.py   # Position sizing and stop-loss
│   └── logger.py            # Trade logging

├── ai/                      # AI training modules
│   ├── environment.py       # Gymnasium trading environment
│   ├── train_agent.py       # Reinforcement learning training
│   └── model.py             # AI model architecture

├── backtest/                # Backtesting tools
│   └── backtester.py

├── examples/                # Example scripts
│   ├── run_live_bot.py
│   └── train_ai_bot.py

└── docs/                    # Additional documentation
└── architecture.md

---

## Installation

Clone the repository

git clone https://github.com/mahi2406/ai-crypto-trading-bot

Navigate to the project folder

cd ai-crypto-trading-bot

Install dependencies

pip install -r requirements.txt

---

## Configuration

Create your configuration file from the example:

cp config.example.yaml config.yaml

Then add your exchange API keys inside **config.yaml**.

---

## Run AI Training

python examples/train_ai_bot.py

---

## Run Trading Bot

python examples/run_live_bot.py

---

## Roadmap

Planned improvements:

* Paper trading mode
* Web dashboard
* Multi-exchange support
* Strategy optimization with AI
* Performance analytics

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## License

This project is licensed under the MIT License.
