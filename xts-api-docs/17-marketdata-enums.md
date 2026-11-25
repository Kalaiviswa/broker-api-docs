# Market Data API: Enums

Each Enum now includes its corresponding numeric constant for easier mapping in client applications.

## 1. ExchangeSegments

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| NSECM | **1** | The equity cash segment of NSE where stocks of listed companies are traded for delivery or intraday. |
| NSEFO | **2** | Derivatives segment of NSE where equity futures, index futures, and options contracts are traded. |
| NSECD | **3** | Currency trading segment at NSE for exchange-traded currency futures and options (USD/INR, EUR/INR, etc.) |
| NSECO | **4** | The commodity derivatives segment of NSE where agricultural and non-agricultural commodities are traded via futures and options contracts. |
| BSECM | **11** | Cash/equity segment of BSE, the oldest stock exchange in Asia, where stocks are bought and sold. |
| BSEFO | **12** | Derivatives segment of BSE offering equity derivatives, index derivatives, and stock futures/options. |
| BSECD | **13** | Currency derivatives platform of BSE that allows trading in exchange-listed currency futures and options. |
| MCXFO | **51** | Derivatives trading segment of MCX for commodities such as gold, silver, crude oil, natural gas, and agricultural products. |
| NCDEX | **21** | A leading exchange focused on agricultural commodity futures like soybean, chana, guar, and other agri-products. |

## 2. MarketType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Normal | **1** | Regular trading segment where standard lot sizes apply and continuous trading happens. |
| Oddlot | **2** | Trading of quantities **less than the standard lot size** (e.g., 1 share when lot size is 10). |
| Retaildebt | **3** | Segment meant for **retail investors** to trade debt instruments like bonds, NCDs, and G-Secs. |
| Auction | **4** | Special session used for **buy-in / sell-out** when obligations are not met (e.g., short delivery). |
| CallAuction1 | **5** | First **call auction session** where orders are collected, matched, and executed at a single equilibrium price. |
| CallAuction2 | **6** | Second call auction session, usually used for **price discovery, illiquid stocks, or special scenarios**. |

## 3. InstrumentType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Futures | **1** | Derivative contracts to buy or sell an asset at a **fixed price on a future date**. |
| Options | **2** | Derivative contracts giving the **right (not obligation)** to buy or sell an asset at a specified price before/on expiry. |
| Spread | **4** | A strategy instrument representing **simultaneous buy & sell** of related contracts (e.g., calendar or inter-commodity spreads). |
| Equity | **8** | Ownership instruments representing **shares of a company**. |
| Spot | **16** | Instruments traded for **immediate settlement** (cash/spot market). |
| PreferenceShares | **32** | Shares with **fixed dividend priority** over equity shares but limited/no voting rights. |
| Debentures | **64** | **Debt instruments** issued by companies to raise capital, typically with fixed interest. |
| Warrants | **128** | Instruments giving the **right to buy equity shares** at a predetermined price within a specified time. |
| Miscellaneous | **256** | Instruments that do not fall into **standard categories** or are exchange-defined special cases. |
| MutualFund | **512** | Investment vehicles that **pool money** from investors to invest in diversified assets. |

## 4. XTS Message Code

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| TouchLineEvent | **1501** | Provides **top-of-book data** — best bid price & quantity and best ask price & quantity. |
| MarketDepthEvent | **1502** | Delivers **order book depth data** (multiple bid/ask levels beyond the touchline). |
| CandleDataEvent | **1505** | Supplies **OHLCV candle data** for a specified interval (e.g., 1m, 5m, daily). |
| OpenInterestEvent | **1510** | Publishes **open interest changes** for derivative instruments, indicating active positions. |

## 5. Exchange Trading Session

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| PreOpenStart | **0** | The pre-open session has **started**. Order entry/modification allowed for price discovery. |
| PreOpenEnd | **1** | The pre-open session has **ended**. Orders are frozen and matched. |
| NormalStart | **2** | **Regular market trading** sessions have started (continuous trading). |
| NormalEnd | **4** | The regular market trading session has **ended**. No new trades allowed. |
| PostClosingStart | **8** | Post-closing session has **started** (trade confirmation, reporting, limited actions). |
| PostClosingEnd | **16** | The post-closing session has **ended**. |
| Closed | **32** | The market is **fully closed** (no trading activity). |
| None | **256** | None above this. |

