# Market-Depth

Retrieving depth for a particular symbol

## Shows market depth for a symbol

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.GetMarketDepth();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
     const depth = apiConnect.GetMarketDepth().then(function(result) {

  }).catch((err) => {console.log("Error depth",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.GetMarketDepth()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.getMarketQuoteDepth();
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/tradebook/v1/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /quote/scrip/{symbol}`

This method will retrieve the depth data for a symbol.

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| symbol | path | string | true | symbol of the scrip |

> Example responses

> 200 Response

```json
{
  "data": {
    "qt": {
      "isOpenLow": false,
      "tkSz": "string",
      "lut": "string",
      "exc": "string",
      "isCasEligible": false,
      "isMTFEnabled": false,
      "alltmhidt": "string",
      "atp": "string",
      "akSz": "string",
      "opInt": "string",
      "ltTQty": "string",
      "alltmlodt": "string",
      "rchFlg": "string",
      "marketCap": "string",
      "chg": "string",
      "avgThreeMonth": "string",
      "trdSym": "string",
      "asSymbols": [],
      "expFlg": false,
      "referenceLimitPrice": "string",
      "isNCD": false,
      "yrLw": "string",
      "ltSz": "string",
      "isTradable": false,
      "desc": "string",
      "chgP": "string",
      "nwsFlg": "string",
      "dpVal": "string",
      "dpNm": "string",
      "sym": "string",
      "altt": "string",
      "opIntChg": "string",
      "bidPr": "string",
      "totalImbalance": "string",
      "isOpenHigh": false,
      "yrH": "string",
      "yrLwDt": "string",
      "vol": "string",
      "coCode": "string",
      "askPr": "string",
      "yrHDt": "string",
      "ntTrdVal": "string",
      "hiCt": "string",
      "c": "string",
      "loCt": "string",
      "bdSz": "string",
      "h": "string",
      "ltp": "string",
      "alltmhi": "string",
      "l": "string",
      "ltt": "string",
      "alltmlo": "string",
      "o": "string",
      "isETF": false,
      "asTyp": "string"
    },
    "mkd": {
      "ask": [
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        }
      ],
      "bid": [
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        },
        {
          "no": "string",
          "price": "string",
          "qty": "string"
        }
      ],
      "buyQty": "string",
      "sellQty": "string"
    },
    "asSym": [
      {
        "exc": "string",
        "optExpIdx": "string",
        "sym": "string",
        "futExpIdx": "string"
      }
    ],
    "fdQtEq": {
      "divYld": "string",
      "pe": "string",
      "mktCap": "string",
      "pbv": "string",
      "eps": "string"
    },
    "rchSt": "string"
  },
  "msgID": "string",
  "srvTm": "string",
  "appID": "string"
}
```

> 222 Response

```json
{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "error": {
    "actCd": "54",
    "errCd": "ETRD0002",
    "errMsg": "Seems like there are an issue with symbol."
  },
  "msgID": "001a05a5-c2ce-405a-a5b2-a1783fbf1849",
  "srvTm": 1623915376485
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [MarketDepthDao](27-schemas.md#marketdepthdao) |
| 222 | Unknown | Empty reponse | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
