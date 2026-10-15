# Order Book, Trade Book & Order History

All requests need the `Authorization: Bearer {access_token}` header — see [Authentication](02-authentication.md).

## Order Book — Pending

This API allows you to retrieve the order book for a client.

```
GET /api/v1/orders?type=pending&client_id=CLIENT123
```

### Response

Success status: `200`

```json
{
  "data": {
    "orders": [
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "1100000020022029",
        "series": "",
        "square_off?": false,
        "exchange": "NSE",
        "mode": "NEW",
        "device": null,
        "lot_size": 1,
        "login_id": "CLIENT123",
        "order_side": "BUY",
        "oms_order_id": "250328000022151",
        "order_type": "LIMIT",
        "trading_symbol": "DISHTV-EQ",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 1,
        "product": "NRML",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "open",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "5.50",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 1743137188,
        "user_order_id": "5002681",
        "rejection_reason": "--",
        "instrument_token": "14537",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 1,
        "client_id": "CLIENT123",
        "order_entry_time": 1743137188
      }
    ]
  },
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/orders?type=pending&client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders?type=pending&client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```

## Order Book — Completed

This API allows you to retrieve the order book for a client.

```
GET /api/v1/orders?type=completed&client_id=CLIENT123
```

### Response

Success status: `200`

Sample trimmed: the upstream list is shortened to the entries that show each distinct exchange / order type / status / product.

