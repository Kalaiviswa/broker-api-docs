# Market Data API: Auth

## Login (POST)

You can log in to the application using the POST /auth/login request. You will receive a token parameter in the response, which must be used in subsequent requests. All request bodies should have the content type application/json and contain valid JSON.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/auth/login
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| secretKey | SecretKey (String, 20) | **Y** | The predefined secret key assigned to the client. |
| appKey | AppKey (String, 20) | **Y** | Api Version number of the server. |

### Request Body JSON

```json
{
"secretKey": "Doqg107#6V",
"appKey": "3064470037e8c577",
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| token | Token (String, 500) | The authentication token used with every subsequent request, unless it is invalidated by the logout API. |
| userID | UserID (String, 15) | UserID of the Dashboard. |
| appVersion | AppVersion (String, 50) | Marketdata app version. |
| application_expiry_date | Application_Expiry_Date (String, 50) | Application expiry date. |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Provided Valid Credentials",
    "result": {
      "token":
      "eyJ1c2VySWQiOiJDSEFVEFMSSIsInB1YmxpY0tleSI6IjMwNjQ0NzdlOGM1NzciLCJpYXQiOjE1NTI0Nzk0NjEsImV4cCI6MTU1MzE1MjMxMX0",
      "userID": "ABC",
      "appVersion": "5.0.15",
      "application_expiry_date": "29-09-2026"
    }
  }
]
```

## Logout (DELETE)

You can log out of the application using the delete /auth/logout request. You need to pass the authorization token in the request. You will receive a success status code in the response.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/auth/logout
```

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "successfully logout"
  }
]
```

## ClientConfig (GET)

You can get the client's configuration information using the GET /config/client request. You will receive the configuration details in the response. Currently, the API returns enums related to exchange segments and message codes. Following are the exchangesegments and messageCodes maintained at our application level:  
  
**exchangeSegments:-{"NSECM": 1, "NSEFO": 2, "NSECD": 3, "BSECM": 11, "BSEFO": 12},  
messageCode:- {"touchlineEvent": 1501, "marketDepthEvent": 1502, "candleDataEvent": 1505, "OIDataEvent": 1510}.**  
  
You need to pass authorization or token to the request.  
  
Note: *Calling of this API is optional.*

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/config/clientConfig
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| exchangeSegments | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) |
| xtsMessageCode | [xtsMessageCode](17-marketdata-enums.md#4-xts-message-code) | [xtsMessageCode](17-marketdata-enums.md#4-xts-message-code) |
| publishFormat | [PublishFormat](17-marketdata-enums.md#10-publishformat) | [PublishFormat](17-marketdata-enums.md#10-publishformat) |
| broadCastMode | [BroadCastMode](17-marketdata-enums.md#11-broadcastmode) | [BroadCastMode](17-marketdata-enums.md#11-broadcastmode) |
| instrumentType | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Fetched configurations successfully",
    "result": {

      "exchangeSegments": {
        "NSECM": 1,
        "NSEFO": 2,
        "NSECD": 3,
        "BSECM": 11,
        "BSEFO": 12,
        "BSECD": 13
      },

      "xtsMessageCode": {
        "TouchLineEvent": 1501,
        "MarketDepthEvent": 1502,
        "CandleDataEvent": 1505,
        "OpenInterestEvent": 1510
      },

      "publishFormat": [
        "Binary",
        "JSON"
      ],

      "broadCastMode": [
        "Binary",
        "JSON"
      ],

      "instrumentType": {
        "Futures": 1,
        "Options": 2,
        "Spread": 4,
        "Equity": 8,
        "Spot": 16,
        "PreferenceShares": 32,
        "Debentures": 64,
        "Warrants": 128,
        "Miscellaneous": 256,
        "MutualFund": 512
      }

    }
  }
]
```
