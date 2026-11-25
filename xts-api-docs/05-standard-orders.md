# Standard Orders

## Place Order API (POST)

### Order Placement Workflow & Key Considerations

- Read all ENUM values from the login response along with the **authentication token**
- Use the ENUM values and token when **constructing the Place Order request**
- The **token must be included in the JSON request headers for all API calls** for all API calls
- The **Place Order request is asynchronous** in nature
- On submission, the user receives an **appOrderID**
- The **appOrderID** can be used later with the **Order Book (Get Order) API** to confirm order execution.
- The **execution of an order** depends on multiple factors: (1.RMS limits, 2.Risk checks, 3.Other validations)
- **Limit orders** may remain **open throughout the trading day** if not executed.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | ExchangeSegment (String, 15) | Y | ExchangeSegment |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Y | Exchange Scrip code or Symbol Token is unique identifier |
| **productType** | ProductType (String, 4) | Y | [ProductType](02-enums.md#2-producttype) |
| **orderType** | OrderType (String, 10) | Y | [OrderType](02-enums.md#3-ordertype) |
| **orderSide** | OrderSide (String, 4) | Y | [OrderSide](02-enums.md#4-orderside) |
| **timeInForce** | TimeInForce (String, 5) | Y | [TimeInForce](02-enums.md#5-timeinforce) |
| **disclosedQuantity** | OrderQuantity (Integer, -) | Y | Quantity to disclose (for equity) |
| **orderQuantity** | OrderQuantity (Integer, -) | Y | Quantity to transact. In terms of Lots |
| **limitPrice** | Price (Double, (15,4)) | Y | The price to execute the order at |
| **stopPrice** | Price (Double, (15,4)) | Y | The price at which an order should be triggered (SL, SL-M) |
| **orderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | N | Echo back to identify order |
| **clientID** | ClientID (String, 15) | N | ClientID Mandatory in case of Dealer |
| **apiOrderSource** | ApiOrderSource (String, 20) | N | API Order Source can be a third party application name which you want to give to your order, which will be used to track your order with a particular source. |

### Request Body JSON

```json
{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 3045,
  "productType": "NRML",
  "orderType": "LIMIT",
  "orderSide": "BUY",
  "timeInForce": "DAY",
  "disclosedQuantity": 0,
  "orderQuantity": 15,
  "limitPrice": 254.55,
  "stopPrice": 245.55,
  "orderUniqueIdentifier": "123abc",
  "clientID": "SYMP1",
  "apiOrderSource": "ThirdPartyAppName"
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **AppOrderID** | AppOrderID (String, 15d) | Unique order ID |
| OrderUniqueIdentifier | OrderUniqueIdentifier (String, 15d) | Echo back to identify order |
| ClientID | ClientID (String, 15d6) | ClientID which is send in request body |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-orders-0001",
  "description": "Request sent",
  "result": {
    "AppOrderID": 2190766863,
    "OrderUniqueIdentifier": "123abc",
    "ClientID": "SYMP1"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders' \
--header 'Authorization: xxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 2885,
  "productType": "NRML",
  "orderType": "LIMIT",
  "orderSide": "BUY",
  "timeInForce": "DAY",
  "disclosedQuantity": 0,
  "orderQuantity": 1,
  "limitPrice": 1500,
  "stopPrice": 0,
  "orderUniqueIdentifier": "testtt"
}'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/orders"

payload = {
    "exchangeSegment": "BSECM",
    "exchangeInstrumentID": 500325,
    "productType": "NRML",
    "orderType": "LIMIT",
    "orderSide": "BUY",
    "timeInForce": "DAY",
    "disclosedQuantity": 0,
    "orderQuantity": 1,
    "limitPrice": 1500,
    "stopPrice": 0,
    "orderUniqueIdentifier": "testtt"
}

headers = {
    "Authorization": "xxxxxxxxxx",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
```

**Go**

```go
package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
)

func main() {

	url := "https://developers.symphonyfintech.in/1interactive/orders"

	payload := []byte(`{
		"exchangeSegment": "NSECM",
		"exchangeInstrumentID": 2885,
		"productType": "NRML",
		"orderType": "LIMIT",
		"orderSide": "BUY",
		"timeInForce": "DAY",
		"disclosedQuantity": 0,
		"orderQuantity": 1,
		"limitPrice": 1500,
		"stopPrice": 0,
		"orderUniqueIdentifier": "testtt",
		"algoID": "21001",
		"algoCategory": "211"
	}`)

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	req.Header.Set("Authorization", "xxxxxxxxxx")
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer res.Body.Close()

	body, err := io.ReadAll(res.Body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	fmt.Println("Status Code:", res.StatusCode)
	fmt.Println("Response:", string(body))
}
```

**Node.js**

```javascript
const axios = require("axios");

const url = "https://developers.symphonyfintech.in/1interactive/orders";

const payload = {
  exchangeSegment: "NSECM",
  exchangeInstrumentID: 2885,
  productType: "NRML",
  orderType: "LIMIT",
  orderSide: "BUY",
  timeInForce: "DAY",
  disclosedQuantity: 0,
  orderQuantity: 1,
  limitPrice: 1500,
  stopPrice: 0,
  orderUniqueIdentifier: "testtt",
  algoID: "21001",
  algoCategory: "211"
};

const config = {
  method: "post",
  url,
  headers: {
    Authorization: "xxxxxxxxxx",
    "Content-Type": "application/json"
  },
  data: payload
};

axios(config)
  .then(response => {
    console.log("Status:", response.status);
    console.log("Response:", response.data);
  })
  .catch(error => {
    if (error.response) {
      console.error("Error Status:", error.response.status);
      console.error("Error Data:", error.response.data);
    } else {
      console.error("Error:", error.message);
    }
  });
```

**C#**

```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var client = new HttpClient();

        var url = "https://developers.symphonyfintech.in/1interactive/orders";

        var payload = new
        {
            exchangeSegment = "NSECM",
            exchangeInstrumentID = 2885,
            productType = "NRML",
            orderType = "LIMIT",
            orderSide = "BUY",
            timeInForce = "DAY",
            disclosedQuantity = 0,
            orderQuantity = 1,
            limitPrice = 1500,
            stopPrice = 0,
            orderUniqueIdentifier = "testtt",
            algoID = "21001",
            algoCategory = "211"
        };

        var json = System.Text.Json.JsonSerializer.Serialize(payload);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        client.DefaultRequestHeaders.Add("Authorization", "xxxxxxxxxx");

        var response = await client.PostAsync(url, content);
        response.EnsureSuccessStatusCode();

        var responseBody = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Response:");
        Console.WriteLine(responseBody);
    }
}
```

**Java**

```java
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class Main {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();

        MediaType mediaType = MediaType.parse("application/json");

        String jsonPayload = """
        {
          "exchangeSegment": "NSECM",
          "exchangeInstrumentID": 2885,
          "productType": "NRML",
          "orderType": "LIMIT",
          "orderSide": "BUY",
          "timeInForce": "DAY",
          "disclosedQuantity": 0,
          "orderQuantity": 1,
          "limitPrice": 1500,
          "stopPrice": 0,
          "orderUniqueIdentifier": "testtt",
          "algoID": "21001",
          "algoCategory": "211"
        }
        """;

        RequestBody body = RequestBody.create(jsonPayload, mediaType);

        Request request = new Request.Builder()
                .url("https://developers.symphonyfintech.in/1interactive/orders")
                .post(body)
                .addHeader("Authorization", "xxxxxxxxxx")
                .addHeader("Content-Type", "application/json")
                .build();

        try (Response response = client.newCall(request).execute()) {
            System.out.println("Status Code: " + response.code());
            System.out.println("Response: " + response.body().string());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## Modify Order API (PUT)

XTS provides the ability to modify open orders by allowing you to change a limit order to a market order (or vice versa), update the price or quantity of an open limit order, and modify the disclosed quantity or stop-loss of any open stop-loss order. ***Note:*** XTS considers open orders whose order status is either New, Replaced, PartiallyFilled.

### URL

```http
PUT https://developers.symphonyfintech.in/1interactive/orders
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appOrderID | AppOrderID (Integer, 10) | **Y** | It is system generated unique order number |
| modifiedProductType | ProductType (String, 4) | **Y** | [ProductType](02-enums.md#2-producttype) |
| modifiedOrderType | OrderType (String, 10) | **Y** | OrderType |
| modifiedDisclosedQuantity | Quantity (Integer, 10) | **Y** | Quantity to disclose (for equity) |
| modifiedOrderQuantity | Quantity (Integer, 10) | **Y** | Quantity to transact. In terms of Lots |
| modifiedLimitPrice | Price (Double, (15,4)) | **Y** | The price to execute the order at |
| modifiedStopPrice | Price (Double, (15,4)) | **Y** | The price at which an order should be triggered (SL, SL-M) |
| modifiedTimeInForce | TimeInForce (String, 5) | **Y** | TimeInForce |
| orderUniqueIdentifier | OrderUniqueIdentifier (String, 20) | **N** | Echo back to identify order |
| apiOrderSource | ApiOrderSource (String, 20) | **N** | API Order Source can be third party application name which you want to give to your order, which will be used to track your order with particular source. |
| clientID | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |

### Request Body JSON

```json
{
  "appOrderID": 2190766863,
  "modifiedProductType": "NRML",
  "modifiedOrderType": "LIMIT",
  "modifiedOrderQuantity": 25,
  "modifiedDisclosedQuantity": 0,
  "modifiedLimitPrice": 255.65,
  "modifiedStopPrice": 0,
  "modifiedTimeInForce": "DAY",
  "orderUniqueIdentifier": "123abc",
  "apiOrderSource": "ThirdPartyAppName"
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **AppOrderID** | AppOrderID | Unique order ID |
| **OrderUniqueIdentifier** | OrderUniqueIdentifier | Echo back to identify order |
| **ClientID** | ClientID | ClientID which is send in request body |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-orders-0001",
  "description": "Request sent",
  "result": {
    "AppOrderID": 2190766863,
    "OrderUniqueIdentifier": "123abc",
    "ClientID": "SYMP1"
  }
}
```

### Code Examples

**cURL**

```bash
curl --location --request PUT 'https://developers.symphonyfintech.in/1interactive/orders' \
--header 'Authorization: xxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "appOrderID": "10001253450000041478",
  "modifiedProductType": "NRML",
  "modifiedOrderType": "LIMIT",
  "modifiedOrderQuantity": 75,
  "modifiedDisclosedQuantity": 0,
  "modifiedLimitPrice": 28000,
  "modifiedStopPrice": 0,
  "modifiedTimeInForce": "DAY",
  "orderUniqueIdentifier": "x12"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders"

payload = json.dumps({
    "appOrderID": "10001253450000041478",
    "modifiedProductType": "NRML",
    "modifiedOrderType": "LIMIT",
    "modifiedOrderQuantity": 75,
    "modifiedDisclosedQuantity": 0,
    "modifiedLimitPrice": 28000,
    "modifiedStopPrice": 0,
    "modifiedTimeInForce": "DAY",
    "orderUniqueIdentifier": "x12"
})

headers = {
    "Authorization": "xxxxxxxxxx",
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

    url := "https://developers.symphonyfintech.in/1interactive/orders"
    method := "PUT"

    payload := strings.NewReader(`{
        "appOrderID": "10001253450000041478",
        "modifiedProductType": "NRML",
        "modifiedOrderType": "LIMIT",
        "modifiedOrderQuantity": 75,
        "modifiedDisclosedQuantity": 0,
        "modifiedLimitPrice": 28000,
        "modifiedStopPrice": 0,
        "modifiedTimeInForce": "DAY",
        "orderUniqueIdentifier": "x12"
    }`)

    client := &http.Client{}
    req, err := http.NewRequest(method, url, payload)

    if err != nil {
        fmt.Println(err)
        return
    }

    req.Header.Add("Authorization", "xxxxxxxxxx")
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
  "appOrderID": "10001253450000041478",
  "modifiedProductType": "NRML",
  "modifiedOrderType": "LIMIT",
  "modifiedOrderQuantity": 75,
  "modifiedDisclosedQuantity": 0,
  "modifiedLimitPrice": 28000,
  "modifiedStopPrice": 0,
  "modifiedTimeInForce": "DAY",
  "orderUniqueIdentifier": "x12"
});

let config = {
  method: "put",
  maxBodyLength: Infinity,
  url: "https://developers.symphonyfintech.in/1interactive/orders",
  headers: {
    "Authorization": "xxxxxxxxxx",
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
    "https://developers.symphonyfintech.in/1interactive/orders"
);

request.Headers.Add("Authorization", "xxxxxxxxxx");

var content = new StringContent(
    "{\r\n" +
    "  \"appOrderID\": \"10001253450000041478\",\r\n" +
    "  \"modifiedProductType\": \"NRML\",\r\n" +
    "  \"modifiedOrderType\": \"LIMIT\",\r\n" +
    "  \"modifiedOrderQuantity\": 75,\r\n" +
    "  \"modifiedDisclosedQuantity\": 0,\r\n" +
    "  \"modifiedLimitPrice\": 28000,\r\n" +
    "  \"modifiedStopPrice\": 0,\r\n" +
    "  \"modifiedTimeInForce\": \"DAY\",\r\n" +
    "  \"orderUniqueIdentifier\": \"x12\"\r\n" +
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
    "  \"appOrderID\": \"10001253450000041478\",\r\n" +
    "  \"modifiedProductType\": \"NRML\",\r\n" +
    "  \"modifiedOrderType\": \"LIMIT\",\r\n" +
    "  \"modifiedOrderQuantity\": 75,\r\n" +
    "  \"modifiedDisclosedQuantity\": 0,\r\n" +
    "  \"modifiedLimitPrice\": 28000,\r\n" +
    "  \"modifiedStopPrice\": 0,\r\n" +
    "  \"modifiedTimeInForce\": \"DAY\",\r\n" +
    "  \"orderUniqueIdentifier\": \"x12\"\r\n" +
    "}"
);

Request request = new Request.Builder()
    .url("https://developers.symphonyfintech.in/1interactive/orders")
    .method("PUT", body)
    .addHeader("Authorization", "xxxxxxxxxx")
    .addHeader("Content-Type", "application/json")
    .build();

Response response = client.newCall(request).execute();
```

## Cancel Order API (DELETE)

This API can be used to cancel any open order by providing the correct appOrderID that matches the selected open order. ***Note:*** XTS considers open orders whose order status is either New, Replaced, PartiallyFilled.

### URL

```http
DELETE https://developers.symphonyfintech.in/1interactive/orders?appOrderID=2190766863
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **AppOrderID** | AppOrderID (Integer, 10) | **Y** | Unique order ID |
| **OrderUniqueIdentifier** | OrderUniqueIdentifier (String, 20) | **Y** | Echo back to identify order |
| **ClientID** | ClientID (String, 15) | **N** | ClientID which is send in request body |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-user-0001",
  "description": "Request sent",
  "result": [
    {
      "AppOrderID": 1200043151,
      "ClientID": "SYMP"
    }
  ]
}
```

### Code Examples

**cURL**

```bash
curl --location --request DELETE 'https://developers.symphonyfintech.in/1interactive/orders?appOrderID=1000125345' \
--header 'Authorization: xxxxxxxxxx' \
--data ''
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/orders?appOrderID=1000125345"

payload = ""

headers = {
    "Authorization": "xxxxxxxxxx"
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

    url := "https://developers.symphonyfintech.in/1interactive/orders?appOrderID=1000125345"
    method := "DELETE"

    payload := strings.NewReader("")

    client := &http.Client{}
    req, err := http.NewRequest(method, url, payload)

    if err != nil {
        fmt.Println(err)
        return
    }

    req.Header.Add("Authorization", "xxxxxxxxxx")

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
  url: "https://developers.symphonyfintech.in/1interactive/orders?appOrderID=1000125345",
  headers: {
    "Authorization": "xxxxxxxxxx"
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
    "https://developers.symphonyfintech.in/1interactive/orders?appOrderID=1000125345"
);

request.Headers.Add("Authorization", "xxxxxxxxxx");

var content = new StringContent(
    "",
    null,
    "text/plain"
);

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
    .url("https://developers.symphonyfintech.in/1interactive/orders?appOrderID=1000125345")
    .method("DELETE", body)
    .addHeader("Authorization", "xxxxxxxxxx")
    .build();

Response response = client.newCall(request).execute();
```

## CancelAll Order (POST)

### This API can be called for a particular segment to either:

- **Cancel all open orders of the user by passing 0 in ExchangeInstrumentID** in the request.
- **Cancel all open orders for a specific instrument by passing its ExchangeInstrumentID (e.g., 3045)** in the request.
- **For example:**
- If you pass ExchangeSegment: NSECM and ExchangeInstrumentID: 0, it will cancel **all open orders for NSECM** for that user.
- If you pass ExchangeSegment: NSECM and ExchangeInstrumentID: 3045, it will cancel **all open orders for NSECM SBIN (3045)** for that user.

***Note:*** XTS considers open orders whose order status is either New, Replaced, PartiallyFilled.

### URL

```http
POST https://developers.symphonyfintech.in/1interactive/orders/cancelall
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | ExchangeSegment (String, 15) | **Y** | ExchangeSegment |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |
| **clientID** | ClientID (String, 15) | **N** | Client ID Mandatory in case of Dealer |

### Request Body JSON

```json
[
  {
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 3045
  }
]
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-cancelAll-0001",
  "description": "Cancel All Order Request Send Successfully",
  "result": ""
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/orders/cancelall' \
--header 'Authorization: xxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": "1333"
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/orders/cancelall"

payload = json.dumps({
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": "1333"
})

headers = {
    "Authorization": "xxxxxxxxxx",
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

    url := "https://developers.symphonyfintech.in/1interactive/orders/cancelall"
    method := "POST"

    payload := strings.NewReader(`{
        "exchangeSegment": "NSECM",
        "exchangeInstrumentID": "1333"
    }`)

    client := &http.Client{}
    req, err := http.NewRequest(method, url, payload)

    if err != nil {
        fmt.Println(err)
        return
    }

    req.Header.Add("Authorization", "xxxxxxxxxx")
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
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": "1333"
});

let config = {
  method: "post",
  maxBodyLength: Infinity,
  url: "https://developers.symphonyfintech.in/1interactive/orders/cancelall",
  headers: {
    "Authorization": "xxxxxxxxxx",
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
    "https://developers.symphonyfintech.in/1interactive/orders/cancelall"
);

request.Headers.Add("Authorization", "xxxxxxxxxx");

var content = new StringContent(
    "{\r\n" +
    "  \"exchangeSegment\": \"NSECM\",\r\n" +
    "  \"exchangeInstrumentID\": \"1333\"\r\n" +
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
    "  \"exchangeSegment\": \"NSECM\",\r\n" +
    "  \"exchangeInstrumentID\": \"1333\"\r\n" +
    "}"
);

Request request = new Request.Builder()
    .url("https://developers.symphonyfintech.in/1interactive/orders/cancelall")
    .method("POST", body)
    .addHeader("Authorization", "xxxxxxxxxx")
    .addHeader("Content-Type", "application/json")
    .build();

Response response = client.newCall(request).execute();
```
