# Market Data API: Search

## Instruments By ID (POST)

You can search for instruments by using the POST /search/instrumentsbyid request. In the response, you will receive the instrument details based on the **instrumentID** provided in the request.  
  
The request body must have the content type **application/json** and must contain valid JSON.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/search/instrumentsbyid
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **instruments** | Array | **Y** | Array of instrument objects |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | **Y** | ExchangeSegment |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | **Y** | Exchange Scrip code or Symbol Token is unique identifier |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **AGM** | AGM (Boolean, 5) | Indicates if an Annual General Meeting is scheduled for the company |
| **AllOrNone** | AllOrNone (Boolean, 5) | Indicates if the order must be executed fully or not at all. |
| **Bonus** | Bonus (Boolean, 5) | Bonus shares declared per existing share. |
| **Dividend** | Dividend (Boolean, 5) | Dividend amount declared per share. |
| **EGM** | EGM (Boolean, 5) | Indicates if an Extraordinary General Meeting is scheduled. |
| **AuctionDetailInfo** | Object | Additional details about an auction event. |
| **AuctionNumber** | AuctionNumber (Integer, 10) | Unique identifier for a specific auction. |
| **AuctionStatus** | AuctionStatus (Integer, 10) | Current status of an auction. |
| **InitiatorType** | InitiatorType (Integer, 10) | Type of entity initiating the auction or corporate action. |
| **SettlementPeriod** | SettlementPeriod (Integer, 10) | Number of days for settlement of trades. |
| **TotalBuyQty** | TotalBuyQty (Integer, 10) | Total buy quantity in the auction or order book. |
| **TotalSellQty** | TotalSellQty (Integer, 10) | Total sell quantity in the auction or order book. |
| **AuctionQty** | AuctionQty (Integer, 10) | Quantity allocated in the auction. |
| **AuctionPrice** | AuctionPrice (Double, (15,4)) | Price at which auction quantity is settled. |
| **BestBuyPrice** | BestBuyPrice (Double, (15,4)) | Highest buy price currently in the stock |
| **BestSellPrice** | BestSellPrice (Double, (15,4)) | Lowest sell price currently in the stock |
| **ELMargin** | ELMargin (Double, (15,4)) | Extreme Loss Margin required for the instrument. |
| **Interest** | Interest (Boolean, 5) | Interest rate applicable to a debt instrument or derivative |
| **ISIN** | ISIN (String, 15) | International Securities Identification Number, unique per security. |
| **MinimumFill** | MinimumFill (Boolean, 5) | Minimum quantity that can be executed in a single order. |
| **Rights** | Rights (Boolean, 5) | Number of rights shares issued per existing share. |
| **IssuedCapital** | IssuedCapital (Integer, 10) | Total capital issued by the company. |
| **BoardLotQuantity** | BoardLotQuantity (Integer, 10) | Minimum number of units that can be traded in one lot. |
| **FaceValue** | FaceValue (Integer, 10) | Face value of the security per unit/share. |
| **Spread** | Spread (Integer, 10) | Difference between best buy and sell price. |
| **CallAuction1Flag** | CallAuction1Flag (Boolean, 5) | Indicates if a first call auction is applicable. |
| **GSMIndicator** | GSMIndicator (Integer, 10) | Indicator for market segments or trading type. |
| **InstrumentID** | InstrumentID (Integer, 10) | Unique identifier for the instrument in the system. |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Identifier of the instrument as per the exchange. |
| **DisplayName** | DisplayName (String, 50) | Name of the instrument as displayed in UI. |
| **Name** | Name (String, 50) | The official symbol or short name of the instrument as defined by the exchange. |
| **AuctionNumber** | AuctionNumber (Integer, 10) | Unique identifier for a specific auction. |
| **MinimumQty** | MinimumQty (Integer, 10) | Minimum tradable quantity for the instrument. |
| **QuantityMultiplier** | QuantityMultiplier (Integer, 10) | Multiplier applied to quantity for derivatives/contracts. |
| **PriceNumerator** | PriceNumerator (Integer, 10) | Numerator for representing price fractions. |
| **PriceDenominator** | PriceDenominator (Integer, 10) | Denominator for representing price fractions. |
| **LotSize** | LotSize (Integer, 10) | Number of units per lot. |
| **InstrumentType** | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) | Type of instrument (Equity, Option, Future, etc.). |
| **SymbolType** | SymbolType (Integer, 20) | Symbol classification type (e.g., Common, Preferred). |
| **CfiCode** | CfiCode (String, 50) | Classification of Financial Instruments code. |
| **Status** | Status (String, 50) | Current status of the instrument (Active, Inactive). |
| **TicksPerPoint** | TicksPerPoint (Integer, 10) | Number of ticks per point for price movement. |
| **TickSize** | TickSize (Double, (15,4)) | Minimum price movement allowed for the instrument. |
| **Description** | Description (String, 50) | Additional description of the instrument. |
| **IsImpliedMarket** | IsImpliedMarket (Boolean, 5) | Indicates if the market is derived from implied instruments. |
| **IsTradeable** | IsTradeable (Boolean, 5) | Indicates if the instrument is currently tradeable. |
| **ExchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | ExchangeSegment |
| **Series** | Series (String, 50) | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **MaxTradeVolume** | MaxTradeVolume (Long, 15) | Maximum allowed trade volume per order. |
| **PriceBand** | Object | Object containing high and low price limits for the instrument. |
| **High** | High (Double, (15,4)) | Highest price of the instrument in the trading session. |
| **Low** | Low (Double, (15,4)) | Lowest price of the instrument in the trading session. |
| **DecimalDisplace** | DecimalDisplace (Integer, 10) | Number of decimal places used for pricing. |
| **ExtendedMarketProperties** | Object | Additional properties related to extended trading sessions. |
| **CallAuctionIndicator** | Object | Indicates if the instrument is in a call auction. |
| **ExpulsionDate** | Object | Date when the instrument is expelled from the exchange. |
| **IssueMaturityDate** | Object | Maturity date for debt instruments. |
| **ReAdmissionDate** | Object | Date when the instrument is readmitted to trading. |
| **CorporateAction** | Object | Type of corporate action applicable (Bonus, Dividend, Split). |
| **NoDeliveryEndDate** | Object | End date of no-delivery period for corporate action. |
| **IssueRate** | Object | Rate of issue for debt instruments or IPOs. |
| **SettlementNo** | Object | Settlement number associated with the trade or contract. |
| **InterestPaymentDate** | Object | Date on which interest is paid for debt instruments. |
| **ListingDate** | Object | Date when the instrument was listed on the exchange. |
| **CompanyName** | Object | Name of the issuing company. |
| **UniqueKey** | Object | Unique identifier for the instrument across systems. |
| **CreditRating** | Object | Credit rating of the instrument or issuer. |
| **RecordDate** | Object | Date on which shareholders are recorded for corporate actions. |
| **NoDeliveryStartDate** | Object | Start date of no-delivery period for corporate actions. |
| **MarketType** | Object | Type of market segment (Normal, Auction, OddLot, etc.). |
| **BookClosureStartDate** | Object | Start date of book closure period for corporate actions. |
| **ExDate** | Object | Ex-dividend or ex-rights date. |
| **WarningPercent** | Object | Warning percentage for price movement alerts. |
| **IssueStartDate** | Object | Start date for issuance of new shares or debt. |
| **BookClosureEndDate** | Object | End date of book closure period. |
| **Remarks** | Object | Additional remarks or notes related to the instrument. |
| **MarketTypeStatusEligibility** | Object | Eligibility status for a particular market type. |
| **Normal** | Object | Indicates if the instrument is eligible for normal trading. |
| **OddLot** | Object | Indicates if odd-lot trading is allowed. |
| **RetailDebt** | Object | Indicates if the instrument is a retail debt security. |
| **Auction** | Object | Indicates if the instrument is part of an auction. |
| **CallAuction1** | Object | Flag for first call auction participation. |
| **CallAuction2** | Object | Flag for second call auction participation. |
| **MarketType** | [MarketType](17-marketdata-enums.md#2-markettype) | Current market type of the instrument. |
| **Eligible** | Eligible (Boolean, 5) | Indicates if the instrument is eligible for trading. |
| **TradingStatus** | TradingStatus (String, 50) | Current trading status (Active, Suspended, Halted). |
| **NameWithSeries** | NameWithSeries (String, 50) | Name combined with series for display purposes. |
| **DisplayNameWithExchange** | DisplayNameWithExchange (String, 50) | Display name including exchange info. |
| **FreezeQty** | FreezeQty (Integer, 10) | Quantity frozen/unavailable for trading. |
| **LastUpdateTime** | LastUpdateTime (Long, 15) | Last update time of the instrument data. |
| **FiftyTwoWeekHigh** | FiftyTwoWeekHigh (Double, (15,4)) | Highest price of the instrument in the past 52 weeks. |
| **FiftyTwoWeekLow** | FiftyTwoWeekLow (Double, (15,4)) | Lowest price of the instrument in the past 52 weeks. |
| **Bhavcopy** | Object | Snapshot or file reference of daily trading data. |
| **Open** | Open (Double, (15,4)) | Opening price of the instrument for the trading session. |
| **High** | High (Double, (15,4)) | Highest price during the trading session. |
| **Low** | Low (Double, (15,4)) | Lowest price during the trading session. |
| **Close** | Close (Double, (15,4)) | Closing price of the instrument for the session. |
| **TotTrdQty** | TotTrdQty (Long, 15) | Total traded quantity in the session. |
| **TotTrdVal** | TotTrdVal (Double, (15,4)) | Total traded value in the session. |
| **TimeStamp** | TimeStamp (String, 50) | Timestamp of the data snapshot. |
| **TotalTrades** | TotalTrades (Long, 15) | Total number of trades executed in the session. |
| **OpenInterest** | OpenInterest (Double, (15,4)) | Open interest for derivatives contracts. |
| **SettlementPrice** | SettlementPrice (Double, (15,4)) | Price used for settlement of derivatives contracts. |
| **AdditionalPreExpiryMarginPerc** | AdditionalPreExpiryMarginPerc (Double, (15,4)) | Additional margin percentage applicable before expiry. |
| **AdditionalMarginPercLong** | AdditionalMarginPercLong (Double, (15,4)) | Additional margin percentage for long positions. |
| **AdditionalMarginPercShort** | AdditionalMarginPercShort (Double, (15,4)) | Additional margin percentage for short positions. |
| **DeliveryMarginPerc** | DeliveryMarginPerc (Double, (15,4)) | Margin percentage required for delivery-based trades. |
| **SpecialMarginPercBuy** | SpecialMarginPercBuy (Double, (15,4)) | Special margin percentage for buying positions. |
| **SpecialMarginPercSell** | SpecialMarginPercSell (Double, (15,4)) | Special margin percentage for selling positions. |
| **TenderMargin** | TenderMargin (Double, (15,4)) | Margin required for participating in tender offers. |
| **ELMLongMargin** | ELMLongMargin (Double, (15,4)) | Extreme loss margin for long positions. |
| **ELMShortMargin** | ELMShortMargin (Double, (15,4)) | Extreme loss margin for short positions. |
| **InitialMarginPerc** | InitialMarginPerc (Double, (15,4)) | Initial margin percentage for derivatives contracts. |
| **ExposureMarginPerc** | ExposureMarginPerc (Double, (15,4)) | Margin based on exposure limit. |
| **CallAuctionIndicator** | Object | Indicates if the instrument is part of a call auction. |
| **MarketType** | [MarketType](17-marketdata-enums.md#2-markettype) | Current market type for trading. |
| **CurrentEligibleMarketType** | CurrentEligibleMarketType (Integer, 10) | Market types the instrument is eligible for currently. |
| **InstrumentLazyLoader** | InstrumentLazyLoader (Integer, 10) | Indicates if instrument data is loaded lazily for performance. |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Instruments Found",
    "result": {
      "AGM": false,
      "AllOrNone": true,
      "Bonus": true,
      "Dividend": true,
      "EGM": true,
      "AuctionDetailInfo": {
        "AuctionNumber": 0,
        "AuctionStatus": 0,
        "InitiatorType": 0,
        "SettlementPeriod": 0,
        "TotalBuyQty": 0,
        "TotalSellQty": 0,
        "AuctionQty": 0,
        "AuctionPrice": 0,
        "BestBuyPrice": 0,
        "BestSellPrice": 0
      },
      "ELMargin": 5,
      "Interest": true,
      "ISIN": "INE012A01025",
      "MinimumFill": true

      "Rights": true,
"VaRMargin": 10.28,
"IssuedCapital": 8924587534,
"BoardLotQuantity": 0,
"FaceValue": 100,
"Spread": 0,
"CallAuction1Flag": false,
"GSMIndicator": 0,
"InstrumentID": 1100100003045,
"ExchangeInstrumentID": 22,
"DisplayName": "ACC",
"Name": "ACC",
"AuctionNumber": 0,
"MinimumQty": 0,
"QuantityMutliplier": 1,
"PriceNumerator": 1,
"PriceDenominator": 1,
"LotSize": 1,
"InstrumentType": 8,
"SymbolType": 0,
"CfiCode": "ESXXXX",
"Status": "ESXXXX",
"TicksPerPoint": 20,
"TickSize": 0.05,
"Description": "ACC LIMITED-EQ",
"IsImpliedMarket": false,
"IsTradeable": false,
"ExchangeSegment": 1,
"Series": "EQ",
"MaxTradeVolume": 2147483647,
"PriceBand": {
  "High": 330.45,
  "Low": 270.45
},
"DecimalDisplace": 2,
"ExtendedMarketProperties": {
  "CallAuctionIndicator": {
    "Name": "CallAuctionIndicator",
    "Value": ""
  },
  "ExpulsionDate": {
    "Name": "ExpulsionDate",
    "Value": "01Jan1980"
  },
  "IssueMaturityDate": {
    "Name": "IssueMaturityDate",
    "Value": "01Jan1980"
  },
"ReAdmissionDate": {
  "Name": "ReAdmissionDate",
  "Value": "01Jan1980"
},
"CorporateAction": {
  "Name": "CorporateAction",
  "Value": "01Jan1980"
},
"NoDeliveryEndDate": {
  "Name": "NoDeliveryEndDate",
  "Value": "01Jan1980"
},
"IssueRate": {
  "Name": "IssueRate",
  "Value": ""
},
"SettlementNo": {
  "Name": "CallAuctionIndicator",
  "Value": "Missing"
},
"InterestPaymentDate": {
  "Name": "InterestPaymentDate",
  "Value": "01Jan1980"
},
"ListingDate": {
  "Name": "ListingDate",
  "Value": "01Jan1980"
},
"CompanyName": {
  "Name": "CompanyName",
  "Value": "ACC LIMITED-EQ"
},
"UniqueKey": {
  "Name": "UniqueKey",
  "Value": "ACC"
},
"CreditRating": {
  "Name": "CreditRating",
  "Value": "270.45-330.45"
},
"RecordDate": {
  "Name": "RecordDate",
  "Value": "01Jan1980"
},
"NoDeliveryStartDate": {
  "Name": "NoDeliveryStartDate",
  "Value": "01Jan1980"
},
"MarketType": {
  "Name": "MarketType",
  "Value": "NORMAL"
},
"BookClosureStartDate": {
  "Name": "BookClosureStartDate",
  "Value": "19Feb2019"
},
"ExDate": {
  "Name": "ExDate",
  "Value": "19Feb2020"
},
"WarningPercent": {
  "Name": "WarningPercent",
  "Value": "0"
},
"IssueStartDate": {
  "Name": "IssueStartDate",
  "Value": "24Oct1994"
},
"BookClosureEndDate": {
  "Name": "BookClosureEndDate",
  "Value": "28Feb2019"
},
"Remarks": {
  "Name": "Remarks",
  "Value": "AGM/CHANGE IN RTA"
}
},
"MarketTypeStatusEligibility": {
  "Normal": {
    "MarketType": 1,
    "Eligibile": true,
    "TradingStatus": 6
  },
  "OddLot": {
    "MarketType": 2,
    "Eligibile": false,
    "TradingStatus": 2
  },
  "RetailDebt": {
    "MarketType": 3,
    "Eligibile": false,
    "TradingStatus": 2
  },
  "Auction": {
    "MarketType": 4,
    "Eligibile": true,
"TradingStatus": 2
        },
"CallAuction1": {
  "MarketType": 5,
  "Eligibile": false,
  "TradingStatus": 1
},
"CallAuction2": {
  "MarketType": 6,
  "Eligibile": true,
  "TradingStatus": 1
}
},
"NameWithSeries": "ACC-EQ",
"DisplayNameWithExchange": "ACC - NSECM",
"FreezeQty": 374832,
"LastUpdateTime": 1220519308,
"FiftyTwoWeekHigh": 351.3,
"FiftyTwoWeekLow": 232.35,
"Bhavcopy": {
  "Open": 266,
  "High": 267.9,
  "Low": 261.5,
  "Close": 263.75,
  "TotTrdQty": 42967696,
  "TotTrdVal": 11389044523.95,
  "TimeStamp": "0001-01-01T00:00:00",
  "TotalTrades": 197824,
  "OpenInterest": 0,
  "SettlementPrice": 0
},
"AdditionalPreExpiryMarginPerc": 0,
"AdditionalMarginPercLong": 0,
"AdditionalMarginPercShort": 0,
"DeliveryMarginPerc": 0,
"SpecialMarginPercBuy": 0,
"SpecialMarginPercSell": 0,
"TenderMargin": 0,
"ELMLongMargin": 0,
"ELMShortMargin": 0,
"InitialMarginPerc": 0,
"ExposureMarginPerc": 0,
"CallAuctionIndicator": 1,
"MarketType": 1,
"CurrentEligibleMarketType": 1,
"InstrumentLazyLoader": null
    }
  }
]
```

## Instruments By Search String (GET)

You can search for instruments by using the GET /search/instruments request. In the response, you will receive the instrument details based on the **searchString** provided in the request.

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/search/instruments?searchString=RELIANCE
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchString | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Y |  |

### Response Body Parameters

| Parameter Name | Type | Description |
| --- | --- | --- |
| **ExchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Exchange segment in which the instrument is listed. |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Exchange script code or Symbol Token is unique identifier. |
| **InstrumentType** | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) | Type of financial instrument. |
| **Name** | Name (String, 50) | The official symbol or short name of the instrument as defined by the exchange. |
| **DisplayName** | DisplayName (String, 50) | A user-friendly name of the instrument used for display purposes in applications. |
| **Description** | Description (String, 200) | A detailed description of the instrument, including company or contract details. |
| **Series** | Series (String, 10) | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| **NameWithSeries** | NameWithSeries (String, 60) | The instrument name appended with its series (e.g., `RELIANCE-EQ`). |
| **InstrumentID** | InstrumentID (Integer, 10) | A unique system-generated identifier assigned to the instrument by the exchange or trading system. |
| **PriceBand** | PriceBand (Object, -) | The permitted price range within which the instrument can trade during a session. |
| **High** | High (Decimal, 10,2) | The upper limit of the price band for the instrument. |
| **Low** | Low (Decimal, 10,2) | The lower limit of the price band for the instrument. |
| **CreditRating** | CreditRating (String, 10) | The credit rating assigned to the instrument, if applicable (typically for debt instruments). |
| **HighString** | HighString (String, 20) | The upper price band is represented as a formatted string. |
| **LowString** | LowString (String, 20) | The lower price band is represented as a formatted string. |
| **HighExecBandString** | HighExecBandString (String, 20) | The upper execution price band displayed as a formatted string. |
| **LowExecBandString** | LowExecBandString (String, 20) | The lower execution price band displayed as a formatted string. |
| **FreezeQty** | FreezeQty (Integer, 10) | The maximum order quantity allowed per order for the instrument. |
| **TickSize** | TickSize (Decimal, 10,2) | The minimum price movement allowed for the instrument. |
| **LotSize** | LotSize (Integer, 10) | The minimum tradable quantity for the instrument. |
| **UnderlyingInstrumentId** | UnderlyingInstrumentId (Integer, 10) | The unique instrument identifier of the underlying asset for a derivative contract. |
| **UnderlyingIndexName** | UnderlyingIndexName (String, 50) | The name of the underlying index on which the derivative contract is based. |
| **ContractExpirationString** | ContractExpirationString (String, 20) | The contract expiration date represented as a formatted string. |
| **RemainingExpiryDays** | RemainingExpiryDays (Integer, 5) | The number of calendar days remaining until the contract expires. |
| **ExchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Exchange segment in which the instrument is listed. |
| **ExchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Exchange script code or Symbol Token is unique identifier. |
| **StrikePrice** | StrikePrice (Decimal, 10,2) | The strike price at which the option buyer can buy or sell the underlying asset. |
| **OptionType** | [OptionType](17-marketdata-enums.md#9-optiontype) | Defines whether the option is a Call or Put. |

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-search-0001",
  "description": "Record Found",
  "result": [
    {
      "ExchangeSegment": 1,
      "ExchangeInstrumentID": "11536",
      "InstrumentType": 8,
      "Name": "TCS",
      "DisplayName": "TCS",
      "ISIN": "INE467B01029",
      "Description": "TCS-EQ",
      "Series": "EQ",
      "NameWithSeries": "TCS-EQ",
      "InstrumentID": 1100100011536,
      "PriceBand": {
        "High": 3412.5,
        "Low": 2792.1,
        "HighString": "3412.50",
        "LowString": "2792.10",
        "CreditRating": "2792.10-3412.50",
        "HighExecBandString": "0.00",
        "LowExecBandString": "0.00",
        "HighExecBand": 0,
        "LowExecBand": 0,
        "TERRange": "0.00-0.00"
      },
      "FreezeQty": 28944,
      "TickSize": 0.1,
      "LotSize": 1,
      "CompanyName": "TATA CONSULTANCY SERV LT-EQ",
      "DecimalDisplace": 2,
      "IsIndex": false,
      "IsTradeable": true,
      "Industry": 11
    },
    {
      "ExchangeSegment": 1,
      "ExchangeInstrumentID": "759146",
      "InstrumentType": 8,
      "Name": "755TCSL28",
      "DisplayName": "755TCSL28",
      "ISIN": "INE729N07107",
      "Description": "755TCSL28-N0",
      "Series": "N0",
      "NameWithSeries": "755TCSL28-N0",
      "InstrumentID": 1100100759146,
      "PriceBand": {
        "High": 120000,
        "Low": 80000,
        "HighString": "120000.00",
        "LowString": "80000.00",
        "CreditRating": "80000.00-120000.00",
        "HighExecBandString": "0.00",
        "LowExecBandString": "0.00",
        "HighExecBand": 0,
        "LowExecBand": 0,
        "TERRange": "0.00-0.00"
      },
      "FreezeQty": 999,
      "TickSize": 0.01,
      "LotSize": 1,
      "CompanyName": "TCSL 7.55% 2028-N0",
      "DecimalDisplace": 2,
      "IsIndex": false,
      "IsTradeable": true,
      "Industry": 0
    }
  ]
}
```
