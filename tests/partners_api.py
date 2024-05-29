import time

from common import *

PUBLIC_KEY = os.getenv("PARTNERS_API_PUBLIC_KEY")
PRIVATE_KEY = os.getenv("PARTNERS_API_PRIVATE_KEY")

if not PUBLIC_KEY or not PRIVATE_KEY:
    raise ValueError("PARTNERS_API_PUBLIC_KEY and PARTNERS_API_PRIVATE_KEY are required")


@pytest.fixture(scope="session")
def partners_client(client):
    client.init_partners_api(PUBLIC_KEY, PRIVATE_KEY)
    return client


@pytest.fixture(scope="session")
def user_id(partners_client):
    response = partners_client.partners_api.create_user(
        "mail" + str(int(time.time())) + "@gmail.com"
    )
    return response.get("response").get("id")


@pytest.fixture(scope="session")
def organization_id(partners_client, user_id):
    response = partners_client.partners_api.create_organization(user_id, "Organization")
    return response.get("response").get("result")


@pytest.fixture(scope="session")
def api_key_id(partners_client, user_id, organization_id):
    response = partners_client.partners_api.create_api_key(user_id, organization_id, "key")
    return response.get("response").get("id")


def test_get_user_by_id(partners_client, user_id):
    response = partners_client.partners_api.get_user_by_id(user_id)
    default_response_success_check(response)


def test_get_users(partners_client):
    response = partners_client.partners_api.get_users()
    default_response_success_check(response)


def test_create_organization(partners_client, user_id):
    response = partners_client.partners_api.create_organization(user_id, "Organization")
    default_response_success_check(response)


def test_get_organizations(partners_client, user_id):
    response = partners_client.partners_api.get_organizations(user_id)
    default_response_success_check(response)


def test_get_user_advanced_balance(partners_client, user_id, organization_id):
    response = partners_client.partners_api.get_user_advanced_balance(user_id, organization_id)
    default_response_success_check(response)


def test_get_general_tariffs(partners_client):
    response = partners_client.partners_api.get_general_tariffs()
    default_response_success_check(response)


def test_create_or_update_tariff(partners_client, user_id, organization_id):
    response = partners_client.partners_api.create_or_update_organization_tariff(
        user_id,
        organization_id,
        "FIAT_CRYPTO_EXCHANGE",
        "1",
        "FIXED"
    )
    default_response_success_check(response)


def test_create_api_key(partners_client, user_id, organization_id):
    response = partners_client.partners_api.create_api_key(user_id, organization_id, "key")
    default_response_success_check(response)


def test_get_api_keys(partners_client, user_id, organization_id):
    response = partners_client.partners_api.get_api_keys(user_id, organization_id)
    default_response_success_check(response)


def test_delete_api_key(partners_client, user_id, organization_id, api_key_id):
    response = partners_client.partners_api.delete_api_key(user_id, organization_id, api_key_id)
    assert response.get("success") is True
