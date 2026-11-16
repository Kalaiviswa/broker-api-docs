# Limits

Retrieving Limits for a particular client

## Retrieving RMSSubLimits for a particular client

Limits refers to the cumulative margins available in your account which can be used for trading and investing
in various products. Limits is a combination of the free cash you have (i.e. un-utilized cash), cash equivalent
securities (usually margin pledged securities), any money which is in transit (T1/T2 day sell transaction
values) and others, all of which can be used for placing orders. Usually whenever you place an order in a given
asset and product type our risk management system assesses your limits available and then lets the orders go
through or blocks the orders. Limits are dynamic in nature and can be influenced by the Mark to Markets in your
positions and sometimes even by the LTP of your holdings.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.Limits();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const Limits = apiConnect.Limits().then(function(result) {

  }).catch((err) => {console.log("Error Limits",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.Limits()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.limits();
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
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/limits/rmssublimits/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /eq/limits/rmssublimits/{userID}`

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |

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
    "cshAvl": "string",
    "mtmMg": "string",
    "nvl": "string",
    "nvlPer": "string",
    "exp": "string",
    "srtFall": {
      "srtFall": "string",
      "spnSrtFall": "string"
    },
    "mrgAvl": {
      "mrgAvl": "string",
      "dayOpenBal": "string",
      "stkColVal": "string",
      "mfOthColVal": "string",
      "fndAdd": "string",
      "adMrg": "string",
      "notMrg": "string"
    },
    "mrgUtd": {
      "mrgUtd": "string",
      "blkRelDlvry": "string",
      "lvPrdMrg": "string",
      "fnoSpnMrg": "string",
      "fnoExpMrg": "string",
      "spnExpMrg": "string",
      "prmPdRcd": "string",
      "rlPnl": "string",
      "unRlMtm": "string",
      "mf": "string",
      "ipoAmt": "string",
      "fndWthdrwn": "string",
      "ttpv": "string"
    },
    "unPstdChrgs": {
      "ntChrg": "string",
      "ntUnPstdChrg": {
        "subaccode": "string",
        "recorddate": "2019-08-24T14:15:22Z",
        "dpdues": "string",
        "dpcharges": "string",
        "ist": "string",
        "comoshortfall": "string",
        "fnopenality": "string",
        "pisbankbal": "string",
        "wealthpoabal": "string",
        "mtfbal": "string",
        "oth4amt": "string",
        "oth5amt": "string",
        "accode": "string"
      }
    }
   }
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [EQLimitsDao](27-schemas.md#eqlimitsdao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
