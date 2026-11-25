# Enums with Numeric Constants

Each Enum now includes its corresponding numeric constant for easier mapping in client applications.

## 1. ExchangeSegments

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| NSECM | **1** | The equity cash segment of NSE where stocks of listed companies are traded for delivery or intraday. |
| NSEFO | **2** | Derivatives segment of NSE where equity futures, index futures, and options contracts are traded. |
| NSECD | **3** | Currency trading segment at NSE for exchange-traded currency futures and options (USD/INR, EUR/INR, etc.) |
| BSECM | **11** | Cash/equity segment of BSE, the oldest stock exchange in Asia, where stocks are bought and sold. |
| BSEFO | **12** | Derivatives segment of BSE offering equity derivatives, index derivatives, and stock futures/options. |
| BSECD | **13** | Currency derivatives platform of BSE that allows trading in exchange-listed currency futures and options. |
| MCXFO | **51** | Derivatives trading segment of MCX for commodities such as gold, silver, crude oil, natural gas, and agricultural products. |
| NCDEX | **21** | A leading exchange focused on agricultural commodity futures like soybean, chana, guar, and other agri-products. |

## 2. ProductType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| MIS | **1** | Intraday trading product type where positions must be squared off before market close. Provides higher leverage compared to delivery. |
| NRML | **2** | Standard product type used for carrying forward positions overnight in derivatives or cash without compulsory intraday square-off. |
| CNC | **4** | Delivery-based product type for equity trades. Shares are delivered to the Demat account, with no leverage. |
| CO | **8** | Intraday order type where a market or limit order is placed along with a mandatory stop-loss order. Provides higher leverage while controlling risk. |
| BO | **16** | Advanced order type where a main order is placed with both a target (profit booking) and stop-loss. Once one is executed, the other is automatically cancelled. Can also include a trailing stop-loss. |
| MTF | **32** | Allows investors to buy stocks by partly paying upfront and borrowing the balance from the broker. Shares can be carried forward as long as margin requirements are met. |

## 3. OrderType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Market | **1** | An order to buy or sell immediately at the best available price in the market. |
| Limit | **2** | An order to buy or sell at a specified price (or better). |
| StopMarket | **4** | An order that becomes a market order once a specified trigger price is reached. Used mainly to limit losses |
| StopLimit | **8** | An order that becomes a limit order once the trigger price is reached. It executes only at the specified limit price or better. |
| OCO | **32** | A conditional order where two linked orders are placed — if one gets executed, the other is automatically cancelled. |
| MTF | **32** | Allows investors to buy stocks by partly paying upfront and borrowing the balance from the broker. Shares can be carried forward as long as margin requirements are met. |

## 4. OrderSide

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| BUY | **49** | Indicates a purchase transaction. Used when entering a long position (expecting the price to rise). |
| SELL | **50** | Indicates a sale transaction. Used when exiting a long position or initiating a short position (expecting the price to fall). |

## 5. TimeInForce

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| DAY | **1** | Order remains valid only for the trading day. If not executed by market close, it is cancelled automatically. |
| GTC | **2** | (Good Till Cancelled) Order remains active until it is explicitly cancelled by the trader. May carry over across multiple trading sessions. |
| IOC | **4** | Order must be executed immediately (full or partial). Any unfilled portion is cancelled instantly. |
| GTD | **8** | (Good Till Date) Order remains valid until a specified date. If not executed by then, it is cancelled automatically. |
| EOS | **16** | Order remains valid until the end of the trading session (intraday cutoff). |
| COL | **32** | Order is executed only at the market close price. |
| GTDYS | **128** | Order remains active for a defined number of trading days. |

