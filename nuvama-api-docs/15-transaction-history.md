# Transaction-History

Retrieving Transaction History for a particular client

## Shows transaction history for a client

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.GetAllTransactionHistory(segment = SegmentTypeEnum.EQUITY, fromDate = "2023-10-06", toDate = "2023-11-06");
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
     const tradeBook = apiConnect.getTransactionHistory(
      "EQUITY",
      "2023-10-06",
      "2023-11-06"
).then(function(result) {

  }).catch((err) => {console.log("Error TransactionHistory",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.GetAllTransactionHistory(segment = SegmentTypeEnum.EQUITY, fromDate = "2023-10-06", toDate = "2023-11-06")
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.getTransactionHistory(
  Segment.EQUITY, "2023-10-06",
  "2023-11-06"
);
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

`GET /equity/pnl/transaction?accountId={accountId}&fromDate={fromDate}&toDate={toDate}`

This method will retrieve the Transaction History.

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| accountID | query | string | true | AccountID of the client |
| fromDate | query | string | false | from Date of transaction |
| toDate | query | string | false | to Date of transaction |

> Example responses

> 200 Response

```json
{"resp":
        {
  "status": "true",
  "data": {
    "totalRecords": "1",
    "transactionList": [
      {
        "accountCode": "string",
        "security": "string",
        "transactionDate": "string",
        "txnType": "string",
        "action": "string",
        "exchangeName": "string",
        "quantity": "float",
        "transactionPrice": "float",
        "brokerage": "float",
        "stampDutyCharges": "float",
        "sebiTax": "float",
        "transactionCharge": "float",
        "other": "int",
        "accountID": "int",
        "tranId": "int",
        "editFlag": "int",
        "filterFlags": {
          "editable": "false"
        },
        "priceEditable": "false",
        "splitAllowed": "false",
        "scripIdentifier": "int",
        "cumulativeQuantity": "float",
        "netCharges": "float",
        "assetType": "string",
        "stax_GST": "float",
        "stt": "float",
        "tstax": "float",
        "isin": "string"
      }
    ]
  }
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [TransactionHistoryDao](27-schemas.md#transactionhistorydao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
