from common import *


@pytest.fixture(scope="session")
def get_min_limit(client):
    response = client.crosschain_bridge.get_limits()
    return response.get("response").get("min")


#
# @pytest.fixture(scope="session")
# def fee_token(client, balance_id, get_min_limit):
#     response = client.crosschain_bridge.get_commission(
#         balance_id,
#         "USDT",
#         "ethereum",
#         "tron",
#         get_min_limit
#     )
#     return response.get("response").get("token")
#
#
# @pytest.fixture(scope="session")
# def transfer_id(client, balance_id, business_wallet_data, payout_wallet_data, fee_token):
#     business_address_id = business_wallet_data[1]
#     payout_address_id = payout_wallet_data[1]
#     response = client.crosschain_bridge.create_transfer(
#         balance_id,
#         business_address_id,
#         payout_address_id,
#         fee_token
#     )
#     return response.get("response").get("id")


def test_get_fee_token(client, get_min_limit):
    response = client.crosschain_bridge.get_commission_token(
        "USDT",
        "ethereum",
        "tron",
        get_min_limit
    )
    default_response_success_check(response)

#
# def test_get_limits(client):
#     response = client.crosschain_bridge.get_limits()
#     default_response_success_check(response)

# def test_get_transfer_by_id(client, transfer_id):
#     response = client.crosschain_bridge.get_transfer_by_id(transfer_id)
#     default_response_success_check(response)
