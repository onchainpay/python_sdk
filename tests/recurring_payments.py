from common import *

MERCHANT_ID = os.getenv("MERCHANT_ID")


@pytest.fixture(scope="session")
def payment_link_id(client, n=0):
    response = client.recurring_payments.get_payment_links(MERCHANT_ID)
    link_id = response.get("response")[n].get("id")
    if link_id:
        return link_id
    payment_link_id(client, n + 1)


@pytest.fixture(scope="session")
def subscription_id(client, payment_link_id):
    response = client.recurring_payments.create_subscription(
        MERCHANT_ID,
        payment_link_id,
        "Title",
        -3,
        "USD",
        "1"
    )
    return response.get("response").get("id")


def test_get_payment_link(client, payment_link_id):
    response = client.recurring_payments.get_payment_link(payment_link_id, MERCHANT_ID)
    default_response_success_check(response)


def test_get_subscription(client, subscription_id):
    response = client.recurring_payments.get_subscription(subscription_id, MERCHANT_ID)
    default_response_success_check(response)


def test_create_payment(client, payment_link_id):
    response = client.recurring_payments.create_payment(
        MERCHANT_ID,
        payment_link_id,
        "1",
    )

    if (response.get("success") is False
            and response.get("error").get("message").startswith(
                "You can't exceed"
            )):
        assert True
        return

    default_response_success_check(response)


def test_cancel_subscription(client, subscription_id):
    response = client.recurring_payments.cancel_subscription(subscription_id, MERCHANT_ID)
    default_response_success_check(response)


def test_disabling_payment_link(client, payment_link_id):
    response = client.recurring_payments.disable_payment_link(payment_link_id, MERCHANT_ID)
    assert response.get("success") is True
