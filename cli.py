import argparse

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True,
    help="Trading symbol (e.g., BTCUSDT)"
)

parser.add_argument(
    "--side",
    required=True,
    help="BUY or SELL"
)

parser.add_argument(
    "--type",
    required=True,
    help="MARKET or LIMIT"
)

parser.add_argument(
    "--quantity",
    type=float,
    required=True,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Required for LIMIT orders"
)

args = parser.parse_args()

try:

    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price

    validate_symbol(symbol)
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol       : {symbol}")
    print(f"Side         : {side}")
    print(f"Order Type   : {order_type}")
    print(f"Quantity     : {quantity}")

    if order_type == "LIMIT":
        validate_price(price)
        print(f"Price        : {price}")

    print("===================================")

    if order_type == "MARKET":

        order = place_market_order(
            symbol,
            side,
            quantity
        )

    else:

        order = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )

    print("\n========== ORDER RESPONSE ==========")

    print(
        "Order ID      :",
        order.get("orderId", "N/A")
    )

    print(
        "Status        :",
        order.get("status", "N/A")
    )

    print(
        "Symbol        :",
        order.get("symbol", "N/A")
    )

    print(
        "Side          :",
        order.get("side", "N/A")
    )

    print(
        "Order Type    :",
        order.get("type", "N/A")
    )

    print(
        "Quantity      :",
        order.get(
            "executedQty",
            order.get(
                "origQty",
                "N/A"
            )
        )
    )

    print(
        "Average Price :",
        order.get(
            "avgPrice",
            order.get(
                "price",
                "N/A"
            )
        )
    )

    print(
        "Client Order  :",
        order.get(
            "clientOrderId",
            "N/A"
        )
    )

    print(
        "Update Time   :",
        order.get(
            "updateTime",
            "N/A"
        )
    )

    print("====================================")

    print(
        "\nSUCCESS: Order placed successfully."
    )

except ValueError as ve:

    print(
        f"\nVALIDATION ERROR: {ve}"
    )

except Exception as e:

    print(
        f"\nFAILED: {str(e)}"
    )