from config_execution import ws_public_url, ticker_1, ticker_2
from time import sleep
from pybit import WebSocket

subs_public = [
    f"orderBookL2_25.{ticker_1}",
    f"orderBookL2_25.{ticker_2}"
]


def handle_message(msg):
    print(msg)


ws_public = WebSocket(
    ws_public_url,
    subscriptions=subs_public
)
