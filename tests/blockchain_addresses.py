from common import *


@pytest.fixture(scope="session")
def payout_wallet_data(client):
    response = client.blockchain_address.create_payout_address(
        "USDT",
        "ethereum",
    )
    address = response.get("response").get("address")
    address_id = response.get("response").get("id")
    return address, address_id


def test_get_business_transactions(client, business_wallet_data):
    address_id = business_wallet_data[1]
    response = client.blockchain_address.get_transactions(
        address_id,
    )
    default_response_success_check(response)


def test_get_payout_transactions(client, payout_wallet_data):
    address_id = payout_wallet_data[1]
    response = client.blockchain_address.get_transactions(
        address_id,
        "withdrawal",
        ["pending"],
    )
    default_response_success_check(response)


def test_get_payout_addresses(client):
    response = client.blockchain_address.get_payout_addresses()
    default_response_success_check(response)


def test_get_payin_addresses(client):
    response = client.blockchain_address.get_payin_addresses()
    default_response_success_check(response)


def test_get_recurrent_addresses(client):
    response = client.blockchain_address.get_recurrent_addresses()
    default_response_success_check(response)


def test_get_business_addresses(client):
    response = client.blockchain_address.get_business_addresses()
    default_response_success_check(response)


def test_set_meta(client, business_wallet_data):
    address_id = business_wallet_data[1]
    response = client.blockchain_address.set_meta(
        address_id,
        {"key": "value"},
    )
    assert response.get("success") is True


def test_find_address_by_id(client, business_wallet_data):
    address_id = business_wallet_data[1]
    response = client.blockchain_address.get_address_by_id(
        address_id,
    )
    default_response_success_check(response)


def test_find_address_by_id_fail(client):
    response = client.blockchain_address.get_address_by_id(
        "123",
    )
    default_response_error_check(response)


def test_find_address_by_address(client, business_wallet_data):
    address = business_wallet_data[0]
    response = client.blockchain_address.get_address_by_address(
        address,
    )
    default_response_success_check(response)


def test_add_transaction_tracking(client, business_wallet_data):
    address = business_wallet_data[0]
    response = client.blockchain_address.add_transaction_tracking(
        address,
        "https://example.com",
    )
    default_response_success_check(response)
