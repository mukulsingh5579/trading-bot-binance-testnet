import click

from bot.client import BinanceClient
from bot.orders import OrderService
from bot.logging_config import setup_logger


API_KEY = "leNBrQQdeYiDuEH2fWcdSfNxpSTAE9B4I7muC0SV8MEE3Hb4ZFHTPJEJovCD6kBk"
API_SECRET = "t2raBOpMAP1uQfmNFD42u3utdP4B7mbdiVdLodS19bckn7W2b4MUQaNx2tJIueCd"


logger = setup_logger()

client = BinanceClient(
    API_KEY,
    API_SECRET
).get_client()

order_service = OrderService(
    client,
    logger
)


@click.command()
@click.option("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
@click.option("--side", required=True, help="BUY or SELL")
@click.option("--type", "order_type", required=True, help="MARKET or LIMIT")
@click.option("--qty", required=True, type=float, help="Order quantity")
@click.option("--price", required=False, type=float, help="Price for LIMIT orders")
def run(symbol, side, order_type, qty, price):

    try:

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {symbol.upper()}")
        print(f"Side     : {side.upper()}")
        print(f"Type     : {order_type.upper()}")
        print(f"Quantity : {qty}")

        if price:
            print(f"Price    : {price}")

        result = order_service.place_order(
            symbol=symbol.upper(),
            side=side.upper(),
            order_type=order_type.upper(),
            quantity=qty,
            price=price
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID     : {result.get('orderId')}")
        print(f"Status       : {result.get('status')}")
        print(f"Symbol       : {result.get('symbol')}")
        print(f"Executed Qty : {result.get('executedQty')}")

        print("\nSUCCESS")

    except Exception as e:

        print("\n===== ORDER FAILED =====")
        print(str(e))


if __name__ == "__main__":
    run()