# Funds

All requests need the `Authorization: Bearer {access_token}` header — see [Authentication](02-authentication.md).

## Cash Positions

This API allows you to retrieve the cash positions for a client.

```
GET /api/v1/funds/view?client_id=CLIENT123&type=all
```

### Response

Success status: `200`

```json
{
  "data": {
    "client_id": "CLIENT123",
    "headers": [
      "Description",
      "MTM_SINGLE_LEVEL-ALL"
    ],
    "values": [
      [
        "Available",
        "74.06"
      ],
      [
        "Adhoc Margin",
        "0.000000"
      ],
      [
        "Margin Used",
        "1.93"
      ],
      [
        "Pay In",
        "0"
      ],
      [
        "Pay Out",
        "0.00"
      ],
      [
        "Cash Margin",
        "75.99"
      ],
      [
        "Collateral",
        "0.00"
      ],
      [
        "Var Margin",
        "0.00"
      ],
      [
        "Span Margin",
        "0.00"
      ],
      [
        "Premium Present",
        "0"
      ],
      [
        "Exposure Margin",
        "0.00"
      ]
    ]
  },
  "message": "",
  "status": "success"
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/funds/view?client_id=CLIENT123&type=all' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/funds/view?client_id=CLIENT123&type=all"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```
