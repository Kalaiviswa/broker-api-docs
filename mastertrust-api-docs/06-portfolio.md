# Portfolio

All requests need the `Authorization: Bearer {access_token}` header — see [Authentication](02-authentication.md).

## Position Book — Daywise

This API allows you to retrieve the position book for a client.

```
GET /api/v1/positions?type=live&client_id=CLIENT123
```

### Response

Success status: `200`

```json
{
  "data": [
    {
      "average_buy_price": 5.88,
      "average_sell_price": 0,
      "buy_amount": 5.88,
      "buy_quantity": 1,
      "cf_buy_amount": 0,
      "cf_buy_quantity": 0,
      "cf_sell_amount": 0,
      "cf_sell_quantity": 0,
      "client_id": "CLIENT123",
      "exchange": "NSE",
      "instrument_token": 14537,
      "ltp": 5.88,
      "multiplier": 1,
      "net_amount": -5.88,
      "net_quantity": 1,
      "previous_close": 5.83,
      "prod_type": "NRML",
      "product": "NRML",
      "realized_mtm": 0,
      "segment": null,
      "sell_amount": 0,
      "sell_quantity": 0,
      "symbol": "DISHTV",
      "token": 14537,
      "trading_symbol": "DISHTV-EQ"
    },
    {
      "average_buy_price": 47.38,
      "average_sell_price": 47.36,
      "buy_amount": 94.76,
      "buy_quantity": 2,
      "cf_buy_amount": 0,
      "cf_buy_quantity": 0,
      "cf_sell_amount": 0,
      "cf_sell_quantity": 0,
      "client_id": "CLIENT123",
      "exchange": "NSE",
      "instrument_token": 11377,
      "ltp": 47.35,
      "multiplier": 1,
      "net_amount": -0.04,
      "net_quantity": 0,
      "previous_close": 46.81,
      "prod_type": "NRML",
      "product": "NRML",
      "realized_mtm": -0.04,
      "segment": null,
      "sell_amount": 94.72,
      "sell_quantity": 2,
      "symbol": "MAHABANK",
      "token": 11377,
      "trading_symbol": "MAHABANK-EQ"
    }
  ],
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/positions?type=live&client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/positions?type=live&client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```

## Position Book — Netwise

This API allows you to retrieve the position book for a client.

```
GET /api/v1/positions?type=historical&client_id=CLIENT123
```

### Response

Success status: `200`

```json
{
  "data": [
    {
      "v_login_id": "CLIENT123",
      "actual_cf_sell_amount": 0,
      "sell_quantity": 0,
      "exchange": "NSE",
      "trading_symbol": "DISHTV-EQ",
      "net_amount_mtm": -5.88,
      "net_quantity": 1,
      "previous_close": 5.83,
      "cf_sell_quantity": 0,
      "buy_quantity": 1,
      "close_price": 5.83,
      "cf_buy_quantity": 0,
      "actual_average_sell_price": 0,
      "client_id": "CLIENT123",
      "actual_average_buy_price": 0,
      "instrument_token": 14537,
      "token": 14537,
      "cf_sell_amount": 0,
      "ltp": 5.88,
      "average_sell_price": 0,
      "prod_type": "NRML",
      "segment": null,
      "realized_mtm": 0,
      "cf_buy_amount": 0,
      "sell_amount": 0,
      "symbol": "DISHTV",
      "product": "NRML",
      "average_buy_price": 5.88,
      "actual_cf_buy_amount": 0,
      "buy_amount": 5.88,
      "pro_cli": "CLIENT",
      "multiplier": 1,
      "average_price": 5.83
    },
    {
      "v_login_id": "CLIENT123",
      "actual_cf_sell_amount": 0,
      "sell_quantity": 2,
      "exchange": "NSE",
      "trading_symbol": "MAHABANK-EQ",
      "net_amount_mtm": -0.04,
      "net_quantity": 0,
      "previous_close": 46.81,
      "cf_sell_quantity": 0,
      "buy_quantity": 2,
      "close_price": 46.81,
      "cf_buy_quantity": 0,
      "actual_average_sell_price": 0,
      "client_id": "CLIENT123",
      "actual_average_buy_price": 0,
      "instrument_token": 11377,
      "token": 11377,
      "cf_sell_amount": 0,
      "ltp": 47.38,
      "average_sell_price": 47.36,
      "prod_type": "NRML",
      "segment": null,
      "realized_mtm": -0.04,
      "cf_buy_amount": 0,
      "sell_amount": 94.72,
      "symbol": "MAHABANK",
      "product": "NRML",
      "average_buy_price": 47.38,
      "actual_cf_buy_amount": 0,
      "buy_amount": 94.76,
      "pro_cli": "CLIENT",
      "multiplier": 1,
      "average_price": 46.81
    }
  ],
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/positions?type=historical&client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/positions?type=historical&client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```

