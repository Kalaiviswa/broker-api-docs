# GTT Orders

## Place GTT Order (POST)

Places a Good Till Triggered (GTT) order that remains active until a specified trigger condition is met. Once the trigger price is reached, the system automatically places the corresponding market or limit order on the exchange.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/gttorder
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **Y** | User-specific identification |
| **source** | ApiOrderSource (String, 20) | **Y** | API/Platform source of the request |
| **stopPrice** | Price (Double, (15,4)) | **Y** | Stop-loss trigger price |
| **limitPrice** | Price (Double, (15,4)) | **Y** | Limit price at which the order should execute |
| **orderQuantity** | OrderQuantity (Integer, 10) | **Y** | Quantity to transact (in units/lots depending on segment) |
| **orderSide** | OrderSide (String, 4) | **Y** | BUY or SELL direction of the order |
| **exchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment where the order is placed |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Unique token/identifier for the trading instrument |

### Request Body JSON

```json
{
        "clientID": "SYMP",
        "source": "Twsapi",
        "stopPrice": 1300,
        "limitPrice": 1320,
        "orderQuantity": 75,
        "orderSide": "BUY",
        "exchangeSegment": "NSECM",
        "exchangeInstrumentID": 2885
      }

```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-gttOrderRequest-0001",
  "description": "GTT order request send."
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/gttorder' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 2885,
  "orderSide": "BUY",
  "stopPrice": 1300,
  "limitPrice": 1320,
  "orderQuantity": 75,
  "clientID": "SYMP",
  "source": "TWSAPI"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/gttorder"

payload = json.dumps({
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 2885,
    "orderSide": "BUY",
    "stopPrice": 1300,
    "limitPrice": 1320,
    "orderQuantity": 75,
    "clientID": "SYMP",
    "source": "TWSAPI"
})

headers = {
    "Authorization": "xxxxxx",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```

**Go**

```go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "https://developers.symphonyfintech.in/1interactive/orders/gttorder"
  method := "POST"

  payload := strings.NewReader(`{
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 2885,
    "orderSide": "BUY",
    "stopPrice": 1300,
    "limitPrice": 1320,
    "orderQuantity": 75,
    "clientID": "SYMP",
    "source": "TWSAPI"
}`)

  client := &http.Client{}
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }

  req.Header.Add("Authorization", "xxxxxx")
  req.Header.Add("Content-Type", "application/json")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }

  fmt.Println(string(body))
}
```

**Node.js**

```javascript
const axios = require('axios');

