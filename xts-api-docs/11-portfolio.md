# Portfolio

A user's portfolio consists of long-term equity holdings and short-term positions.

## Holding (GET)

The Holdings API allows users to check their long-term holdings with the broker. An authorization token must be included with the request.

### URL

```http
GET https://developers.symphonyfintech.in/1interactive/portfolio/holdings?clientID=SYMP1
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **clientID** | String (Boolean, 15) | **N** | Client ID Mandatory in case of Dealer |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **ClientId** | UserID (String, 15) | User specific identification |
| **RMSHoldingList** | RMSHoldingList |  |
| **Holdings** | Holdings |  |
| **ISIN** | ISIN (String, 10) | The standard ISIN representing stocks listed on multiple exchanges |
| **RMSHoldingId** | RMSHoldingId (Integer, 10) | Unique holding ID |
| **ExchangeNSEInstrumentId** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **ExchangeBSEInstrumentId** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **ExchangeMSEInstrumentId** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **HoldingType** | HoldingType (Integer, 15) | It represents Holding Type i.e. [HoldingTypes](02-enums.md#17-holdingtype) |
| **HoldingQuantity** | Quantity (Integer, 10) | Holding quantity |
| **CollateralValuationType** | ValuationType (Integer, 5) | [ValuationType](02-enums.md#16-valuationtype) |
| **Haircut** | Haircut (Integer, 10) | **Haircut** refers to the **percentage reduction applied to the market value of a security** when calculating its collateral value |
| **CollateralQuantity** | Quantity (Integer, 10) | Quantities placed as collateral with broker |
| **CreatedBy** | CreatedBy (String, 20) | User or system identifier that created the holding record |
| **LastUpdatedBy** | LastUpdatedBy (String, 20) | User or system identifier that last modified or updated the holding record |
| **CreatedOn** | CreatedOn (String, 20) | Date and time when the holding record was first created |
| **LastUpdatedOn** | LastUpdatedOn (String, 20) | The date and time when the holding record was last modified or updated |
| **UsedQuantity** | Quantity (Integer, 10) | Quantity sold from the net holding quantity |
| **IsCollateralHolding** | IsCollateralHolding (Boolean, 5) | Indicates whether the holding is being used as **collateral** for margin or leverage |
| **BuyAvgPrice** | Price (Double, (15,4)) | Average price at which all shares were bought |
| **IsBuyAvgPriceProvided** | IsBuyAvgPriceProvided (Boolean, 5) | Indicates whether the **buy average price** for the holding has been provided or not |
| **AuthorizeQuantity** | Quantity (Integer, 10) | Quantity Authorized at the depository for sale |
| **IsNeedToDelete** | IsNeedToDelete (Boolean, 5) | Indicates whether the holding record needs to be **deleted or marked for removal** from the system |
| **CollateralHoldingList** | CollateralHoldingList |  |
| Holdings | Holdings |  |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-portfolio-0012",
  "description": "Success holding",
  "result": {
    "ClientId": "SYMP1",
    "RMSHoldingList": [
      {
        "Holdings": {
          "INF457M01133": {
            "ISIN": "INF457M01133",
            "RMSHoldingId": 21885,
            "ClientId": "SYMP1",
            "ExchangeNSEInstrumentId": 2328,
            "ExchangeBSEInstrumentId": 538057,
            "ExchangeMSEIInstrumentId": 0,
            "HoldingType": 2,
            "HoldingQuantity": 1,
            "CollateralValuationType": 1,
            "Haircut": 15,
            "CollateralQuantity": 1,
            "CreatedBy": "ADMIN2",
            "LastUpdatedBy": "ADMIN2",
            "CreatedOn": "2019-07-06T12:18:21",
            "LastUpdatedOn": "2019-07-06T11:39:29",
            "UsedQuantity": 0,
            "IsCollateralHolding": true,
            "BuyAvgPrice": 0,
            "IsBuyAvgPriceProvided": false,
            "AuthorizeQuantity": 0,
            "IsNeedToDelete": false
          }
        }
      }
    ],
    "CollateralHoldingList": [
      {
        "Holdings": {
          "INF457M01133": {
            "ISIN": "INF457M01133",
            "RMSHoldingId": 21885,
            "ClientId": "SYMP1",
            "ExchangeNSEInstrumentId": 2328,
            "ExchangeBSEInstrumentId": 538057,
            "ExchangeMSEIInstrumentId": 0,
            "HoldingType": 2,
            "HoldingQuantity": 1,
            "CollateralValuationType": 1,
            "Haircut": 15,
            "CollateralQuantity": 1,
            "CreatedBy": "ADMIN2",
            "LastUpdatedBy": "ADMIN2",
            "CreatedOn": "2019-07-06T12:18:21",
            "LastUpdatedOn": "2019-07-06T11:39:29",
            "UsedQuantity": 0,
            "IsCollateralHolding": true,
            "BuyAvgPrice": 0,
            "IsBuyAvgPriceProvided": false,
            "AuthorizeQuantity": 0,
            "IsNeedToDelete": false
          }
        }
      }
    ]
  }
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/portfolio/holdings' \
--header 'Authorization: xxxxxx'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/portfolio/holdings"

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

  url := "https://developers.symphonyfintech.in/1interactive/portfolio/holdings"
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
  url: 'https://developers.symphonyfintech.in/1interactive/portfolio/holdings',
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
var request = new HttpRequestMessage(HttpMethod.Get, "https://developers.symphonyfintech.in/1interactive/portfolio/holdings");
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
  .url("https://developers.symphonyfintech.in/1interactive/portfolio/holdings")
  .method("GET", body)
  .addHeader("Authorization", "xxxxxx")
  .build();
Response response = client.newCall(request).execute();
```