## Demat Holdings

This API allows you to retrieve the demat holdings for a client.

```
GET /api/v1/holdings?client_id=CLIENT123
```

### Response

Success status: `200`

Sample trimmed: the upstream list is shortened to the entries that show each distinct exchange / order type / status / product.

```json
{
  "data": {
    "holdings": [
      {
        "actual_buy_avg": 6.42,
        "branch_code": "",
        "buy_avg": 5.83,
        "buy_avg_mtm": 8.58,
        "client_id": "CLIENT123",
        "collateral_quantity": "2",
        "exchange": "NSE",
        "instrument_details": {
          "exchange": 1,
          "instrument_name": "EQ",
          "instrument_token": 14537,
          "trading_symbol": "DISHTV-EQ"
        },
        "isin": "INE836F01026",
        "ltp": 5.9,
        "previous_close": 5.83,
        "product": "CNC",
        "quantity": 2,
        "symbol": "DISHTV-EQ",
        "t0_price": 0,
        "t0_quantity": 0,
        "t1_price": 0,
        "t1_quantity": 0,
        "t2_price": 0,
        "t2_quantity": 0,
        "token": 14537,
        "trading_symbol": "DISHTV-EQ",
        "used_quantity": 0
      },
      {
        "actual_buy_avg": 52.25,
        "branch_code": "",
        "buy_avg": 44.23,
        "buy_avg_mtm": 52.92,
        "client_id": "CLIENT123",
        "collateral_quantity": "1",
        "exchange": "NSE",
        "instrument_details": {
          "exchange": 1,
          "instrument_name": "EQ",
          "instrument_token": 1491,
          "trading_symbol": "IFCI-EQ"
        },
        "isin": "INE039A01010",
        "ltp": 44.7,
        "previous_close": 44.23,
        "product": "CNC",
        "quantity": 1,
        "symbol": "IFCI-EQ",
        "t0_price": 0,
        "t0_quantity": 0,
        "t1_price": 0,
        "t1_quantity": 0,
        "t2_price": 0,
        "t2_quantity": 0,
        "token": 1491,
        "trading_symbol": "IFCI-EQ",
        "used_quantity": 0
      },
      {
        "actual_buy_avg": 0.76,
        "branch_code": "",
        "buy_avg": 0.69,
        "buy_avg_mtm": 0.69,
        "client_id": "CLIENT123",
        "collateral_quantity": "0",
        "exchange": "BSE",
        "instrument_details": {
          "exchange": 6,
          "instrument_name": "E",
          "instrument_token": 505343,
          "trading_symbol": "MONOT-Z"
        },
        "isin": "INE811D01024",
        "ltp": 0.7,
        "previous_close": 0.69,
        "product": "CNC",
        "quantity": 1,
        "symbol": "MONOT",
        "t0_price": 0,
        "t0_quantity": 0,
        "t1_price": 0,
        "t1_quantity": 0,
        "t2_price": 0,
        "t2_quantity": 0,
        "token": 505343,
        "trading_symbol": "MONOT",
        "used_quantity": 0
      }
    ]
  },
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/holdings?client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/holdings?client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```