let data = JSON.stringify({
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 2885,
  "orderSide": "BUY",
  "stopPrice": 1300,
  "limitPrice": 1320,
  "orderQuantity": 75,
  "clientID": "SYMP",
  "source": "TWSAPI"
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/gttorder',
  headers: {
    'Authorization': 'xxxxxx',
    'Content-Type': 'application/json'
  },
  data: data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
```

**C#**

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(
    HttpMethod.Post,
    "https://developers.symphonyfintech.in/1interactive/orders/gttorder"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(
@"{
    ""exchangeSegment"": ""NSECM"",
    ""exchangeInstrumentID"": 2885,
    ""orderSide"": ""BUY"",
    ""stopPrice"": 1300,
    ""limitPrice"": 1320,
    ""orderQuantity"": 75,
    ""clientID"": ""SYMP"",
    ""source"": ""TWSAPI""
}",
System.Text.Encoding.UTF8,
"application/json"
);

request.Content = content;

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(mediaType, "{\r\n" +
"    \"exchangeSegment\": \"NSECM\",\r\n" +
"    \"exchangeInstrumentID\": 2885,\r\n" +
"    \"orderSide\": \"BUY\",\r\n" +
"    \"stopPrice\": 1300,\r\n" +
"    \"limitPrice\": 1320,\r\n" +
"    \"orderQuantity\": 75,\r\n" +
"    \"clientID\": \"SYMP\",\r\n" +
"    \"source\": \"TWSAPI\"\r\n" +
"}");

Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/gttorder")
  .method("POST", body)
  .addHeader("Authorization", "xxxxxx")
  .addHeader("Content-Type", "application/json")
  .build();

Response response = client.newCall(request).execute();
```

## GTT Order Modify (PUT)

Allows modification of an Open existing GTT order by updating trigger price or order parameters

### URL

```http
PUT https://developers.symphonyfintech.in/1interactive/orders/gttorder
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **Y** | Unique client identification code |
| **orderSide** | OrderSide (String, 10) | **Y** | BUY/SELL instruction for the order |
| **orderSessionType** | OrderSessionType (String, 10) | **Y** | Session type (e.g., GTT, DAY, IOC) |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Unique exchange token / scrip ID |
| **exchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment (e.g., NSECM, NSEFO) |
| **appOrderID** | AppOrderID (Integer, 10) | **Y** | Unique RMS-generated order ID |
| **modifiedLimitPrice** | Price (Double, (15,4)) | **N** | New modified limit price |
| **orderCategoryType** | OrderCategoryType (String, 15) | **Y** | Order category (NORMAL, STOPLOSS, etc.) |
| **modifiedOrderType** | OrderType (String, 15) | **N** | Modified order type (Market, Limit, SL, SLM) |
| **modifiedProductType** | ProductType (String, 10) | **N** | Modified product type (e.g., NRML, CNC, MIS) |
| **modifiedOrderQuantity** | OrderQuantity (Integer, 10) | **N** | Modified quantity for the order |
| **source** | Source (String, 20) | **N** | Source of the request (e.g., TWSAPI, WEB) |
| **modifiedStopPrice** | Price (Double, (15,4)) | **N** | Modified stop-loss trigger price |
| **participationCode** | ParticipationCode (String, 10) | **N** | Order participation code (NONE / DARK / etc.) |

### Request Body JSON

```json
{
  "clientID": "SYMP",
  "orderSide": "BUY",
  "orderSessionType": "GTT",
  "exchangeInstrumentID": 2885,
  "exchangeSegment": "NSECM",
  "appOrderID": "1343000794",
  "modifiedLimitPrice": 1360,
  "orderCategoryType": "NORMAL",
  "modifiedOrderType": "Limit",
  "modifiedProductType": "NRML",
  "modifiedOrderQuantity": 75,
  "source": "Twsapi",
  "modifiedStopPrice": 1310,
  "participationCode": "NONE"
}
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-modifygttOrder-0001",
  "description": "Modify GTT order request send."
}
```

### Code Examples

**cURL**

```bash
curl --location --request PUT 'https://developers.symphonyfintech.in/1interactive/orders/gttorder' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
    "clientID": "SYMP",
    "orderSide": "BUY",
    "orderSessionType": "GTT",
    "exchangeInstrumentID": 2885,
    "exchangeSegment": "NSECM",
    "appOrderID": "1343000794",
    "modifiedLimitPrice": 1360,
    "orderCategoryType": "NORMAL",
    "modifiedOrderType": "Limit",
    "modifiedProductType": "NRML",
    "modifiedOrderQuantity": 75,
    "source": "Twsapi",
    "modifiedStopPrice": 1310,
    "participationCode": "NONE"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/gttorder"

payload = json.dumps({
  "clientID": "SYMP",
  "orderSide": "BUY",
  "orderSessionType": "GTT",
  "exchangeInstrumentID": 2885,
  "exchangeSegment": "NSECM",
  "appOrderID": "1343000794",
  "modifiedLimitPrice": 1360,
  "orderCategoryType": "NORMAL",
  "modifiedOrderType": "Limit",
  "modifiedProductType": "NRML",
  "modifiedOrderQuantity": 75,
  "source": "Twsapi",
  "modifiedStopPrice": 1310,
  "participationCode": "NONE"
})
headers = {
  'Authorization': 'xxxxxx',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)
```

**Go**

```go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io"
)