## Position (GET)

**The user's portfolio consists of short-term open positions in derivatives (futures and options contracts) and intraday equities.**

- Positions in a portfolio remain open until they are sold or until expiry.
- Derivative contracts usually expire in a **monthly sliding window** or a **weekly sliding window** of three periods, called **current, near, and far.**
- Long equity positions are moved to the **holding’s portfolio** after the settlement day.
- The **Positions API** returns two sets of positions:
- **Net →** The actual, current net position portfolio.
- **Day →** A snapshot of buying and selling activity for that particular day.

This distinction is useful for computing **profits and losses** for trading strategies.

### URL

```http
GET https://developers.symphonyfintech.in/1interactive/portfolio/positions?dayOrNet=DayWise
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **dayOrNet** | [DayOrNet](02-enums.md#13-dayornet) | Y | **Net →** The actual, current net position portfolio<br>**Day →** A snapshot of buying and selling activity for that particular day |
| **clientID** | String (Boolean, 15) | N | Client ID mandatory in case of Dealer |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **ExchangeSegment** | ExchangeSegment (String, 15) | ExchangeSegment |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **ProductType** | ProductType (String, 4) | Is the minimum number of shares or units of a security that can be traded on an exchange. |
| **Marketlot** | Marketlot (Integer, 5) | Multiplying factor for currency F&O |
| **Multiplier** | Multiplier (Integer, 5) | Multiplying factor for currency F&O |
| **BuyAveragePrice** | Price (Double, (15,4)) | Average price at which all shares were bought |
| **SellAveragePrice** | Price (Double, (15,4)) | Average price at which quantities were sold |
| **OpenBuyQuantity** | Quantity (Integer, 10) | Total bought quantity |
| **OpenSellQuantity** | Quantity (Integer, 10) | Total sold quantity |
| **Quantity** | Quantity (Integer, 10) | Net outstanding quantity |
| **BuyAmount** | Amount (Double, (15,4)) | Total buy value of position in rupees |
| **SellAmount** | SellAmount (Double, (15,4)) | Total sell value of position in rupees |
| **NetAmount** | UnrealizedMTM (Double, (15,4)) | Outstanding position value in rupees |
| **UnrealizedMTM** | UnrealizedMTM (Double, (15,4)) | It's unrealized profit or loss which has not been booked by client |
| **RealizedMTM** | RealizedMTM (Double, (15,4)) | It's realized profit or loss which has been booked by client |
| **MTM** | MTM (Double, (15,4)) | Mark to market returns (computed based on last close and last traded price) |
| **BEP** | BEP (Double, (15,4)) | It's break even point of position |
| **SumOfTradedQuantityAndPriceBuy** | SumOfQuantityAndPrice (Double, (15,4)) | Total buy value of position in rupees |
| **SumOfTradedQuantityAndPriceSell** | SumOfQuantityAndPrice (Double, (15,4)) | Total sell value of position in rupees |
| **statisticsLevel** | StatisticsLevel (String, 15) | [StatisticsLevel](02-enums.md#18-statisticslevel) |
| **isInterOpPosition** | IsInterOpPosition (Boolean, 5) | Interoperability is enabled or disabled |
| **MessageCode** | MessageCode (String, 10) | API MessageCode |
| **MessageVersion** | MessageVersion (String, 10) | API Message Version |
| **TokenID** | TokenID (String, 10) | API TokenID |
| **ApplicationType** | ApplicationType (String, 15) | API ApplicationType |
| **SequenceNumber** | SequenceNumber (String, 15) | API SequenceNumber |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-portfolio-0001",
  "description": "Success position",
  "result": [
    {
      "AccountID": "SYMP1",
      "TradingSymbol": "ACC",
      "ExchangeSegment": "NSECM",
      "ExchangeInstrumentID": 22,
      "ProductType": "CNC",
      "Marketlot": 1,
      "Multiplier": 1,
      "BuyAveragePrice": 41.78,
      "SellAveragePrice": 41.63,
      "OpenBuyQuantity": 10,
      "OpenSellQuantity": 0,
      "Quantity": 10,
      "BuyAmount": 1671,
      "SellAmount": 2498,
      "NetAmount": 827,
      "UnrealizedMTM": 0,
      "RealizedMTM": 0,
      "MTM": 0,
      "BEP": 0,
      "SumOfTradedQuantityAndPriceBuy": 1671,
      "SumOfTradedQuantityAndPriceSell": 2498,
      "statisticsLevel": "ParentLevel",
      "isInterOpPosition": "true",
      "childPositions": {
        "AccountID": "SYMP1",
        "TradingSymbol": "ACC",
        "ExchangeSegment": "NSECM",
        "ExchangeInstrumentID": "22",
        "ProductType": "CNC",
        "Marketlot": "1",
        "Multiplier": "1",
        "BuyAveragePrice": "41.78",
        "SellAveragePrice": "41.63",
        "OpenBuyQuantity": "10",
        "OpenSellQuantity": "0",
        "Quantity": "10",
        "BuyAmount": "1671.00",
        "SellAmount": "2498.00",
        "NetAmount": "827.00",
        "UnrealizedMTM": "0",
        "RealizedMTM": "0",
        "MTM": "0",
        "BEP": "0",
        "SumOfTradedQuantityAndPriceBuy": "1671.00",
        "SumOfTradedQuantityAndPriceSell": "2498.00",
        "statisticsLevel": "ParentLevel",
        "isInterOpPosition": "true"
      },
      "MessageCode": 9002,
      "MessageVersion": 1,
      "TokenID": 0,
      "ApplicationType": 0,
      "SequenceNumber": 0
    }
  ]
}
```

