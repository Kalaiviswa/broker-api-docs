# Spread Orders

## Place Spread Order (POST)

Places a spread order involving spread instruments (buy/sell) in a single request, ensuring all legs are executed together.

### URL

```http
POST https://developers.symphonyfintech.in//interactive/orders/spread
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | ExchangeSegment (String, 15) | **Y** | [Exchange Segment](02-enums.md#1-exchangesegments) |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **productType** | ProductType (String, 4) | **Y** | [ProductType](02-enums.md#2-producttype) |
| **action** | OrderSide (String, 4) | **Y** | [OrderSide](02-enums.md#4-orderside) |
| **orderType** | OrderType (String, 10) | **Y** | [OrderType](02-enums.md#3-ordertype) |
| **orderDuration** | TimeInForce (String, 5) | **Y** | [TimeInForce](02-enums.md#5-timeinforce) |
| **quantity** | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| **spreadPrice** | Price (Double, (15,4)) | **Y** | Spread Price difference |
| **totalPrice** | Price (Double, (15,4)) | **N** | Total price used in some spread structures |
| **leg1ExchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment for Leg 1 |
| **leg1ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Instrument token for Leg 1 |
| **leg2ExchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment for Leg 2 |
| **leg2ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Instrument token for Leg 2 |
| **spreadExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Main spread instrument ID |
| **apiOrderSource** | ApiOrderSource (String, 20) | **N** | API Order Source can be third party application name which you want to give to your order, which will be used to track your order with particular source. |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |
| **userID** | UserID (String, 15) | **N** | User ID authenticated for API |

### Request Body JSON

```json
{
  "exchangeSegment": "NSEFO",
  "exchangeInstrumentID": 13620424,
  "productType": "NRML",
  "action": "BUY",
  "orderType": "LIMIT",
  "orderDuration": "DAY",
  "quantity": "75",
  "spreadPrice": 1000,
  "totalPrice": 0,
  "leg1ExchangeSegment": "NSEFO",
  "leg1ExchangeInstrumentID": 53001,
  "leg2ExchangeSegment": "NSEFO",
  "leg2ExchangeInstrumentID": 52168,
  "spreadExchangeInstrumentID": 13620424,
  "apiOrderSource": "WEB",
  "clientID": "SYMP",
  "userID": "SYMPTEST"
}
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-spreadorder-0001",
  "description": "Spread order place successfully",
  "result": {}
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/spread' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "exchangeSegment": "NSEFO",
  "exchangeInstrumentID": "39543",
  "productType": "NRML",
  "action": "Buy",
  "orderDuration": "DAY",
  "quantity": "75",
  "spreadPrice": 100,
  "leg1ExchangeSegment": "NSEFO",
  "leg1ExchangeInstrumentID": 49953,
  "leg2ExchangeSegment": "NSEFO",
  "leg2ExchangeInstrumentID": 48772,
  "spreadExchangeInstrumentID": 12836740,
  "apiOrderSource": "WEB",
  "clientID": "SYMPH"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/spread"

payload = json.dumps({
    "exchangeSegment": "NSEFO",
    "exchangeInstrumentID": "39543",
    "productType": "NRML",
    "action": "Buy",
    "orderDuration": "DAY",
    "quantity": "75",
    "spreadPrice": 100,
    "leg1ExchangeSegment": "NSEFO",
    "leg1ExchangeInstrumentID": 49953,
    "leg2ExchangeSegment": "NSEFO",
    "leg2ExchangeInstrumentID": 48772,
    "spreadExchangeInstrumentID": 12836740,
    "apiOrderSource": "WEB",
    "clientID": "SYMPH"
})

headers = {
    "Authorization": "xxxxxx",
    "Content-Type": "application/json"
}