## 6. Order Status

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Open or New | **48** | The order has been placed successfully and is waiting for execution. |
| PartiallyFilled | **49** | Only part of the order quantity has been executed. The remaining is still pending in the market. |
| Filled | **50** | The entire order quantity has been executed successfully. |
| Cancelled | **52** | The order has been withdrawn by the trader before it was executed. |
| Replaced | **53** | The original order has been modified (e.g., price or quantity) and is now treated as a new order with updated details. |
| PendingCancel | **54** | A cancel request has been sent but the order has not yet been cancelled. |
| Rejected | **56** | The order was not accepted due to validation errors, insufficient margin, trading rules, or exchange rejection. |
| PendingNew | **65** | The order has been submitted but is still waiting for acknowledgement from the exchange. |
| PendingReplace | **69** | A modification request has been sent for the order but confirmation from the exchange is pending. |

## 7. OrderSource

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| TWS | **1** | Orders placed directly from the broker’s desktop trading terminal. |
| TWSAPI | **2** | Orders submitted via the Trader Workstation’s API integration, typically through algorithmic or automated trading systems. |
| WEB | **21** | Orders entered manually by the trader through the broker’s web-based trading platform. |
| WEBAPI | **22** | Orders placed programmatically via web API integrations — used by custom applications or third-party tools. |
| MOBILEANDROID | **41** | Orders placed through the broker’s Android mobile trading application. |
| MOBILEIOS | **81** | Orders placed through the broker’s iOS mobile trading application. |
| EnterpriseWeb | **154** | Orders originating from an enterprise-grade web trading application. |
| EnterpriseMobile | **155** | Orders generated from enterprise-level mobile apps built for institutional traders. |
| EnterpriseTWS | **156** | Orders placed via an advanced or customized version of the Trader Workstation used in enterprise setups. |

## 8. Position Square Off Mode

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| DayWise | **1** | Tracks intraday positions separately for each trading day. |
| NetWise | **2** | Consolidates positions across multiple days into a net position. |

## 9. Position Square Off Quantity Type

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Percentage | **0** | Exit is defined as a percentage of the total position. |
| ExactQty | **1** | Exit is defined as a fixed quantity of the position. |

## 10. MarketType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Normal | **1** | Standard market segment where regular equity and derivative trades are placed. Most buy/sell orders are routed here. |
| Oddlot | **2** | Used when the order quantity is less than the standard market lot size. Allows trading of small or non-standard quantities of shares. |
| Retaildebt | **3** | Segment dedicated to retail trading in debt instruments like corporate bonds, government securities, or debentures. |
| Auction | **4** | Segment where auctions are conducted, usually for settlement shortages or special situations (e.g., buy-in auctions when sellers fail to deliver). |
| CallAuction1 | **5** | Call auction mechanism session 1 — typically for illiquid securities. Orders are pooled and executed together at a uniform price. |
| CallAuction2 | **6** | Call auction mechanism session 2 — another session for specific securities or time slots where orders are batched and executed at a single price. |

## 11. OrderLegStatus

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| SingleOrderLeg | **1** | Represents a simple standalone order with no linked legs. |
| SpreadFirstLeg | **2** | The primary leg of a spread order strategy. |
| SpreadSecondLeg | **3** | The counter leg of a spread order that offsets the first leg. |
| MultilegFirstLeg | **4** | The first leg in a multi-leg strategy (often options) |
| MultilegSecondLeg | **5** | The second leg in a multi-leg strategy. |
| MultilegThirdLeg | **6** | The third leg in advanced multi-leg strategies. |

## 12. Bo_Leg_Details

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| EntryLeg | **1** | The main order leg where the trader enters the position (buy or sell). |
| ProfitTargetExitLeg | **2** | An automatic exit leg placed along with the entry order to book profit once the target price is reached. |
| StoplossExitLeg | **3** | A protective exit leg that closes the position if the price moves unfavorably beyond a defined limit. |

## 13. DayOrNet

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| DAY | **1** | Positions are valid only for the trading day. |
| NET | **2** | Includes delivery trades (CNC) or carry-forward derivative positions (NRML). |