### Code Examples

**cURL**

```bash
curl --location 'https://developers.symphonyfintech.in/1interactive/portfolio/positions?dayOrNet=daywise' \
--header 'Authorization: xxxxxx'
```

**Python**

```python
import requests

url = "https://developers.symphonyfintech.in/1interactive/portfolio/positions?dayOrNet=daywise"

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

  url := "https://developers.symphonyfintech.in/1interactive/portfolio/positions?dayOrNet=daywise"
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
  url: 'https://developers.symphonyfintech.in/1interactive/portfolio/positions?dayOrNet=daywise',
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
var request = new HttpRequestMessage(HttpMethod.Get, "https://developers.symphonyfintech.in/1interactive/portfolio/positions?dayOrNet=daywise");
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
  .url("https://developers.symphonyfintech.in/1interactive/portfolio/positions?dayOrNet=daywise")
  .method("GET", body)
  .addHeader("Authorization", "xxxxxx")
  .build();
Response response = client.newCall(request).execute();
```

## Position Convert (PUT)

Convert Position API enables users to convert their open positions from NRML (Normal) to MIS (Margin Intraday Square-off) or vice versa, provided there is sufficient margin or funds in the account to complete the conversion.

### URL

```http
PUT https://developers.symphonyfintech.in/1interactive/portfolio/positions/convert
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [DayOrNet](02-enums.md#13-dayornet) | Y | **Net** → The actual, current net position portfolio<br>**Day** → A snapshot of buying and selling activity for that particular day |
| **exchangeInstrumentID** | ClientID (String, 15) | Y | Client ID Mandatory in case of Dealer |
| **oldProductType** | ProductType (String, 4) | Y | [ProductType](02-enums.md#2-producttype) |
| **newProductType** | ProductType (String, 4) | Y | [ProductType](02-enums.md#2-producttype) |
| **isDayWise** | IsDayWise (Boolean, 5) | Y | IsDayWise position conversion |
| **targetQty** | Quantity (Integer, 10) | Y | Quantity that needs to convert |
| **statisticsLevel** | StatisticsLevel (String, 15) | Y | [StatisticsLevel](02-enums.md#18-statisticslevel) |
| **isInterOpPosition** | sInterOpPosition (Boolean, 5) | Y | Interoperability is enabled or disabled |

### Request Body JSON

```json
{
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 2885,
  "oldProductType": "NRML",
  "newProductType": "MIS",
  "isDayWise": true,
  "targetQty": 0,
  "statisticsLevel": "ParentLevel",
  "isInterOpPosition": true
}
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-portfolio-0005",
  "description": "success position convert"
}
```

### Code Examples

**cURL**

```bash
curl --location --request PUT 'https://developers.symphonyfintech.in/1interactive/portfolio/positions/convert' \
--header 'Authorization: xxxxxx' \
--header 'Content-Type: application/json' \
--data '{
    "exchangeSegment": "NSECM",
    "exchangeInstrumentID": 2885,
    "targetQty": 1,
    "isDayWise": true,
    "oldProductType": "NRML",
    "newProductType": "MIS",
    "statisticsLevel":"0",
    "isInterOpPosition":false
}'
```

**Python**

```python
import requests
import json

