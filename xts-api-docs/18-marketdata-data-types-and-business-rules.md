# Market Data API: Data Types & Business Rules

All data types now use business-oriented names, specify allowed sizes, and clearly state any validation rules.

| Field Name | Data Type | Size | Description |
| --- | --- | --- | --- |
| SecretKey | String | **20** | The predefined secret key assigned to the client. |
| AppKey | String | **20** | The application key used for authentication. |
| Token | String | **500** | The authentication token used with every subsequent request. |
| UserID | String | **15** | UserID of investor client. |
| AppVersion | String | **50** | Marketdata app version. |
| Application_Expiry_Date | String | **50** | User application expiry date. |
| ExchangeSegments | Integer | **2** | [Exchange Segment](17-marketdata-enums.md#1-exchangesegments) |
| xtsMessageCode | Integer | **5** | [XTS Message Code](17-marketdata-enums.md#4-xts-message-code) |
| ExchangeInstrumentID | Integer | **10** | Exchange Scrip code or Symbol Token is unique identifier. |
| PublishFormat | String | **10** | [PublishFormat](17-marketdata-enums.md#10-publishformat) |
| BroadCastMode | String | **10** | [BroadCastMode](17-marketdata-enums.md#11-broadcastmode) |
| InstrumentType | Integer | **2** | [InstrumentType](17-marketdata-enums.md#3-instrumenttype) |
| LastTradedPrice | Double | **(15,4)** | The price at which the most recent trade for the instrument was executed. |
| LastTradedQuantity | Integer | **10** | The quantity traded in the most recent transaction. |
| TotalBuyQuantity | Integer | **10** | The total quantity of buy orders currently available in the market. |
| TotalSellQuantity | Integer | **10** | The total quantity of sell orders currently available in the market. |
| TotalTradedQuantity | Integer | **10** | The cumulative quantity of the instrument traded during the trading session. |
| AverageTradedPrice | Double | **(15,4)** | The volume-weighted average price (VWAP) of all trades executed during the trading session. |
| LastTradedTime | Long | **15** | The timestamp at which the most recent trade occurred (exchange time). |
| LastUpdateTime | Long | **15** | The timestamp of the latest market data update received from the exchange. |
| PercentChange | Double | **(15,4)** | The percentage change in price compared to the previous close. |
| Open | Double | **(15,4)** | The price at which the instrument first traded when the market opened for the session. |
| High | Double | **(15,4)** | The highest traded price of the instrument during the trading session. |
| Low | Double | **(15,4)** | The lowest traded price of the instrument during the trading session. |
| Close | Double | **(15,4)** | The most recent traded price or the official closing price of the session. |
| TotalValueTraded | Double | **(15,4)** | The total traded value during the session, calculated as price × quantity for all trades. |
| BuyBackTotalBuy | Integer | **10** | The total buy quantity placed under buy-back activity (exchange-specific). |
| BuyBackTotalSell | Integer | **10** | The total sell quantity placed under buy-back activity (exchange-specific). |
| BookType | Integer | **10** | BookType |
| XMarketType | Integer | **10** | XMarketType |
| Name | String | **50** | The official symbol or short name of the instrument as defined by the exchange. |
| DisplayName | String | **50** | A user-friendly name of the instrument used for display purposes in applications. |
| Symbol | String | **50** | Exchange-defined trading code used to identify an instrument. |
| Description | String | **50** | A detailed description of the instrument, including company or contract details. |
| ExpiryDate | String | **20** | ExpiryDate represents the date on which a derivative contract (futures or options) expires and is settled as per exchange rules. |
| Series | String | **50** | The exchange-defined series under which the instrument is listed (e.g., EQ, BL, A). |
| NameWithSeries | String | **50** | The instrument name appended with its series (e.g., RELIANCE-EQ). |
| InstrumentID | Integer | **10** | A unique system-generated identifier assigned to the instrument by the exchange or trading system. |
| CreditRating | String | **50** | The credit rating assigned to the instrument, if applicable (typically for debt instruments). |
| HighString | String | **50** | The upper price band is represented as a formatted string. |
| LowString | String | **50** | The lower price band is represented as a formatted string. |
| HighExecBandString | String | **50** | The upper execution price band displayed as a formatted string. |
| LowExecBandString | String | **50** | The lower execution price band displayed as a formatted string. |
| TERRange | String | **50** | Denotes the trading exposure range or price/quantity limit range applicable for the instrument. |
| FreezeQty | Integer | **10** | The maximum order quantity allowed per order for the instrument. |
| TickSize | Double | **(15,4)** | The minimum price movement allowed for the instrument. |
| LotSize | Integer | **10** | The minimum tradable quantity for the instrument. |
| UnderlyingInstrumentId | Integer | **10** | The unique instrument identifier of the underlying asset for a derivative contract. |
| UnderlyingIndexName | String | **50** | The name of the underlying index on which the derivative contract is based. |
| ContractExpiration | String | **50** | The date on which a derivatives contract expires. After this date, the contract ceases to exist for trading. |
| ContractExpirationString | String | **50** | The contract expiration date represented as a formatted string, as defined by the exchange. |
| RemainingExpiryDays | Integer | **10** | The number of calendar days remaining until the contract expires. |
| OptionType | Integer | **10** | [OptionType](17-marketdata-enums.md#9-optiontype) |
| StrikePrice | Double | **(15,4)** | The strike price is the predetermined price at which the buyer of an options contract can buy or sell the underlying asset. |
| AGM | Boolean | **5** | Indicates if an Annual General Meeting is scheduled for the company. |
| AllOrNone | Boolean | **5** | Indicates if the order must be executed fully or not at all. |
| Bonus | Boolean | **5** | Bonus shares declared per existing share. |
| Dividend | Boolean | **5** | Dividend amount declared per share. |
| EGM | Boolean | **5** | Indicates if an Extraordinary General Meeting is scheduled. |
| AuctionNumber | Integer | **10** | Unique identifier for a specific auction. |
| AuctionStatus | Integer | **10** | Current status of an auction. |
| InitiatorType | Integer | **10** | Type of entity initiating the auction or corporate action. |
| SettlementPeriod | Integer | **10** | Number of days for settlement of trades. |
| TotalBuyQty | Integer | **10** | Total buy quantity in the auction or order book. |
| TotalSellQty | Integer | **10** | Total sell quantity in the auction or order book. |
| AuctionQty | Integer | **10** | Quantity allocated in the auction. |
| AuctionPrice | Double | **(15,4)** | Price at which auction quantity is settled. |
| BestBuyPrice | Double | **(15,4)** | Highest buy price currently available in the stock. |
| BestSellPrice | Double | **(15,4)** | Lowest sell price currently available in the stock. |
| ELMargin | Double | **(15,4)** | Extreme Loss Margin required for the instrument. |
| Interest | Boolean | **10** | Interest rate applicable to a debt instrument or derivative. |
| ISIN | String | **15** | International Securities Identification Number, unique per security. |
| MinimumFill | Boolean | **5** | Minimum quantity that can be executed in a single order. |
| Rights | Boolean | **5** | Number of rights shares issued per existing share. |
| VaRMargin | Double | **(15,4)** | Total capital issued by the company. |
| IssuedCapital | Integer | **10** | Total capital issued by the company. |
| BoardLotQuantity | Integer | **10** | Minimum number of units that can be traded in one lot. |
| FaceValue | Integer | **10** | Face value of the security per unit/share. |
| Spread | Integer | **10** | Difference between best buy and sell price. |
| CallAuction1Flag | Boolean | **5** | Indicates if a first call auction is applicable. |
| GSMIndicator | Integer | **10** | Indicator for market segments or trading type. |
| MinimumQty | Integer | **10** | Minimum tradable quantity for the instrument. |
| QuantityMultiplier | Integer | **10** | Multiplier applied to quantity for derivatives/contracts. |
| PriceNumerator | Integer | **10** | Numerator for representing price fractions. |
| PriceDenominator | Integer | **10** | Denominator for representing price fractions. |
| SymbolType | Integer | **20** | Symbol classification type (e.g., Common, Preferred). |
| CfiCode | String | **50** | Classification of Financial Instruments code. |
| Status | String | **50** | Current status of the instrument (Active, Inactive). |
| TicksPerPoint | Integer | **10** | Number of ticks per point for price movement. |
| IsImpliedMarket | Double | **(15,4)** | Indicates if the market is derived from implied instruments. |
| IsTradeable | Boolean | **5** | Indicates if the instrument is currently tradeable. |
| MaxTradeVolume | Long | **15** | Maximum allowed trade volume per order. |
| DecimalDisplace | Integer | **10** | Number of decimal places used for pricing. |
| Eligible | Boolean | **5** | Indicates if the instrument is eligible for trading. |
| TradingStatus | Integer | **10** | Current trading status (Active, Suspended, Halted). |
| DisplayNameWithExchange | String | **50** | Display name including exchange information. |
| FiftyTwoWeekHigh | Double | **(15,4)** | Highest price of the instrument in the past 52 weeks. |
| FiftyTwoWeekLow | Double | **(15,4)** | Lowest price of the instrument in the past 52 weeks. |
| TotTrdQty | Long | **15** | Total traded quantity in the session. |
| TotTrdVal | Double | **(15,4)** | Total traded value in the session. |
| TimeStamp | String | **50** | Timestamp of the data snapshot. |
| TotalTrades | Long | **15** | Total number of trades executed in the session. |
| OpenInterest | Double | **(15,4)** | Open interest for derivatives contracts. |
| SettlementPrice | Double | **(15,4)** | Price used for settlement of derivatives contracts. |
| AdditionalPreExpiryMarginPerc | Double | **(15,4)** | Additional margin percentage applicable before expiry. |
| AdditionalMarginPercLong | Double | **(15,4)** | Additional margin percentage for long positions. |
| AdditionalMarginPercShort | Double | **(15,4)** | Additional margin percentage for short positions. |
| DeliveryMarginPerc | Double | **(15,4)** | Margin percentage required for delivery-based trades. |
| SpecialMarginPercBuy | Double | **(15,4)** | Special margin percentage for buying positions. |
| SpecialMarginPercSell | Double | **(15,4)** | Special margin percentage for selling positions. |
| TenderMargin | Double | **(15,4)** | Margin required for participating in tender offers. |
| ELMLongMargin | Double | **(15,4)** | Extreme loss margin for long positions. |
| ELMShortMargin | Double | **(15,4)** | Extreme loss margin for short positions. |
| InitialMarginPerc | Double | **(15,4)** | Initial margin percentage for derivatives contracts. |
| ExposureMarginPerc | Double | **(15,4)** | Margin based on exposure limit. |
| CallAuctionIndicator | Integer | **10** | Indicates if the instrument is part of a call auction. |
| CurrentEligibleMarketType | Integer | **10** | Market types the instrument is eligible for currently. |
| InstrumentLazyLoader | Integer | **10** | Indicates if instrument data is loaded lazily for performance. |
| StartTime | String | **30** | The starting timestamp from which OHLC data should be retrieved. |
| EndTime | String | **30** | The ending timestamp up to which OHLC data should be retrieved. |
| CompressionValue | String | **30** | The interval or granularity of OHLC data. |
