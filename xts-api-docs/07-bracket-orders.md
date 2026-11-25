# Bracket Order

## Bracket Order (POST)

**Bracket Order (BO)** is a type of order where you can enter a new position along with a **target/exit** and a **stop-loss order.**

- As soon as the **main order** is executed, the system will automatically place **two more orders:**
    - A **profit-taking order**
    - A **stop-loss order**
- When either the **profit-taking order** or the **stop-loss order** is executed, the other order is **automatically cancelled.**

**Bracket Orders** are essentially **algorithmic orders.**

- Entry with Bracket Orders can be done using **Limit Orders** or **Stop-Loss Orders based on triggers.**
- The stop-loss for exit will always be an **SL order.**

You can also use a **Trailing Stop-Loss.** This means:

- If the contract/stock moves in your favor (i.e., the position becomes profitable) by a certain number of ticks, the stop-loss will automatically adjust upward or downward based on whether you are **long** or **short.**

Using a trailing stop-loss is **optional**, but if you enable it, you **cannot modify the Bracket Order** after placement.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/bracket
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | ExchangeSegment (String, 15) | **Y** | [ExchangeSegment](02-enums.md#1-exchangesegments) |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **orderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 4) | **Y** | OrderSide |
| **disclosedQuantity** | Quantity (Integer, 10) | **Y** | Quantity to disclose (for equity) |
| **orderQuantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **limitPrice** | Price (Double, (15,4)) | **Y** | The price to execute the order at |
| **stopLossPrice** | StopLossPrice (Double, (15,4)) | **Y** | A stoploss price is the price in a stop order that triggers the creation of a market order. |
| **squarOff** | SquarOff (Integer, 10) | **Y** | Represents the profit-taking offset value |
| **trailingStoploss** | TrailingStoploss (Integer, 10) | **Y** | It is an incremental value (in ticks or price units) that moves your stop-loss in the profitable direction |
| **orderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | **N** | Echo back to identify order |
| **apiOrderSource** | ApiOrderSource (String, 20) | **N** | API Order Source can be third party application name which you want to give to your order, which will be used to track your order with particular source. |
| **clientID** | ClientID (String, 15) | **N** | ClientID Mandatory in case of Dealer |

### Request Body JSON

```json
{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 3045,
  "orderType": "LIMIT",
  "orderSide": "BUY",
  "disclosedQuantity": 0,
  "orderQuantity": 15,
  "limitPrice": 254.55,
  "stopLossPrice": 245.55,
  "squarOff": 5,
  "trailingStoploss": 5,
  "orderUniqueIdentifier": "123abc",
  "apiOrderSource": "ThirdPartyAppName",
  "clientID": "SYMP1"
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **AppOrderID** | AppOrderID (Integer, 10) | Unique order ID |
| **OrderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | Echo back to identify order |
| **ClientID** | ClientID (String, 15) | ClientID which is sent in request body |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-bracketorders-0002",
  "description": "Request sent",
  "result": {
    "AppOrderID": 1290766863,
    "OrderUniqueIdentifier": "123abc",
    "ClientID": "SYMP1"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/bracket' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 2885,
  "orderType": "LIMIT",
  "orderSide": "BUY",
  "orderQuantity": 1,
  "disclosedQuantity": 0,
  "limitPrice": 1250,
  "stopLossPrice": 20,
  "squareOff": 20,
  "trailingStopLoss": 0,
  "apiOrderSource": "WEB",
  "clientID": "SYMPH",
  "orderUniqueIdentifier": "TEST123"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/bracket"

payload = json.dumps({
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 2885,
    "orderType": "LIMIT",
    "orderSide": "BUY",
    "orderQuantity": 1,
    "disclosedQuantity": 0,
    "limitPrice": 1250,
    "stopLossPrice": 20,
    "squareOff": 20,
    "trailingStopLoss": 0,
    "apiOrderSource": "WEB",
    "clientID": "SYMPH",
    "orderUniqueIdentifier": "TEST123"
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/bracket"
  method := "POST"

  payload := strings.NewReader(`{
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 2885,
    "orderType": "LIMIT",
    "orderSide": "BUY",
    "orderQuantity": 1,
    "disclosedQuantity": 0,
    "limitPrice": 1250,
    "stopLossPrice": 20,
    "squareOff": 20,
    "trailingStopLoss": 0,
    "apiOrderSource": "WEB",
    "clientID": "SYMPH",
    "orderUniqueIdentifier": "TEST123"
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
  "orderType": "LIMIT",
  "orderSide": "BUY",
  "orderQuantity": 1,
  "disclosedQuantity": 0,
  "limitPrice": 1250,
  "stopLossPrice": 20,
  "squareOff": 20,
  "trailingStopLoss": 0,
  "apiOrderSource": "WEB",
  "clientID": "SYMPH",
  "orderUniqueIdentifier": "TEST123"
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/bracket',
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
var request = new HttpRequestMessage(HttpMethod.Post, "https://developers.symphonyfintech.in/1interactive/orders/bracket");

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(
@"{
    ""exchangeSegment"": ""NSECM"",
    ""exchangeInstrumentID"": 2885,
    ""orderType"": ""LIMIT"",
    ""orderSide"": ""BUY"",
    ""orderQuantity"": 1,
    ""disclosedQuantity"": 0,
    ""limitPrice"": 1250,
    ""stopLossPrice"": 20,
    ""squareOff"": 20,
    ""trailingStopLoss"": 0,
    ""apiOrderSource"": ""WEB"",
    ""clientID"": ""SYMPH"",
    ""orderUniqueIdentifier"": ""TEST123""
}",
System.Text.Encoding.UTF8,
"application/json");

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
"    \"orderType\": \"LIMIT\",\r\n" +
"    \"orderSide\": \"BUY\",\r\n" +
"    \"orderQuantity\": 1,\r\n" +
"    \"disclosedQuantity\": 0,\r\n" +
"    \"limitPrice\": 1250,\r\n" +
"    \"stopLossPrice\": 20,\r\n" +
"    \"squareOff\": 20,\r\n" +
"    \"trailingStopLoss\": 0,\r\n" +
"    \"apiOrderSource\": \"WEB\",\r\n" +
"    \"clientID\": \"SYMPH\",\r\n" +
"    \"orderUniqueIdentifier\": \"TEST123\"\r\n" +
"}");

Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/bracket")
  .method("POST", body)
  .addHeader("Authorization", "xxxxxx")
  .addHeader("Content-Type", "application/json")
  .build();

