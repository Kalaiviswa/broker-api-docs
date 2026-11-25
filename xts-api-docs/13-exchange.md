# Exchange

## Exchange Status (GET)

Exchange Status indicates the availability of eligible exchanges for normal trading. It allows users to determine whether they can place an order or not.

### URL

```http
GET https://developers.symphonyfintech.in/1interactive/status/exchange?userID=SYMP
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **userID** | UserID (String, 15) | Y | User specific identification |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](02-enums.md#1-exchangesegments) | [ExchangeSegment](02-enums.md#1-exchangesegments) |
| **exchangeMarketType** | MarketType | MarketType |
| **exchangeTradingSession** | [TradingSession](02-enums.md#15-tradingsession) | [TradingSession](02-enums.md#15-tradingsession) |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-status-0002",
  "description": "Exchange status available",
  "result": {
    "marketStatus": [
      {
        "exchangeSegment": "NSECM",
        "exchangeMarketType": "AUCTION",
        "exchangeTradingSession": "NormalEnd"
      },
      {
        "exchangeSegment": "NSECM",
        "exchangeMarketType": "CALLAUCTION2",
        "exchangeTradingSession": "PreOpenStart"
      },
      {
        "exchangeSegment": "NSECM",
        "exchangeMarketType": "ODDLOT",
        "exchangeTradingSession": "NormalEnd"
      },
      {
        "exchangeSegment": "NSECM",
        "exchangeMarketType": "NORMAL",
        "exchangeTradingSession": "PreClosingStart"
      },
      {
        "exchangeSegment": "NSEFO",
        "exchangeMarketType": "NORMAL",
        "exchangeTradingSession": "NormalEnd"
      },
      {
        "exchangeSegment": "BSECM",
        "exchangeMarketType": "AUCTION",
        "exchangeTradingSession": "NormalStart"
      },
      {
        "exchangeSegment": "BSECM",
        "exchangeMarketType": "CALLAUCTION2",
        "exchangeTradingSession": "NormalEnd"
      },
      {
        "exchangeSegment": "BSECM",
        "exchangeMarketType": "NORMAL",
        "exchangeTradingSession": "PreClosingStart"
      }
    ]
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/status/exchange?userID=SYMPTEST' \
--header 'Authorization: xxxxxx'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/status/exchange?userID=SYMPTEST"

payload = {}
headers = {
  'Authorization': 'xxxxxx'
}

response = requests.request("GET", url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/status/exchange?userID=SYMPTEST"
  method := "GET"

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
  method: 'get',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/status/exchange?userID=SYMPTEST',
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
var request = new HttpRequestMessage(HttpMethod.Get, "https://developers.symphonyfintech.in/1interactive/status/exchange?userID=SYMPTEST");
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
  .url("https://developers.symphonyfintech.in/1interactive/status/exchange?userID=SYMPTEST")
  .method("GET", body)
  .addHeader("Authorization", "xxxxxx")
  .build();
Response response = client.newCall(request).execute();
```

## Exchange Message (GET)

The exchange sends various messages to connected brokers, such as information about bans, circuit limits, and news about listed companies. Users can access messages relevant to them using this API.

### URL

```http
GET https://developers.symphonyfintech.in/1interactive/messages/exchange?exchangeSegment=NSECM
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](02-enums.md#1-exchangesegments) | Y | ExchangeSegment |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](02-enums.md#1-exchangesegments) | [ExchangeSegment](02-enums.md#1-exchangesegments) |
| **ExchangeTimeStamp** | ExchangeTimeStamp | Date and time provided by the exchange when a specific event or message was generated. |
| **BroadcastMessage** | BroadcastMessage (String, 500) | Message Send by exchange |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-messages-0001",
  "description": "Exchange messages",
  "result": {
    "messageList": [
      {
        "ExchangeSegment": 2,
        "ExchangeTimeStamp": 1452777915,
        "BroadcastMessage": "Listing -> CORPORATE ANNOUNCEMENTS",
        "SequenceId": 1904678908069178,
        "ExchangeInstrumentID": 0,
        "MessageCode": 1506,
        "MessageVersion": 8,
        "TokenID": 0,
        "ApplicationType": 0,
        "SequenceNumber": 1904678908069177
      }
    ]
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/messages/exchange?exchangeSegment=NSECM' \
--header 'Authorization: xxxxxx' \
--data ''
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/messages/exchange?exchangeSegment=NSECM"

payload = ""
headers = {
  'Authorization': 'xxxxxx'
}

response = requests.request("GET", url, headers=headers, data=payload)
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

  url := "https://developers.symphonyfintech.in/1interactive/messages/exchange?exchangeSegment=NSECM"
  method := "GET"

  payload := strings.NewReader(``)

  client := &http.Client {
  }
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
const axios = require('axios');
let data = '';

let config = {
  method: 'get',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/messages/exchange?exchangeSegment=NSECM',
  headers: {
    'Authorization': 'xxxxxx'
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
var request = new HttpRequestMessage(HttpMethod.Get, "https://developers.symphonyfintech.in/1interactive/messages/exchange?exchangeSegment=NSECM");
request.Headers.Add("Authorization", "xxxxxx");
var content = new StringContent("", null, "text/plain");
request.Content = content;
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
  .url("https://developers.symphonyfintech.in/1interactive/messages/exchange?exchangeSegment=NSECM")
  .method("GET", body)
  .addHeader("Authorization", "xxxxxx")
  .build();
Response response = client.newCall(request).execute();
```
