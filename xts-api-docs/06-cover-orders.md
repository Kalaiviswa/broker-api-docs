# Cover orders (CO)

## Place Cover Order (POST)

**A Cover Order (CO)** is an advanced intraday order that is always accompanied by a **mandatory Stop-Loss Order.**  
This helps users minimize potential losses by safeguarding against unexpected market movements.

A Cover Order offers **high leverage** and is available in the following segments:

- **Equity Cash**
- **Equity F&O**
- **Commodity F&O**
- **Currency F&O**

A Cover Order consists of **embedded orders:**

- **Limit/Market Order**
  The investor aims to enter a trade at either the best available market price or a desired limit price of the asset at that time.
- **Stop-Loss Order**
  The main order is always accompanied by a **Stop-Loss Order** and the position is **squared off automatically** if the market price reaches the specified stop-loss price.
- The stop-loss order **can be modified** but **cannot be cancelled.**

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/cover
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | ExchangeSegment (String, 15) | **Y** | [ExchangeSegment](02-enums.md#1-exchangesegments) |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **orderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 4) | **Y** | [OrderSide](02-enums.md#4-orderside) |
| **disclosedQuantity** | Quantity (Integer, 10) | **Y** | Quantity to disclose (for equity) |
| **orderQuantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **limitPrice** | Price (Double, (15,4)) | **Y** | The price to execute the order at |
| **stopPrice** | Price (Double, (15,4)) | **Y** | The price at which an order should be triggered (SL, SL-M) |
| **orderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | **N** | Echo back to identify order |
| **apiOrderSource** | ApiOrderSource (String, 20) | **N** | API Order Source can be third party application name which you want to give to your order, which will be used to track your order with particular source. |
| **clientID** | ClientID (String, 15) | **N** | ClientID Mandatory in case of Dealer |

### Request Body JSON

```json
{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 3045,
  "orderSide": "BUY",
  "orderQuantity": 15,
  "disclosedQuantity": 0,
  "limitPrice": 254.55,
  "stopPrice": 251.5,
  "orderType": "LIMIT",
  "orderUniqueIdentifier": "123abc",
  "clientID": "SYMP1",
  "apiOrderSource": "ThirdPartyAppName"
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **EntryAppOrderID** | EntryAppOrderID (Integer, 10) | The unique order ID for the **main/entry order** |
| **ExitAppOrderID** | ExitAppOrderID (Integer, 10) | The unique order ID for the **linked exit order** (Stop-Loss or Target) |
| **OrderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | Echo back to identify order |
| **ClientID** | ClientID (String, 15) | ClientID which is send in request body |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-orders-0001",
  "description": "Request sent",
  "result": {
    "EntryAppOrderID": 1323797170,
    "ExitAppOrderID": 3727296468,
    "OrderUniqueIdentifier": "123abc",
    "ClientID": "SYMP1"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/cover' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 3045,
  "orderSide": "BUY",
  "orderQuantity": 15,
  "disclosedQuantity": 0,
  "limitPrice": 254.55,
  "stopPrice": 251.5,
  "orderType": "LIMIT",
  "orderUniqueIdentifier": "123abc",
  "clientID": "SYMP1",
  "apiOrderSource": "ThirdPartyAppName"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/cover"

payload = json.dumps({
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 3045,
    "orderSide": "BUY",
    "orderQuantity": 15,
    "disclosedQuantity": 0,
    "limitPrice": 254.55,
    "stopPrice": 251.5,
    "orderType": "LIMIT",
    "orderUniqueIdentifier": "123abc",
    "clientID": "SYMP1",
    "apiOrderSource": "ThirdPartyAppName"
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/cover"
  method := "POST"

  payload := strings.NewReader(`{
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 3045,
    "orderSide": "BUY",
    "orderQuantity": 15,
    "disclosedQuantity": 0,
    "limitPrice": 254.55,
    "stopPrice": 251.5,
    "orderType": "LIMIT",
    "orderUniqueIdentifier": "123abc",
    "clientID": "SYMP1",
    "apiOrderSource": "ThirdPartyAppName"
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
  "exchangeInstrumentID": 3045,
  "orderSide": "BUY",
  "orderQuantity": 15,
  "disclosedQuantity": 0,
  "limitPrice": 254.55,
  "stopPrice": 251.5,
  "orderType": "LIMIT",
  "orderUniqueIdentifier": "123abc",
  "clientID": "SYMP1",
  "apiOrderSource": "ThirdPartyAppName"
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/cover',
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
    "https://developers.symphonyfintech.in/1interactive/orders/cover"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(
@"{
    ""exchangeSegment"": ""NSECM"",
    ""exchangeInstrumentID"": 3045,
    ""orderSide"": ""BUY"",
    ""orderQuantity"": 15,
    ""disclosedQuantity"": 0,
    ""limitPrice"": 254.55,
    ""stopPrice"": 251.5,
    ""orderType"": ""LIMIT"",
    ""orderUniqueIdentifier"": ""123abc"",
    ""clientID"": ""SYMP1"",
    ""apiOrderSource"": ""ThirdPartyAppName""
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
"    \"exchangeInstrumentID\": 3045,\r\n" +
"    \"orderSide\": \"BUY\",\r\n" +
"    \"orderQuantity\": 15,\r\n" +
"    \"disclosedQuantity\": 0,\r\n" +
"    \"limitPrice\": 254.55,\r\n" +
"    \"stopPrice\": 251.5,\r\n" +
"    \"orderType\": \"LIMIT\",\r\n" +
"    \"orderUniqueIdentifier\": \"123abc\",\r\n" +
"    \"clientID\": \"SYMP1\",\r\n" +
"    \"apiOrderSource\": \"ThirdPartyAppName\"\r\n" +
"}");

Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/cover")
  .method("POST", body)
  .addHeader("Authorization", "xxxxxx")
  .addHeader("Content-Type", "application/json")
  .build();

Response response = client.newCall(request).execute();
```

## Exit Cover Order (PUT)

The Exit Cover API allows the user to easily exit an open stop-loss order by converting it into an exit order.

### URL

```http
PUT https://developers.symphonyfintech.in/1interactive/orders/cover
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **appOrderID** | AppOrderID (Integer, 10) | **Y** | Unique order ID |
| **orderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | **N** | Echo back to identify order |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |

### Request Body JSON

```json
{
  "appOrderID": 3727296468,
  "OrderUniqueIdentifier": "123abc",
  "ClientID": "SYMP1"
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
  "code": "s-orders-0001",
  "description": "Request sent",
  "result": {
    "AppOrderID": 3727296468,
    "ClientID": "SYMP1"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location --request PUT 'https://developers.symphonyfintech.in/1interactive/orders/cover' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "appOrderID": 3727296468,
  "OrderUniqueIdentifier": "123abc",
  "ClientID": "SYMP1"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/cover"

payload = json.dumps({
    "appOrderID": 3727296468,
    "OrderUniqueIdentifier": "123abc",
    "ClientID": "SYMP1"
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/cover"
  method := "PUT"

  payload := strings.NewReader(`{
    "appOrderID": 3727296468,
    "OrderUniqueIdentifier": "123abc",
    "ClientID": "SYMP1"
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
  "appOrderID": 3727296468,
  "OrderUniqueIdentifier": "123abc",
  "ClientID": "SYMP1"
});

let config = {
  method: 'put',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/cover',
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
    HttpMethod.Put,
    "https://developers.symphonyfintech.in/1interactive/orders/cover"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(
@"{
    ""appOrderID"": 3727296468,
    ""OrderUniqueIdentifier"": ""123abc"",
    ""ClientID"": ""SYMP1""
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
"    \"appOrderID\": 3727296468,\r\n" +
"    \"OrderUniqueIdentifier\": \"123abc\",\r\n" +
"    \"ClientID\": \"SYMP1\"\r\n" +
"}");

Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/orders/cover")
  .method("PUT", body)
  .addHeader("Authorization", "xxxxxx")
  .addHeader("Content-Type", "application/json")
  .build();

Response response = client.newCall(request).execute();
```
