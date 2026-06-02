from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):

    try:

        logger.info(
            f"MARKET Request -> "
            f"Symbol={symbol}, "
            f"Side={side}, "
            f"Qty={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        order_details = client.futures_get_order(
            symbol=symbol,
            orderId=order["orderId"]
        )

        logger.info(
            f"MARKET Response -> {order_details}"
        )

        return order_details

    except Exception as e:

        logger.error(
            f"MARKET Error -> {str(e)}"
        )

        raise


def place_limit_order(
        symbol,
        side,
        quantity,
        price
):

    try:

        logger.info(
            f"LIMIT Request -> "
            f"Symbol={symbol}, "
            f"Side={side}, "
            f"Qty={quantity}, "
            f"Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        order_details = client.futures_get_order(
            symbol=symbol,
            orderId=order["orderId"]
        )

        logger.info(
            f"LIMIT Response -> {order_details}"
        )

        return order_details

    except Exception as e:

        logger.error(
            f"LIMIT Error -> {str(e)}"
        )

        raise