func main() {

  url := "https://developers.symphonyfintech.in/1interactive/orders/gttorder"
  method := "PUT"

  payload := strings.NewReader(`{`+"
"+`
    "clientID": "SYMP",`+"
"+`
    "orderSide": "BUY",`+"
"+`
    "orderSessionType": "GTT",`+"
"+`
    "exchangeInstrumentID": 2885,`+"
"+`
    "exchangeSegment": "NSECM",`+"
"+`
    "appOrderID": "1343000794",`+"
"+`
    "modifiedLimitPrice": 1360,`+"
"+`
    "orderCategoryType": "NORMAL",`+"
"+`
    "modifiedOrderType": "Limit",`+"
"+`
    "modifiedProductType": "NRML",`+"
"+`
    "modifiedOrderQuantity": 75,`+"
"+`
    "source": "Twsapi",`+"
"+`
    "modifiedStopPrice": 1310,`+"
"+`
    "participationCode": "NONE"`+"
"+`
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "xxxxxx")
  req.Header.Add("Content-Type", "application/json")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

**Node.js**

```javascript
const axios = require('axios');
let data = JSON.stringify({
  "clientID": "SYMP",
  "orderSide": "BUY",
  "orderSessionType": "GTT",
  "exchangeInstrumentID": 2885,
  "exchangeSegment": "NSECM",
  "appOrderID": "1343000794",
  "modifiedLimitPrice": 1360,
  "orderCategoryType": "NORMAL",
  "modifiedOrderType": "Limit",
  "modifiedProductType": "NRML",
  "modifiedOrderQuantity": 75,
  "source": "Twsapi",
  "modifiedStopPrice": 1310,
  "participationCode": "NONE"
});

let config = {
  method: 'put',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/gttorder',
  headers: {
    'Authorization': 'xxxxxx',
    'Content-Type': 'application/json'
  },
  data : data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
```

**C#**

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Put, "https://developers.symphonyfintech.in/1interactive/orders/gttorder");
request.Headers.Add("Authorization", "xxxxxx");
var content = new StringContent("{\r\n    \"clientID\": \"SYMP\",\r\n    \"orderSide\": \"BUY\",\r\n    \"orderSessionType\": \"GTT\",\r\n    \"exchangeInstrumentID\": 2885,\r\n    \"exchangeSegment\": \"NSECM\",\r\n    \"appOrderID\": \"1343000794\",\r\n    \"modifiedLimitPrice\": 1360,\r\n    \"orderCategoryType\": \"NORMAL\",\r\n    \"modifiedOrderType\": \"Limit\",\r\n    \"modifiedProductType\": \"NRML\",\r\n    \"modifiedOrderQuantity\": 75,\r\n    \"source\": \"Twsapi\",\r\n    \"modifiedStopPrice\": 1310,\r\n    \"participationCode\": \"NONE\"\r\n}", null, "application/json");
request.Content = content;
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"clientID\": \"SYMP\",\r\n    \"orderSide\": \"BUY\",\r\n    \"orderSessionType\": \"GTT\",\r\n    \"exchangeInstrumentID\": 2885,\r\n    \"exchangeSegment\": \"NSECM\",\r\n    \"appOrderID\": \"1343000794\",\r\n    \"modifiedLimitPrice\": 1360,\r\n    \"orderCategoryType\": \"NORMAL\",\r\n    \"modifiedOrderType\": \"Limit\",\r\n    \"modifiedProductType\": \"NRML\",\r\n    \"modifiedOrderQuantity\": 75,\r\n    \"source\": \"Twsapi\",\r\n    \"modifiedStopPrice\": 1310,\r\n    \"participationCode\": \"NONE\"\r\n}");
Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/gttorder")
  .method("PUT", body)
  .addHeader("Authorization", "xxxxxx")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

## GTT Order Cancel (DELETE)

Cancels an active GTT order, preventing it from being triggered even if the trigger condition is met in the future.

### URL

```http
DELETE https://developers.symphonyfintech.in//interactive/orders/gttorder?clientID=SYMP&appOrderID=1343000794&exchangeSegment=NSECM&exchangeInstrumentID=2885
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **Y** | Unique client identification code |
| **appOrderID** | AppOrderID (String, 15) | **Y** | Unique order ID generated by RMS |
| **exchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment where order is placed (e.g., NSECM) |
| **exchangeInstrumentID** | ExchangeInstrumentID (String, 15) | **Y** | Unique token/ID for the trading instrument |

### Request Body JSON

```json
{
  "type": "success",
  "code": "s-cancelgttOrder-0001",
  "description": "Cancel GTT order request send."
}
```

### Code Examples

**cURL**

```bash
curl --location --request DELETE 'https://developers.symphonyfintech.in/1interactive/orders/gttorder?appOrderID=1343000794&clientID=SYMP&userID=SYMP&exchangeSegment=NSECM&exchangeInstrumentID=2885' \
--header 'Authorization: xxxxxx'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/orders/gttorder?appOrderID=1343000794&clientID=SYMP&userID=SYMP&exchangeSegment=NSECM&exchangeInstrumentID=2885"

