# OnchainPay SDK

OnchainPay SDK is a comprehensive JavaScript library designed to streamline the integration of blockchain-based payment solutions into various applications. This SDK provides developers with the tools necessary to facilitate secure, transparent, and efficient transactions on supported blockchain networks.

Key Features:

- **Ease of Integration**: Simplifies the process of adding blockchain payment capabilities to your applications.
- **Security**: Ensures high-level security for all transactions using blockchain technology.
- **Transparency**: Leverages the transparency of blockchain networks to provide clear and verifiable transaction records.
- **Multi-Network Support**: Supports multiple blockchain networks, providing flexibility and scalability.

For detailed documentation, installation guides, and API references, please visit OnchainPay Documentation.

This package makes it easy [OnChainPay Api](https://docs.onchainpay.io/).

## Installation

`pip install onchainpay-api`

## Use

Go to your personal account
[https://ocp.onchainpay.io/api-keys](https://ocp.onchainpay.io/api-keys)
and get api-keys.

*Substitute keys in class call:*

```python
from onchainpay_api import Client

client = Client("__PUBLIC_KEY__", "__PRIVATE_KEY__")
```

### Check signature

You can test your signature within this method

```python
checkSignature = client.basic_actions.check_x_api_signature

if not checkSignature["success"]:
    print("Signature incorrect", checkSignature)
else:
    if checkSignature["response"]["checkSignatureResult"]:
        print("Signature correct")
    else:
        print("Signature incorrect:", checkSignature["response"]["errors"][0])
```

### Fetch available currencies

Get list of available currencies for depositing/withdrawing

```python
availableCurrencies = client.basic_actions.get_currencies()

if not availableCurrencies["success"]:
    print("Request error", availableCurrencies)
else:
    for currency in availableCurrencies["response"]:
        print("%s (%s) = %s".format(currency["currency"], currency["alias"], currency["priceUSD"]))
        
        if len(currency["networks"]) > 0:
            print("\tnetworks:")
            
            for network in currency["networks"]:
                print("\t\t%s %s".format(network["name"], network["alias"]))
```

### Get currencies price-rate

Get price rate from one currency to another


```python
price = client.basic_actions.get_currency_price(fromCurrency="ETH", toCurrency="USDT")

if not price["success"]:
    print("Request error", price)
else:
    print("Price", price["response"])
```

### Get advanced balances info

Get info about advanced balance by its id

```python
balance = client.advanced_account.get_advanced_balance()

if not balance["success"]:
    print("Request error", balance)
else:
    print("[%s] (%s) \n\tAvailable for deposit: %s".format(balance["response"]["advancedBalanceId"], balance["response"]["currency"], ", ".join(balance["response"]["availableCurrenciesForDeposit"])))
```

### Create order

```python
from onchainpay_api import Client


def main():
    order_link = create_order(currency="USDT", network="tron", amount="100")

    #


def create_order(currency, network, amount):
    client = Client("__PUBLIC_KEY__", "__PRIVATE_KEY__")

    order = client.orders.create_order(
        currency=currency,
        network=network,
        amount=amount,
        order="Order #1234567",
        errorWebhook="https://merchant.domain/webhook-url",
        successWebhook="https://merchant.domain/webhook-url",
        returnUrl="https://merchant.domain",
        description="Buy some item",
    )

    if not order["success"]:
        raise order["error"]["message"]

    return order["response"]["link"]
```

### Auto-swap to external address

```python
from onchainpay_api import Client


def main():
    auto_swap_id = make_withdrawal(currency="USDT", network="tron", address="TUfVHn...DDC", amount="100")
    
    #


def make_withdrawal(currency, network, address, amount):
    client = Client("__PUBLIC_KEY__", "__PRIVATE_KEY__")

    swap = client.auto_swaps.create_swap(
        address=address,
        currency=currency,
        network=network,
        amountTo=amount,
        webhook="https://merchant.domain/webhook-url",
    )

    if not swap["success"]:
        raise swap["error"]["message"]

    return swap["response"]["id"]
```
