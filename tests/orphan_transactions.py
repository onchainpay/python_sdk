from common import *


def test_get_transactions(client):
    response = client.orphan_transactions.get_transactions()
    default_response_success_check(response)


def test_get_transaction_by_id_fail(client):
    response = client.orphan_transactions.get_transaction_by_id(
        "test123"
    )
    default_response_error_check(response)


def test_get_commission_token_fail(client):
    response = client.orphan_transactions.get_commission_token(
        "test123"
    )
    default_response_error_check(response)
