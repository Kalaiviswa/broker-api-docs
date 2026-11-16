# PositionBook

Retrieving Positions(both net and day) for a particular client

## Retrieving NetPositions for a particular client

Net position usually is referred to in context of trades placed during the day in case of Equity, or can refer
to carry forward positions in case of Derivatives, Currency and Commodity. It indicates the net obligation
(either buy or sell) for the given day in a given symbol. Usually you monitor the net positions screen to track
the profit or loss made from the given trades and will have options to square off your entire position and book
the entire profit and loss.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.NetPosition();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const NetPosition = apiConnect.NetPosition().then(function(result) {

  }).catch((err) => {console.log("Error NetPosition",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.NetPosition()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.netPosition();
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
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/positions/net/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /eq/positions/net/{userID}`

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | none |

> Example responses

> 200 Response

```json
 {"resp":{
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "pos": [
      {
        "sym": "string",
        "ltp": "string",
        "ltt": "string",
        "chg": "string",
        "chgP": "string",
        "exc": "string",
        "vol": "string",
        "dpName": "string",
        "trdSym": "string",
        "asTyp": "string",
        "ltSz": "string",
        "tkSz": "string",
        "dpInsTyp": "string",
        "desc": "string",
        "dpVal": "string",
        "stkPrc": "string",
        "opTyp": "string",
        "exp": "string",
        "dpExpDt": "string",
        "opInt": "string",
        "opIntChg": "string",
        "opIntChgP": "string",
        "spot": "string",
        "rlOvrP": "string",
        "rlCAbs": "string",
        "trsTyp": "string",
        "prdCode": "CNC",
        "avgSlPrc": "string",
        "avgByPrc": "string",
        "byAmt": "string",
        "byQty": "string",
        "slAmt": "string",
        "slQty": "string",
        "ntQty": "string",
        "ntAmt": "string",
        "rlzPL": "string",
        "urlzPL": "string",
        "ntPL": "string",
        "mtm": "string",
        "prc": "string",
        "sqOff": "string",
        "mul": "string",
        "cpName": "string",
        "rchFlg": "string",
        "nwsFlg": "string",
        "cfAvgSlPrc": "string",
        "cfAvgByPrc": "string",
        "cfSlQty": "string",
        "cfByQty": "string",
        "cfSlAmt": "string",
        "cfByAmt": "string",
        "ntSlQty": "string",
        "ntByQty": "string",
        "ntSlAmt": "string",
        "ntByAmt": "string",
        "brkEvnPrc": "string",
        "uniqKey": "string",
        "pn": "string",
        "gn": "string",
        "gd": "string",
        "pd": "string"
      }
    ],
    "ntMTM": "string",
    "tdyMtm": "string",
    "urlMtm": "string",
    "npos": "string",
    "opn": "string",
    "cls": "string"
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
    "errCd": "ETRD0004",
    "errMsg": "Seems like there are no positions in your account currently"
  },
  "msgID": "06bd0d76-574c-40c6-ae04-fed4261fd968",
  "srvTm": 1624426313506
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [NetPositionsDao](27-schemas.md#netpositionsdao) |
| 222 | Unknown | No positions | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
