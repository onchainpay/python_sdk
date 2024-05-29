from common import *


def test_check_x_api_signature(client):
    response = client.basic_actions.check_x_api_signature()
    default_response_success_check(response)


def test_get_currencies(client):
    response = client.basic_actions.get_currencies()
    default_response_success_check(response)


def test_get_currency_price(client):
    response = client.basic_actions.get_currency_price(
        "BTC",
        "USDT"
    )
    default_response_success_check(response)


def test_get_operation_by_tx_hash_fail(client):
    response = client.basic_actions.get_operation_by_tx_hash("0x1234567890")
    default_response_error_check(response)


def test_check_address_format(client):
    response = client.basic_actions.check_address_format(
        "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        "bitcoin",
    )
    default_response_success_check(response)
