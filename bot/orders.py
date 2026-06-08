from bot.validators import validate_order


class OrderService:

    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        validate_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        try:

            self.logger.info(
                f"Request: {symbol} {side} {order_type} {quantity}"
            )

            if order_type == "MARKET":

                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            else:

                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )

            self.logger.info(f"Response: {order}")

            return order

        except Exception as e:

            self.logger.error(str(e))

            raise