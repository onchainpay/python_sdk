from common import *


@pytest.fixture(scope="session")
def invoice_id(client):
    response = client.invoices.create_invoice(
        "USDT",
        "1",
        3600,
    )
    return response.get("response").get("id")


def test_get_invoice_by_id(client, invoice_id):
    response = client.invoices.get_invoice_by_id(invoice_id)
    default_response_success_check(response)


def test_get_invoice_by_id_fail(client):
    response = client.invoices.get_invoice_by_id("123")
    default_response_error_check(response)


def test_get_invoices(client):
    response = client.invoices.get_invoices()
    default_response_success_check(response)
