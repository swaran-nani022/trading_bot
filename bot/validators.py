def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol cannot be empty")


def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError(
            "Side must be BUY or SELL"
        )


def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError(
            "Order type must be MARKET or LIMIT"
        )


def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than 0"
        )


def validate_price(price):
    if price is None or price <= 0:
        raise ValueError(
            "Price must be greater than 0"
        )