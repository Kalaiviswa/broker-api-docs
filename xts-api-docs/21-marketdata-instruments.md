# Market Data API: Instruments

## Master (POST)

XTS provides an API call to fetch all tradable instruments as well as additional data in a single structure. This call can be made once per day, and the response can be persisted in local storage or a file based on your application design. You can then fetch instruments or symbols from this dataset throughout the day.  
  
The structure of the response is as follows. The pipe (|) and line-separated values can be easily tokenized and bulk-loaded into your storage of choice.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/master
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegmentList** | Array | Y | Array of exchange segments |

### Request Body JSON

```json
{
  "exchangeSegmentList": [
    "NSECM",
    "NSECD",
    "NSEFO"
  ]
}
```

### Terminalogy

**If InstrumentType is Equities then use below header format:**  
  
ExchangeSegment|ExchangeInstrumentID|InstrumentType|Name|Description|Series|NameWithSeries| InstrumentID|PriceBand.High|PriceBand.Low| FreezeQty|TickSize|LotSize|Multiplier|DisplayName| ISIN|PriceNumerator|PriceDenominator|DetailedDescription|ExtendedSurvIndicator|CautionIndicator|GSMIndicator

**Example:**  
NSECM|2885|8|RELIANCE|RELIANCE-EQ|EQ|RELIANCE-EQ|1100100002885|1598|1307.6|67662|0.1|1|1|RELIANCE|INE002A01018|1|1|RELIANCE INDUSTRIES LTD-EQ|0|-1|-1

**If InstrumentType is Options then use below header format:**  
  
ExchangeSegment|ExchangeInstrumentID|InstrumentType|Name|Description|Series|NameWithSeries|InstrumentID  
|PriceBand.High|PriceBand.Low|FreezeQty|TickSize|LotSize|Multiplier|UnderlyingInstrumentId  
|UnderlyingIndexName|ContractExpiration|StrikePrice|OptionType|DisplayName|PriceNumerator|PriceDenominator|DetailedDescription

**Example:**  
NSEFO|48225|2|NIFTY|NIFTY2621725700PE|OPTIDX|NIFTY-OPTIDX|2604800048225|588|114.5|1801|0.05|65|1|-1|Nifty 50|2026-02-17T14:30:00|25700|4|NIFTY 17FEB2026 PE 25700|1|1|NIFTY2621725700PE

**If InstrumentType is Futures, spread then use below header format:**  
  
ExchangeSegment|ExchangeInstrumentID|InstrumentType|Name|Description|Series|NameWithSeries|InstrumentID |PriceBand.High|PriceBand.Low|FreezeQty|TickSize|LotSize|Multiplier|UnderlyingInstrumentId|UnderlyingIndexName|ContractExpiration| DisplayName|PriceNumerator|PriceDenominator|DetailedDescription

**Example:**  
NSEFO|49229|1|NIFTY|NIFTY26JANFUT|FUTIDX|NIFTY-FUTIDX|2602700049229|28369.8|23211.8|1801|0.1|65|1|-1|Nifty 50  
|2026-01-27T14:30:00|NIFTY 27JAN2026|1|1|NIFTY26JANFUT

## Quote (POST)

