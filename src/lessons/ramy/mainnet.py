from pybit import WebSocket, HTTP
import time


endpoint_public = "wss://stream.bybit.com/realtime"

session = HTTP(
    endpoint="https://api.bybit.com",
    api_key="X5efT4J84FrZVGaCcU",
    api_secret="gUJ8r3CnefTTGrWUxg7yVDifuOBJxjQH6Mq8",
)
ws = WebSocket(
    endpoint="wss://stream.bybit.com/realtime",
    subscriptions=["order", "position", "trade.BTCUSD", "orderBookL2_25.BTCUSD"],
    api_key="X5efT4J84FrZVGaCcU",
    api_secret="gUJ8r3CnefTTGrWUxg7yVDifuOBJxjQH6Mq8",
)
# ------------------------GET BEST PRICE------------------------------

subs = ["orderBookL2_25.BTCUSD"]
ws = WebSocket("wss://stream.bybit.com/realtime", subscriptions=subs)


def get_best_bid(best_buy_price):
    datas = ws.fetch(subs[0])
    while not datas:

        datas = ws.fetch(subs[0])

    buy_data = [data.get("price") for data in datas if data.get("side") == "Buy"]
    if max(buy_data) != best_buy_price:
        best_buy_price = max(buy_data)
    return best_buy_price


# ---------------------------STEP 2 --------------------------------------------

orders_id = []


def get_new_order(orders_id):
    active = session.get_active_order(symbol="BTCUSD", order_status="New")
    active

    orders = active.get("result").get("data")
    for order in orders:
        if order.get("order_id") not in orders_id:
            orders_id.append(order.get("order_id"))
    return orders_id


def deuxieme_achat(price):
    session.place_active_order(
        symbol="BTCUSD",
        side="Buy",
        order_type="Limit",
        price=float(price) - 50,
        qty=10,
        time_in_force="PostOnly",
    )


def vente(filled_price):
    session.place_active_order(
        symbol="BTCUSD",
        side="Sell",
        order_type="Limit",
        price=float(filled_price) + 50,
        qty=10,
        time_in_force="PostOnly",
        reduce_only=True,
    )


def check_order_status(orders_id):

    response = session.get_active_order(symbol="BTCUSD", order_status="Filled")
    orders = response.get("result").get("data")
    active = session.get_active_order(symbol="BTCUSD", order_status="New")

    active_orders = active.get("result").get("data")

    if orders:
        min_order = get_min_order(active_orders)
        for order in orders:
            if order.get("order_id") in orders_id and order.get("side") == "Buy":
                # print("Buy")
                # print(order.get("order_status"), order.get('qty'), order.get("price"), order.get("side"), order.get("order_id"))
                deuxieme_achat(min_order.get("price"))
                vente(order.get("price"))
                orders_id.remove(order.get("order_id"))
            elif order.get("order_id") in orders_id and order.get("side") == "Sell":
                # print("Sell")
                # print(order.get("order_status"), order.get('qty'), order.get("price"), order.get("side"), order.get("order_id"))
                deuxieme_achat(min_order.get("price"))
                orders_id.remove(order.get("order_id"))
            return orders_id


# ------------------------------STEP 3------------------------------------


def buyfunction(price):
    session.place_active_order(
        symbol="BTCUSD",
        side="Buy",
        order_type="Limit",
        price=float(price) + 50,
        qty=10,
        time_in_force="PostOnly",
    )


def cancel_order(order_id):
    session.cancel_active_order(symbol="BTCUSD", order_id=order_id)


def get_min_order(order_list):
    min_order = order_list[-1]
    for order in order_list:
        if float(min_order.get("price")) > float(order.get("price")):
            min_order = order
    return min_order


def get_max_order(order_list):
    max_order = order_list[-1]
    for order in order_list:
        if float(max_order.get("price")) < float(order.get("price")):
            max_order = order
    return max_order


def check_and_place_new_order(best_buy_price):
    active = session.get_active_order(symbol="BTCUSD", order_status="New")
    active

    orders = active.get("result").get("data")
    if orders:
        min_order = get_min_order(orders)
        first_order = get_max_order(orders)
        if float(best_buy_price) - float(first_order.get("price")) > 10:
            try:
                cancel_order(min_order.get("order_id"))
                buyfunction(first_order.get("price"))
            except:
                pass
    return None


# -----------------------------------------STEP 4----------------------------------------


def premier_achat(best_buy_price):
    prix = best_buy_price

    for i in range(0, 10):
        session.place_active_order(
            symbol="BTCUSD",
            side="Buy",
            order_type="Limit",
            price=prix,
            qty=10,
            time_in_force="PostOnly",
        )
        prix = float(prix) - 50
    return None


best_buy_price = 0
best_buy_price = get_best_bid(best_buy_price)
premier_achat(best_buy_price)
orders_id = get_new_order(orders_id)


while True:
    best_buy_price = get_best_bid(best_buy_price)
    orders_id = check_order_status(orders_id)
    orders_id = get_new_order(orders_id)
    check_and_place_new_order(best_buy_price)
