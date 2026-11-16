# TradeBook

Retrieving Equity TradeBook for a particular client

## Shows trade book for a client in equity/ commodity

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.TradeBook();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
     const tradeBook = apiConnect.TradeBook().then(function(result) {

  }).catch((err) => {console.log("Error tradeBook",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.TradeBook()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.tradeBook();
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

`GET /eq/tradebook/v1/{userID}`

This method will retrieve the Trade Book.

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| nOID | query | string | false | OrderID |

> Example responses

> 200 Response

```json
 {"resp":{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "trade": [
      {
        "ordTim": "string",
        "trdSym": "string",
        "exONo": "string",
        "dpInsTyp": "string",
        "ntPrc": "string",
        "rmk": "string",
        "dpExpDt": "string",
        "ltSz": "string",
        "cpName": "string",
        "prdCode": "CNC",
        "flTim": "string",
        "flDt": "string",
        "flLeg": "string",
        "flID": "string",
        "fldQty": "string",
        "psCnv": "string",
        "qty": "string",
        "rjRsn": "string",
        "opTyp": "string",
        "sym": "string",
        "dpName": "string",
        "ordID": "string",
        "trsTyp": "string",
        "stkPrc": "string",
        "exc": "string",
        "chgP": "string",
        "sts": "string",
        "asTyp": "string",
        "tkSz": "string",
        "ordType": "string",
        "trdID": "string",
        "ltp": "string",
        "flQty": "string",
        "chg": "string",
        "srs": "string",
        "rcvTim": "string",
        "nstReqID": "string",
        "flPrc": "string",
        "exp": "string",
        "qtyUnits": "string",
        "epochTim": "string"
      }
    ]
  }
 }
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
    "errMsg": "Seems like there are no trades in your trade book."
  },
  "msgID": "001a05a5-c2ce-405a-a5b2-a1783fbf1849",
  "srvTm": 1623915376485
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [EqTradeBookDao](27-schemas.md#eqtradebookdao) |
| 222 | Unknown | Empty trade book | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