You can fetch the quote details by using the POST /instruments/quotes request. In the response, you will receive the quote details based on the exchangeSegment and instrumentID, along with the publishFormat provided in the request. The request body must have the content type application/json and should be valid JSON.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/quotes
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **instruments** | Array | Y | Array of instrument objects |
| **exchangeSegment** | ExchangeSegment | Y | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) |
| **exchangeInstrumentID** | ExchangeInstrumentID | Y | Exchange Scrip code or Symbol Token is unique identifier |
| **xtsMessageCode** | [xtsMessageCode](17-marketdata-enums.md#4-xts-message-code) | Y | It is system generated message code |
| **publishFormat** | PublishFormat | Y | [PublishFormat](17-marketdata-enums.md#10-publishformat) |

### Request Body JSON

```json
{
  "instruments": [
    {
      "exchangeSegment": 1,
      "exchangeInstrumentID": 22
    }
  ],
  "xtsMessageCode": 1502,
  "publishFormat": "JSON"
}
```

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| mdp | [xtsMessageCode](17-marketdata-enums.md#4-xts-message-code) | xtsMessageCode |
| quoteList | Object | Response of subscribe instrument |
| listQuotes | Object | Market data for the list of requested instruments |
| MessageCode | MessageCode (Integer, 5) | It is system generated message code |
| MessageVersion | MessageVersion (String, 10) | It is system generated message version |
| ApplicationType | ApplicationType (String, 20) | It is system generated ApplicationType |
| TokenID | TokenID (String, 500) | It is system generated TokenID |
| ExchangeSegment | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | ExchangeSegment |
| ExchangeInstrumentID | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| ExchangeTimeStamp | ExchangeTimeStamp (Long, 15) | A timestamp represents the time at which an event occurred, as recorded by the exchange. |
| Bids | Object | The bid price displayed in most quote services is the highest bid price in the market. The ask or offer price on the other hand is the lowest price a seller of a particular stock is willing to sell a share of that given stock. |
| Asks | Object | The ask price is the lowest price a seller is willing to accept for a share of a stock. |
| Size | Size (Integer, 10) | Total quantity available at the Ask or Bid price. |
| Price | Price (Double, (15,4)) | Highest price at which buyers are willing to purchase the instrument |
| TotalOrders | TotalOrders (Integer, 10) | Total number of buy orders placed at the bid or ask price. |
| BuyBackMarketMaker | BuyBackMarketMaker (Boolean, 5) | Indicates whether the bid is placed by a buy-back market maker |
| Touchline | Object | Touchline represents the best bid and best ask prices for a security at any given time during the trading day—specifically, the highest price a buyer is willing to pay and the lowest price at which a seller is willing to sell. |
| BidInfo | Object | The bid price displayed in most quote services represents the highest price a buyer is willing to pay in the market. The ask (or offer) price represents the lowest price at which a seller is willing to sell a share of the given stock. |
| AskInfo | Object | The ask price is the lowest price at which a seller is willing to accept for a share of a given stock. |
| LastTradedPrice | LastTradedPrice (Double, (15,4)) | The price at which the most recent trade for the instrument was executed. |
| LastTradedQuantity | LastTradedQuantity (Integer, 10) | The quantity traded in the most recent transaction. |
| TotalBuyQuantity | TotalBuyQuantity (Integer, 10) | The total quantity of buy orders currently available in the market. |
| TotalSellQuantity | TotalSellQuantity (Integer, 10) | The total quantity of sell orders currently available in the market. |
| TotalTradedQuantity | TotalTradedQuantity (Integer, 10) | The cumulative quantity of the instrument traded during the trading session. |
| AverageTradedPrice | AverageTradedPrice (Double, (15,4)) | The volume-weighted average price (VWAP) of all trades executed during the trading session. |
| LastTradedTime | LastTradedTime (Long, 15) | The timestamp at which the most recent trade occurred (exchange time). |
| LastUpdateTime | LastUpdateTime (Long, 15) | The timestamp of the latest market data update received from the exchange. |
| PercentChange | PercentChange (Double, (15,4)) | The percentage change in price compared to the previous close. |
| Open | Open (Double, (15,4)) | The price at which the instrument first traded when the market opened for the session. |
| High | High (Double, (15,4)) | The highest traded price of the instrument during the trading session. |
| Low | Low (Double, (15,4)) | The lowest traded price of the instrument during the trading session. |
| Close | Close (Double, (15,4)) | The most recent traded price or the official closing price of the session. |
| TotalValueTraded | TotalValueTraded (Double, (15,4)) | The total traded value during the session, calculated as price × quantity for all trades. |
| BuyBackTotalBuy | BuyBackTotalBuy (Integer, 10) | The total buy quantity placed under buy-back activity (exchange-specific). |
| BuyBackTotalSell | BuyBackTotalSell (Integer, 10) | The total sell quantity placed under buy-back activity (exchange-specific). |
| BookType | [BookType](17-marketdata-enums.md#8-booktype) | BookType |
| XMarketType | [XMarketType](17-marketdata-enums.md#2-markettype) | XMarketType |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Instrument subscribed successfully!",
    "result": {
      "mdp": 1502,
      "quoteList": {
        "exchangeSegment": 1,
        "exchangeInstrumentID": 2885
      },
      "listQuotes": {
        "MessageCode": 1502,
        "MessageVersion": 1,
        "ApplicationType": 0,
        "TokenID": 0,
        "ExchangeSegment": 1,
        "ExchangeInstrumentID": 2885,
        "ExchangeTimeStamp": 1205682353,
        "Bids": {
          "Size": 0,
          "Price": 0,
          "TotalOrders": 0,
          "BuyBackMarketMaker": 0
        },
        "Asks": {
          "Size": 14916,
          "Price": 900.05,
          "TotalOrders": 10,
          "BuyBackMarketMaker": 0
        },
        "Touchline": {
          "BidInfo": {
            "Size": 0,
            "Price": 0,
            "TotalOrders": 0,
            "BuyBackMarketMaker": 0
          },
          "AskInfo": {
            "Size": 14916,
            "Price": 900.05,
            "TotalOrders": 10,
            "BuyBackMarketMaker": 0
          },
          "LastTradedPrice": 900.05,
          "LastTradedQunatity": 1,
          "TotalBuyQuantity": 0,
          "TotalSellQuantity": 14916,
          "TotalTradedQuantity": 14085685,
          "AverageTradedPrice": 898.81,
          "LastTradedTime": 1205682353,
          "LastUpdateTime": 1205682353,
          "PercentChange": 0,
          "Open": 900,
          "High": 909.1,
          "Low": 890.7,
          "Close": 900.05,
          "TotalValueTraded": 1865862348,
          "BuyBackTotalBuy": 38125,
          "BuyBackTotalSell": 16903
        },
        "BookType": 0,
        "XMarketType": 0
      }
    }
  }
]
```

## GetIndexList (GET)

You can retrieve the list of indices by using the GET /instruments/indexlist request. In the response, you will receive the names of all indices that belong to the specified **exchangeSegment.**

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/indexlist?exchangeSegment=1
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | **Y** | ExchangeSegment |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | ExchangeSegment |
| **indexList** | Array | IndexList |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Record Found",
    "result": {
      "exchangeSegment": 1,
      "indexList": [
        "NIFTY 50_26000",
        "NIFTY BANK_26001",
        "INDIA VIX_26002",
        "NIFTY IT_26003",
        "NIFTY 100_26004",
        "NIFTY MIDCAP 50_26005",
        "NIFTY GS 11 15YR_26006",
        "NIFTY INFRA_26007"
      ]
    }
  }
]
```

## GetSeries (GET)

You can search for the series by using the GET /instruments/instrument/series request. In the response, you will receive the series that you searched for based on the exchangeSegment sent in the request.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/instrument/series?exchangeSegment=1
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Y | ExchangeSegment |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **series** | Array | The series field represents the trading category or segment under which an instrument is listed on the exchange. |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Record Found",
    "result": {
      "series": [
        "BL",
        "BT",
        "MF",
        "NF",
        "EQ",
        "BE",
        "N8",
        "RL",
        "NV"
      ]
    }
  }
]
```

## GetEquitySymbol (GET)

You can search for the equity symbol by using the GET /instruments/instrument/symbol request. In the response, you will receive the equity symbol information based on the exchangeSegment, series, and symbol provided in the request.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/instrument/symbol?exchangeSegment=1&series=EQ&symbol=Acc
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Y | ExchangeSegment |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **ExchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | ExchangeSegment |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **InstrumentType** | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) | InstrumentType |
| **Name** | Name (String, 50) | The official symbol or short name of the instrument as defined by the exchange. |
| **DisplayName** | DisplayName (String, 50) | A user-friendly name of the instrument used for display purposes in applications. |
| **Description** | Description (String, 50) | A detailed description of the instrument, including company or contract details |
| **Series** | Series (String, 50) | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **NameWithSeries** | NameWithSeries (String, 50) | The instrument name appended with its series (e.g., RELIANCE-EQ). |
| **InstrumentID** | InstrumentID (Integer, 10) | A unique system-generated identifier assigned to the instrument by the exchange or trading system. |
| **PriceBand** | Object | The permitted price range within which the instrument can trade during a session. |
| **High** | High (Double, (15,4)) | The upper limit of the price band for the instrument. |
| **Low** | Low (Double, (15,4)) | The lower limit of the price band for the instrument. |
| **CreditRating** | CreditRating (String, 50) | The credit rating assigned to the instrument, if applicable (typically for debt instruments). |
| **FreezeQty** | FreezeQty (Integer, 10) | The maximum order quantity allowed per order for the instrument. |
| **TickSize** | TickSize (Double, (15,4)) | The minimum price movement allowed for the instrument. |
| **LotSize** | LotSize (Integer, 10) | The minimum tradable quantity for the instrument. |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Record Found",
    "result": {
      "ExchangeSegment": 1,
      "ExchangeInstrumentID": 22,
      "InstrumentType": 8,
      "Name": "ACC",
      "DisplayName": "ACC",
      "Description": "ACC LIMITED",
      "Series": "EQ",
      "NameWithSeries": "ACC-EQ",
      "InstrumentID": 1100100000022,
      "PriceBand": {
        "High": 1804.9,
        "Low": 1476.8,
        "CreditRating": "1476.80-1804.90",
        "HighString": "1804.90",
        "LowString": "1476.80"
      },
      "FreezeQty": 66476,
      "TickSize": 0.05,
      "LotSize": 1
    }
  }
]
```

## GetExpiryDate (GET)

You can search for the expiry date by using the GET /instruments/instrument/expiryDate request. In the response, you will receive the expiry date based on the **exchangeSegment, series,** and **symbol** provided in the request.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/instrument/expiryDate?exchangeSegment=2&series=FUTIDX&symbol=NIFTY
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | **Y** | ExchangeSegment |
| **series** | series (String, 50) | **Y** | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **symbol** | symbol (String, 50) | **Y** | Exchange-defined trading code used to identify an instrument. |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-response-0001",
  "description": "Record Found",
  "result": [
    "2025-01-30T14:30:00",
    "2025-02-27T14:30:00",
    "2025-03-27T14:30:00",
    "2025-02-27T14:30:00"
  ]
}
```

## GetFutureSymbol (GET)

You can search for the future symbol by using the GET /instruments/instrument/futureSymbol request. In the response, you will receive the future symbol based on the **exchangeSegment, series, symbol,** and **expiryDate** provided in the request.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/instrument/futureSymbol?exchangeSegment=2&series=FUTIDX&symbol=NIFTY&expiryDate=30Jan2025
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | **Y** | ExchangeSegment |
| **series** | series (String, 50) | **Y** | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **symbol** | symbol (String, 50) | **Y** | Exchange-defined trading code used to identify an instrument. |
| **expiryDate** | String (DateTime, 20) | **Y** | ExpiryDate represents the date on which a derivative contract (futures or options) expires and is settled as per exchange rules. |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **ExchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | ExchangeSegment |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **InstrumentType** | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) | InstrumentType |
| **Name** | Name (String, 50) | The official symbol or short name of the instrument as defined by the exchange. |
| **DisplayName** | DisplayName (String, 50) | A user-friendly name of the instrument used for display purposes in applications. |
| **Description** | Description (String, 50) | A detailed description of the instrument, including company or contract details. |
| **Series** | Series (String, 50) | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **NameWithSeries** | NameWithSeries (String, 50) | The instrument name appended with its series (e.g., RELIANCE-EQ). |
| **InstrumentID** | InstrumentID (Integer, 10) | A unique system-generated identifier assigned to the instrument. |
| **PriceBand** | Object | The permitted price range within which the instrument can trade during a session. |
| **High** | High (Double, (15,4)) | The upper limit of the price band for the instrument. |
| **Low** | Low (Double, (15,4)) | The lower limit of the price band for the instrument. |
| **CreditRating** | CreditRating (String, 50) | The credit rating assigned to the instrument, if applicable (typically for debt instruments). |
| **HighString** | HighString (String, 50) | The upper price band is represented as a formatted string. |
| **LowString** | LowString (String, 50) | The lower price band is represented as a formatted string. |
| **HighExecBandString** | HighExecBandString (String, 50) | The upper execution price band displayed as a formatted string. |
| **LowExecBandString** | LowExecBandString (String, 50) | The lower execution price band displayed as a formatted string. |
| **FreezeQty** | FreezeQty (Integer, 10) | The maximum order quantity allowed per order for the instrument. |
| **TickSize** | TickSize (Double, (15,4)) | The minimum price movement allowed for the instrument. |
| **LotSize** | LotSize (Integer, 10) | The minimum tradable quantity for the instrument. |
| **UnderlyingInstrumentId** | UnderlyingInstrumentId (Integer, 10) | The unique instrument identifier of the underlying asset for a derivative contract. |
| **UnderlyingIndexName** | UnderlyingIndexName (String, 50) | The name of the underlying index on which the derivative contract is based. |
| **ContractExpiration** | ContractExpiration (String, 50) | The date on which a derivatives contract expires. After this date, the contract ceases to exist for trading. |
| **ContractExpirationString** | ContractExpirationString (String, 50) | The contract expiration date is represented as a formatted string, as defined by the exchange. |
| **RemainingExpiryDays** | RemainingExpiryDays (Integer, 10) | The number of calendar days remaining until the contract expires. |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Record Found",
    "result": {
      "ExchangeSegment": 2,
      "ExchangeInstrumentID": 35006,
      "InstrumentType": 1,
      "Name": "NIFTY",
      "DisplayName": "NIFTY 30JAN2025",
      "Description": "NIFTY25JANFUT",
      "Series": "FUTIDX",
      "InstrumentID": 2503000035006,
      "PriceBand": {
        "High": 25131.1,
        "Low": 20561.85,
        "CreditRating": "20561.85-25131.10",
        "HighString": "23354.10",
        "LowString": "22438.85",
        "HighExecBandString": "23354.20",
        "LowExecBandString": "22438.35",
        "TERRange": "22438.35-23354.20"
      },
      "FreezeQty": 1801,
      "TickSize": 0.05,
      "LotSize": 25,
      "UnderlyingInstrumentId": -1,
      "UnderlyingIndexName": "Nifty 50",
      "ContractExpiration": "2025-01-30T14:30:00",
      "ContractExpirationString": "30Jan2025",
      "RemainingExpiryDays": 3
    }
  }
]
```

