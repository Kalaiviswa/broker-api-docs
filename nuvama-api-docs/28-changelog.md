# Changelog

## Python

All notable changes to this project will be documented in this file.

## [2.0.11] - 2026-03-30

### Added

- 2 New fields added to the orderbook and orderdetails APIs

### Changed

- API usage threshold
- Static IP Mandatory

### Removed

- Removed Bracket Orders API
- Removed Basket Orders API

## [2.0.10] - 2026-01-11

### Changed

- Removed commodity specific APIs
- Now trade APIs are common for both commodity and equity
- AMOFLAG API URL has been changed

## [2.0.8] - 2024-06-28

### Added

- Bug Fixes

## [2.0.7] - 2024-03-18

### Added

- Added exchange segment : BFO

## [2.0.5] - 2023-12-29

### Added

- Transaction History

## [2.0.4] - 2023-11-03

### Added

- Order slicing
- PIT IRF

### Changed

- Request structure of Position square off api in equity segment
- Response structure of Place trade (including amo) api in equity segment has changed for order which are getting sliced
- Response structure of Modify trade (including amo) api in equity segment has changed for order which are getting sliced
- Request structure of Modify trade (including amo) api in equity segment
- Request structure of cancel trade (including amo) api in equity segment

## [2.0.3] - 2023-07-28

### Added

- MiniQuote Feed
- Market Depth Feed and API
- New Price Feed (reduced quote feed in human readable format)
- Bug Fixes

### Note

- We shall keep existing price feed for some days so as to ensure smooth transition from the existing to the newer one

## [2.0.2] - 2023-05-20

### Added

- Commodity changes
- Bug Fixes

### Changed

- Discontinuation of Reasearch calls
- Changes in the Logout , ConvertPosition and AmoFlag API's

## [2.0.0] - 2022-12-16

### Added

- Added Live News Streaming feature

### Changed

- In view of brand name change from Edelweiss to nuvama, necessary changes were made in accordance.
- Now Streamers would work after login only.
- Code changes for calling Streamers subscribe and unsubscribe calls.

### Fixed

## [1.0.3] - 2022-08-30

### Added

- Added charting feature for NSE, BSE, NFO, CDS, MCX, NCDEX and INDEX exchanges
- Added Live News feature
- Added Research Calls feature for Equity, Currency and Futures and Options
- Added Watchlist feature

### Changed

- Most features now expect inputs as enums. Below methods will be impacted by this – PlaceTrade, ModifyTrade PlaceCoverTrade, PlaceBracketTrade, ModifyCoverTrade, PlaceGtcGtdTrade, CancelTrade, ConvertPosition, PlaceAMOTrade, ModifyAMOTrade, CancelAMOTrade, OrderDetails . Please refer to code examples in documentation for more details.
- PlaceBasketTrade and PositionSquareOff methods now take as input a list of instances of Order class. Please refer to code examples for more details.
- Feed class is now located in feed module. Please refer to code examples for more details.

### Fixed

Streamer now does not block execution of code

## [1.0.2] - 2021-07-29

### Added

- Added support for commodity trading with MCX and NCDEX exchanges
- Added support for enabling proxy
- Added Logging functionality to library with configurable logging levels
- Added configuration file for user configurable settings related to logging, proxy and streaming

### Changed

- APIConnect class will now take an additional input parameter 'conf' - path for
  configuration file
- All responses will now be returned as JSON object
- Most responses will now have a format of {"eq":...,"comm":...}, "eq" will
  contain details for NSE/BSE exchanges, whereas "comm" will relate to MCX/NCDEX. Check method
  responses in documentation for more details.
  Below methods will be impacted by this change - OrderBook, TradeBook, NetPosition, OrderHistory, Holdings,
  Limits and GetAMOStatus
- OrderDetails will now have an additional input parameter for Exchange e.g. NSE, BSE, MCX or NCDEX
- PlaceGtcGtdTrade will now have an additional input parameter for Streaming_Symbol
- CancelTrade will now have additional input parameters for Exchange, Order_Type and Product_Code
- CancelAMOTrade will now have additional input parameters for Exchange, Order_Type and Product_Code
- ConvertPosition will now have additional input parameters for Exchange and Order_Type
- PlaceMF will now have an additional input parameter for Mandate_Id
- ModifyMF will now have an additional input parameter for Mandate_Id
- Feed class will now take only three parameters accid, userid, 'conf' - path for configuration file
- Feed class has new method 'subscribe', check documentation for details

### Fixed

### Added

Python library release with support for NSE and BSE exchanges

### Changed

### Fixed

Streamer now does not block execution of code