response = requests.request(
    "POST",
    url,
    headers=headers,
    data=payload
)

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

    url := "https://developers.symphonyfintech.in/1interactive/orders/spread"
    method := "POST"

    payload := strings.NewReader(`{
        "exchangeSegment": "NSEFO",
        "exchangeInstrumentID": "39543",
        "productType": "NRML",
        "action": "Buy",
        "orderDuration": "DAY",
        "quantity": "75",
        "spreadPrice": 100,
        "leg1ExchangeSegment": "NSEFO",
        "leg1ExchangeInstrumentID": 49953,
        "leg2ExchangeSegment": "NSEFO",
        "leg2ExchangeInstrumentID": 48772,
        "spreadExchangeInstrumentID": 12836740,
        "apiOrderSource": "WEB",
        "clientID": "SYMPH"
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
const axios = require("axios");

let data = JSON.stringify({
  "exchangeSegment": "NSEFO",
  "exchangeInstrumentID": "39543",
  "productType": "NRML",
  "action": "Buy",
  "orderDuration": "DAY",
  "quantity": "75",
  "spreadPrice": 100,
  "leg1ExchangeSegment": "NSEFO",
  "leg1ExchangeInstrumentID": 49953,
  "leg2ExchangeSegment": "NSEFO",
  "leg2ExchangeInstrumentID": 48772,
  "spreadExchangeInstrumentID": 12836740,
  "apiOrderSource": "WEB",
  "clientID": "SYMPH"
});

let config = {
  method: "post",
  maxBodyLength: Infinity,
  url: "https://developers.symphonyfintech.in/1interactive/orders/spread",
  headers: {
    "Authorization": "xxxxxx",
    "Content-Type": "application/json"
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
    "https://developers.symphonyfintech.in/1interactive/orders/spread"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(
    "{\r\n" +
    "  \"exchangeSegment\": \"NSEFO\",\r\n" +
    "  \"exchangeInstrumentID\": \"39543\",\r\n" +
    "  \"productType\": \"NRML\",\r\n" +
    "  \"action\": \"Buy\",\r\n" +
    "  \"orderDuration\": \"DAY\",\r\n" +
    "  \"quantity\": \"75\",\r\n" +
    "  \"spreadPrice\": 100,\r\n" +
    "  \"leg1ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg1ExchangeInstrumentID\": 49953,\r\n" +
    "  \"leg2ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg2ExchangeInstrumentID\": 48772,\r\n" +
    "  \"spreadExchangeInstrumentID\": 12836740,\r\n" +
    "  \"apiOrderSource\": \"WEB\",\r\n" +
    "  \"clientID\": \"SYMPH\"\r\n" +
    "}",
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
OkHttpClient client = new OkHttpClient().newBuilder().build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(
    mediaType,
    "{\r\n" +
    "  \"exchangeSegment\": \"NSEFO\",\r\n" +
    "  \"exchangeInstrumentID\": \"39543\",\r\n" +
    "  \"productType\": \"NRML\",\r\n" +
    "  \"action\": \"Buy\",\r\n" +
    "  \"orderDuration\": \"DAY\",\r\n" +
    "  \"quantity\": \"75\",\r\n" +
    "  \"spreadPrice\": 100,\r\n" +
    "  \"leg1ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg1ExchangeInstrumentID\": 49953,\r\n" +
    "  \"leg2ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg2ExchangeInstrumentID\": 48772,\r\n" +
    "  \"spreadExchangeInstrumentID\": 12836740,\r\n" +
    "  \"apiOrderSource\": \"WEB\",\r\n" +
    "  \"clientID\": \"SYMPH\"\r\n" +
    "}"
);

Request request = new Request.Builder()
    .url("https://developers.symphonyfintech.in/1interactive/orders/spread")
    .method("POST", body)
    .addHeader("Authorization", "xxxxxx")
    .addHeader("Content-Type", "application/json")
    .build();

Response response = client.newCall(request).execute();
```

## SpreadOrder Modify (PUT)

Modifies an existing open spread order by updating allowed parameters such as price or quantity for one or more legs.

### URL

```http
PUT https://developers.symphonyfintech.in//interactive/orders/spread
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeOrderID** | ExchangeOrderID (String, 20) | **Y** | It is unique OrderID generated by exchange |
| **productType** | ProductType (String, 10) | **Y** | [ProductType](02-enums.md#2-producttype) |
| **action** | Action | **Y** | BUY/SELL instruction |
| **orderDuration** | OrderDuration | **Y** | Duration for which the order remains valid |
| **quantity** | OrderQuantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots. |
| **spreadPrice** | Price (Double, (15,4)) | **Y** | Spread price for the order |
| **orderID** | OrderID (String, 20) | **Y** | Unique order ID generated by RMS |
| **leg1ExchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment of first leg **(All below content verify)** |
| **leg1ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Instrument token of first leg |
| **leg2ExchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment of second leg |
| **leg2ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Instrument token of second leg |
| **spreadExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Combined spread instrument token |
| **apiOrderSource** | ApiOrderSource (String, 20) | **N** | Source of order placement (e.g., WEB) |
| **clientID** | ClientID (String, 20) | **N** | Unique client identification |

### Request Body JSON

```json
{
  "exchangeOrderID": "X_174305899",
  "productType": "NRML",
  "action": "BUY",
  "orderDuration": "DAY",
  "quantity": "75",
  "spreadPrice": 900,
  "orderID": "1240992685",
  "leg1ExchangeSegment": "NSEFO",
  "leg1ExchangeInstrumentID": 53216,
  "leg2ExchangeSegment": "NSEFO",
  "leg2ExchangeInstrumentID": 64103,
  "spreadExchangeInstrumentID": 13687399,
  "apiOrderSource": "WEB",
  "clientID": "SYMP"
}
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-updatespreadorder-0001",
  "description": "Success modify spread",
  "result": {}
}
```

### Code Examples

**cURL**

```bash
curl --location --request PUT 'https://developers.symphonyfintech.in/1interactive/orders/spread' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "exchangeOrderID": "124270000004574",
  "productType": "NRML",
  "action": "Buy",
  "orderDuration": "DAY",
  "quantity": "75",
  "spreadPrice": 100,
  "orderID": "124270000004574",
  "leg1ExchangeSegment": "NSEFO",
  "leg1ExchangeInstrumentID": 49953,
  "leg2ExchangeSegment": "NSEFO",
  "leg2ExchangeInstrumentID": 48772,
  "spreadExchangeInstrumentID": 12836740,
  "apiOrderSource": "WEB",
  "clientID": "SYMPH"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/spread"