## GetOptionType (GET)

You can search for the option type by using the GET /instruments/instrument/optionType request. In the response, you will receive the option type based on the **exchangeSegment, series, symbol,** and **expiryDate** provided in the request.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/instrument/optionType?exchangeSegment=2&series=OPTIDX&symbol=NIFTY&expiryDate=30Jan2025
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | **Y** | ExchangeSegment |
| **series** | series (String, 50) | **Y** | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **symbol** | symbol (String, 50) | **Y** | Exchange-defined trading code used to identify an instrument. |
| **expiryDate** | String (DateTime, 20) | **Y** | ExpiryDate represents the date on which a derivative contract (futures or options) expires and is settled as per exchange rules. |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **series** | Array | Series |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Record Found",
    "result": {
      "series": [
        "PE",
        "CE"
      ]
    }
  }
]
```

## GetStrikePrice (GET)

You can search for the strike prices by using the GET /instruments/instrument/strikePrice request. In the response, you will receive all strike prices for the specified **symbol** and **expiryDate.**

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/instrument/strikePrice?exchangeSegment=2&series=OPTIDX&symbol=NIFTY&expiryDate=30Jan2025&optionType=CE
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | **Y** | ExchangeSegment |
| **series** | Series (String, 50) | **Y** | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **symbol** | Symbol (String, 50) | **Y** | Exchange-defined trading code used to identify an instrument. |
| **expiryDate** | ExpiryDate (String, 20) | **Y** | ExpiryDate represents the date on which a derivative contract (futures or options) expires and is settled as per exchange rules. |
| **optionType** | [OptionType](17-marketdata-enums.md#9-optiontype) | **Y** | OptionType |

### Response Body Parameters

```json
[
  {
    "result": [
      "29350",
      "28300",
      "21350",
      "21400",
      "27550",
      "18400",
      "24200",
      "26350",
      "19200"
    ]
  }
]
```

## GetOptionSymbol (GET)

You can search for the option symbol by using the GET /instruments/instrument/optionSymbol request. In the response, you will receive the option symbol based on the **exchangeSegment, series, symbol, expiryDate, optionType,** and **strikePrice** provided in the request.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/instrument/optionSymbol?exchangeSegment=2&series=OPTIDX&symbol=NIFTY&expiryDate=06Feb2025&optionType=CE&strikePrice=22500
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | **Y** | ExchangeSegment |
| **series** | Series (String, 50) | **Y** | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **symbol** | Symbol (String, 50) | **Y** | Exchange-defined trading code used to identify an instrument. |
| **expiryDate** | ExpiryDate (String, 20) | **Y** | ExpiryDate represents the date on which a derivative contract (futures or options) expires and is settled as per exchange rules. |
| **optionType** | [OptionType](17-marketdata-enums.md#9-optiontype) | **Y** | OptionType |
| **strikePrice** | StrikePrice (Double, (15,4)) | **Y** | The strike price is the predetermined price at which the buyer of an options contract can buy (call option) or sell (put option) the underlying asset, on or before the option’s expiration date. |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **ExchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | ExchangeSegment |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **InstrumentType** | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) | InstrumentType |
| **Name** | Name (String, 50) | The official symbol or short name of the instrument as defined by the exchange. |
| **DisplayName** | DisplayName (String, 50) | A user-friendly name of the instrument used for display purposes in applications. |
| **Description** | Description (String, 50) | A detailed description of the instrument, including company or contract details. |
| **Series** | Series (String, 50) | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **NameWithSeries** | NameWithSeries (String, 50) | The instrument name appended with its series (e.g., RELIANCE-EQ). |
| **InstrumentID** | InstrumentID (Integer, 10) | A unique system-generated identifier assigned to the instrument. |
| **PriceBand** | Object | The permitted price range within which the instrument can trade during a session. |
| **High** | High (Double, (15,4)) | The upper limit of the price band for the instrument. |
| **Low** | Low (Double, (15,4)) | The lower limit of the price band for the instrument. |
| **CreditRating** | CreditRating (String, 50) | The credit rating assigned to the instrument, if applicable. |
| **HighString** | HighString (String, 50) | The upper price band is represented as a formatted string. |
| **LowString** | LowString (String, 50) | The lower price band is represented as a formatted string. |
| **HighExecBandString** | HighExecBandString (String, 50) | The upper execution price band displayed as a formatted string. |
| **LowExecBandString** | LowExecBandString (String, 50) | The lower execution price band displayed as a formatted string. |
| **FreezeQty** | FreezeQty (Integer, 10) | The maximum order quantity allowed per order for the instrument. |
| **TickSize** | TickSize (Double, (15,4)) | The minimum price movement allowed for the instrument. |
| **LotSize** | LotSize (Integer, 10) | The minimum tradable quantity for the instrument. |
| **UnderlyingInstrumentId** | UnderlyingInstrumentId (Integer, 10) | The unique instrument identifier of the underlying asset for a derivative contract. |
| **UnderlyingIndexName** | UnderlyingIndexName (String, 50) | The name of the underlying index on which the derivative contract is based. |
| **ContractExpiration** | ContractExpiration (String, 50) | The date on which a derivatives contract expires. |
| **ContractExpirationString** | ContractExpirationString (String, 50) | The contract expiration date is represented as a formatted string. |
| **RemainingExpiryDays** | RemainingExpiryDays (Integer, 10) | The number of calendar days remaining until the contract expires. |
| **ExchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | ExchangeSegment |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Exchange Scrip code or Symbol Token is unique identifier |
| **StrikePrice** | StrikePrice (Double, (15,4)) | The strike price is the predetermined price at which the buyer of an options contract can buy or sell the underlying asset. |
| **OptionType** | [OptionType](17-marketdata-enums.md#9-optiontype) | OptionType |
