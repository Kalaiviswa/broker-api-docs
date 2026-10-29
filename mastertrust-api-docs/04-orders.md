# Orders

All requests need the `Authorization: Bearer {access_token}` header — see [Authentication](02-authentication.md). Order placement, modification, cancellation, and Cover/Bracket orders.

## Place Normal Order

This API allows you to place a normal trading order.

```
POST /api/v1/orders
```

### Request Body

```json
{
  "client_id": "CLIENT123",
  "disclosed_quantity": 0,
  "exchange": "NSE",
  "instrument_token": "14537",
  "market_protection_percentage": 10,
  "order_side": "BUY",
  "order_type": "LIMIT",
  "price": 5.5,
  "product": "NRML",
  "quantity": 1,
  "trigger_price": 0,
  "validity": "DAY",
  "user_order_id": "5002681"
}
```

### Response

Success status: `200`

```json
{
  "data": {
    "client_order_id": "250328000022151",
    "oms_order_id": "250328000022151",
    "user_order_id": 5002681
  },
  "message": "Order place successfully",
  "status": "success"
}
```

### Example

```bash
curl -X POST 'https://masterswift-beta.mastertrust.co.in/api/v1/orders' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Content-Type: application/json' \
  -d '{"client_id": "CLIENT123", "disclosed_quantity": 0, "exchange": "NSE", "instrument_token": "14537", "market_protection_percentage": 10, "order_side": "BUY", "order_type": "LIMIT", "price": 5.5, "product": "NRML", "quantity": 1, "trigger_price": 0, "validity": "DAY", "user_order_id": "5002681"}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders"
headers = {"Authorization": "Bearer {access_token}"}

payload = {
    "client_id": "CLIENT123",
    "disclosed_quantity": 0,
    "exchange": "NSE",
    "instrument_token": "14537",
    "market_protection_percentage": 10,
    "order_side": "BUY",
    "order_type": "LIMIT",
    "price": 5.5,
    "product": "NRML",
    "quantity": 1,
    "trigger_price": 0,
    "validity": "DAY",
    "user_order_id": "5002681"
}

response = requests.request("POST", url, headers=headers, json=payload)
print(response.text)
```

## Modify Order

This API allows you to modify an existing normal trading order.

```
PUT /api/v1/orders
```

### Request Body

```json
{
  "exchange": "NSE",
  "order_type": "LIMIT",
  "instrument_token": 14537,
  "quantity": 1,
  "disclosed_quantity": 0,
  "price": 5.6,
  "trigger_price": 0,
  "order_side": "BUY",
  "product": "NRML",
  "client_id": "CLIENT123",
  "oms_order_id": "250328000020616",
  "validity": "DAY"
}
```

### Response

Success status: `200`

```json
{
  "data": {
    "oms_order_id": [
      " 250328000020616"
    ]
  },
  "message": "Order modification request submitted",
  "status": "success"
}
```

### Example

```bash
curl -X PUT 'https://masterswift-beta.mastertrust.co.in/api/v1/orders' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Content-Type: application/json' \
  -d '{"exchange": "NSE", "order_type": "LIMIT", "instrument_token": 14537, "quantity": 1, "disclosed_quantity": 0, "price": 5.6, "trigger_price": 0, "order_side": "BUY", "product": "NRML", "client_id": "CLIENT123", "oms_order_id": "250328000020616", "validity": "DAY"}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders"
headers = {"Authorization": "Bearer {access_token}"}

payload = {
    "exchange": "NSE",
    "order_type": "LIMIT",
    "instrument_token": 14537,
    "quantity": 1,
    "disclosed_quantity": 0,
    "price": 5.6,
    "trigger_price": 0,
    "order_side": "BUY",
    "product": "NRML",
    "client_id": "CLIENT123",
    "oms_order_id": "250328000020616",
    "validity": "DAY"
}

response = requests.request("PUT", url, headers=headers, json=payload)
print(response.text)
```

## Cancel Normal Order

This API allows you to cancel an existing normal trading order.

```
DELETE /api/v1/orders/<omsOrderNum>?client_id=<clientID>
```

Example:

```
DELETE /api/v1/orders/250328000020616?client_id=CLIENT123
```

### Response

Success status: `200`

```json
{
  "data": {
    "oms_order_id": "250328000020616"
  },
  "message": "Order cancellation request submitted for OMS Order: 250328000020616",
  "status": "success"
}
```

### Example

```bash
curl -X DELETE 'https://masterswift-beta.mastertrust.co.in/api/v1/orders/250328000020616?client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders/250328000020616?client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("DELETE", url, headers=headers)
print(response.text)
```

## Place Cover Order (CO)

This API allows you to place a cover order. Note: May not be supported / enabled in all environments by default, please check with your Broker.

```
POST /api/v1/orders
```

### Request Body

```json
{
  "client_id": "CLIENT123",
  "disclosed_quantity": 0,
  "exchange": "NSE",
  "instrument_token": "14537",
  "market_protection_percentage": 10,
  "order_side": "BUY",
  "order_type": "LIMIT",
  "price": 5.5,
  "product": "CO",
  "quantity": 1,
  "trigger_price": 5.4,
  "validity": "DAY",
  "user_order_id": "5002681",
  "device": "WEB"
}
```

### Response

Success status: `200`

```json
{
  "data": {
    "client_order_id": "250328000026369",
    "oms_order_id": "250328000026369",
    "user_order_id": 5002681
  },
  "message": "Order place successfully",
  "status": "success"
}
```

### Example