## 6. Exchange Market Type

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Normal | **1** | Regular trading segment where standard lot sizes apply and continuous trading happens. |
| OddLot | **2** | Trading of quantities **less than the standard lot size** (e.g., 1 share when lot size is 10). |
| RetailDebt | **3** | Segment meant for **retail investors to trade debt instruments** like bonds, NCDs, G-Secs. |
| Auction | **4** | Special session used for **buy-in / sell-out** when obligations are not met (e.g., short delivery). |
| CallAuction1 | **5** | First **call auction session** where orders are collected, matched, and executed at a single equilibrium price. |
| CallAuction2 | **6** | Second call auction session, usually used for **price discovery, illiquid stocks, or special scenarios**. |

## 7. CallAuction Type

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| NonCallAuction | **0** | Regular **non-call auction trading** where orders are matched continuously (price–time priority). |
| PreOpen | **1** | **Pre-open session** used for order collection and **price discovery** before normal market opens. |
| IPOPreOpen | **2** | Special **pre-open session for IPOs**, used to discover opening price on the listing day. |
| RelistPreOpen | **3** | Pre-open session for **re-listed securities** (e.g., after suspension, merger, restructuring). |
| Illiquid | **4** | Market segment for **illiquid securities**, often traded via call auctions to improve price discovery. |
| SME | **5** | Market segment for **Small and Medium Enterprises**, with distinct trading and settlement rules. |
| SCAS | **6** | **Special Call Auction Session** used in exceptional cases such as **volatility control**, surveillance actions, or **regulatory intervention**. |

## 8. BookType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| None | **0** | No **specific order book type** applicable. |
| Regular | **1** | Standard **continuous trading order book** for normal market orders. |
| SpecialTerms | **2** | Orders executed under **special settlement or contract terms** defined by the exchange. |
| StopLoss | **3** | Order book for **stop-loss / trigger-based orders**, activated when trigger price is hit. |
| Negotiated | **4** | Book for **privately negotiated trades** reported to the exchange. |
| OddLot | **5** | Order book for **odd-lot quantities** (less than normal lot size). |
| Spot | **6** | Book for **spot market trades** with immediate or short settlement. |
| Auction | **7** | Book used during **auction sessions** (buy-in, sell-out, surveillance auctions). |
| CallAuction1 | **11** | First call the **auction order book** for price discovery. |
| CallAuction2 | **12** | Second **call auction order book** for subsequent matching. |

## 9. OptionType

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| CA | **1** | **Corporate Action** — events initiated by a company that impact securities. |
| PA | **2** | **Product Action / Portfolio Action** — exchange or system-driven actions affecting instruments or positions. |
| CE | **3** | **Call Option** — option giving the right to **buy** the underlying at the strike price on expiry. |
| PE | **4** | **Put Option** — option giving the right to **sell** the underlying at the strike price on expiry. |
| None | **5** | No **specific action or option type** applicable. |

## 10. PublishFormat

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Binary | **1** | Market data is published in **binary-encoded format** for **low latency, high throughput** consumption. |
| JSON | **2** | Market data is published in **JSON (text) format**, making it **human-readable and easy to parse**. |

## 11. BroadCastMode

| Enum Name | Numeric Code | Description |
| --- | --- | --- |
| Full | **1** | The server **broadcasts the complete dataset** to subscribers in **JSON format**. |
| Partial | **2** | The server **broadcasts the complete dataset** to subscribers but in **\| (Pipe) separated** and **trimmed format**. |

## 12. Socket Event

| Enum Name | Description |
| --- | --- |
| joined | Websocket Joined acknowledgement |
| error | Erro during Websocket connection |
| warning | Warning message |
| success | Success Response |
