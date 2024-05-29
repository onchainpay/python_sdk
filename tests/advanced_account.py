from common import default_response_success_check, client


def test_get_all_advanced_balances(client):
    response = client.advanced_account.get_advanced_balances()
    default_response_success_check(response)


def test_get_advanced_address_by_id(client):
    response = client.advanced_account.get_advanced_balance()
    default_response_success_check(response)


def test_get_payment_address(client):
    response = client.advanced_account.get_payment_address(
        "USDT",
        "ethereum",
    )
    default_response_success_check(response)