Node Changelog

## Node

All notable changes to this project will be documented in this file.

## [2.0.15] - 2026-03-30

### Added

- 2 New fields added to the orderbook and orderdetails APIs

### Changed

- API usage threshold
- Static IP Mandatory

### Removed

- Removed Bracket Orders API
- Removed Basket Orders API

## [2.0.14] - 2026-01-11

### Changed

- Removed commodity specific APIs
- Now trade APIs are common for both commodity and equity
- AMOFLAG API URL has been changed

## [2.0.12] - 2024-03-18

### Added

- Added exchange segment : BFO

## [2.0.11] - 2023-12-29

### Added

- Transaction History

## [2.0.10] - 2023-11-03

### Added

- Order slicing
- PIT IRF

### Changed

- Request structure of Position square off api in equity segment
- Response structure of Place trade (including amo) api in equity segment has changed for order which are getting sliced
- Response structure of Modify trade (including amo) api in equity segment has changed for order which are getting sliced
- Request structure of Modify trade (including amo) api in equity segment
- Request structure of cancel trade (including amo) api in equity segment

## [2.0.5] - 2023-07-28

### Added

- MiniQuote Feed
- Market Depth Feed and API
- New Price Feed (reduced quote feed in human readable format)
- Bug Fixes

### Note

- We shall keep existing price feed for some days so as to ensure smooth transition from the existing to the newer one

## [2.0.4] - 2023-05-20

### Added

- Commodity changes
- Bug Fixes

### Changed

- Discontinuation of Reasearch calls
- Changes in the Logout , ConvertPosition and AmoFlag API's

## [2.0.0] - 2022-12-16

### Added

- Added Live News Streaming feature

### Changed

- In view of brand name change from to Nuvama, necessary changes were made in accordance to class names. Please refer to code examples in documentation for more details.
- Streaming now requires to go through login flow.
- Code changes for calling Streamers subscribe and unsubscribe calls. Please refer to code examples in documentation for more details.

### Fixed

## [1.0.1] - 2022-08-30

### Added

- Added Charts Feature.
- Added Live News Feature.
- Added Research Calls Feature.
- Added Watchlist Feature.

### Changed

- PlaceMF will now have an additional input parameter for Mandate_Id
- ModifyMF will now have an additional input parameter for Mandate_Id

Java Changelog

## Java

All notable changes to this project will be documented in this file.

## [2.0.10] - 2026-03-30

### Added

- 2 New fields added to the orderbook and orderdetails APIs

### Changed

- API usage threshold
- Static IP Mandatory

### Removed

- Removed Bracket Orders API
2- Removed Basket Orders API

## [2.0.9] - 2026-01-11

### Changed

- Removed commodity specific APIs
- Now trade APIs are common for both commodity and equity
- AMOFLAG API URL has been changed

## [2.0.7] - 2024-06-28

### Added

- Bug Fixes

## [2.0.6] - 2024-03-18

### Added

- Added exchange segment : BFO

## [2.0.5] - 2023-12-29

### Added

- Transaction History

## [2.0.4] - 2023-11-03

### Added

- Order slicing
- PIT IRF

### Changed

- Request structure of Position square off api in equity segment
- Response structure of Place trade (including amo) api in equity segment has changed for order which are getting sliced
- Response structure of Modify trade (including amo) api in equity segment has changed for order which are getting sliced
- Request structure of Modify trade (including amo) api in equity segment
- Request structure of cancel trade (including amo) api in equity segment

## [2.0.2] - 2023-07-28

### Added

- MiniQuote Feed
- Market Depth Feed and API
- New Price Feed (reduced quote feed in human readable format)
- Bug Fixes

### Note

- We shall keep existing price feed for some days so as to ensure smooth transition from the existing to the newer one

## [2.0.1] - 2023-05-20

### Added

- Commodity changes
- Bug Fixes

### Changed

- Discontinuation of Reasearch calls
- Changes in the Logout , ConvertPosition and AmoFlag API's

## [2.0.0] - 2022-12-16

### Added

- Added Live News Streaming feature

### Changed

- In view of brand name change from to Nuvama, necessary changes were made in accordance to class names. Please refer to code examples in documentation for more details.
- Streaming now requires to go through login flow.
- Code changes for calling Streamers subscribe and unsubscribe calls. Please refer to code examples in documentation for more details.

### Fixed

## [1.0.1] - 2022-08-30

### Added

- Added Charts Feature.
- Added Live News Feature.

### Changed

- PlaceMF will now have an additional input parameter for Mandate_Id
- ModifyMF will now have an additional input parameter for Mandate_Id

### Fixed
