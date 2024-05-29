import os

import pytest
from dotenv import load_dotenv
from onchainpay_api import Client

load_dotenv()

PUBLIC_KEY = os.getenv("ONCHAINPAY_PUBLIC_KEY")
PRIVATE_KEY = os.getenv("ONCHAINPAY_PRIVATE_KEY")

if not PUBLIC_KEY or not PRIVATE_KEY:
    raise ValueError("PUBLIC_KEY and PRIVATE_KEY are required")


@pytest.fixture(scope="session")
def client():
    return Client(PUBLIC_KEY, PRIVATE_KEY)


@pytest.fixture(scope="session")
def business_wallet_data(client):
    response = client.blockchain_address.create_business_address(
        currency="USDT",
        network="ethereum",
        alias="USDT",
        comment="Comment...",
    )
    address = response.get("response").get("address")
    address_id = response.get("response").get("id")
    return address, address_id


def default_response_success_check(response):
    assert response.get("success") is True
    assert response.get("error") is None
    assert response.get("response") is not None


def default_response_error_check(response):
    assert response.get("success") is False
    assert response.get("error") is not None
    assert response.get("response") is None