payload = json.dumps({
    "exchangeOrderID": "124270000004574",
    "productType": "NRML",
    "action": "Buy",
    "orderDuration": "DAY",
    "quantity": "75",
    "spreadPrice": 100,
    "orderID": "124270000004574",
    "leg1ExchangeSegment": "NSEFO",
    "leg1ExchangeInstrumentID": 49953,
    "leg2ExchangeSegment": "NSEFO",
    "leg2ExchangeInstrumentID": 48772,
    "spreadExchangeInstrumentID": 12836740,
    "apiOrderSource": "WEB",
    "clientID": "SYMPH"
})

headers = {
    "Authorization": "xxxxxx",
    "Content-Type": "application/json"
}

response = requests.request(
    "PUT",
    url,
    headers=headers,
    data=payload
)

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

    url := "https://developers.symphonyfintech.in/1interactive/orders/spread"
    method := "PUT"

    payload := strings.NewReader(`{
        "exchangeOrderID": "124270000004574",
        "productType": "NRML",
        "action": "Buy",
        "orderDuration": "DAY",
        "quantity": "75",
        "spreadPrice": 100,
        "orderID": "124270000004574",
        "leg1ExchangeSegment": "NSEFO",
        "leg1ExchangeInstrumentID": 49953,
        "leg2ExchangeSegment": "NSEFO",
        "leg2ExchangeInstrumentID": 48772,
        "spreadExchangeInstrumentID": 12836740,
        "apiOrderSource": "WEB",
        "clientID": "SYMPH"
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
const axios = require("axios");

let data = JSON.stringify({
  "exchangeOrderID": "124270000004574",
  "productType": "NRML",
  "action": "Buy",
  "orderDuration": "DAY",
  "quantity": "75",
  "spreadPrice": 100,
  "orderID": "124270000004574",
  "leg1ExchangeSegment": "NSEFO",
  "leg1ExchangeInstrumentID": 49953,
  "leg2ExchangeSegment": "NSEFO",
  "leg2ExchangeInstrumentID": 48772,
  "spreadExchangeInstrumentID": 12836740,
  "apiOrderSource": "WEB",
  "clientID": "SYMPH"
});

let config = {
  method: "put",
  maxBodyLength: Infinity,
  url: "https://developers.symphonyfintech.in/1interactive/orders/spread",
  headers: {
    "Authorization": "xxxxxx",
    "Content-Type": "application/json"
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
    "https://developers.symphonyfintech.in/1interactive/orders/spread"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent(
    "{\r\n" +
    "  \"exchangeOrderID\": \"124270000004574\",\r\n" +
    "  \"productType\": \"NRML\",\r\n" +
    "  \"action\": \"Buy\",\r\n" +
    "  \"orderDuration\": \"DAY\",\r\n" +
    "  \"quantity\": \"75\",\r\n" +
    "  \"spreadPrice\": 100,\r\n" +
    "  \"orderID\": \"124270000004574\",\r\n" +
    "  \"leg1ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg1ExchangeInstrumentID\": 49953,\r\n" +
    "  \"leg2ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg2ExchangeInstrumentID\": 48772,\r\n" +
    "  \"spreadExchangeInstrumentID\": 12836740,\r\n" +
    "  \"apiOrderSource\": \"WEB\",\r\n" +
    "  \"clientID\": \"SYMPH\"\r\n" +
    "}",
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
OkHttpClient client = new OkHttpClient().newBuilder().build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(
    mediaType,
    "{\r\n" +
    "  \"exchangeOrderID\": \"124270000004574\",\r\n" +
    "  \"productType\": \"NRML\",\r\n" +
    "  \"action\": \"Buy\",\r\n" +
    "  \"orderDuration\": \"DAY\",\r\n" +
    "  \"quantity\": \"75\",\r\n" +
    "  \"spreadPrice\": 100,\r\n" +
    "  \"orderID\": \"124270000004574\",\r\n" +
    "  \"leg1ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg1ExchangeInstrumentID\": 49953,\r\n" +
    "  \"leg2ExchangeSegment\": \"NSEFO\",\r\n" +
    "  \"leg2ExchangeInstrumentID\": 48772,\r\n" +
    "  \"spreadExchangeInstrumentID\": 12836740,\r\n" +
    "  \"apiOrderSource\": \"WEB\",\r\n" +
    "  \"clientID\": \"SYMPH\"\r\n" +
    "}"
);

Request request = new Request.Builder()
    .url("https://developers.symphonyfintech.in/1interactive/orders/spread")
    .method("PUT", body)
    .addHeader("Authorization", "xxxxxx")
    .addHeader("Content-Type", "application/json")
    .build();

Response response = client.newCall(request).execute();
```

## SpreadOrder Cancel (DELETE)

Cancels an existing open spread order along with all its associated legs, provided the order has not been fully executed.

### URL

```http
DELETE https://developers.symphonyfintech.in/1interactive/orders/spread?spreadExchangeSegment=NSEFO&spreadExchangeInstrumentID=13687399&exchangeOrderID=X_174305899&orderID=1240992685&apiOrderSource=WebAPI
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **spreadExchangeSegment** | ExchangeSegment (String, 15) | **Y** | Exchange segment of the spread order (e.g., NSEFO) |
| **spreadExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Spread instrument token used for querying the order |
| **exchangeOrderID** | ExchangeOrderID (String, 20) | **N** | Exchange-generated order identifier |
| **orderID** | OrderID (String, 20) | **N** | Unique internal order ID assigned by RMS/system |
| **apiOrderSource** | ApiOrderSource (String, 20) | **N** | Source from where the API request originated (e.g., WebAPI) |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **OrderID** | ExchangeSegment (String, 15) | Unique order ID that was deleted |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-deletespreadorder-0001",
  "description": "Spread Order Delete Successfully",
  "result": {
    "OrderID": "800125184000005256"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location --request DELETE 'https://developers.symphonyfintech.in/1interactive/orders/spread?spreadExchangeSegment=NSEFO&spreadExchangeInstrumentID=13687399&exchangeOrderID=X_174305899&orderID=1240992685&apiOrderSource=WebAPI' \
--header 'Authorization: xxxxxx' \
--data ''
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/orders/spread?spreadExchangeSegment=NSEFO&spreadExchangeInstrumentID=13687399&exchangeOrderID=X_174305899&orderID=1240992685&apiOrderSource=WebAPI"

payload = ""
headers = {
    "Authorization": "xxxxxx"
}

response = requests.request(
    "DELETE",
    url,
    headers=headers,
    data=payload
)

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

    url := "https://developers.symphonyfintech.in/1interactive/orders/spread?spreadExchangeSegment=NSEFO&spreadExchangeInstrumentID=13687399&exchangeOrderID=X_174305899&orderID=1240992685&apiOrderSource=WebAPI"
    method := "DELETE"

    payload := strings.NewReader(``)

    client := &http.Client{}
    req, err := http.NewRequest(method, url, payload)

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
const axios = require("axios");

let data = "";

let config = {
  method: "delete",
  maxBodyLength: Infinity,
  url: "https://developers.symphonyfintech.in/1interactive/orders/spread?spreadExchangeSegment=NSEFO&spreadExchangeInstrumentID=13687399&exchangeOrderID=X_174305899&orderID=1240992685&apiOrderSource=WebAPI",
  headers: {
    "Authorization": "xxxxxx"
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
    HttpMethod.Delete,
    "https://developers.symphonyfintech.in/1interactive/orders/spread?spreadExchangeSegment=NSEFO&spreadExchangeInstrumentID=13687399&exchangeOrderID=X_174305899&orderID=1240992685&apiOrderSource=WebAPI"
);

request.Headers.Add("Authorization", "xxxxxx");

var content = new StringContent("", null, "text/plain");
request.Content = content;

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder().build();

MediaType mediaType = MediaType.parse("text/plain");

RequestBody body = RequestBody.create(
    mediaType,
    ""
);

Request request = new Request.Builder()
    .url("https://developers.symphonyfintech.in/1interactive/orders/spread?spreadExchangeSegment=NSEFO&spreadExchangeInstrumentID=13687399&exchangeOrderID=X_174305899&orderID=1240992685&apiOrderSource=WebAPI")
    .method("DELETE", body)
    .addHeader("Authorization", "xxxxxx")
    .build();

Response response = client.newCall(request).execute();
```

## Spread Order Book (GET)

Retrieves the current status of all spread orders placed by the user, including leg-wise details and execution status.

### URL

```http
GET https://developers.symphonyfintech.in/1interactive/orders/spread?clientID=SYMP&userID=SYMPTEST
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |
| **userID** | ClientID (String, 15) | **N** | User ID Mandatory |

### Response Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **cancelable** | Boolean (Boolean, 5) | N | Whether the order can be cancelled |
| **editable** | Boolean (Boolean, 5) | N | Whether the order can be edited |
| **expiration** | Expiration (String, 10) | N | Order validity (e.g., DAY) |
| **orderID** | OrderID (String, 20) | N | Exchange-generated order ID |
| **orderNumber** | OrderNumber (String, 20) | N | System-generated unique order number |
| **orderType** | OrderType (String, 10) | N | [OrderType](02-enums.md#3-ordertype) |
| **productType** | ProductType (String, 4) | N | [ProductType](02-enums.md#2-producttype) |
| **receivedTime** | TimeStamp (String, 20) | N | Time order was received |
| **status** | Status (String, 10) | N | Current order status |
| **exchange** | Exchange (String, 10) | N | Exchange segment (e.g., NSEFO) |
| **nowOrderStatus** | NowOrderStatus (String, 20) | N | Latest updated status |
| **symbolName** | SymbolName (String, 50) | N | Symbol of the instrument |
| **spreadExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | N | Spread Instrument Token |
| **participantCode** | ParticipantCode (String, 20) | N | Participant Code (if applicable) |
| **rejectReason** | Reason (String, 500) | N | Reason for rejection (if any) |

### Response Body JSON

```json
{
  "orders": [
    {
      "action": "BUY",
      "assetType": "Futures",
      "dTradingSym": "NIFTY",
      "description": "NIFTY 31JUL2025",
      "exchange": "NSEFO",
      "executionPrice": "",
      "filledQuantity": "0",
      "limitPrice": "100",
      "marketlot": "75",
      "quantity": "75",
      "remainingQuantity": "75",
      "series": "FUTIDX",
      "symbol": "53216_NSEFO",
      "tickSize": "0.1",
      "tradingSymbol": "NIFTY 31JUL2025",
      "orderLegStatus": "SpreadFirstLeg",
      "nowOrderStatus": "Cancelled",
      "expiryDate": "31-07-2025 14:30:00"
    },
    {
      "action": "SELL",
      "assetType": "Futures",
      "dTradingSym": "NIFTY",
      "description": "NIFTY 28AUG2025",
      "exchange": "NSEFO",
      "executionPrice": "",
      "filledQuantity": "0",
      "limitPrice": "100",
      "marketlot": "75",
      "quantity": "75",
      "remainingQuantity": "75",
      "series": "FUTIDX",
      "symbol": "64103_NSEFO",
      "tickSize": "0.1",
      "tradingSymbol": "NIFTY 28AUG2025",
      "orderLegStatus": "SpreadSecondLeg",
      "nowOrderStatus": "Cancelled",
      "expiryDate": "28-08-2025 14:30:00"
    }
  ]
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/spread?accountID=SYMPH' \
--header 'Authorization: xxxxxx'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/orders/spread?accountID=SYMPH"

payload = {}
headers = {
    "Authorization": "xxxxxx"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    data=payload
)

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

    url := "https://developers.symphonyfintech.in/1interactive/orders/spread?accountID=SYMPH"
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
const axios = require("axios");

let config = {
  method: "get",
  maxBodyLength: Infinity,
  url: "https://developers.symphonyfintech.in/1interactive/orders/spread?accountID=SYMPH",
  headers: {
    "Authorization": "xxxxxx"
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
    "https://developers.symphonyfintech.in/1interactive/orders/spread?accountID=SYMPH"
);

request.Headers.Add("Authorization", "xxxxxx");

var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();

Console.WriteLine(await response.Content.ReadAsStringAsync());
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder().build();

Request request = new Request.Builder()
    .url("https://developers.symphonyfintech.in/1interactive/orders/spread?accountID=SYMPH")
    .method("GET", null)
    .addHeader("Authorization", "xxxxxx")
    .build();

Response response = client.newCall(request).execute();
```
