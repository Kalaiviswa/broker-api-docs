# Holdings

Retrieving holdings response (both rms and mf) for a particular client

## Retrieving CNC and MTF RMS holdings response for a particular client

Holdings comprises of the user's portfolio of long-term equity delivery stocks. An instrument in a holding's
portfolio remains there indefinitely until its sold or is delisted or changed by the exchanges. Underneath it
all, instruments in the holdings reside in the user's DEMAT account, as settled by exchanges and clearing
institutions.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.Holdings();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const Holdings = apiConnect.Holdings().then(function(result) {

  }).catch((err) => {console.log("Error Holdings",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.Holdings()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.holdings();
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
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/holdings/v1/rmsholdings/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /eq/holdings/v1/rmsholdings/{userID}`

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | none |

> Example responses

> 200 Response

```json
{"resp":
        {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "eqHv": "string",
    "rmsHdg": [
      {
        "asTyp": "string",
        "cpName": "string",
        "dpName": "string",
        "exc": "string",
        "isin": "string",
        "ltSz": "string",
        "ltp": "string",
        "tkSz": "string",
        "trdSym": "string",
        "totalQty": "string",
        "totalVal": "string",
        "sym": "string",
        "cncRmsHdg": {
          "td": "string",
          "hdgVl": "string",
          "clUQty": "string",
          "hdgUQty": "string",
          "usdQty": "string",
          "t1HQty": "string",
          "clQty": "string",
          "qty": "string",
          "pdQty": "string",
          "pdCnt": "string",
          "sym": "string",
          "totQty": "string"
        },
        "mtfRmsHdg": {
          "td": "string",
          "hdgVl": "string",
          "clUQty": "string",
          "hdgUQty": "string",
          "usdQty": "string",
          "t1HQty": "string",
          "clQty": "string",
          "qty": "string",
          "pdQty": "string",
          "pdCnt": "string",
          "sym": "string",
          "totQty": "string"
        }
      }
    ]
   }
  }
 }
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [HoldingsRMSDao](27-schemas.md#holdingsrmsdao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
