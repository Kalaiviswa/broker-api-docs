# Margin

The Margin API allows clients to fetch the required margin, available margin, and margin utilization details for a given user or for a specific trade order.  
  
It helps verify whether sufficient funds are available before placing an order.

## Regular Order Margin (POST)

Calculates the margin required to place a regular order based on order details such as exchange, instrument, order type, price, and quantity, before actually placing the order.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/margindetails
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |
| **portfolio** | Array | **Y** |  |
| **exchange** | ExchangeSegment (String, 15) | **Y** | ExchangeSegment |
| **exchangeInstrumentId** | ExchangeInstrumentID (String, 15) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **productType** | ProductType (String, 4) | **Y** | [ProductType](02-enums.md#2-producttype) |
| **orderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 10) | **Y** | [OrderSide](02-enums.md#4-orderside) |
| **quantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **price** | Price (Integer, 10) | **Y** | The price to execute the order at |
| **stopPrice** | Price (Integer, 10) | **Y** | The price at which an order should be triggered (SL, SL-M) |
| **userID** | UserID (String, 15) | **Y** | User login ID |
| **orderSessionType** | OrderSessionType (String, 10) | **Y** | [Order Session Type](02-enums.md#20-order-session-type) |

### Request Body JSON

```json
{
  "clientID": "SYMP",
  "portfolio": [
    {
      "exchange": 1,
      "exchangeInstrumentId": 2885,
      "productType": "NRML",
      "orderType": "LIMIT",
      "orderSide": "BUY",
      "quantity": 1,
      "price": 1200,
      "stopPrice": 1180,
      "userID": "SYMP",
      "orderSessionType": "NORMAL"
    }
  ]
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **brokerageDeatils** | Object |  |
| **IsValid** | OrderUniqueIdentifier (String, 20) | Indicates whether the order is valid based on margin checks. `true` means the order can proceed. |
| **MarginRequired** | MarginRequired (Double, (15,4)) | Total margin required (in currency units) to place the order |
| **MarginAvailable** | MarginRequired (Double, (15,4)) | Total margin currently available in the user’s account |
| **MarginShortfall** | MarginRequired (Double, (15,4)) | Margin deficit amount if available margin is insufficient. |
| **ErrorMessage** | MarginRequired (Double, (15,4)) | Error message when `IsValid = false`. Empty string means no error. |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-calculatemargin-0001",
  "description": "Request sent",
  "result": {
    "brokerageDeatils": {
      "IsValid": true,
      "MarginRequired": 150,
      "MarginAvailable": 9816624.5775,
      "MarginShortfall": 0,
      "ErrorMessage": ""
    }
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/margindetails' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "clientID": "SYMP",
  "portfolio": [
    {
      "exchange": 1,
      "exchangeInstrumentId": 2885,
      "productType": "NRML",
      "orderType": "LIMIT",
      "orderSide": "BUY",
      "quantity": 1,
      "price": 1200,
      "stopPrice": 1180,
      "userID": "SYMP",
      "orderSessionType": "NORMAL"
    }
  ]
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/margindetails"

payload = json.dumps({
  "clientID": "SYMP",
  "portfolio": [
    {
      "exchange": 1,
      "exchangeInstrumentId": 2885,
      "productType": "NRML",
      "orderType": "LIMIT",
      "orderSide": "BUY",
      "quantity": 1,
      "price": 1200,
      "stopPrice": 1180,
      "userID": "SYMP",
      "orderSessionType": "NORMAL"
    }
  ]
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/margindetails"
  method := "POST"

  payload := strings.NewReader(`{
    "clientID": "SYMP",
    "portfolio": [
      {
        "exchange": 1,
        "exchangeInstrumentId": 2885,
        "productType": "NRML",
        "orderType": "LIMIT",
        "orderSide": "BUY",
        "quantity": 1,
        "price": 1200,
        "stopPrice": 1180,
        "userID": "SYMP",
        "orderSessionType": "NORMAL"
      }
    ]
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

  body, _ := io.ReadAll(res.Body)
  fmt.Println(string(body))
}
```

**Node.js**

```javascript
const axios = require('axios');

const axios = require('axios');
let data = JSON.stringify({
  "clientID": "SYMP",
  "portfolio": [
    {
      "exchange": 1,
      "exchangeInstrumentId": 2885,
      "productType": "NRML",
      "orderType": "LIMIT",
      "orderSide": "BUY",
      "quantity": 1,
      "price": 1200,
      "stopPrice": 1180,
      "userID": "SYMP",
      "orderSessionType": "NORMAL"
    }
  ]
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/margindetails',
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

var request = new HttpRequestMessage(
    HttpMethod.Post,
    "https://developers.symphonyfintech.in/1interactive/orders/margindetails"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(@"
{
  ""clientID"": ""SYMP"",
  ""portfolio"": [
    {
      ""exchange"": 1,
      ""exchangeInstrumentId"": 2885,
      ""productType"": ""NRML"",
      ""orderType"": ""LIMIT"",
      ""orderSide"": ""BUY"",
      ""quantity"": 1,
      ""price"": 1200,
      ""stopPrice"": 1180,
      ""userID"": ""SYMP"",
      ""orderSessionType"": ""NORMAL""
    }
  ]
}", null, "application/json");

request.Content = content;

var response = await client.SendAsync(request);

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
  OkHttpClient client = new OkHttpClient()
        .newBuilder()
        .build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(
        mediaType,
        "{\r\n" +
        "  \"clientID\": \"SYMP\",\r\n" +
        "  \"portfolio\": [\r\n" +
        "    {\r\n" +
        "      \"exchange\": 1,\r\n" +
        "      \"exchangeInstrumentId\": 2885,\r\n" +
        "      \"productType\": \"NRML\",\r\n" +
        "      \"orderType\": \"LIMIT\",\r\n" +
        "      \"orderSide\": \"BUY\",\r\n" +
        "      \"quantity\": 1,\r\n" +
        "      \"price\": 1200,\r\n" +
        "      \"stopPrice\": 1180,\r\n" +
        "      \"userID\": \"SYMP\",\r\n" +
        "      \"orderSessionType\": \"NORMAL\"\r\n" +
        "    }\r\n" +
        "  ]\r\n" +
        "}"
);

Request request = new Request.Builder()
        .url("https://developers.symphonyfintech.in/1interactive/orders/margindetails")
        .method("POST", body)
        .addHeader("Authorization", "xxxxxx")
        .addHeader("Content-Type", "application/json")
        .build();

Response response = client.newCall(request).execute();
```

## Modify Regular Order Margin (POST)

Recalculates the margin requirement for a regular order after modifying parameters like price, quantity, Product type helping users understand the updated margin impact before applying the changes.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/modifyordermargindetails
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |
| **orderID** | AppOrderID (Integer, 10) | **Y** | Unique Order ID as received in Order Entry Response |
| **instrumentInformation** | Array | **Y** | Array of Instrument Information |
| **exchange** | ExchangeSegment (String, 15) | **Y** | Exchange Segment |
| **exchangeInstrumentId** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **productType** | ProductType (String, 4) | **Y** | [ProductType](02-enums.md#2-producttype) |
| **orderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 4) | **Y** | [OrderSide](02-enums.md#4-orderside) |
| **quantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **price** | Price (Double, (15,4)) | **Y** | Price in Rupees. Up to 4 decimal places |
| **stopPrice** | StopPrice (Double, (15,4)) | **Y** | Price in Rupees. Up to 4 decimal places. |
| **userID** | UserID (String, 15) | **Y** | UserID of investor client |
| **orderSessionType** | TimeInForce (String, 5) | **Y** | Represents order validity such as DAY, IOC, GTD |

### Request Body JSON

```json
{
  "clientID": "SYMP",
  "orderID": "1210910568",
  "instrumentInformation": {
    "exchange": 1,
    "exchangeInstrumentId": "2885",
    "orderSide": "BUY",
    "orderSessionType": 1,
    "productType": "NRML",
    "orderType": "LIMIT",
    "quantity": 1,
    "price": 1200,
    "stopPrice": 1190
  }
}
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-ModifyOrderMarginQueryRequest-0001",
  "description": "Request sent",
  "result": {
    "brokerageDeatils": {
      "IsValid": true,
      "MarginRequired": 150,
      "MarginAvailable": 9816624.5775,
      "MarginShortfall": 0,
      "ErrorMessage": ""
    }
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/modifyordermargindetails' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
    "clientID": "SYMP",
    "orderID": "1210910568",
    "instrumentInformation": {
        "exchange": 1,
        "exchangeInstrumentId": "2885",
        "orderSide": "BUY",
        "orderSessionType": 1,
        "productType": "NRML",
        "orderType": "LIMIT",
        "quantity": 1,
        "price": 1200,
        "stopPrice": 1190
    }
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/modifyordermargindetails"

payload = json.dumps({
  "clientID": "SYMP",
  "orderID": "1210910568",
  "instrumentInformation": {
    "exchange": 1,
    "exchangeInstrumentId": "2885",
    "orderSide": "BUY",
    "orderSessionType": 1,
    "productType": "NRML",
    "orderType": "LIMIT",
    "quantity": 1,
    "price": 1200,
    "stopPrice": 1190
  }
})
headers = {
  'Authorization': 'xxxxxx',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/modifyordermargindetails"
  method := "POST"

  payload := strings.NewReader(`{`+"
"+`
    "clientID": "SYMP",`+"
"+`
    "orderID": "1210910568",`+"
"+`
    "instrumentInformation": {`+"
"+`
        "exchange": 1,`+"
"+`
        "exchangeInstrumentId": "2885",`+"
"+`
        "orderSide": "BUY",`+"
"+`
        "orderSessionType": 1,`+"
"+`
        "productType": "NRML",`+"
"+`
        "orderType": "LIMIT",`+"
"+`
        "quantity": 1,`+"
"+`
        "price": 1200,`+"
"+`
        "stopPrice": 1190`+"
"+`
    }`+"
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
  "orderID": "1210910568",
  "instrumentInformation": {
    "exchange": 1,
    "exchangeInstrumentId": "2885",
    "orderSide": "BUY",
    "orderSessionType": 1,
    "productType": "NRML",
    "orderType": "LIMIT",
    "quantity": 1,
    "price": 1200,
    "stopPrice": 1190
  }
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/modifyordermargindetails',
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

var request = new HttpRequestMessage(
    HttpMethod.Post,
    "https://developers.symphonyfintech.in/1interactive/orders/modifyordermargindetails"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(@"
{
  ""clientID"": ""SYMP"",
  ""orderID"": ""1210910568"",
  ""instrumentInformation"": {
    ""exchange"": 1,
    ""exchangeInstrumentId"": ""2885"",
    ""orderSide"": ""BUY"",
    ""orderSessionType"": 1,
    ""productType"": ""NRML"",
    ""orderType"": ""LIMIT"",
    ""quantity"": 1,
    ""price"": 1200,
    ""stopPrice"": 1190
  }
}",
null,
"application/json"
);

request.Content = content;

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient()
        .newBuilder()
        .build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(
        mediaType,
        "{\r\n" +
        "  \"clientID\": \"SYMP\",\r\n" +
        "  \"orderID\": \"1210910568\",\r\n" +
        "  \"instrumentInformation\": {\r\n" +
        "    \"exchange\": 1,\r\n" +
        "    \"exchangeInstrumentId\": \"2885\",\r\n" +
        "    \"orderSide\": \"BUY\",\r\n" +
        "    \"orderSessionType\": 1,\r\n" +
        "    \"productType\": \"NRML\",\r\n" +
        "    \"orderType\": \"LIMIT\",\r\n" +
        "    \"quantity\": 1,\r\n" +
        "    \"price\": 1200,\r\n" +
        "    \"stopPrice\": 1190\r\n" +
        "  }\r\n" +
        "}"
);

Request request = new Request.Builder()
        .url("https://developers.symphonyfintech.in/1interactive/orders/modifyordermargindetails")
        .method("POST", body)
        .addHeader("Authorization", "xxxxxx")
        .addHeader("Content-Type", "application/json")
        .build();

Response response = client.newCall(request).execute();
```

## Cover Order Margin (POST)

Calculates the margin required to place a cover order by considering both the main order and the compulsory stop-loss order, providing the total margin requirement upfront.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/comargindetails
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |
| **exchange** | ExchangeSegment (String, 15) | **Y** | Exchange Segment |
| **exchangeInstrumentId** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **entryOrderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 4) | **Y** | [OrderSide](02-enums.md#4-orderside) |
| **quantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **entryPrice** | Price (Double, (15,4)) | **Y** | The price to execute the order at |
| **stopPrice** | StopLossPrice (Double, (15,4)) | **Y** | A stoploss price is the price in a stop order that triggers the creation of a market order. |

### Request Body JSON

```json
{
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": "2885",
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **brokerageDeatils** | Object | Contains brokerage, margin, and validation information. |
| **IsValid** | IsValid (Boolean, 5) | Indicates whether the order is valid based on margin checks. |
| **MarginRequired** | MarginRequired (Double, (15,4)) | Total margin required (in currency units) to place the order. |
| **MarginAvailable** | MarginAvailable (Double, (15,4)) | Total margin currently available in the user’s account. |
| **MarginShortfall** | MarginShortfall (Double, (15,4)) | Margin deficit amount if available margin is insufficient. |
| **ErrorMessage** | ErrorMessage (String, 500) | Error message when the order is invalid. Empty string means no error. |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-calculateCoMargin-0001",
  "description": "Request sent",
  "result": {
    "brokerageDeatils": {
      "IsValid": true,
      "MarginRequired": 1200.94,
      "MarginAvailable": 9816624.5775,
      "MarginShortfall": 0,
      "ErrorMessage": ""
    }
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/comargindetails' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": "2885",
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/comargindetails"

payload = json.dumps({
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": "2885",
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1
})

headers = {
  "Authorization": "xxxxxx",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/comargindetails"
  method := "POST"

  payload := strings.NewReader(`{`+"
"+`
    "clientID": "SYMP",`+"
"+`
    "exchange": 1,`+"
"+`
    "exchangeInstrumentId": "2885",`+"
"+`
    "orderSide": "BUY",`+"
"+`
    "entryOrderType": "LIMIT",`+"
"+`
    "quantity": 1,`+"
"+`
    "entryPrice": 1200,`+"
"+`
    "stopPrice": 1180,`+"
"+`
    "requestId": 1`+"
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
  "exchange": 1,
  "exchangeInstrumentId": "2885",
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/comargindetails',
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
    "https://developers.symphonyfintech.in/1interactive/orders/comargindetails"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(@"
{
  ""clientID"": ""SYMP"",
  ""exchange"": 1,
  ""exchangeInstrumentId"": ""2885"",
  ""orderSide"": ""BUY"",
  ""entryOrderType"": ""LIMIT"",
  ""quantity"": 1,
  ""entryPrice"": 1200,
  ""stopPrice"": 1180,
  ""requestId"": 1
}",
null,
"application/json"
);

request.Content = content;

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient()
        .newBuilder()
        .build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(
        mediaType,
        "{\r\n" +
        "  \"clientID\": \"SYMP\",\r\n" +
        "  \"exchange\": 1,\r\n" +
        "  \"exchangeInstrumentId\": \"2885\",\r\n" +
        "  \"orderSide\": \"BUY\",\r\n" +
        "  \"entryOrderType\": \"LIMIT\",\r\n" +
        "  \"quantity\": 1,\r\n" +
        "  \"entryPrice\": 1200,\r\n" +
        "  \"stopPrice\": 1180,\r\n" +
        "  \"requestId\": 1\r\n" +
        "}"
);

Request request = new Request.Builder()
        .url("https://developers.symphonyfintech.in/1interactive/orders/comargindetails")
        .method("POST", body)
        .addHeader("Authorization", "xxxxxx")
        .addHeader("Content-Type", "application/json")
        .build();

Response response = client.newCall(request).execute();
```

## Modify Cover Order Margin (POST)

Recalculates the margin requirement for a cover order when order parameters are modified, reflecting any changes in margin due to updated price, quantity, or stop-loss values.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/comodifymargindetails
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |
| **exchange** | ExchangeSegment (String, 15) | **Y** | Exchange Segment |
| **exchangeInstrumentId** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **entryOrderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 4) | **Y** | [OrderSide](02-enums.md#4-orderside) |
| **quantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **entryPrice** | Price (Double, (15,4)) | **Y** | The price to execute the order at |
| **stopPrice** | StopLossPrice (Double, (15,4)) | **Y** | A stoploss price is the price in a stop order that triggers the creation of a market order. |
| **orderID** | AppOrderID (Integer, 10) | **Y** | Unique order ID |

### Request Body JSON

```json
{
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1,
  "orderID": "1410911680"
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **brokerageDeatils** | Object |  |
| **IsValid** | IsValid (Boolean, 5) | Indicates whether the order is valid based on margin checks. `true` means the order can proceed. |
| **MarginRequired** | MarginRequired (Double, (15,4)) | Total margin required (in currency units) to place the order. |
| **MarginAvailable** | MarginAvailable (Double, (15,4)) | Total margin currently available in the user’s account. |
| **MarginShortfall** | MarginShortfall (Double, (15,4)) | Margin deficit amount if available margin is insufficient. |
| **ErrorMessage** | ErrorMessage (String, 500) | Error message when `IsValid = false`. Empty string means no error. |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-COModifyMarginQueryRequest-0001",
  "description": "Request sent",
  "result": {
    "brokerageDeatils": {
      "IsValid": true,
      "MarginRequired": 1200,
      "MarginAvailable": 9816624.5775,
      "MarginShortfall": 0,
      "ErrorMessage": ""
    }
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/comodifymargindetails' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1,
  "orderID": "1410911680"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/comodifymargindetails"

payload = json.dumps({
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1,
  "orderID": "1410911680"
})

headers = {
  "Authorization": "xxxxxx",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/comodifymargindetails"
  method := "POST"

  payload := strings.NewReader(`{
    "clientID": "SYMP",
    "exchange": 1,
    "exchangeInstrumentId": 2885,
    "orderSide": "BUY",
    "entryOrderType": "LIMIT",
    "quantity": 1,
    "entryPrice": 1200,
    "stopPrice": 1180,
    "requestId": 1,
    "orderID": "1410911680"
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
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "entryPrice": 1200,
  "stopPrice": 1180,
  "requestId": 1,
  "orderID": "1410911680"
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/comodifymargindetails',
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
    "https://developers.symphonyfintech.in/1interactive/orders/comodifymargindetails"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(@"
{
  ""clientID"": ""SYMP"",
  ""exchange"": 1,
  ""exchangeInstrumentId"": 2885,
  ""orderSide"": ""BUY"",
  ""entryOrderType"": ""LIMIT"",
  ""quantity"": 1,
  ""entryPrice"": 1200,
  ""stopPrice"": 1180,
  ""requestId"": 1,
  ""orderID"": ""1410911680""
}",
null,
"application/json"
);

request.Content = content;

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient()
        .newBuilder()
        .build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(
        mediaType,
        "{\r\n" +
        "  \"clientID\": \"SYMP\",\r\n" +
        "  \"exchange\": 1,\r\n" +
        "  \"exchangeInstrumentId\": 2885,\r\n" +
        "  \"orderSide\": \"BUY\",\r\n" +
        "  \"entryOrderType\": \"LIMIT\",\r\n" +
        "  \"quantity\": 1,\r\n" +
        "  \"entryPrice\": 1200,\r\n" +
        "  \"stopPrice\": 1180,\r\n" +
        "  \"requestId\": 1,\r\n" +
        "  \"orderID\": \"1410911680\"\r\n" +
        "}"
);

Request request = new Request.Builder()
        .url("https://developers.symphonyfintech.in/1interactive/orders/comodifymargindetails")
        .method("POST", body)
        .addHeader("Authorization", "xxxxxx")
        .addHeader("Content-Type", "application/json")
        .build();

Response response = client.newCall(request).execute();
```

## Bracket Order Margin (POST)

Calculates the margin required to place a bracket order by considering the main order along with the associated target and stop-loss orders, giving users clarity on total margin usage before placing the order.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/bomargindetails
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |
| **exchange** | ExchangeSegment (String, 15) | **Y** | Exchange Segment |
| **exchangeInstrumentId** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **entryOrderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 4) | **Y** | [OrderSide](02-enums.md#4-orderside) |
| **quantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **limitPrice** | Price (Double, (15,4)) | **Y** | Price in Rupees. Up to 4 decimal places |
| **stopLoss** | StopLossPrice (Double, (15,4)) | **Y** | Price in Rupees. Up to 4 decimal places |
| **squarOff** | SquarOff (Integer, 10) | **Y** | Represents the profit-taking offset value |

### Request Body JSON

```json
{
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "limitPrice": 1200,
  "squarOff": 1290,
  "stopLoss": 1150
}
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-calculateBoMargin-0001",
  "description": "Request sent",
  "result": {
    "brokerageDeatils": {
      "IsValid": true,
      "MarginRequired": 1200,
      "MarginAvailable": 9816624.5775,
      "MarginShortfall": 0,
      "ErrorMessage": ""
    }
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/bomargindetails' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "limitPrice": 1200,
  "squarOff": 1290,
  "stopLoss": 1150
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/bomargindetails"

payload = json.dumps({
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "limitPrice": 1200,
  "squarOff": 1290,
  "stopLoss": 1150
})

headers = {
  "Authorization": "xxxxxx",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/orders/bomargindetails"
  method := "POST"

  payload := strings.NewReader(`{
    "clientID": "SYMP",
    "exchange": 1,
    "exchangeInstrumentId": 2885,
    "orderSide": "BUY",
    "entryOrderType": "LIMIT",
    "quantity": 1,
    "limitPrice": 1200,
    "squarOff": 1290,
    "stopLoss": 1150
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
  "clientID": "SYMP",
  "exchange": 1,
  "exchangeInstrumentId": 2885,
  "orderSide": "BUY",
  "entryOrderType": "LIMIT",
  "quantity": 1,
  "limitPrice": 1200,
  "squarOff": 1290,
  "stopLoss": 1150
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/orders/bomargindetails',
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
    "https://developers.symphonyfintech.in/1interactive/orders/bomargindetails"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(@"
{
  ""clientID"": ""SYMP"",
  ""exchange"": 1,
  ""exchangeInstrumentId"": 2885,
  ""orderSide"": ""BUY"",
  ""entryOrderType"": ""LIMIT"",
  ""quantity"": 1,
  ""limitPrice"": 1200,
  ""squarOff"": 1290,
  ""stopLoss"": 1150
}",
null,
"application/json"
);

request.Content = content;

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient()
        .newBuilder()
        .build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(
        mediaType,
        "{\r\n" +
        "  \"clientID\": \"SYMP\",\r\n" +
        "  \"exchange\": 1,\r\n" +
        "  \"exchangeInstrumentId\": 2885,\r\n" +
        "  \"orderSide\": \"BUY\",\r\n" +
        "  \"entryOrderType\": \"LIMIT\",\r\n" +
        "  \"quantity\": 1,\r\n" +
        "  \"limitPrice\": 1200,\r\n" +
        "  \"squarOff\": 1290,\r\n" +
        "  \"stopLoss\": 1150\r\n" +
        "}"
);

Request request = new Request.Builder()
        .url("https://developers.symphonyfintech.in/1interactive/orders/bomargindetails")
        .method("POST", body)
        .addHeader("Authorization", "xxxxxx")
        .addHeader("Content-Type", "application/json")
        .build();

Response response = client.newCall(request).execute();
```
