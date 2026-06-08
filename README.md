# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot for Binance USDT-M Futures Testnet.

The bot supports:

* Market Orders
* Limit Orders
* BUY and SELL operations
* Input validation
* Logging
* Error handling
* Command Line Interface (CLI)

## Project Structure

trading_bot/

├── bot/

│ ├── client.py

│ ├── orders.py

│ ├── validators.py

│ └── logging_config.py

├── cli.py

├── README.md

├── requirements.txt

└── logs/

## Installation

1. Create virtual environment

python -m venv venv

2. Activate virtual environment

Windows:

venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

## Configuration

Update API credentials in cli.py

API_KEY = "YOUR_API_KEY"

API_SECRET = "YOUR_API_SECRET"

## Run Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

## Run Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 200000

## Logging

All API requests, responses and errors are stored in:

logs/trading.log

## Features Implemented

* Binance Futures Testnet Integration
* Market Orders
* Limit Orders
* BUY / SELL Support
* CLI Input Handling
* Validation Layer
* Logging Layer
* Exception Handling

## Assumptions

* Binance Futures Testnet account is active.
* Valid API Key and Secret Key are configured.
* User has sufficient testnet balance.
