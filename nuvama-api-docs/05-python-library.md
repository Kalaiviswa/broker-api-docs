# Python library for Accessing the Services Provided by Nuvama

The Library API Connect is a set of REST-like APIs that expose many capabilities required to build
a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live
market data, and more, with the simple HTTP API collection This module provides an easy to use abstraction
over the HTTP APIs. The HTTP calls have been converted to methods and their JSON responses are returned.

Python SDK :

- API version: v1

## Python supported

- Python 3.7 or later [with optional venv]

## PyPi Dependencies

- [urllib3](https://pypi.org/project/urllib3/) == 1.26.6
- [requests](https://pypi.org/project/requests/) == 2.26.0

We recommend using [pip](https://pip.pypa.io/en/stable/installation/) to install the latest
version of the packages:

```python
pip install urllib3==1.26.6
pip install requests==2.26.0
```

For Specific version Installation:

```python
pip install APIConnect==2.0.0
```

NOTE: It is recommend to install dependencies after activating virtual enviroment, to avoid conflicts between
installed packages.
Here you can find, [How to create virtual enviroment?](https://docs.python.org/3/library/venv.html)

## Configuration from external INI file

When using APIConnect wrapper ,various parameters are read from the [Settings.ini](https://www.nuvamawealth.com/library-documentation/source/assets/settings-python.zip) file.These
parameters are configurable. Description for these parameters is given below.

| Parameters | Description | Remarks |
| --- | --- | --- |
| [GLOBAL] | Contains global configuration |  |
| LOG_LEVEL | Contains logging related configuration | DEBUG |
| LOG_FILE | Absolute path to the logging file. | apiconnect.log |
| [PROXY] | Contains proxy related configuration |  |
| HTTP_PROXY | HTTP connection proxy URL. |  |
| HTTPS_PROXY | HTTP connection proxy URL. |  |
| SSL_VERIFY | SSL Verification. | False |
| [STREAM] | Streaming socket proxy related configuration |  |
| HOST | Host address of streaming socket. | ncst.nuvamawealth.com |
| PORT | Port of streaming socket. | 9443 |

# APIConnect documentation

- [User Login Flow](https://www.nuvamawealth.com/library-documentation/docs/UserLoginFlow.md.html)

## Getting Started

```python
#!python
  from APIConnect.APIConnect import APIConnect
# Redirect the user to the login url - <https://www.nuvamawealth.com/api-connect/login?api_key=xxx>
# after the login flow, You will get requestId.
# Generate a session with this request id
# as follows.
api_connect = APIConnect("apiKey", "api_secret_password", "requestId", True, "File_path_to_external_INI_file");
# Place an order
response = api_connect.PlaceTrade('symbol',
                          'exchange',
                          'buy-sell',
                          validity',
                          'orderType',
                          'quantity',
                          'exchangeCode',
                          'limitPrice',
                          'productCode');
# Fetch all orders
api_connect.OrderBook();
#Fetch all trades
api_connect.TradeBook();
```
