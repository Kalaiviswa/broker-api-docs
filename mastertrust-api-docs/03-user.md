# User

All requests need the `Authorization: Bearer {access_token}` header — see [Authentication](02-authentication.md).

## Profile

Get user profile information.

```
GET /api/v1/user/profile?client_id=CLIENT123
```

### Response

Success status: `200`

```json
{
  "data": {
    "account_id": "CLIENT123",
    "account_type": "",
    "backoffice_enabled": true,
    "bank_account_number": "XXXXXXXXXXXXXX",
    "bank_branch_name": "BRANCH NAME",
    "bank_name": "BANK OF BARODA",
    "branch": "BANK OF BARODA",
    "broker_id": "RCHNO",
    "city": "",
    "client_id": "CLIENT123",
    "depository": "NSDL",
    "dob": "01/01/1990",
    "dp_id": "",
    "dp_number": "IN30XXXXXXXXXXXX",
    "email_id": "user@example.com",
    "exchange_nnf": {
      "BFO": 0,
      "BSE": 0,
      "MCX": 0,
      "NFO": 0,
      "NSE": 0
    },
    "exchanges_subscribed": [
      "BSE",
      "BFO",
      "MCX",
      "NSE",
      "NFO"
    ],
    "ifsc_code": "",
    "name": "JOHN DOE",
    "office_addr": "OFFICE ADDRESS",
    "pan_number": "ABCDE1234F",
    "permanent_addr": "PERMANENT ADDRESS",
    "phone_number": "9999999999",
    "products_enabled": [
      "CNC",
      "CO",
      "MIS",
      "NRML"
    ],
    "role": {
      "id": 1,
      "name": "CLIENT"
    },
    "sex": "",
    "state": "",
    "status": "Activated",
    "twofa_enabled": true,
    "user_type": "Non-Institutional"
  },
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/user/profile?client_id=CLIENT123' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/user/profile?client_id=CLIENT123"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```

## Trading Info

Get Trading information.

```
GET /api/v1/user/trading_info
```

### Response

Success status: `200`

```json
{
  "data": {
    "client_id": "CLIENT123",
    "email_id": "user@example.com",
    "exchanges_subscribed": [
      "BSE",
      "BFO",
      "MCX",
      "NSE",
      "NFO"
    ],
    "name": "JOHN DOE",
    "products_enabled": [
      "CNC",
      "CO",
      "MIS",
      "NRML"
    ],
    "status": "Activated"
  },
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/user/trading_info' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/user/trading_info"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```