Response response = client.newCall(request).execute();
```

## Modify Bracket Order (PUT)

**XTS provides the ability to modify open bracket orders by allowing you to update the quantity, limit price, and stop-loss price of an open entry order.**

- You can change the **limit price** of an open target order.
- You can change the **stop-loss price** of any open stop-loss order.
- **However:**
- When modifying a **stop-loss order,** the **limit price** will **not** be updated.
- Similarly, when modifying a **profit (target) order,** the **stop-loss price** will **not** be updated.

***Note:*** XTS considers open orders whose order status is either New, Replaced, PartiallyFilled.

### URL

```http
PUT https://developers.symphonyfintech.in/1interactive/orders/bracket
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **appOrderID** | AppOrderID (Integer, 10) | **Y** | Unique order ID |
| **orderQuantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **limitPrice** | Price (Double, (15,4)) | **Y** | The price to execute the order at |
| **stopLossPrice** | Price (Double, (15,4)) | **Y** | A stop loss price is the price in a stop order that triggers the creation of a market order. |
| **orderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | **N** | Echo back to identify order |
| **apiOrderSource** | ApiOrderSource (String, 20) | **N** | API Order Source can be a third party application name which you want to give to your order, which will be used to track your order with a particular source. |
| **clientID** | ClientID (String, 15) | **N** | ClientID Mandatory in case of Dealer |

### Request Body JSON