payload = {}
headers = {
  'Authorization': 'xxxxxx'
}

response = requests.request("DELETE", url, headers=headers, data=payload)
print(response.text)
```

**Go**

```go
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "https://developers.symphonyfintech.in/1interactive/orders/gttorder?appOrderID=1343000794&clientID=SYMP&userID=SYMP&exchangeSegment=NSECM&exchangeInstrumentID=2885"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "xxxxxx")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

**Node.js**

```javascript
const axios = require('axios');

let config = {
  method: 'delete',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/gttorder?appOrderID=1343000794&clientID=SYMP&userID=SYMP&exchangeSegment=NSECM&exchangeInstrumentID=2885',
  headers: {
    'Authorization': 'xxxxxx'
  }
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
```

**C#**

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Delete, "https://developers.symphonyfintech.in/1interactive/orders/gttorder?appOrderID=1343000794&clientID=SYMP&userID=SYMP&exchangeSegment=NSECM&exchangeInstrumentID=2885");
request.Headers.Add("Authorization", "xxxxxx");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/gttorder?appOrderID=1343000794&clientID=SYMP&userID=SYMP&exchangeSegment=NSECM&exchangeInstrumentID=2885")
  .method("DELETE", body)
  .addHeader("Authorization", "xxxxxx")
  .build();