url = "https://developers.symphonyfintech.in/1interactive/portfolio/positions/convert"

payload = json.dumps({
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 2885,
  "targetQty": 1,
  "isDayWise": True,
  "oldProductType": "NRML",
  "newProductType": "MIS",
  "statisticsLevel": "0",
  "isInterOpPosition": False
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

  url := "https://developers.symphonyfintech.in/1interactive/portfolio/positions/convert"
  method := "PUT"

  payload := strings.NewReader(`{`+"
"+`
    "exchangeSegment": "NSECM",`+"
"+`
    "exchangeInstrumentID": 2885,`+"
"+`
    "targetQty": 1,`+"
"+`
    "isDayWise": true,`+"
"+`
    "oldProductType": "NRML",`+"
"+`
    "newProductType": "MIS",`+"
"+`
    "statisticsLevel":"0",`+"
"+`
    "isInterOpPosition":false`+"
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
  "exchangeSegment": "NSECM",
  "exchangeInstrumentID": 2885,
  "targetQty": 1,
  "isDayWise": true,
  "oldProductType": "NRML",
  "newProductType": "MIS",
  "statisticsLevel": "0",
  "isInterOpPosition": false
});

let config = {
  method: 'put',
  maxBodyLength: Infinity,
  url: 'https://developers.symphonyfintech.in/1interactive/portfolio/positions/convert',
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
var request = new HttpRequestMessage(HttpMethod.Put, "https://developers.symphonyfintech.in/1interactive/portfolio/positions/convert");
request.Headers.Add("Authorization", "xxxxxx");
var content = new StringContent("{\r\n    \"exchangeSegment\": \"NSECM\",\r\n    \"exchangeInstrumentID\": 2885,\r\n    \"targetQty\": 1,\r\n    \"isDayWise\": true,\r\n    \"oldProductType\": \"NRML\",\r\n    \"newProductType\": \"MIS\",\r\n    \"statisticsLevel\":\"0\",\r\n    \"isInterOpPosition\":false\r\n}", null, "application/json");
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
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"exchangeSegment\": \"NSECM\",\r\n    \"exchangeInstrumentID\": 2885,\r\n    \"targetQty\": 1,\r\n    \"isDayWise\": true,\r\n    \"oldProductType\": \"NRML\",\r\n    \"newProductType\": \"MIS\",\r\n    \"statisticsLevel\":\"0\",\r\n    \"isInterOpPosition\":false\r\n}");
Request request = new Request.Builder()
  .url("https://developers.symphonyfintech.in/1interactive/portfolio/positions/convert")
  .method("PUT", body)
  .addHeader("Authorization", "xxxxxx")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```
