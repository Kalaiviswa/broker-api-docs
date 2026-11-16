# Live News

Api's related to Live News

## News Categories

Categories that user can chose based on his/her discretion

> Code samples

```javascript
 const { APIConnect } = require("api_connect_nodejs");
 const apiConnect = new APIConnect(
   apiKey,
   password,
   reqId,
   downloadContract
 );
 apiConnect
   .Init()
   .then(() => {
     const newsCategories = apiConnect
       .getNewsCategories()
       .then(function (result) {})
       .catch((err) => {
         console.log("Error newsCategories", err);
         throw err;
       });
   })
   .catch((err) => console.log("Init Failed", err));
        
 
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.getNewsCategories()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
connect. getNewsCategories();
 
```

`GET /liveNews/getfiltersandcatagories`

> Example responses

> 200 Response

```
   {"resp":
   {
     "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
     "srvTm": 1660900624895,
     "data": {
        "ctLst": [
          {
            "dpNm": "string",
            "cat": "string",
            "uiTyp": "string"
          }
        ],
        "newsFilters": [
          {
            "dpNm": "string",
            "inc": [
              "string"
            ],
            "exc": [
              "string"
            ],
            "lgrq": true,
            "uiTyp": "string"
          }
        ]
   } 
  }
}
 
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

News Categories Ends Here
Live News Starts Here

## Live News

Provides the user with the live news of the equity stocks

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.getLiveNews(string category, bool holdings, string searchText, int pgNum);
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const liveNews = apiConnect
      .getLiveNews(category, searchText, holdings, pageNumber)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error liveNews", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.getLiveNews(holdings = False, category = "Budget", searchText = "price", pageNumber = 1)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
connect.getLiveNews(String category, boolean holdings, String searchText , String fromDate , int pgNum);        
```

`POST /liveNews/general`

### Parameters

| Parameter | Description |
| --- | --- |
| Category | Categories that user can chose based on his/her discretion |
| Holdings | This will help fetch the news only for that holdings held in the user account |
| Search_Text | Will help filter out the news content that user is seeking |
| Page_Number | Mention the page number and then search |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
        "listResponse": {
          "content": [
            {
              "title": "string",
              "desc": "string",
              "guid": "string",
              "category": "string",
              "date": "string",
              "timeText": "string",
              "customElements": [
                {
                  "hghlTxt": "string",
                  "dpName": "string",
                  "sym": "string",
                  "trdSym": "string",
                  "chgP": "string"
                }
              ]
            }
          ],
          "totalElements": 0,
          "first": true,
          "last": true,
          "totalPages": 0,
          "size": 0,
          "number": 0
        },
        "groupResponse": {
          "content": [
            {
              "sym": "string",
              "ltp": "string",
              "ltt": "string",
              "chg": "string",
              "chgP": "string",
              "exc": "string",
              "vol": "string",
              "dpName": "string",
              "trdSym": "string",
              "asTyp": "string",
              "ltSz": "string",
              "tkSz": "string",
              "dpInsTyp": "string",
              "desc": "string",
              "dpVal": "string",
              "symbol": "string",
              "hasMoreNewsItems": true,
              "newsItems": [
                {
                  "title": "string",
                  "desc": "string",
                  "guid": "string",
                  "category": "string",
                  "date": "string",
                  "timeText": "string",
                  "customElements": {
                    "hghlTxt": "string",
                    "dpName": "string",
                    "sym": "string",
                    "trdSym": "string",
                    "chgP": "string"
                  }
                }
              ]
            }
          ],
          "totalElements": 0,
          "first": true,
          "last": true,
          "totalPages": 0,
          "size": 0,
          "number": 0
        }        
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Live News Ends Here
Results & News Starts Here

## Results & News

Results that are announced for all stocks that user holds in the account

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.getResultsAndStocksNews(bool holdings, string searchText, int pgNum);
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const resultAndStocksNews = apiConnect
      .getResultsAndStocksNews(searchText, holdings, pageNumber)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error resultAndStocksNews", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.getNewsForResultsAndStocks(holdings = False, searchText = "price", pageNumber = 1)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
connect.getResultsAndStocksNews(boolean holdings, String searchText , String fromDate , int pgNum);
```

`POST /liveNews/general`

### Parameters

| Parameter | Description |
| --- | --- |
| Holdings | This will help fetch the news only for that holdings held in the user account |
| Search_Text | Will help filter out the news content that user is seeking |
| Page_Number | Mention the page number and then search |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "listResponse": {
        "content": [
          {
            "title": "string",
            "desc": "string",
            "guid": "string",
            "category": "string",
            "date": "string",
            "timeText": "string",
            "customElements": [
              {
                "hghlTxt": "string",
                "dpName": "string",
                "sym": "string",
                "trdSym": "string",
                "chgP": "string"
              }
            ]
          }
        ],
        "totalElements": 0,
        "first": true,
        "last": true,
        "totalPages": 0,
        "size": 0,
        "number": 0
      },
      "groupResponse": {
        "content": [
          {
            "sym": "string",
            "ltp": "string",
            "ltt": "string",
            "chg": "string",
            "chgP": "string",
            "exc": "string",
            "vol": "string",
            "dpName": "string",
            "trdSym": "string",
            "asTyp": "string",
            "ltSz": "string",
            "tkSz": "string",
            "dpInsTyp": "string",
            "desc": "string",
            "dpVal": "string",
            "symbol": "string",
            "hasMoreNewsItems": true,
            "newsItems": [
              {
                "title": "string",
                "desc": "string",
                "guid": "string",
                "category": "string",
                "date": "string",
                "timeText": "string",
                "customElements": {
                  "hghlTxt": "string",
                  "dpName": "string",
                  "sym": "string",
                  "trdSym": "string",
                  "chgP": "string"
                }
              }
            ]
          }
        ],
        "totalElements": 0,
        "first": true,
        "last": true,
        "totalPages": 0,
        "size": 0,
        "number": 0
      }    
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Results & Stocks Ends Here
Corporate Actions Starts Here

## Latest Corporate Actions

This will help user see if there are any corporate actions only for stocks that user hold in the account

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect. getLatestCorporateActions(string symbol);
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const corporateAction = apiConnect
      .getCorporateAction(symbol)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error corporateAction", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err)); 
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.getLatestCorporateActions(symbol = "14977_NSE")
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
connect.getCorporateActions(String symbol);
```

`GET /events/latestcorpactions/{sym}`

### Parameters

| Parameter | Description |
| --- | --- |
| Symbol | Each Symbol is unique and represents the stock identity. This is the exchange token to be obtained from the contract file downloaded |

> Example responses

> 200 Response

```
{"resp":
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "resLst": [
    {
      "date": "string",
      "event": "string",
      "val": "string"
    }
  ],
  "dpName": "string"
  } 
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Corporate Actions Ends Here
Get Watchlist groups starts here
