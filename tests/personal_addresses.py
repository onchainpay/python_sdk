import time

from common import *


@pytest.fixture(scope="session")
def user_id(client):
    response = client.personal_addresses.create_or_update_user(
        "user" + str(int(1000 * time.time())),
        "user@mail.com",
        "User Name",
    )
    return response.get("response").get("id")


def test_get_user_address(client, user_id):
    response = client.personal_addresses.get_user_address(user_id, "USDT", "ethereum")
    default_response_success_check(response)


def test_get_user_by_id(client, user_id):
    response = client.personal_addresses.get_user(user_id)
    default_response_success_check(response)


def test_get_user_addresses(client, user_id):
    response = client.personal_addresses.get_user_addresses(user_id, network=["ethereum"])
    default_response_success_check(response)


def test_get_user_addresses_without_user_id(client):
    response = client.personal_addresses.get_user_addresses(
        currency=["USDT"]
    )
    default_response_success_check(response)
