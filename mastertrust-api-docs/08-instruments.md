# Instruments

All requests need the `Authorization: Bearer {access_token}` header — see [Authentication](02-authentication.md).

## Contract Master (Scrip Token) Download

The full instrument/token list can be downloaded from:

```
GET https://masterswift-beta.mastertrust.co.in/api/v1/contract/Compact?info=download
```

## Scrip Info

This API provides detailed information about a specific script.

```
GET /api/v1/contract/<exchange>?info=scrip&token=<instrumentToken>
```

Example:

```
GET /api/v1/contract/NSE?info=scrip&token=14537
```

### Response

Success status: `200`

```json
{
  "error": {
    "code": 0,
    "message": ""
  },
  "result": {
    "board_lot_quantity": 1,
    "change_in_oi": 0,
    "exchange": 1,
    "expiry": 0,
    "higher_circuit_limit": 6.99,
    "instrument_name": "EQ",
    "instrument_token": 14537,
    "isin": "INE836F01026",
    "lower_circuit_limit": 4.66,
    "multiplier": 1,
    "open_interest": 0,
    "option_type": "",
    "precision": 2,
    "series": "EQ",
    "strike": 0,
    "symbol": "DISHTV",
    "tick_size": 0.01,
    "trading_symbol": "DISHTV-EQ",
    "underlying_token": 14537,
    "raw_expiry": 0,
    "freeze": 0,
    "instrument_type": "0",
    "issue_rate": 0,
    "issue_start_date": "18-Apr-2007",
    "list_date": "18-Apr-2007",
    "max_order_size": 0,
    "price_numerator": 0,
    "price_denominator": 0,
    "comments": "INT DIV - RE 0.50 PER SH",
    "circuit_rating": "",
    "company_name": "DISH TV INDIA LTD.",
    "display_name": "DISHTV EQ",
    "raw_tick_size": 1,
    "is_index": false,
    "tradable": true,
    "max_single_qty": 0,
    "expiry_string": "",
    "local_update_time": "",
    "market_type": "",
    "price_units": "",
    "trading_units": "",
    "last_trading_date": "",
    "tender_period_end_date": "",
    "delivery_start_date": "",
    "price_quotation": 0,
    "general_denominator": "",
    "tender_period_start_date": "",
    "delivery_units": "",
    "delivery_end_date": "",
    "trading_unit_factor": 0,
    "delivery_unit_factor": 0,
    "book_closure_end_date": "1-Jan-1980",
    "book_closure_start_date": "1-Jan-1980",
    "no_delivery_date_end": "0",
    "no_delivery_date_start": "0",
    "re_admission_date": "0",
    "record_date": "1225929600",
    "warning": "1",
    "dpr": "4.6600 - 6.9900",
    "trade_to_trade": false,
    "surveillance_indicator": 0,
    "partition_id": 0,
    "product_id": 0,
    "product_category": "",
    "month_identifier": 0,
    "close_price": "",
    "special_preopen": 1,
    "alternate_exchange": "BSE",
    "alternate_token": 532839,
    "asm": "-1",
    "gsm": "-1",
    "execution": "NA",
    "symbol2": "",
    "raw_tender_period_start_date": "",
    "raw_tender_period_end_date": "",
    "yearly_high_price": "19.55",
    "yearly_low_price": "5.77",
    "issue_maturity_date": 0,
    "var": "",
    "exposure": "",
    "span": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "tag": "",
    "last_trade_vol": "",
    "alternate_trading_symbol": "",
    "face_value": 1,
    "short_code": ""
  }
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/contract/NSE?info=scrip&token=14537' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/contract/NSE?info=scrip&token=14537"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```

## Search Scrip

This API allows you to search for scripts by keyword.

```
GET /api/v1/search?key=<keyword>
```

Example:

```
GET /api/v1/search?key=TCS
```

### Response

Success status: `200`

Sample trimmed: the upstream list is shortened to the entries that show each distinct exchange / order type / status / product.

```json
{
  "error": {
    "code": 0,
    "message": ""
  },
  "result": [
    {
      "token": 11536,
      "exchange": "NSE",
      "company": "TATA CONSULTANCY SERV LT",
      "symbol": "TCS",
      "trading_symbol": "TCS-EQ",
      "display_name": "TCS EQ",
      "score": 0.210094,
      "isin": "INE467B01029",
      "close_price": "",
      "segment": "Equity",
      "alternate": {
        "token": 532540,
        "exchange": "BSE",
        "company": "TATA CONSULTANCY SERVICES LTD.",
        "symbol": "TCS",
        "trading_symbol": "TCS-A",
        "display_name": "TCS A",
        "isin": "INE467B01029"
      }
    },
    {
      "token": 532540,
      "exchange": "BSE",
      "company": "TATA CONSULTANCY SERVICES LTD.",
      "symbol": "TCS",
      "trading_symbol": "TCS-A",
      "display_name": "TCS A",
      "score": 0.190095,
      "isin": "INE467B01029",
      "close_price": "",
      "segment": "",
      "alternate": {
        "token": 11536,
        "exchange": "NSE",
        "company": "TATA CONSULTANCY SERV LT",
        "symbol": "TCS",
        "trading_symbol": "TCS-EQ",
        "display_name": "TCS EQ",
        "isin": "INE467B01029",
        "segment": "Equity"
      }
    },
    {
      "token": 73627,
      "exchange": "NFO",
      "company": "TCS",
      "symbol": "TCS25APRFUT",
      "trading_symbol": "TCS25APRFUT",
      "display_name": "TCS25APRFUT",
      "score": 0.17969249576,
      "close_price": "",
      "segment": "NFO",
      "alternate": {}
    }
  ]
}
```

### Example

```bash
curl -X GET 'https://masterswift-beta.mastertrust.co.in/api/v1/search?key=TCS' \
  -H 'Authorization: Bearer {access_token}'
```

```python
import requests

url = "https://masterswift-beta.mastertrust.co.in/api/v1/search?key=TCS"
headers = {"Authorization": "Bearer {access_token}"}

response = requests.request("GET", url, headers=headers)
print(response.text)
```
