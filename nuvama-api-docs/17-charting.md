# Charting

Api's related to Charting

## Intraday tick by tick Historical Data

The exchange provides data for every tick received by the exchange from various market participants.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.GetIntradayChart(ChartExchangeEnum exchange,ChartAssetTypeEnum assetType,
ChartIntradayIntervalEnum interval,string symbol,string tillDate=null,bool includeContinousFuture=false);
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
    const intradayChart = apiConnect
      .getIntradayChart(
        interval,
        assetType,
        symbol,
        exchangeType,
        tillDate,
        includeContinuousFuture
      )
      .then(function (result) {})
      .catch((err) => {
        console.log("Error intradayChart", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
from constants.asset_type import AssetTypeEnum
from constants.chart_exchange import ChartExchangeEnum
from constants.intraday_interval import IntradayIntervalEnum
response = api_connect.getIntradayChart(ChartExchangeEnum.NSE, AssetTypeEnum.EQUITY, "11423_NSE", IntradayIntervalEnum.H1, TillDate = "2022-01-01", IncludeContinuousFutures = False)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
connect.getIntradayChart(ChartExchangeEnum exchange, ChartAssetTypeEnum assetType,ChartIntradayIntervalEnum interval, String streamingSymbol,String tillDate, Boolean includeContinuousFuture)
```

`POST /charts/v2/main/{interval}/{exc}/{aTyp}/{symbol}`

### Parameters

| Parameter | Description |
| --- | --- |
| Interval | It is the candle interval or length of time that one chooses for a candle data to be displayed. The body of the candle represents the opening and closing price including high and low of candle based on the interval. The available time intervals are M15,H1,M5,M1,M30,M3 |
| Asset_Type | It is the class of asset FUTCOM,FUTSTK,OPTCUR,OPTIDX,INDEX,OPTSTK,EQUITY,OPTFUT,FUTIDX,FUTCUR |
| Symbol | Each Symbol is unique and represents the stock identity. This is the exchange token to be obtained from the contract file downloaded |
| Exchange_Type | It is the name of the segment like BSE, CDS,NSE,INDEX,NFO,NCDEX,MCX |
| Till_Date | If user passes the value against the till date variable then the data is fetched until a day prior to the date selected. For eg: if you choose till date as 2022-12-07 while sending the request, the response will have the data until 2022-12-06 If user passes the ‘NULL’ against the till date variable then data is fetched till today. For eg: if the current date is 2022-12-07, when you pass None, the data is fetched till 2022-12-07 |
| Include_Continuous_Future | This attribute is applicable only for the futures - FUTIDX, FUTSTK, FUTCUR, FUTCOM |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| body | body | true | none |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": [
      ["2021-05-27 00:00:00", 11, 11.22, 11, 11, 56087],
      ["2021-06-21 00:00:00", 10.8, 10.8, 9.8, 9.8, 909],
      ["2021-07-29 00:00:00", 9.8, 9.94, 9.51, 9.7, 2440],
      ["2021-08-30 00:00:00", 9.51, 9.51, 8.39, 8.39, 5490],
      ["2021-09-30 00:00:00", 8.39, 8.39, 8.39, 8.39, 20],
      ["2021-10-25 00:00:00", 8.39, 8.39, 8.39, 8.39, 152],
      ["2021-11-29 00:00:00", 8.55, 8.71, 8.55, 8.71, 100],
      ["2021-12-31 00:00:00", 8.71, 9.09, 8.71, 9.09, 49203]
    ],
    "nextTillDate": "2006-05-29 00:00:00"
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Charting Intraday Ends Here
Charting EOD Starts Here

## EOD Historical Data

Provides an historical data with OHLC (open, high, low and close) values.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.GetEODChart(ChartExchangeEnum exchange, ChartAssetTypeEnum assetType,ChartEODIntervalEnum interval, string symbol, string tillDate = null, bool includeContinousFuture = false)
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
    const eodChart = apiConnect
      .getEODChart(
        interval,
        assetType,
        symbol,
        exchangeType,
        tillDate,
        includeContinuousFuture
      )
      .then(function (result) {})
      .catch((err) => {
        console.log("Error eodChart", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
from constants.asset_type import AssetTypeEnum
from constants.chart_exchange import ChartExchangeEnum
from constants.eod_Interval import EODIntervalEnum
response = api_connect.getEODChart(ChartExchangeEnum.NSE, AssetTypeEnum.EQUITY, "11423_NSE", EODIntervalEnum.D1, TillDate = "2022-01-01", IncludeContinuousFutures = False)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
connect.getEODChart(ChartExchangeEnum exchange, ChartAssetTypeEnum assetType,ChartEODIntervalEnum interval, String streamingSymbol,String tillDate, Boolean includeContinuousFuture)   
```

`POST /charts/v2/main/{interval}/{exc}/{aTyp}/{symbol}`

### Parameters

| Parameter | Description |
| --- | --- |
| Interval | It is the candle interval or length of time that one chooses for a candle data to be displayed. The body of the candle represents the opening and closing price including high and low of candle based on the interval. The available time intervals are MN1,W1,D1 respectively |
| Asset_Type | It is the class of asset FUTCOM,FUTSTK,OPTCUR,OPTIDX,INDEX,OPTSTK,EQUITY,OPTFUT,FUTIDX,FUTCUR |
| Symbol | Each Symbol is unique and represents the stock identity. This is the exchange token to be obtained from the contract file downloaded |
| Exchange_Type | It is the name of the segment like BSE, CDS,NSE,INDEX,NFO,NCDEX,MCX |
| Till_Date | If user passes the value against the till date variable then the data is fetched until the preceding year of the same day . For eg: if you choose till date as 2021-12-31 while sending the request, then the response will have the data until 2020-12-31 If user passes the NULL value against the till date then the data will be fetched till date. |
| Include_Continuous_Future | This attribute is applicable only for the futures - FUTIDX, FUTSTK, FUTCUR, FUTCOM |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| body | body | true | none |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": [
      ["2021-05-27 00:00:00", 11, 11.22, 11, 11, 56087],
      ["2021-06-21 00:00:00", 10.8, 10.8, 9.8, 9.8, 909],
      ["2021-07-29 00:00:00", 9.8, 9.94, 9.51, 9.7, 2440],
      ["2021-08-30 00:00:00", 9.51, 9.51, 8.39, 8.39, 5490],
      ["2021-09-30 00:00:00", 8.39, 8.39, 8.39, 8.39, 20],
      ["2021-10-25 00:00:00", 8.39, 8.39, 8.39, 8.39, 152],
      ["2021-11-29 00:00:00", 8.55, 8.71, 8.55, 8.71, 100],
      ["2021-12-31 00:00:00", 8.71, 9.09, 8.71, 9.09, 49203]
    ],
    "nextTillDate": "2006-05-29 00:00:00"
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Charting EOD Ends Here
News Categories Starts Here
