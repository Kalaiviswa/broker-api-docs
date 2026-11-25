# Symphony XTS Front End API v2 Documentation

Sources:

- Trading (Interactive): https://symphonyfintech.com/xts-trading-front-end-api-v2/ (files 01-15)
- Market Data: https://symphonyfintech.com/xts-market-data-front-end-api-v2/ (files 16-24)

Converted from Symphony Fintech's two single-page XTS API v2 docs. One file per top-level section. XTS is the platform behind several Indian brokers' APIs. Each broker hosts its own XTS server, so swap the sample host for your broker's.

- Sample host: `https://developers.symphonyfintech.in`
- HostLookup: `POST /hostlookup` returns the `UniqueKey` and `ConnectionString` (the Interactive path, for example `/1interactive`)
- Interactive REST base (sample): `https://developers.symphonyfintech.in/1interactive`
- Streaming: Socket.IO on the same host, path `/1interactive/socket.io`, query `token`, `userID`, `apiType=INTERACTIVE`
- Market data REST base (sample): `https://developers.symphonyfintech.in/apibinarymarketdata`
- Market data streaming: Socket.IO, path `/apibinarymarketdata/socketio` in the sample code, query `token`, `userID`, `publishFormat`, `broadcastMode`

## Overview and reference

- [Overview](01-overview.md): introduction, environment URL, SDKs, getting API credentials, auth token, request/response structure, HTTP errors, rate limits
- [Enums](02-enums.md): exchange segments, product type, order type, order side, time in force, order status, order source, square-off mode and quantity type, market type, leg status, day/net, instrument type, trading session, valuation and holding type, statistics level, socket events, order session type (with numeric codes)
- [Data Types & Business Rules](03-data-types-and-business-rules.md): every field's type, size and meaning

## REST APIs

- [User](04-user.md): OAuth login flow, HostLookup, login, logout, balance, profile, brokerage calculator
- [Standard Orders](05-standard-orders.md): place, modify, cancel, cancel all
- [Cover Orders](06-cover-orders.md): place, exit
- [Bracket Orders](07-bracket-orders.md): place, modify, cancel
- [OrderBook and TradeBook](08-orderbook-and-tradebook.md): order book, trade book, order history
- [Spread Orders](09-spread-orders.md): place, modify, cancel, spread order book
- [GTT Orders](10-gtt-orders.md): place, modify, cancel, GTT order book
- [Portfolio](11-portfolio.md): holdings, positions, position convert
- [Margin](12-margin.md): regular, modify regular, cover, modify cover and bracket order margin
- [Exchange](13-exchange.md): exchange status, exchange messages

## Streaming and calculations

- [Socket Streaming](14-socket-streaming.md): Socket.IO connection and events (connect, joined, error, disconnect, order, trade, position, trade conversion, GTT order, GTT rejection, market status, exchange adapter state, logout)
- [MTM Calculation](15-mtm-calculation.md): realized and unrealized MTM from position data and LTP (the API does not return MTM)

## Market Data API

- [Overview](16-marketdata-overview.md): introduction, environment URL, SDKs, getting API credentials, auth token, request/response structure, HTTP errors
- [Enums](17-marketdata-enums.md): exchange segments, market type, instrument type, XTS message codes, trading session, exchange market type, call auction type, book type, option type, publish format, broadcast mode, socket events
- [Data Types & Business Rules](18-marketdata-data-types-and-business-rules.md)
- [Auth](19-marketdata-auth.md): login, logout, client config
- [Search](20-marketdata-search.md): instruments by ID, instruments by search string
- [Instruments](21-marketdata-instruments.md): master, quote, index list, series, equity symbol, expiry date, future symbol, option type, strike price, option symbol
- [OHLC](22-marketdata-ohlc.md): intraday candles and compression values
- [Socket Subscription](23-marketdata-subscription.md): subscribe and unsubscribe
- [Socket Streaming](24-marketdata-socket-streaming.md): Socket.IO connection, events, binary packet layouts (touchline 1501, market depth 1502, candle 1505, open interest 1510)

## Conversion notes

- The Trading files keep the source's own top headings. The Market Data files are titled `Market Data API: <section>` so the two halves don't clash.
- Each request/response field's "Type" cell is the source's hover tooltip, written as `Name (data type, size)`. Sizes such as `15d` and `15d6` are copied as the source gives them.
- Enum and data-type links (`#enums-...` on the source page) point to the matching heading in [02-enums.md](02-enums.md) or the file that holds it.
- The source's language tabs (cURL, Python, Go, Node.js, C#, Java) are written one after another under each "Code Examples" heading.
- Icons (ticks, copy buttons, step numbers) are dropped. The OAuth step screenshots stay as links to the source images.
- Text, typos and sample values are kept as published. Things that look wrong on the source page and are left unchanged:
  - URL paths are not consistent. Most use `/1interactive/...`, but Get Balance uses `/interactive/user/balance`, Order History uses `/orders` with no prefix, TradeBook shows a raw IP (`http://160.30.125.86:10955/interactive/orders/trades`), and spread place/modify and GTT cancel use `//interactive/...`. Use the path your HostLookup returns.
  - GTT OrderBook is labelled `POST` in its heading and URL, but the rate-limit table lists `/orders/gttorderbook` as `GET`.
  - The Orders socket sample registers `@sio.on("ordert")`. The Socket Event enum in [02-enums.md](02-enums.md) names the event `order`, so `ordert` looks like a typo.
  - OAuth step 1 ("Navigate to the above URL for login & enter valid UserID") appears twice, once before and once after the password step.
  - `OCO` and `MTF` both have numeric code 32 in the OrderType enum.
- Things on the Market Data page left unchanged:
  - Most Market Data endpoints show only the URL, with no HTTP method. The method is in each heading, for example `Login (POST)`.
  - Subscribe and Unsubscribe both show `PUT` on the same `/instruments/subscription` URL. OpenAlgo's XTS adapters (for example `broker/compositedge/streaming/compositedge_websocket.py`) subscribe with `POST` and unsubscribe with `PUT`.
  - The Subscribe request table lists `MessageCode`, but the sample JSON sends `xtsMessageCode`. The Unsubscribe table uses `xtsMessageCode`.
  - The socket sample's path is `/apibinarymarketdata/socketio`, but the Connect text says to set the path to `/socket.io`. OpenAlgo's XTS adapters use `/apimarketdata/socket.io`.
  - The OHLC table calls `startTime` and `endTime` `Long`, but the format is `MMM DD YYYY HHMMSS` text, for example `Jan 27 2025 090000`.
