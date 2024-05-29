from common import *


@pytest.fixture(scope="session")
def get_min_limit(client):
    response = client.crosschain_swaps.get_limits()
    return response.get("response").get("min")


# @pytest.fixture(scope="session")
# def fee_token(client, balance_id):
#     response = client.crosschain_swaps.get_commission(
#         balance_id,
#         "USDT",
#         "USDT",
#         "ethereum",
#         "tron",
#         "0.1"
#     )
#     return response.get("response").get("token")


# @pytest.fixture(scope="session")
# def swap_id(client, balance_id, business_wallet_data, payout_wallet_data, fee_token):
#     business_address_id = business_wallet_data[1]
#     payout_address_id = payout_wallet_data[1]
#     response = client.crosschain_swaps.create_swap(
#         balance_id,
#         business_address_id,
#         payout_address_id,
#         fee_token
#     )
#     return response.get("response").get("id")


def test_get_fee_token(client, get_min_limit):
    response = client.crosschain_swaps.get_commission_token(
        "USDT",
        "USDC",
        "ethereum",
        "tron",
        get_min_limit
    )
    default_response_success_check(response)

#
# def test_get_limits(client):
#     response = client.crosschain_swaps.get_limits()
#     default_response_success_check(response)
#
#
# def test_get_withdrawal_by_id(client, swap_id):
#     response = client.crosschain_swaps.get_swaps_by_id(swap_id)
#     default_response_success_check(response)
