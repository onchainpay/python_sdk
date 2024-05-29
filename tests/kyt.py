from common import *


def test_check_withdrawal(client, business_wallet_data):
    address = business_wallet_data[0]
    response = client.kyt.check_withdrawal_risks(
        address,
        "USDT",
        "tron",
        "100"
    )
    default_response_success_check(response)


def test_check_withdrawal_address(client, business_wallet_data):
    address = business_wallet_data[0]
    response = client.kyt.check_withdrawal_address(
        address,
        "USDT",
        "tron",
    )
    default_response_success_check(response)
