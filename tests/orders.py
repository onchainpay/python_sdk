import time

from common import *


@pytest.fixture(scope="session")
def order_id(client):
    response = client.orders.create_order(
        "USDT",
        "ethereum",
        "0.1",
        "order" + str(int(1000 * time.time())),
        3600,
    )
    return response.get("response").get("orderId")


def test_get_order_by_id(client, order_id):
    response = client.orders.get_order_by_id(order_id)
    default_response_success_check(response)


def test_get_order_by_id_fail(client):
    response = client.orders.get_order_by_id("123")
    default_response_error_check(response)


def test_get_orders(client):
    response = client.orders.get_orders()
    default_response_success_check(response)