```json
{
  "appOrderID": 1290766863,
  "orderQuantity": 15,
  "limitPrice": 254.55,
  "stopLossPrice": 245.55,
  "orderUniqueIdentifier": "123abc",
  "apiOrderSource": "ThirdPartyAppName",
  "clientID": "SYMP1"
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **AppOrderID** | AppOrderID (Integer, 10) | Unique order ID |
| **OrderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | Echo back to identify order |
| **ClientID** | ClientID (String, 15) | ClientID which is send in request body |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-bracketorder-0008",
  "description": "Request sent",
  "result": {
    "AppOrderID": 1290766863,
    "orderUniqueIdentifier": "123abc",
    "ClientID": "SYMP1"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location --request PUT 'https://developers.symphonyfintech.in/1interactive/orders/bracket' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "limitPrice": "1251",
  "stopLossPrice": "21",
  "orderQuantity": "1",
  "appOrderID": "1800125097"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/bracket"

payload = json.dumps({
    "limitPrice": "1251",
    "stopLossPrice": "21",
    "orderQuantity": "1",
    "appOrderID": "1800125097"
})

headers = {
    "Authorization": "xxxxxx",
    "Content-Type": "application/json"
}

response = requests.put(url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/bracket"
  method := "PUT"

  payload := strings.NewReader(`{
    "limitPrice": "1251",
    "stopLossPrice": "21",
    "orderQuantity": "1",
    "appOrderID": "1800125097"
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
  "limitPrice": "1251",
  "stopLossPrice": "21",
  "orderQuantity": "1",
  "appOrderID": "1800125097"
});

let config = {
  method: 'put',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/bracket',
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
var request = new HttpRequestMessage(HttpMethod.Put, "https://developers.symphonyfintech.in/1interactive/orders/bracket");

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(
@"{
    ""limitPrice"": ""1251"",
    ""stopLossPrice"": ""21"",
    ""orderQuantity"": ""1"",
    ""appOrderID"": ""1800125097""
}",
System.Text.Encoding.UTF8,
"application/json");

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
"    \"limitPrice\": \"1251\",\r\n" +
"    \"stopLossPrice\": \"21\",\r\n" +
"    \"orderQuantity\": \"1\",\r\n" +
"    \"appOrderID\": \"1800125097\"\r\n" +
"}");

Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/bracket")
  .method("PUT", body)
  .addHeader("Authorization", "xxxxxx")
  .addHeader("Content-Type", "application/json")
  .build();

Response response = client.newCall(request).execute();
```

## Cancel Bracket Order (Delete)

This API can be used to cancel any open Bracket Order by providing the correct BOEntryOrderID that matches the selected open order to be cancelled.

### URL

```http
DELETE https://developers.symphonyfintech.in/1interactive/orders/bracket?boEntryOrderId =2190766863
```

***Note:*** XTS considers open orders whose order status is either New, Replaced, PartiallyFilled.

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **boEntryOrderId** | AppOrderID (Integer, 10) | **Y** | Unique order ID |
| **orderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | **N** | Echo back to identify order |
| **clientID** | ClientID (String, 15) | **N** | Client ID mandatory in case of Dealer |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **AppOrderID** | AppOrderID (Integer, 10) | Unique order ID |
| **OrderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | Echo back to identify order |
| **ClientID** | ClientID (String, 15) | ClientID which is send in request body |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-bracketorder-0014",
  "description": "Request sent",
  "result": {
    "AppOrderID": 1290766863,
    "ClientID": "SYMP1"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location --request DELETE 'https://developers.symphonyfintech.in/1interactive/orders/bracket?boEntryOrderId=1800125097' \
--header 'Authorization: xxxxxx'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/orders/bracket?boEntryOrderId=1800125097"

payload = {}
headers = {
    "Authorization": "xxxxxx"
}

response = requests.delete(url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/bracket?boEntryOrderId=1800125097"
  method := "DELETE"

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
  method: 'delete',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/bracket?boEntryOrderId=1800125097',
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
    HttpMethod.Delete,
    "https://developers.symphonyfintech.in/1interactive/orders/bracket?boEntryOrderId=1800125097"
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
  .url("https://developers.symphonyfintech.in/1interactive/orders/bracket?boEntryOrderId=1800125097")
  .method("DELETE", body)
  .addHeader("Authorization", "xxxxxx")
  .build();

Response response = client.newCall(request).execute();
```
