# Orders

Apis Related to clients orders, consists of order book, order logs, order history, trade book and trade history

## Show order book for a client in equity (including BO)/ commodity.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.OrderBook();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
   const orderBook = apiConnect.OrderBook().then(function(result) {

  }).catch((err) => {console.log("Error orderBook",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.OrderBook()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.orderBook();
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
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/order/book/{userID}/v1", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /eq/order/book/{userID}/v1`

This method will retrieve the equity and commodity Order Book.

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| rTyp | query | [Rtype](27-schemas.md#rtype) | true | Request Type (PAYOUT) |

#### Enumerated Values

| Parameter | Value |
| --- | --- |
| rTyp | PAYOUT |
| rTyp | PAYIN |

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
    "ord": [
      {
        "lstPos": 0,
        "stkPrc": "string",
        "isCOSecLeg": "string",
        "dur": "string",
        "vlDt": "string",
        "rcvTim": "string",
        "rcvEpTim": "string",
        "sym": "string",
        "cpName": "string",
        "exit": "string",
        "syomID": "string",
        "exc": "string",
        "ntQty": "string",
        "dpName": "string",
        "cancel": "string",
        "sipID": "string",
        "nstReqID": "string",
        "ordTyp": "LIMIT",
        "qtyUnits": "string",
        "opTyp": "string",
        "trsTyp": "string",
        "srs": "string",
        "reqQty": "string",
        "prdCode": "CNC",
        "ogt": "string",
        "flQty": "string",
        "trdSym": "string",
        "edit": "string",
        "asTyp": "string",
        "trgPrc": "string",
        "avgPrc": "string",
        "dsQty": "string",
        "ordID": "string",
        "sts": "string",
        "dpInsTyp": "string",
        "rjRsn": "string",
        "userID": "string",
        "dpExpDt": "string",
        "ltSz": "string",
        "tkSz": "string",
        "desc": "string",
        "prc": "string",
        "exONo": "string",
        "exp": "string",
        "rcvDt": "string",
        "pdQty": "string",
        "userCmnt": "string",
        "isSL": false,
        "isTgt": false,
        "flId": "string",
        "rmk": "string",
        "boSeqId": "string",
        "epochTim": "string",
        "ordTim": "string",
        "trgId": "string",
        "dpVal": "string",
        "cta": "string",
        "ltp": "string",
        "vndSrc": "string",
        "bsktOrdId": "string",
        "bsktEpch": "string",
        "algoId": "string"
        "algoCategory": "string"
        "brkOrd": [
          {
            "flLg": {
              "lstPos": 0,
              "stkPrc": "string",
              "isCOSecLeg": "string",
              "dur": "DAY",
              "vlDt": "string",
              "rcvTim": "string",
              "rcvEpTim": "string",
              "sym": "string",
              "cpName": "string",
              "exit": "string",
              "syomID": "string",
              "exc": "string",
              "ntQty": "string",
              "dpName": "string",
              "cancel": "string",
              "sipID": "string",
              "nstReqID": "string",
              "ordTyp": "LIMIT",
              "qtyUnits": "string",
              "opTyp": "string",
              "trsTyp": "string",
              "srs": "string",
              "reqQty": "string",
              "prdCode": "CNC",
              "ogt": "string",
              "flQty": "string",
              "trdSym": "string",
              "edit": "string",
              "asTyp": "string",
              "trgPrc": "string",
              "avgPrc": "string",
              "dsQty": "string",
              "ordID": "string",
              "sts": "string",
              "dpInsTyp": "string",
              "rjRsn": "string",
              "userID": "string",
              "dpExpDt": "string",
              "ltSz": "string",
              "tkSz": "string",
              "desc": "string",
              "prc": "string",
              "exONo": "string",
              "exp": "string",
              "rcvDt": "string",
              "pdQty": "string",
              "userCmnt": "string",
              "isSL": false,
              "isTgt": false,
              "flId": "string",
              "rmk": "string",
              "boSeqId": "string",
              "epochTim": "string",
              "ordTim": "string",
              "trgId": "string",
              "dpVal": "string",
              "cta": "string",
              "ltp": "string",
              "vndSrc": "string",
              "bsktOrdId": "string",
              "bsktEpch": "string"
            },
            "slLg": {
              "lstPos": 0,
              "stkPrc": "string",
              "isCOSecLeg": "string",
              "dur": "DAY",
              "vlDt": "string",
              "rcvTim": "string",
              "rcvEpTim": "string",
              "sym": "string",
              "cpName": "string",
              "exit": "string",
              "syomID": "string",
              "exc": "string",
              "ntQty": "string",
              "dpName": "string",
              "cancel": "string",
              "sipID": "string",
              "nstReqID": "string",
              "ordTyp": "LIMIT",
              "qtyUnits": "string",
              "opTyp": "string",
              "trsTyp": "string",
              "srs": "string",
              "reqQty": "string",
              "prdCode": "CNC",
              "ogt": "string",
              "flQty": "string",
              "trdSym": "string",
              "edit": "string",
              "asTyp": "string",
              "trgPrc": "string",
              "avgPrc": "string",
              "dsQty": "string",
              "ordID": "string",
              "sts": "string",
              "dpInsTyp": "string",
              "rjRsn": "string",
              "userID": "string",
              "dpExpDt": "string",
              "ltSz": "string",
              "tkSz": "string",
              "desc": "string",
              "prc": "string",
              "exONo": "string",
              "exp": "string",
              "rcvDt": "string",
              "pdQty": "string",
              "userCmnt": "string",
              "isSL": false,
              "isTgt": false,
              "flId": "string",
              "rmk": "string",
              "boSeqId": "string",
              "epochTim": "string",
              "ordTim": "string",
              "trgId": "string",
              "dpVal": "string",
              "cta": "string",
              "ltp": "string",
              "vndSrc": "string",
              "bsktOrdId": "string",
              "bsktEpch": "string"
            },
            "tgtLg": {
              "lstPos": 0,
              "stkPrc": "string",
              "isCOSecLeg": "string",
              "dur": "DAY",
              "vlDt": "string",
              "rcvTim": "string",
              "rcvEpTim": "string",
              "sym": "string",
              "cpName": "string",
              "exit": "string",
              "syomID": "string",
              "exc": "string",
              "ntQty": "string",
              "dpName": "string",
              "cancel": "string",
              "sipID": "string",
              "nstReqID": "string",
              "ordTyp": "LIMIT",
              "qtyUnits": "string",
              "opTyp": "string",
              "trsTyp": "string",
              "srs": "string",
              "reqQty": "string",
              "prdCode": "CNC",
              "ogt": "string",
              "flQty": "string",
              "trdSym": "string",
              "edit": "string",
              "asTyp": "string",
              "trgPrc": "string",
              "avgPrc": "string",
              "dsQty": "string",
              "ordID": "string",
              "sts": "string",
              "dpInsTyp": "string",
              "rjRsn": "string",
              "userID": "string",
              "dpExpDt": "string",
              "ltSz": "string",
              "tkSz": "string",
              "desc": "string",
              "prc": "string",
              "exONo": "string",
              "exp": "string",
              "rcvDt": "string",
              "pdQty": "string",
              "userCmnt": "string",
              "isSL": false,
              "isTgt": false,
              "flId": "string",
              "rmk": "string",
              "boSeqId": "string",
              "epochTim": "string",
              "ordTim": "string",
              "trgId": "string",
              "dpVal": "string",
              "cta": "string",
              "ltp": "string",
              "vndSrc": "string",
              "bsktOrdId": "string",
              "bsktEpch": "string"
            }
          }
        ]
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
    "errCd": "ETRD0007",
    "errMsg": "Seems like there are no orders in your order book"
  },
  "msgID": "6a4b455e-26aa-4bce-9d4c-206eb56e4672",
  "srvTm": 1623912574579
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [OrderBookResponse](27-schemas.md#orderbookresponse) |
| 222 | Unknown | Empty order book | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Shows order details for a client in Equity/ Commodity

Please use this method to retrieve the details of single order.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.OrderDetail(orderId, exchange);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const OrderDetails = apiConnect.OrderDetails(orderId, Exchange).then(function(result) {

  }).catch((err) => {console.log("Error OrderDetails",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
        
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum

response = api_connect.OrderDetails(OrderId= 211101000000001, Exchange=ExchangeEnum.NSE)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.orderDetails(OrderId,Exchange);
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
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/order/details/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /eq/order/details/{userID}`

### Parameters

| Parameter | Description |
| --- | --- |
| OrderId | Order Id |
| Exchange | Name of the exchange, BSE/NSE/MCX/NCDEX |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| nOID | query | string | true | nOID |

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
    "ord": [
      {
        "exc": "string",
        "ordID": "string",
        "nstReqID": "string",
        "trsTyp": "string",
        "symName": "string",
        "scName": "string",
        "prcTF": "string",
        "avgPrc": "string",
        "trgPrc": "string",
        "qtyTF": "string",
        "unFlSz": "string",
        "dsQty": "string",
        "exOID": "string",
        "sts": "string",
        "tim": "string",
        "txt": "string",
        "prcTyp": "string",
        "dur": "string",
        "prdCode": "CNC"
        "algoId": "string"
        "algoCategory": "string"
      }
    ]
  }
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [EqOrderDetailsDao](27-schemas.md#eqorderdetailsdao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Shows order history for a client in equity/ commodity

This method will retrieve all the historical orders placed from StartDate to EndDate

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.OrderHistory(startDate, endDate);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const OrderHistory = apiConnect.OrderHistory(StartDate, EndDate).then(function(result) {

  }).catch((err) => {console.log("Error OrderHistory",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.OrderHistory(StartDate, EndDate)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.orderHistory(StartDate, EndDate);
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
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/order/history/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /eq/order/history/{userID}`

### Parameters

| Parameter | Description |
| --- | --- |
| StartDate | Start Date of search |
| EndDate | End Date of search |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| sDt | query | string | true | From Date(MM/DD/YYYY) |
| eDt | query | string | true | To Date((MM/DD/YYYY) |

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
    "hstOrdBk": [
      {
        "exc": "string",
        "ordID": "string",
        "nstReqID": "string",
        "trsTyp": "string",
        "symName": "string",
        "prcTF": "string",
        "avgPrc": "string",
        "trgPrc": "string",
        "qtyTF": "string",
        "unFlSz": "string",
        "dsQty": "string",
        "exOID": "string",
        "sts": "string",
        "rjRsn": "string",
        "ordTyp": "string",
        "dur": "string",
        "prdCode": "CNC",
        "rpTyp": "string",
        "trdSym": "string",
        "cstFirm": "string",
        "flQty": "string",
        "exTimStm": "string",
        "ordSrc": "string",
        "flDtTim": "string",
        "ordGenTyp": "string",
        "ordEntTyp": "string",
        "cta": "string"
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
    "errCd": "ETRD0009",
    "errMsg": "No data available"
  },
  "msgID": "831b9b6a-cdd3-42cd-a24f-fd863e7cab3b",
  "srvTm": 1623910403937
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [EqOrderHistoryDao](27-schemas.md#eqorderhistorydao) |
| 222 | Unknown | No data available | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