```json
{
  "data": {
    "orders": [
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "1100000017829964",
        "series": "",
        "square_off?": false,
        "exchange": "NSE",
        "mode": "NEW",
        "device": null,
        "lot_size": 1,
        "login_id": "CLIENT123",
        "order_side": "BUY",
        "oms_order_id": "250328000020616",
        "order_type": "LIMIT",
        "trading_symbol": "DISHTV-EQ",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 1,
        "product": "NRML",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "cancelled",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "5.60",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 1743136998,
        "user_order_id": "5002681",
        "rejection_reason": "--",
        "instrument_token": "14537",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 1,
        "client_id": "CLIENT123",
        "order_entry_time": 1743136651
      },
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "NA",
        "series": "",
        "square_off?": false,
        "exchange": "NSE",
        "mode": "NEW",
        "device": null,
        "lot_size": 600,
        "login_id": "CLIENT123",
        "order_side": "SELL",
        "oms_order_id": "250328000000260",
        "order_type": "LIMIT",
        "trading_symbol": "ACTIVEINFR-ST",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 600,
        "product": "CNC",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "rejected",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "99.85",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 0,
        "user_order_id": null,
        "rejection_reason": "RMS:Rule: Check T1 holdings including TT/BE/Z/T/TS ,No Holdings Present  for entity account-CLIENT123 across exchange for  segment CASH across product ",
        "instrument_token": "30467",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 600,
        "client_id": "CLIENT123",
        "order_entry_time": 1743131694
      },
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "NA",
        "series": "",
        "square_off?": false,
        "exchange": "MCX",
        "mode": "NEW",
        "device": null,
        "lot_size": 100,
        "login_id": "CLIENT123",
        "order_side": "SELL",
        "oms_order_id": "250328000000247",
        "order_type": "LIMIT",
        "trading_symbol": "CRUDEOIL25APRFUT",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 1,
        "product": "NRML",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "rejected",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "5991.00",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 0,
        "user_order_id": null,
        "rejection_reason": "RMS:Margin Exceeds,Required:205832.94, Available:75.99 for entity account-CLIENT123 across exchange across segment across product ",
        "instrument_token": "441305",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 1,
        "client_id": "CLIENT123",
        "order_entry_time": 1743131653
      },
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "NA",
        "series": "",
        "square_off?": false,
        "exchange": "NFO",
        "mode": "NEW",
        "device": null,
        "lot_size": 75,
        "login_id": "CLIENT123",
        "order_side": "SELL",
        "oms_order_id": "250328000000238",
        "order_type": "LIMIT",
        "trading_symbol": "NIFTY25APRFUT",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 75,
        "product": "NRML",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "rejected",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "23699.75",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 0,
        "user_order_id": null,
        "rejection_reason": "RMS:Margin Exceeds,Required:200544.22, Available:75.99 for entity account-CLIENT123 across exchange across segment across product ",
        "instrument_token": "54452",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 75,
        "client_id": "CLIENT123",
        "order_entry_time": 1743131614
      },
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "NA",
        "series": "",
        "square_off?": false,
        "exchange": "BFO",
        "mode": "NEW",
        "device": null,
        "lot_size": 20,
        "login_id": "CLIENT123",
        "order_side": "SELL",
        "oms_order_id": "250328000000236",
        "order_type": "LIMIT",
        "trading_symbol": "SENSEX25401FUT",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 20,
        "product": "NRML",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "rejected",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "77899.75",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 0,
        "user_order_id": "10003",
        "rejection_reason": "RMS:Margin Exceeds,Required:175144.34, Available:75.99 for entity account-CLIENT123 across exchange across segment across product ",
        "instrument_token": "863673",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 20,
        "client_id": "CLIENT123",
        "order_entry_time": 1743131604
      },
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "NA",
        "series": "",
        "square_off?": false,
        "exchange": "BSE",
        "mode": "NEW",
        "device": null,
        "lot_size": 1,
        "login_id": "CLIENT123",
        "order_side": "SELL",
        "oms_order_id": "250328000000234",
        "order_type": "LIMIT",
        "trading_symbol": "SBIN-A",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 1,
        "product": "CNC",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "rejected",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "769.80",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 0,
        "user_order_id": null,
        "rejection_reason": "RMS:Rule: Check T1 holdings including TT/BE/Z/T/TS ,No Holdings Present  for entity account-CLIENT123 across exchange for  segment CASH across product ",
        "instrument_token": "500112",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 1,
        "client_id": "CLIENT123",
        "order_entry_time": 1743131595
      },
      {
        "disclosed_quantity": 0,
        "average_price": "0.00",
        "exchange_order_id": "NA",
        "series": "",
        "square_off?": false,
        "exchange": "BFO",
        "mode": "NEW",
        "device": null,
        "lot_size": 4000,
        "login_id": "CLIENT123",
        "order_side": "BUY",
        "oms_order_id": "250328000000058",
        "order_type": "MARKET",
        "trading_symbol": "SAIL25APRFUT",
        "stop_loss_value": null,
        "market_protection_percentage": 0,
        "quantity": 4000,
        "product": "NRML",
        "trailing_stop_loss": null,
        "last_activity_reference": 0,
        "order_tag": "",
        "validity": "DAY",
        "segment": "",
        "average_trade_price": "0.00",
        "square_off_value": null,
        "pro_cli": "CLIENT",
        "order_status": "rejected",
        "order_status_info": "",
        "nnf_id": 0,
        "amo": false,
        "trigger_price": "0.00",
        "leg_order_indicator": "",
        "price": "0.00",
        "is_trailing": false,
        "trade_price": 0,
        "rejection_code": 0,
        "filled_quantity": 0,
        "target_price_type": "absolute",
        "exchange_time": 0,
        "user_order_id": "10003",
        "rejection_reason": "RMS:Margin Exceeds,Required:120826.66, Available:75.99 for entity account-CLIENT123 across exchange across segment across product ",
        "instrument_token": "847780",
        "deposit": 0,
        "contract_description": {},
        "remaining_quantity": 4000,
        "client_id": "CLIENT123",
        "order_entry_time": 1743130175
      }
    ]
  },
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/orders?type=completed&client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders?type=completed&client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```

## Trade Book

This API allows you to retrieve the trade book for a client.

```
GET /api/v1/trades?client_id=CLIENT123
```

### Response

Success status: `200`