```bash
curl -X POST 'https://masterswift-beta.mastertrust.co.in/api/v1/orders' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Content-Type: application/json' \
  -d '{"client_id": "CLIENT123", "disclosed_quantity": 0, "exchange": "NSE", "instrument_token": "14537", "market_protection_percentage": 10, "order_side": "BUY", "order_type": "LIMIT", "price": 5.5, "product": "CO", "quantity": 1, "trigger_price": 5.4, "validity": "DAY", "user_order_id": "5002681", "device": "WEB"}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders"
headers = {"Authorization": "Bearer {access_token}"}

payload = {
    "client_id": "CLIENT123",
    "disclosed_quantity": 0,
    "exchange": "NSE",
    "instrument_token": "14537",
    "market_protection_percentage": 10,
    "order_side": "BUY",
    "order_type": "LIMIT",
    "price": 5.5,
    "product": "CO",
    "quantity": 1,
    "trigger_price": 5.4,
    "validity": "DAY",
    "user_order_id": "5002681",
    "device": "WEB"
}

response = requests.request("POST", url, headers=headers, json=payload)
print(response.text)
```

## Place Bracket Order (BO)

This API allows you to place a bracket order. Note: May not be supported / enabled in all environments by default, please check with your Broker.

```
POST /api/v1/orders/bracket
```

### Request Body

```json
{
  "exchange": "NSE",
  "instrument_token": 14537,
  "client_id": "CLIENT123",
  "order_type": "LIMIT",
  "price": "5.5",
  "quantity": 1,
  "disclosed_quantity": 0,
  "validity": "DAY",
  "product": "BO",
  "order_side": "BUY",
  "device": "WEB",
  "user_order_id": 10002,
  "trigger_price": 0,
  "stop_loss_value": "5",
  "square_off_value": "6",
  "trailing_stop_loss": 0,
  "is_trailing": false
}
```

### Response

Success status: `200`

```json
{
  "data": {
    "client_order_id": "250328000028314"
  },
  "message": "Order place successfully",
  "status": "success"
}
```

### Example

```bash
curl -X POST 'https://masterswift-beta.mastertrust.co.in/api/v1/orders/bracket' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Content-Type: application/json' \
  -d '{"exchange": "NSE", "instrument_token": 14537, "client_id": "CLIENT123", "order_type": "LIMIT", "price": "5.5", "quantity": 1, "disclosed_quantity": 0, "validity": "DAY", "product": "BO", "order_side": "BUY", "device": "WEB", "user_order_id": 10002, "trigger_price": 0, "stop_loss_value": "5", "square_off_value": "6", "trailing_stop_loss": 0, "is_trailing": false}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders/bracket"
headers = {"Authorization": "Bearer {access_token}"}

payload = {
    "exchange": "NSE",
    "instrument_token": 14537,
    "client_id": "CLIENT123",
    "order_type": "LIMIT",
    "price": "5.5",
    "quantity": 1,
    "disclosed_quantity": 0,
    "validity": "DAY",
    "product": "BO",
    "order_side": "BUY",
    "device": "WEB",
    "user_order_id": 10002,
    "trigger_price": 0,
    "stop_loss_value": "5",
    "square_off_value": "6",
    "trailing_stop_loss": 0,
    "is_trailing": false
}

response = requests.request("POST", url, headers=headers, json=payload)
print(response.text)
```

## Exit Bracket Order

This API allows you to exit a bracket order. Note: May not be supported / enabled in all environments by default, please check with your Broker.

```
DELETE /api/v1/orders/bracket
```

### Request Body

```json
{
  "oms_order_id": "250328000028870",
  "leg_order_indicator": "250328000028870",
  "status": "open",
  "client_id": "CLIENT123"
}
```

### Response

Success status: `200`

```json
{
  "data": {},
  "message": "Ok",
  "status": "success"
}
```

### Example

```bash
curl -X DELETE 'https://masterswift-beta.mastertrust.co.in/api/v1/orders/bracket?=' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Content-Type: application/json' \
  -d '{"oms_order_id": "250328000028870", "leg_order_indicator": "250328000028870", "status": "open", "client_id": "CLIENT123"}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders/bracket?="
headers = {"Authorization": "Bearer {access_token}"}

payload = {
    "oms_order_id": "250328000028870",
    "leg_order_indicator": "250328000028870",
    "status": "open",
    "client_id": "CLIENT123"
}

response = requests.request("DELETE", url, headers=headers, json=payload)
print(response.text)
```

## Exit Cover Order

This API allows you to exit a cover order. Note: May not be supported / enabled in all environments by default, please check with your Broker.

```
DELETE /api/v1/orders/cover
```

### Request Body

```json
{
  "oms_order_id": "250328000026369",
  "leg_order_indicator": "250328000026369",
  "client_id": "CLIENT123"
}
```

### Response

Success status: `200`

```json
{
  "data": {
    "oms_order_id": "250328000026369"
  },
  "message": "Exit Cover Order request submitted for OMS Order: 250328000026369",
  "status": "success"
}
```

### Example

```bash
curl -X DELETE 'https://masterswift-beta.mastertrust.co.in/api/v1/orders/cover' \
  -H 'Authorization: Bearer {access_token}' \
  -H 'Content-Type: application/json' \
  -d '{"oms_order_id": "250328000026369", "leg_order_indicator": "250328000026369", "client_id": "CLIENT123"}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/orders/cover"
headers = {"Authorization": "Bearer {access_token}"}

payload = {
    "oms_order_id": "250328000026369",
    "leg_order_indicator": "250328000026369",
    "client_id": "CLIENT123"
}

response = requests.request("DELETE", url, headers=headers, json=payload)
print(response.text)
```
