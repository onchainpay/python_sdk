from common import *


# @pytest.fixture(scope="session")
# def fee_token(client, balance_id, business_wallet_data):
#     business_address_id = business_wallet_data[1]
#     response = client.withdraws.get_commission(
#         balance_id,
#         business_address_id,
#         "0.1"
#     )
#     return response.get("response").get("token")
#
#
# @pytest.fixture(scope="session")
# def withdrawal_id(client, balance_id, business_wallet_data, payout_wallet_data, fee_token):
#     business_address_id = business_wallet_data[1]
#     payout_address = payout_wallet_data[0]
#     response = client.withdraws.create_withdrawal(
#         balance_id,
#         business_address_id,
#         payout_address,
#         "0.1",
#         fee_token
#     )
#     return response.get("response").get("id")


# def test_create_async_withdrawal(
#         client,
#         balance_id,
#         business_wallet_data,
#         payout_wallet_data,
#         fee_token
# ):
#     business_address_id = business_wallet_data[1]
#     payout_address = payout_wallet_data[0]
#     response = client.withdraws.create_async_withdrawal(
#         balance_id,
#         business_address_id,
#         payout_address,
#         "0.1",
#         fee_token,
#         webhook_url="https://webhook.site/example"
#     )
#     default_response_success_check(response)

def test_get_fee(client, business_wallet_data):
    business_address_id = business_wallet_data[1]
    response = client.withdraws.get_commission_token(
        business_address_id,
        "0.1"
    )
    default_response_success_check(response)

#
# def test_get_withdrawal_by_id(client, withdrawal_id):
#     response = client.withdraws.get_withdrawal_by_id(withdrawal_id)
#     default_response_success_check(response)