```json
{
  "data": {
    "trades": [
      {
        "book_type": "",
        "broker_id": "",
        "client_id": "CLIENT123",
        "disclosed_vol": 0,
        "disclosed_vol_remaining": 0,
        "exchange": "NSE",
        "exchange_order_id": "1100000020022029",
        "exchange_time": 1743137188,
        "fill_number": "202485785",
        "filled_quantity": 1,
        "good_till_date": "",
        "instrument_token": 14537,
        "login_id": null,
        "oms_order_id": "250328000022151",
        "order_entry_time": 1743137537,
        "order_price": 5.88,
        "order_side": "BUY",
        "order_type": "MKT",
        "original_vol": 0,
        "pan": "ABCDE1234F",
        "pro_cli": "--",
        "product": "NRML",
        "remaining_quantity": null,
        "trade_number": "202485785",
        "trade_price": 5.88,
        "trade_quantity": 1,
        "trade_time": 1743137537,
        "trading_symbol": "DISHTV-EQ",
        "trigger_price": 0,
        "v_login_id": null,
        "vol_filled_today": "Filledqty"
      }
    ]
  },
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/trades?client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/trades?client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```

## Order History

This API allows you to retrieve the history of a specific order.

```
GET /api/v1/order/<omsOrderNum>/history?client_id=<clientID>
```

Example:

```
GET /api/v1/order/250328000022151/history?client_id=CLIENT123
```

### Response

Success status: `200`

Sample trimmed: the upstream list is shortened to the entries that show each distinct exchange / order type / status / product.

```json
{
  "data": [
    {
      "avg_price": 5.88,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": "1100000020022029",
      "exchange_time": "28-Mar-2025 10:22:17",
      "fill_quantity": 1,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "MARKET",
      "price": 0,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "complete",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    },
    {
      "avg_price": 0,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": "1100000020022029",
      "exchange_time": "28-Mar-2025 10:22:17",
      "fill_quantity": 0,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "MARKET",
      "price": 0,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "open",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    },
    {
      "avg_price": 0,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": "1100000020022029",
      "exchange_time": "28-Mar-2025 10:22:17",
      "fill_quantity": 0,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "LIMIT",
      "price": 5.5,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "modified",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    },
    {
      "avg_price": 0,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": "1100000020022029",
      "exchange_time": "28-Mar-2025 10:16:28",
      "fill_quantity": 0,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "LIMIT",
      "price": 5.5,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "modify pending",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    },
    {
      "avg_price": 0,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": "1100000020022029",
      "exchange_time": "28-Mar-2025 10:16:28",
      "fill_quantity": 0,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "LIMIT",
      "price": 5.5,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "modify validation pending",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    },
    {
      "avg_price": 0,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": null,
      "exchange_time": "--",
      "fill_quantity": 0,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "LIMIT",
      "price": 5.5,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "open pending",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    },
    {
      "avg_price": 0,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": null,
      "exchange_time": "--",
      "fill_quantity": 0,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "LIMIT",
      "price": 5.5,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "validation pending",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    },
    {
      "avg_price": 0,
      "client_id": "CLIENT123",
      "client_order_id": "5002681",
      "created_at": null,
      "disclosed_quantity": "0",
      "exchange": "NSE",
      "exchange_order_id": null,
      "exchange_time": "--",
      "fill_quantity": 0,
      "last_modified": null,
      "login_id": "CLIENT123",
      "modified_at": null,
      "order_id": "250328000022151",
      "order_mode": null,
      "order_side": "BUY",
      "order_type": "LIMIT",
      "price": 5.5,
      "product": "NRML",
      "quantity": 1,
      "reject_reason": "--",
      "remaining_quantity": null,
      "segment": "Capital",
      "status": "put order req received",
      "symbol": "DISHTV",
      "token": 14537,
      "trigger_price": 0,
      "underlying_token": 14537,
      "validity": "DAY"
    }
  ],
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/order/250328000022151/history?client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/order/250328000022151/history?client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```
