# Nuvama Wealth (API Connect) Documentation

Source: https://www.nuvamawealth.com/library-documentation/#swagger-spec-for-our-equity-rest-project-uat-version

Converted from Nuvama's single-page API Connect docs (Swagger spec, UAT version). One file per top-level section.

- REST base URL (UAT, as given in the samples): `https://emtuat.edelweiss.in/edelmw-eq-uat` (for example `/eq/trade/placetrade/v1/{userID}` and `/accounts/loginvendor/{vendorID}`)
- Login URL: `https://www.nuvamawealth.com/api-connect/login?api_key=xxx`. After login, the redirect URL carries the `requestId`.
- Streaming host: `ncst.nuvamawealth.com:9443`

## Overview and SDKs

- [API Connect Document](01-api-connect-document.md): introduction
- [API Usage Threshold](02-api-usage-threshold.md): rate limits and what happens when you breach them
- [Java library](03-java-library.md)
- [NodeJS library](04-nodejs-library.md)
- [Python library](05-python-library.md)
- [C# library](06-csharp-library.md)

## REST APIs

- [Authentication](07-authentication.md): `Authorization` header
- [Common-Login](08-common-login.md): validate vendor id and password and generate a session, get login data for a request id, log out
- [Trade](09-trade.md): place trade and order slicing, modify, cancel, AMO flag, position square-off, convert position, AMO place/modify/cancel
- [Orders](10-orders.md): order book, order details, order history
- [Holdings](11-holdings.md): CNC and MTF RMS holdings
- [Limits](12-limits.md): RMS sub-limits
- [PositionBook](13-positionbook.md): net positions
- [TradeBook](14-tradebook.md): trade book
- [Transaction-History](15-transaction-history.md): transaction history
- [Market-Depth](16-market-depth.md): market depth for a symbol
- [Charting](17-charting.md): intraday tick-by-tick and EOD historical data
- [Live News](18-live-news.md): news categories, live news, results and news, corporate actions
- [Watchlist](19-watchlist.md): watchlist groups and scrips (get, create, delete, rename, add and delete symbols)
- [Instruments](20-instruments.md): instrument master

## Streaming

- [Streaming](21-streaming.md): overview and subscribing
- [Reduced Quotes Streamer](22-reduced-quotes-streamer.md)
- [Mini Quote Streamer](23-mini-quote-streamer.md)
- [Market Depth Streamer](24-market-depth-streamer.md)
- [Orders Streamer](25-orders-streamer.md)
- [Live News Streamer](26-live-news-streamer.md)

## Reference

- [Schemas](27-schemas.md): request and response models, enums
- [Changelog](28-changelog.md)

## Conversion notes

- The source page's Go samples read `"net/R"`, `R.NewRequest` and `"Rs://..."`. That looks like a broken find-and-replace of `http`, so they are corrected here to `net/http`, `http.NewRequest` and `https://`.
- Schema links (`#schema...` on the source page) point to [27-schemas.md](27-schemas.md). `MarketDepthDao` and `TransactionHistoryDao` are referenced but not defined on the source page.
- The source's empty code-sample tabs (for example under Instruments) are omitted.
- The rate-limit table used a merged cell. It is rewritten in [02-api-usage-threshold.md](02-api-usage-threshold.md) so each row is complete.
