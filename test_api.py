from binance.client import Client

API_KEY = "leNBrQQdeYiDuEH2fWcdSfNxpSTAE9B4I7muC0SV8MEE3Hb4ZFHTPJEJovCD6kBk"
API_SECRET = "t2raBOpMAP1uQfmNFD42u3utdP4B7mbdiVdLodS19bckn7W2b4MUQaNx2tJIueCd"

client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET,
    testnet=True
)

try:
    balance = client.futures_account_balance()
    print("SUCCESS")
    print(balance)

except Exception as e:
    print("ERROR")
    print(e)