Response response = client.newCall(request).execute();
```

## GTT OrderBook (POST)

Fetches the list of all GTT orders placed by the user, along with their trigger conditions, order details, and current status.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/gttorderbook?clientID=SYMP
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **Y** | Description Client ID Mandatory |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **LoginID** | LoginID (String, 20) | User login ID |
| **ClientID** | ClientID (String, 20) | Client code associated with the order |
| **AppOrderID** | AppOrderID (Integer, 10) | Unique application order ID |
| **OrderReferenceID** | OrderReferenceID (String, 20) | Reference ID sent during order placement |
| **GeneratedBy** | GeneratedBy (String, 15) | Source that generated the order (TWSAPI, Web, etc.) |
| **ExchangeOrderID** | ExchangeOrderID (String, 20) | Exchange-generated order ID (if available) |
| **OrderCategoryType** | OrderCategoryType (String, 10) | NORMAL / SYSTEM / OCO / GTT etc. |
| **ExchangeSegment** | ExchangeSegment (String, 15) | Exchange segment (e.g., NSECM) |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Token ID of the trading instrument |
| **OrderSide** | OrderSide (String, 4) | BUY or SELL |
| **OrderType** | OrderType (String, 10) | Market / Limit / SL / SL-M |
| **ProductType** | ProductType (String, 10) | CNC / MIS / NRML |
| **TimeInForce** | TimeInForce (String, 10) | DAY / IOC / None |
| **OrderPrice** | Price (Double, (15,4)) | Price entered for the order |
| **OrderQuantity** | Quantity (Integer, 10) | Total order quantity |
| **OrderStopPrice** | StopPrice (Double, (15,4)) | Stop-loss trigger price |
| **OrderStatus** | OrderStatus (String, 20) | Current status: New / Filled / Cancelled / Rejected |
| **OrderAverageTradedPrice** | Price (Double, (15,4)) | Average price at which quantity is traded |
| **LeavesQuantity** | LeavesQuantity (Integer, 10) | Remaining quantity not yet executed |
| **CumulativeQuantity** | CumulativeQuantity (Integer, 10) | Total executed quantity |
| **OrderDisclosedQuantity** | DisclosedQuantity (Integer, 10) | Quantity disclosed to the market |
| **OrderGeneratedDateTime** | DateTime (String, 20) | Order generation timestamp |
| **ExchangeTransactTime** | DateTime (String, 20) | Exchange transaction timestamp |
| **TradingSymbol** | TradingSymbol (String, 50) | Symbol name (e.g., RELIANCE) |
| **LastUpdateDateTime** | DateTime (String, 20) | Last updated timestamp |
| **OrderExpiryDate** | DateTime (String, 20) | Order validity expiry date |
| **CancelRejectReason** | Reason (String, 500) | Reason for cancellation or rejection |
| **OrderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | Unique identifier sent in request |
| **OrderLegStatus** | OrderLegStatus (String, 20) | SingleOrderLeg / SpreadFirstLeg / SpreadSecondLeg |
| **BoLegDetails** | BoLegDetails (Integer, 10) | BO leg details (if applicable) |
| **IsSpread** | IsSpread (Boolean, 5) | Whether the order is a spread order |
| **BoEntryOrderId** | BoEntryOrderId (String, 20) | BO entry order reference |
| **ApiOrderSource** | ApiOrderSource (String, 20) | API source (WEB / TWSAPI etc.) |
| **MessageCode** | MessageCode (String, 10) | System message code for order update |
| **MessageVersion** | MessageVersion (String, 10) | Version of the message format |
| **TokenID** | TokenID (String, 10) | Internal token ID |
| **ApplicationType** | ApplicationType (String, 15) | Application type flag |
| **SequenceNumber** | SequenceNumber (String, 15) | Order sequence number |

### Response Body JSON

```json
{
  "LoginID": "SYMP",
  "ClientID": "SYMP",
  "AppOrderID": 1343000794,
  "OrderReferenceID": "",
  "GeneratedBy": "TWSAPI",
  "ExchangeOrderID": "",
  "OrderCategoryType": "NORMAL",
  "ExchangeSegment": "NSECM",
  "ExchangeInstrumentID": 2885,
  "OrderSide": "BUY",
  "OrderType": "Limit",
  "ProductType": "CNC",
  "TimeInForce": "None",
  "OrderPrice": 1350,
  "OrderQuantity": 75,
  "OrderStopPrice": 1300,
  "OrderStatus": "New",
  "OrderAverageTradedPrice": "",
  "LeavesQuantity": 75,
  "CumulativeQuantity": 0,
  "OrderDisclosedQuantity": 0,
  "OrderGeneratedDateTime": "26-11-2025 14:00:00",
  "ExchangeTransactTime": "26-11-2025 14:00:00",
  "TradingSymbol": "RELIANCE",
  "LastUpdateDateTime": "26-11-2025 14:00:00",
  "OrderExpiryDate": "26-11-2026 14:00:00",
  "CancelRejectReason": "",
  "OrderUniqueIdentifier": "",
  "OrderLegStatus": "SingleOrderLeg",
  "BoLegDetails": 0,
  "IsSpread": "false",
  "BoEntryOrderId": "",
  "ApiOrderSource": "",
  "MessageCode": 9004,
  "MessageVersion": 4,
  "TokenID": 0,
  "ApplicationType": 0,
  "SequenceNumber": 0
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/gttorderbook?clientID=SYMP' \
--header 'Authorization: XXXXXX'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/orders/gttorderbook?clientID=SYMP"

payload = {}
headers = {
    "Authorization": "XXXXXX"
}

response = requests.get(url, headers=headers, data=payload)
print(response.text)
```

**Go**

```go
package main

import (
  "fmt"
  "net/http"
  "io"
)

func main() {

  url := "https://developers.symphonyfintech.in/1interactive/orders/gttorderbook?clientID=SYMP"
  method := "GET"

  client := &http.Client{}
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }

  req.Header.Add("Authorization", "xxxxxx")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := io.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }

  fmt.Println(string(body))
}
```

**Node.js**

```javascript
const axios = require('axios');

let config = {
  method: 'get',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/gttorderbook?clientID=SYMP',
  headers: {
    'Authorization': 'xxxxxx'
  }
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
```

**C#**

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(
    HttpMethod.Get,
    "https://developers.symphonyfintech.in/1interactive/orders/gttorderbook?clientID=SYMP"
);

request.Headers.Add("Authorization", "xxxxxx");

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();

MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");

Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/gttorderbook?clientID=SYMP")
  .method("GET", body)
  .addHeader("Authorization", "xxxxxx")
  .build();

Response response = client.newCall(request).execute();
```