## 14. InstrumentType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Futures | **1** | Standardized derivative contracts to buy or sell an asset (stock, index, commodity, or currency) at a predetermined price on a future date. |
| Options | **2** | Derivative contracts that give the buyer the right, but not the obligation, to buy (Call) or sell (Put) the underlying asset at a fixed price within a specified time. |
| Spread | **4** | A strategy involving simultaneous buying and selling of related instruments. |
| Equity | **8** | Shares of listed companies traded in the cash market segment. |
| Spot | **16** | Trades for immediate delivery and settlement at the current market price, typically used in currencies and commodities. |
| PreferenceShares | **32** | A class of shares that provides fixed dividends and has priority over equity shares in dividend distribution and liquidation, but usually with limited voting rights. |
| Debentures | **64** | Long-term debt instruments issued by companies or governments to raise funds. Typically carry fixed interest payments. |
| Warrants | **128** | Financial instruments that give the holder the right to buy equity shares at a specific price before a set expiry date. |
| Miscellaneous | **256** | Category for instruments that do not fall into standard classifications (used for special or rare products). |
| MutualFund | **512** | Units of pooled investment schemes managed by Asset Management Companies (AMCs). |

## 15. TradingSession

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| PreOpenStart | **0** | The beginning of the pre-open session where orders can be placed but are not matched immediately. |
| PreOpenEnd | **1** | The end of the pre-open session when accumulated orders are matched, and the opening price is determined. |
| NormalStart | **2** | The start of the regular trading session where continuous matching of buy and sell orders happens. |
| NormalEnd | **4** | The close of the regular trading session; after this point, no further trades are executed in the normal market. |
| PreClosingStart | **8** | The start of the pre-closing session, where the system collects data to calculate the closing price (closing auction). |
| PreClosingEnd | **16** | The end of the pre-closing session when the official closing price is determined and published. |

## 16. ValuationType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| NONE | **0** | Default flag when no special settlement type is applied. The order follows the normal market settlement rules. |
| CL | **1** | Orders specifically placed to be executed at the market’s closing price during the closing session. |
| LT | **2** | Segment used for block deals, bulk trades, or special limited trading windows defined by the exchange. |

## 17. HoldingType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| T1_Holdings | **1** | Securities bought but not yet fully settled (i.e., on T+1 day). |
| Holdings | **3** | Fully settled securities that are credited to the client’s Demat account. |
| MTFHoldings | **3** | Securities purchased under Margin Trading Facility where part of the funds are borrowed from the broker. |

## 18. StatisticsLevel

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| ParentLevel | **0** | Represents the top-level entity in a hierarchy. |
| ChildLevel | **1** | Represents a sub-entity under a parent. |

## 19. Socket Event

| Enum Name | Description |
| --- | --- |
| joined | Sent when a client successfully connects and joins the WebSocket channel. Confirms that the real-time stream is active. |
| error | Indicates a failure or issue (e.g., invalid request, authentication failure, or system error). Requires client-side handling. |
| warning | Non-critical issue or advisory message (e.g., rate-limit approaching, deprecated API usage). |
| success | Confirms that a client request was processed successfully (e.g., order placement acknowledged). |
| order | Event carrying real-time updates about an order lifecycle — placed, modified, filled, cancelled, or rejected. |
| trade | Sent when an order results in an actual trade execution (full or partial). Contains trade ID, price, and quantity details. |
| logout | Notification that the session or WebSocket connection has been terminated — either manually or due to token expiry. |
| position | Real-time updates about portfolio positions, including intraday (DayWise) or carry-forward (NetWise) quantities. |
| tradeConversion | Event triggered when an order/trade is converted from one product type to another (e.g., Intraday MIS → Delivery CNC). |
| gttOrder | Event update for GTT orders (orders that activate only when a trigger price is met). |
| gttOrderRejection | Notification when a GTT order fails to activate due to invalid conditions, margin shortfall, or exchange rejection. |

## 20. Order Session Type

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| AMO | **1** | Standard market order placed during regular market hours. |
| OT | **2** | *After Market Order –* Orders placed after market hours to be processed when the market opens |
| INSTI | **4** | *Institutional –* Orders placed through institutional trading sessions. |
| GTT | **5** | Good Till Triggered – Order remains pending until the trigger condition is met. |
