import time

from common import *


@pytest.fixture(scope="session")
def address_id(client):
    response = client.address_book.add_address(
        "0xe2d3A739EFFCd3A99387d015E260eEFAc72EBea2",
        ["ethereum"],
        "test" + str(int(time.time()))
    )
    return response.get("response").get("id")


def test_update_address(client, address_id):
    response = client.address_book.update_address(
        address_id,
        "0x3E2d3A739EFFCd3A99387d015E260eEFAc72EBea2",
        "test" + str(int(time.time()))
    )
    assert response.get("success") is True


def test_delete_address(client, address_id):
    response = client.address_book.delete_address(address_id)
    assert response.get("success") is True


def test_get_addresses(client):
    response = client.address_book.get_addresses()
    default_response_success_check(response)
