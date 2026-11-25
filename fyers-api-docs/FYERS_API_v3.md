# FYERS API v3 Documentation

> Generated from the live FYERS API v3 docs at https://fyers.in/api-docs/v3/ on 2026-11-25
> (186 pages, in the site's own page order) by `regenerate_fyers_api_v3.py`.
> Re-run that script to refresh this file; do not edit it by hand. Each section
> names its source page and the date Fyers last updated it. Only the code samples
> the server renders are kept (mostly Python and the JSON response).

## Contents

- Overview (`getting-started/`)
- Create an App (`getting-started/create-an-app/`)
- Authentication (`api/authentication/`)
- SDKs & Libraries (`getting-started/sdks-and-libraries/`)
- API Reference (`api/`)
- Single Order (`api/trading/order-placement/sync/single-order/`)
- Multi Order (`api/trading/order-placement/sync/multi-order/`)
- Multi-leg Order (`api/trading/order-placement/sync/multi-leg-order/`)
- Single Order (`api/trading/order-placement/async/single-order/`)
- Multi Order (`api/trading/order-placement/async/multi-order/`)
- Modify Single Order (`api/trading/order-management/sync/modify-single-order/`)
- Modify Multi Order (`api/trading/order-management/sync/modify-multi-order/`)
- Cancel Single Order (`api/trading/order-management/sync/cancel-single-order/`)
- Cancel Multi Order (`api/trading/order-management/sync/cancel-multi-order/`)
- Cancel Pending Orders (`api/trading/order-management/sync/cancel-pending-orders/`)
- Modify Single Order (`api/trading/order-management/async/modify-single-order/`)
- Modify Multi Order (`api/trading/order-management/async/modify-multi-order/`)
- Cancel Single Order (`api/trading/order-management/async/cancel-single-order/`)
- Cancel Multi Order (`api/trading/order-management/async/cancel-multi-order/`)
- GTT Single Order (`api/trading/order-placement/gtt-orders/gtt-single-order/`)
- GTT OCO Order (`api/trading/order-placement/gtt-orders/gtt-oco-order/`)
- Modify GTT Order (`api/trading/order-placement/gtt-orders/modify-gtt-order/`)
- Cancel GTT Order (`api/trading/order-placement/gtt-orders/cancel-gtt-order/`)
- Smart Limit Order (`api/trading/order-placement/smart-orders/smart-limit-order/`)
- Smart Trail (`api/trading/order-placement/smart-orders/smart-trail/`)
- Smart Step Order (`api/trading/order-placement/smart-orders/smart-step-order/`)
- Smart SIP (`api/trading/order-placement/smart-orders/smart-sip/`)
- Modify Smart Order (`api/trading/order-placement/smart-orders/modify-smart-order/`)
- Cancel Smart Order (`api/trading/order-placement/smart-orders/cancel-smart-order/`)
- Pause or Resume Smart Order (`api/trading/order-placement/smart-orders/pause-or-resume-smart-order/`)
- Exit Position (`api/trading/positions/exit-position/`)
- Exit Position by ID (`api/trading/positions/exit-position-by-id/`)
- Exit Positions by Filters (`api/trading/positions/exit-positions-by-filters/`)
- Convert Position (`api/trading/positions/convert-position/`)
- Set Stop Loss & Target (`api/trading/positions/set-stop-loss-and-target/`)
- Modify Stop Loss & Target (`api/trading/positions/modify-stop-loss-and-target/`)
- Cancel Stop Loss & Target (`api/trading/positions/cancel-stop-loss-and-target/`)
- Individual App (`getting-started/create-an-app/individual-app/`)
- Third-Party App (`getting-started/create-an-app/third-party-app/`)
- Plans & Limits (`getting-started/plans-and-limits/`)
- Individual App Authentication (`api/authentication/individual-app/`)
- Third-Party App Authentication (`api/authentication/third-party-app/`)
- API Error Codes (`api/appendix/common-api-error-codes/`)
- API Standards (`api/api-standards/`)
- Sample Code (`resources/sample-code/`)
- Postman Collection (`resources/postman-collection/`)
- Quickstart (`getting-started/quickstart/`)
- How-to Guides (`getting-started/guides/`)
- Trading (`api/trading/`)
- Market Data (`api/market-data/`)
- Reports (`api/reports/`)
- Account (`api/account/`)
- Market Information (`api/market-information/`)
- Margin Calculator (`api/calculators/`)
- Price Alerts (`api/price-alerts/`)
- WebSocket Overview (`api/websockets/websocket-overview/`)
- Appendix (`api/appendix/`)
- Troubleshooting (`getting-started/guides/troubleshooting-guide/`)
- Order Placement (`api/trading/order-placement/`)
- Sync (`api/trading/order-placement/sync/`)
- Order Placement Guide (`getting-started/guides/order-placement-guide/`)
- Order Types (`api/appendix/order-types/`)
- Order Sides (`api/appendix/order-sides/`)
- Product Types (`api/appendix/product-types/`)
- Symbol Master JSON (`api/market-information/symbol-master/symbol-master-json/`)
- Async (`api/trading/order-placement/async/`)
- General WebSocket - Connect (`api/websockets/general-socket/overview/general-socket-connect/`)
- Get Orders (`api/trading/order-book/get-orders/`)
- GTT Orders (`api/trading/order-placement/gtt-orders/`)
- Order Management (`api/trading/order-management/`)
- Sync (`api/trading/order-management/sync/`)
- Async (`api/trading/order-management/async/`)
- Order Book (`api/trading/order-book/`)
- GTT Order Book (`api/trading/order-placement/gtt-orders/gtt-order-book/`)
- Smart Orders (`api/trading/order-placement/smart-orders/`)
- Smart Order Book (`api/trading/order-placement/smart-orders/smart-order-book/`)
- Positions (`api/trading/positions/`)
- Get Positions (`api/trading/positions/get-positions/`)
- Position Sides (`api/appendix/position-sides/`)
- Webhooks / Postbacks (`api/trading/webhooks/`)
- Permission Templates (`getting-started/create-an-app/permission-templates/`)
- Authentication Flow (`api/authentication/individual-app/authentication-flow/`)
- Generate Auth Code (`api/authentication/individual-app/generate-auth-code/`)
- Validate Auth Code (Generate Access Token) (`api/authentication/individual-app/validate-auth-code/`)
- Best Practices (`api/authentication/individual-app/best-practices/`)
- Best Practices (`api/authentication/third-party-app/best-practices/`)
- OAuth 2.0 Flow (`api/authentication/third-party-app/oauth-2-0-flow/`)
- User Authorization (`api/authentication/third-party-app/user-authorization/`)
- Authorization Code (`api/authentication/third-party-app/authorization-code/`)
- Generate Access Token (`api/authentication/third-party-app/generate-access-token/`)
- Handle errors and rate limits (`getting-started/guides/handle-errors-rate-limits/`)
- Order Sources (`api/appendix/order-sources/`)
- Resources (`resources/`)
- Video Tutorials (`resources/video-tutorials/`)
- Profile (`api/account/profile/`)
- Place your first order (`getting-started/guides/place-your-first-order/`)
- Stream live market data (`getting-started/guides/stream-live-market-data/`)
- Monitor orders and positions in real time (`getting-started/guides/monitor-orders-and-positions/`)
- Work with historical market data (`getting-started/guides/work-with-historical-market-data/`)
- Manage positions, funds and risk (`getting-started/guides/manage-positions-funds-and-risk/`)
- Place basket and multi-leg orders safely (`getting-started/guides/place-basket-and-multi-leg-orders/`)
- Use Symbol Master to find instruments (`getting-started/guides/use-symbol-master/`)
- Trade Book (`api/trading/trade-book/`)
- Historical Data (`api/market-data/historical-data/`)
- Quotes (`api/market-data/quotes/`)
- Market Depth (`api/market-data/market-depth/`)
- Option Chain (`api/market-data/option-chain/`)
- Futures Chain (`api/market-data/futures-chain/`)
- Expired F&O Data (`api/market-data/expired-fo-data/`)
- Screeners (`api/market-data/screeners/`)
- Blacklisting (`api/trading/webhooks/blacklisting/`)
- Order History (`api/reports/order-history/`)
- Trade History (`api/reports/trade-history/`)
- Charges Report (`api/reports/charges-report/`)
- Realised P&L Report (`api/reports/realised-pnl-report/`)
- Tax P&L Report (`api/reports/tax-pnl-report/`)
- Ledger Report (`api/reports/ledger-report/`)
- Technical screeners (`api/market-data/screeners/technical-screeners/`)
- Funds (`api/account/funds/`)
- Holdings (`api/account/holdings/`)
- Logout (`api/account/logout/`)
- Kill Switch (`api/account/kill-switch/`)
- EDIS / DDPI (`api/account/edis-ddpi/`)
- Market Status (`api/market-information/market-status/`)
- Symbol Master (`api/market-information/symbol-master/`)
- EDIS Inquiry (`api/account/edis-ddpi/edis-inquiry/`)
- SPAN Margin Calculator (`api/calculators/span-margin-calculator/`)
- Multi-order Margin Calculator (`api/calculators/multi-order-margin-calculator/`)
- General WebSocket Overview (`api/websockets/general-socket/overview/`)
- Create Price Alert (`api/price-alerts/create-price-alert/`)
- Get Price Alerts (`api/price-alerts/get-price-alerts/`)
- Modify Price Alert (`api/price-alerts/modify-price-alert/`)
- Delete Price Alert (`api/price-alerts/delete-price-alert/`)
- Enable / Disable Price Alert (`api/price-alerts/enable-or-disable-price-alert/`)
- WebSocket Overview (`api/websockets/`)
- Data Socket Overview (`api/websockets/data-socket/overview/`)
- Tick-by-Tick (TBT) Socket Overview (`api/websockets/tick-by-tick-socket/overview/`)
- Data Socket Overview (`api/websockets/data-socket/`)
- Fytoken (`api/appendix/fytoken/`)
- Exchanges (`api/appendix/exchanges/`)
- Segments (`api/appendix/segments/`)
- Exchange-Segment Mapping (`api/appendix/available-exchange-segment-combinations/`)
- Instrument Types (`api/appendix/instrument-types/`)
- Symbol Format (`api/appendix/symbology-format/`)
- Symbol Values (`api/appendix/symbology-possible-values/`)
- Order Status (`api/appendix/order-status/`)
- Holding Types (`api/appendix/holding-types/`)
- General Socket - General Events (`api/websockets/general-socket/general-socket-general-events/`)
- Symbol Master File (`api/market-information/symbol-master/symbol-master-file/`)
- General WebSocket Overview (`api/websockets/general-socket/`)
- General WebSocket - Subscribe (`api/websockets/general-socket/overview/general-socket-subscribe/`)
- Get Order by Order ID (`api/trading/order-book/get-order-by-order-id/`)
- Get Orders by Order Tag (`api/trading/order-book/get-orders-by-order-tag/`)
- Get Trades by Order Tag (`api/trading/trade-book/get-trades-by-order-tag/`)
- Create Webhook (`api/trading/webhooks/create-webhook/`)
- Activate App (`api/trading/webhooks/activate-app/`)
- Webhook Response (`api/trading/webhooks/webhook-response/`)
- Learn Algo Trading with FYERS (`learning/`)
- Change Log (`changelog/`)
- Data Socket - Connect and Subscribe (`api/websockets/data-socket/overview/data-socket-connect-and-subscribe/`)
- Data Socket - Symbol Update (`api/websockets/data-socket/data-socket-symbol-update/`)
- Data Socket - Market Depth Update (`api/websockets/data-socket/data-socket-depth-update/`)
- Data Socket - Unsubscribe and Connection Management (`api/websockets/data-socket/overview/data-socket-unsubscribe-and-connection-management/`)
- Data Socket - Advanced Configuration (`api/websockets/data-socket/overview/advanced-configuration/`)
- Get Trades (`api/trading/trade-book/get-trades/`)
- General WebSocket - Unsubscribe (`api/websockets/general-socket/overview/general-socket-unsubscribe/`)
- General WebSocket - Ping and Mandatory Fields (`api/websockets/general-socket/overview/ping-method/`)
- General Socket - Order Events (`api/websockets/general-socket/general-socket-order-events/`)
- General Socket - Trade Events (`api/websockets/general-socket/general-socket-trade-events/`)
- General Socket - Position Events (`api/websockets/general-socket/general-socket-position-events/`)
- Get Expiry Dates (`api/market-data/expired-fo-data/get-expiry-dates/`)
- Get Expired Contracts (`api/market-data/expired-fo-data/get-expired-contracts/`)
- Get Expired F&O Data (`api/market-data/expired-fo-data/get-expired-fo-data/`)
- Configuration (`api/market-data/screeners/config/`)
- Standard screeners (`api/market-data/screeners/standard-screeners/`)
- Candlestick screeners (`api/market-data/screeners/candlestick-screeners/`)
- Activate Kill Switch (`api/account/kill-switch/activate-kill-switch/`)
- Kill Switch Status (`api/account/kill-switch/kill-switch-status/`)
- EDIS Details (`api/account/edis-ddpi/edis-details/`)
- TPIN Generation (`api/account/edis-ddpi/tpin-generation/`)
- Verify DIS (`api/account/edis-ddpi/verify-dis/`)
- Data Socket - Indices Update (`api/websockets/data-socket/data-socket-indices-update/`)
- Data Socket - Lite Mode (`api/websockets/data-socket/data-socket-lite-mode/`)
- Tick-by-Tick (TBT) Socket Overview (`api/websockets/tick-by-tick-socket/`)
- Tick-by-Tick (TBT) Socket - Connection (50 Market Depth) (`api/websockets/tick-by-tick-socket/overview/tbt-websocket-connection/`)
- Tick-by-Tick (TBT) Socket - Channels and Message Types (`api/websockets/tick-by-tick-socket/overview/concept-of-channels/`)

## Overview

*Source: https://fyers.in/api-docs/v3/getting-started/*

Start with FYERS APIs in the way that suits your use case. Create an app, use the App ID and App Secret, authenticate, and call REST APIs or official SDKs directly. You can also use FYERS MCP, FYERS GPT or FYERS AI Skills to understand requirements, generate implementation guidance and create API-based trading systems with AI assistance.

### Ways to get started

Work directly with APIs

[STEP 01Create AppCreate an API app in the FYERS API dashboard.](https://fyers.in/api-docs/v3/getting-started/create-an-app/)[STEP 02AuthenticateUse the App ID and App Secret to complete authentication.](https://fyers.in/api-docs/v3/api/authentication/)[STEP 03Choose SDKChoose REST or an official SDK.](https://fyers.in/api-docs/v3/getting-started/sdks-and-libraries/)[STEP 04API ReferenceUse API Reference for endpoint-level implementation details.](https://fyers.in/api-docs/v3/api/)

### Types of APIs

FYERS provides 3 core categories of APIs tailored for order execution, account management, and real-time market data.

Transaction

Execute, modify, and manage orders and positions.

Order placement

* [Single Order](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/)
* [Multi Order](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-order/)
* [Multi-leg Order](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-leg-order/)
* [Single Order (Async)](https://fyers.in/api-docs/v3/api/trading/order-placement/async/single-order/)
* [Multi Order (Async)](https://fyers.in/api-docs/v3/api/trading/order-placement/async/multi-order/)

Order management

* [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/)
* [Modify Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-multi-order/)
* [Cancel Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/)
* [Cancel Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-multi-order/)
* [Cancel Pending Orders](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-pending-orders/)
* [Modify Single Order (Async)](https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-single-order/)
* [Modify Multi Order (Async)](https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-multi-order/)
* [Cancel Single Order (Async)](https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-single-order/)
* [Cancel Multi Order (Async)](https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-multi-order/)

GTT orders

* [GTT Single Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-single-order/)
* [GTT OCO Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-oco-order/)
* [Modify GTT Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/modify-gtt-order/)
* [Cancel GTT Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/cancel-gtt-order/)

Smart orders

* [Smart Limit Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-limit-order/)
* [Smart Trail](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-trail/)
* [Smart Step Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-step-order/)
* [Smart SIP](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-sip/)
* [Modify Smart Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/modify-smart-order/)
* [Cancel Smart Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/cancel-smart-order/)
* [Pause Smart Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/pause-or-resume-smart-order/)

Positions

* [Exit Position](https://fyers.in/api-docs/v3/api/trading/positions/exit-position/)
* [Exit Position by ID](https://fyers.in/api-docs/v3/api/trading/positions/exit-position-by-id/)
* [Exit Positions by Filters](https://fyers.in/api-docs/v3/api/trading/positions/exit-positions-by-filters/)
* [Convert Position](https://fyers.in/api-docs/v3/api/trading/positions/convert-position/)
* [Set Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/set-stop-loss-and-target/)
* [Modify Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/modify-stop-loss-and-target/)
* [Cancel Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/cancel-stop-loss-and-target/)

## Create an App

*Source: https://fyers.in/api-docs/v3/getting-started/create-an-app/ (last updated 2026-10-14)*

**SEBI update:**

SEBI’s retail algo trading regulations are now in effect. To check the changes related to the algo trading regulations, refer to the [SEBI algo trading rules](https://fyers.in/community/t/sebis-new-algo-trading-rules-kick-in-on-april-1-here-is-what-changes-for-you/12267).

### App types

FYERS supports two types of API apps. Choose the one that matches how your application will be used.

| App type | Who it is for | How to create it |
| --- | --- | --- |
| [Individual App](https://fyers.in/api-docs/v3/getting-started/create-an-app/individual-app/) | Your own trading account. Use it to build tools, strategies, and integrations for yourself. Comes as one trading app (order placement, static IP required) and any number of non-trading apps (data only). See [Trading app and non-trading app](https://fyers.in/api-docs/v3/getting-started/create-an-app/individual-app/#trading-app-and-non-trading-app). | Activate your trading app or create non-trading apps from the FYERS API dashboard. |
| [Third-Party App](https://fyers.in/api-docs/v3/getting-started/create-an-app/third-party-app/) | Platform providers whose applications let FYERS clients log in and use their functionality. | Get in touch with us at [[email protected]](/cdn-cgi/l/email-protection#7514051c58060005051a070135130c1007065b1c1b) to create a common app. |

## Authentication

*Source: https://fyers.in/api-docs/v3/api/authentication/ (last updated 2026-10-14)*

This section explains how to log in to the FYERS API and get the `access_token` that every later API request must carry.

Use an [individual app](https://fyers.in/api-docs/v3/api/authentication/individual-app/) to call the APIs for your own account. Use a [third-party app](https://fyers.in/api-docs/v3/api/authentication/third-party-app/) when you build a platform where other FYERS clients log in with their own credentials.

* Access tokens expire daily at 6:30 AM. Generate a new token after 6:30 AM for it to remain valid throughout the day.
* Send `app_id:access_token` in the HTTP `Authorization` header on every request after login. See [API Standards](https://fyers.in/api-docs/v3/api/api-standards/#authorization-header).
* `redirect_uri` must be the same URL provided at app creation, and should be in your control because the auth token is sensitive.
* Expired or invalid tokens return error code -8, -15, -16 or -17. See [API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/).

| Endpoint | Method | Description |
| --- | --- | --- |
| [Individual App Authentication](https://fyers.in/api-docs/v3/api/authentication/individual-app/) | — | This section explains how to authenticate your own FYERS account with an individual app and get an access token for all later requests. |
| [Third-Party App Authentication](https://fyers.in/api-docs/v3/api/authentication/third-party-app/) | — | This section explains how to let FYERS clients log in to your platform with their own credentials. Third-party apps are created by platform providers so that FYERS clients can use their applications. |

## SDKs & Libraries

*Source: https://fyers.in/api-docs/v3/getting-started/sdks-and-libraries/ (last updated 2026-10-14)*

Choose REST for direct HTTP integration or use an official SDK for language-native development. To make it easier to use the FYERS API in different programming languages, we provide dedicated libraries/packages that handle the API calls for you. These libraries/packages abstract away the complexities of raw HTTP calls, allowing you to focus on integrating the API seamlessly into your applications. The table below lists each SDK with its supported versions, official package link and tutorial playlist.

| SDK | Supported versions | Official link | Tutorial link |
| --- | --- | --- | --- |
| REST | Up to latest | [Current API documentation](https://fyers.in/api-docs/v3/api/) | [Watch tutorial](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60) |
| Python SDK | Python 3.8 to latest | [PyPI: fyers-apiv3](https://pypi.org/project/fyers-apiv3/) | [Watch tutorial](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw) |
| Node.js SDK | Node.js 12 to latest | [npm: fyers-api-v3](https://www.npmjs.com/package/fyers-api-v3) | [Watch tutorial](https://www.youtube.com/playlist?list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda) |
| Web JavaScript SDK | Node.js 16 to latest | [npm: fyers-web-sdk-v3](https://www.npmjs.com/package/fyers-web-sdk-v3) | [Watch tutorial](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60) |
| C# SDK | .NET 8.0.4 to latest | [NuGet: fyers-api-v3](https://www.nuget.org/packages/fyers-api-v3) | [Watch tutorial](https://www.youtube.com/playlist?list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla) |
| Java SDK | Java 8 to latest | [GitHub: fyers-java-sdk](https://github.com/FyersDev/fyers-java-sdk) | [Watch tutorial](https://www.youtube.com/playlist?list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6) |
| Go SDK | Go 1.18 to latest | [GitHub: fyers-go-sdk](https://github.com/FyersDev/fyers-go-sdk) | Coming soon |
| C SDK | C11 to latest | [GitHub: fyers-c-sdk](https://github.com/FyersDev/fyers-c-sdk) | Coming soon |

### Python SDK: FyersModel class

`FyersModel` needs `client_id` and your access token (passed as `token`) for authentication. It runs synchronously by default (`is_async=False`). You can write logs to a file with `log_path`. The default log level is `ERROR`; set it to `DEBUG` for more detailed logs.

| Argument | Data Type | Description |
| --- | --- | --- |
| `client_id` | string | For authentication. |
| `token` | string | Your access token, for authentication (pass as `token=access_token`). |
| `is_async` (optional) | boolean | Defaults to `False` for synchronous flow. Set to `True` for asynchronous flow. |
| `log_path` (optional) | string | File path where logs are stored. |
| `log_level` (optional) | string | Defaults to `ERROR`. Set to `DEBUG` for more detailed logs. |

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(
    client_id=client_id,
    token=access_token,
    is_async=False,
    log_path="",
)

response = fyers.get_profile()
print(response)
```

### Web SDK CDN

| Version | URL |
| --- | --- |
| 1.3.0 | <https://cdn.fyers.in/js/sdk/1.3.0/fyers-web-sdk-v3/index.min.js> |
| 1.2.1 | <https://cdn.fyers.in/js/sdk/1.2.1/fyers-web-sdk-v3/index.min.js> |
| 1.2.0 | <https://cdn.fyers.in/js/sdk/1.2.0/fyers-web-sdk-v3/index.min.js> |
| 1.1.0 | <https://cdn.fyers.in/js/sdk/1.1.0/fyers-web-sdk-v3/index.min.js> |
| 1.0.0 | <https://cdn.fyers.in/js/sdk/1.0.0/fyers-web-sdk-v3/index.min.js> |

Sample scripts: [fyers-api-sample-code](https://github.com/FyersDev/fyers-api-sample-code). See also [Sample Code](https://fyers.in/api-docs/v3/resources/sample-code/) and the [Postman Collection](https://fyers.in/api-docs/v3/resources/postman-collection/).

## API Reference

*Source: https://fyers.in/api-docs/v3/api/ (last updated 2026-10-14)*

API Reference is organised by API segment so you can move directly to the operation, resource or socket you need. Each page contains the purpose, prerequisites, endpoint area, example request attributes, example code, example response attributes, response example, errors and related documentation.

### API Reference sections

| Section | What it contains |
| --- | --- |
| [API Standards](https://fyers.in/api-docs/v3/api/api-standards/) | Shared formats, authentication headers, timestamps, errors, and retry behaviour. |
| [Authentication](https://fyers.in/api-docs/v3/api/authentication/) | Authorization-code and access-token operations for individual and third-party apps. |
| [Trading](https://fyers.in/api-docs/v3/api/trading/) | Order placement and management, order book, trade book, positions, and webhooks. |
| [Market Data](https://fyers.in/api-docs/v3/api/market-data/) | Quotes, historical candles, depth, option/futures chains, expired F&O data and screeners. |
| [Reports](https://fyers.in/api-docs/v3/api/reports/) | Order, trade, charges, P&L, tax and ledger reporting resources. |
| [Account](https://fyers.in/api-docs/v3/api/account/) | Profile, funds, holdings, logout, and EDIS / DDPI workflows. |
| [Market Information](https://fyers.in/api-docs/v3/api/market-information/) | Market status and Symbol Master files. |
| [Margin Calculator](https://fyers.in/api-docs/v3/api/calculators/) | SPAN and multi-order margin estimation. |
| [Price Alerts](https://fyers.in/api-docs/v3/api/price-alerts/) | Create, read, modify, delete, and enable/disable price alerts. |
| [WebSockets](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/) | Data Socket (including Tick By Tick depth) and General Socket lifecycle and events. |
| [Appendix](https://fyers.in/api-docs/v3/api/appendix/) | Symbol Master, symbology resources, and common API error codes. |

## Single Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/ (last updated 2026-10-14)*

This API allows you to place an order to any supported exchange.

USE CASE

Place a buy or sell order for a specific instrument.

Details

* This allows the user to place an order to any exchange via Fyers
* Placing orders needs an app with the Order Placement permission.
* Placing, modifying and cancelling orders together must stay within 10 orders per second. Requests beyond this limit are rejected.
* Every price input (`limitPrice`, `stopPrice`, `stopLoss`, `takeProfit`) must be a multiple of the symbol tick size, which is available in the symbol master.
* Quantity must be in multiples of 1 for equities, currency and commodity derivatives, and in multiples of the exchange lot size for equity derivatives.
* For a stop order, `stopPrice` must not be above LTP for a sell or below LTP for a buy. For a stop-limit order it must also be below `limitPrice` for a buy and above it for a sell.
* `orderTag` must be 1 to 30 letters or digits, with no spaces or special characters, and cannot be your client ID or `Untagged`.
* Set `isSliceOrder` to `true` to split a quantity above the freeze limit into separate orders, each with its own order id. Allowed only for NSE CM, NFO and BFO, with at most 10 slices per request.
* If the response code is 201, the order request was made but not acknowledged. Check the order book before placing the order again.
* To add Take Profit and Stop Loss (TPSL) to the order, see [Creating TPSL](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#creating-tpsl) in the Order Placement Guide.
* To change or cancel this order, use [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/) or [Cancel Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/).
* For order types, product types, validations and sync vs async behaviour, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).
* When order rate limiting is triggered, the API returns `429 Too Many Requests`.
* Retry timing is provided through response headers, not in the response body.
* `Retry-After` — Wait time before retrying, in seconds
* `X-Retry-After-Ms` — Wait time before retrying, in milliseconds
* Use the retry interval returned in the response headers before sending another order request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Eg: NSE:SBIN-EQ |
| `qty`\* | int | The quantity should be in multiples of lot size for derivatives. |
| `type`\* | int | * 1 => Limit Order * 2 => Market Order (MPP: Market Price Protection ) * 3 => Stop Order (SL-M, MPP: Market Price Protection ) * 4 => Stoplimit Order (SL-L) * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-types/) |
| `side`\* | int | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `productType`\* | string | * CNC => For equity only * INTRADAY => Applicable for all segments. * MARGIN => Applicable only for derivatives * MTF => Approved Symbols Only * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `limitPrice`\* | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN (required for Limit and Stoplimit orders). |
| `stopPrice`\* | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN (required for Stop and Stoplimit orders). |
| `disclosedQty`\* | int | * Default => 0 * Allowed only for Equity |
| `validity`\* | string | * IOC => Immediate or Cancel * DAY => Valid till the end of the day |
| `offlineOrder`\* | boolean | * False => When market is open * True => When placing AMO order |
| `stopLoss` | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN. |
| `takeProfit` | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN. |
| `orderTag` | string | (Optional) Tag you want to assign to the specific order |
| `isSliceOrder` | boolean | * False => The full quantity is placed as one single order. * True => The quantity is placed in multiple smaller orders if the total quantity is more than the [freeze quantity](https://support.fyers.in/portal/en/kb/articles/what-are-price-bands-and-freeze-quantities#Freeze_quantity). |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | * This is the code to identify specific responses * If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| `message` | string | * Message to clarify the request status. * Eg: Order submitted successfully. * Your Order Ref. No.119062829763 |
| `id` | string | * The order number of the placed order. * Eg: 119031547242 |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "symbol":"NSE:IDEA-EQ",
    "qty":1,
    "type":1,
    "side":1,
    "productType":"INTRADAY",
    "limitPrice":0,
    "stopPrice":0,
    "validity":"DAY",
    "disclosedQty":0,
    "offlineOrder":False,
    "orderTag":"tag1",
    "isSliceOrder":False
}
response = fyers.place_order(data=data)
print(response)
```

```
{
    "s": "ok",
    "code": 1101,
    "message": "Order submitted successfully. Your Order Ref. No.808058117761",
    "id":"808058117761"
  }
```

VIDEO LEARNING

### Video learning

[How to place your order? (REST and cURL)REST and cURL · 12:03](https://www.youtube.com/watch?v=VIdhpmqqbiU&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[How to place stock orders? (Python)Python · 20:01](https://www.youtube.com/watch?v=0jbtkJP2RpY&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Order placement guide (Node.js)Node.js · 15:26](https://www.youtube.com/watch?v=gzmzBAhIB84&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Order placement guide (C#)C# · 13:30](https://www.youtube.com/watch?v=JwRkEg7r33A&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Order placement guide (Java)Java · 11:26](https://www.youtube.com/watch?v=Q64uoAMAdcU&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Multi Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-order/ (last updated 2026-10-14)*

This API allows you to place multiple orders in a single request.

USE CASE

Place multiple buy or sell orders in a single request.

Details

* You can place upto 10 orders simultaneously via the API.
* While Placing Multi orders you need to pass an ARRAY containing the orders request attributes
* Send an array of up to 10 orders. Each order uses the same attributes as the Single Order API.
* Placing orders needs an app with the Order Placement permission.
* Placing, modifying and cancelling orders together must stay within 10 orders per second. Requests beyond this limit are rejected.
* Price inputs must be multiples of the symbol tick size, and quantity must follow the lot-size rules, for every order in the array.
* `orderTag`, when passed, must be 1 to 30 letters or digits and cannot be your client ID or `Untagged`.
* The response has one entry per order, each with its own `statusCode`, `code`, `message` and order `id`. Check every entry, not only the top-level status.
* To get hedge margin benefits on related orders, use this API rather than the Multi-leg Order API, which does not support them.
* To add Take Profit and Stop Loss (TPSL) to an order, see [Creating TPSL](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#creating-tpsl) in the Order Placement Guide.
* To change or cancel these orders, use [Modify Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-multi-order/) or [Cancel Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-multi-order/).
* For order types, product types, validations and sync vs async behaviour, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).
* When order rate limiting is triggered, the API returns `429 Too Many Requests`.
* Retry timing is provided through response headers, not in the response body.
* `Retry-After` — Wait time before retrying, in seconds
* `X-Retry-After-Ms` — Wait time before retrying, in milliseconds
* Use the retry interval returned in the response headers before sending another order request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Eg: NSE:SBIN-EQ |
| `qty`\* | int | The quantity should be in multiples of lot size for derivatives. |
| `type`\* | int | * 1 => Limit Order * 2 => Market Order (MPP: Market Price Protection ) * 3 => Stop Order (SL-M, MPP: Market Price Protection ) * 4 => Stoplimit Order (SL-L) * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-types/) |
| `side`\* | int | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `productType`\* | string | * CNC => For equity only * INTRADAY => Applicable for all segments. * MARGIN => Applicable only for derivatives * MTF => Approved Symbols Only * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `limitPrice`\* | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN (required for Limit and Stoplimit orders). |
| `stopPrice`\* | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN (required for Stop and Stoplimit orders). |
| `disclosedQty`\* | int | * Default => 0 * Allowed only for Equity |
| `validity`\* | string | * IOC => Immediate or Cancel * DAY => Valid till the end of the day |
| `offlineOrder`\* | boolean | * False => When market is open * True => When placing AMO order |
| `stopLoss` | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN. |
| `takeProfit` | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Overall status of the batch request: `ok` or `error`. |
| `code` | int | Overall response code for the batch request, e.g. `200`. |
| `message` | string | Overall message for the batch request (empty string on success). |
| `data` | array | Array of per-order results, one entry for each order submitted in the request array, in the same order. |
| `data[].statusCode` | int | HTTP-style status code for this individual order within the batch, e.g. `200` on success or `400` on failure. |
| `data[].statusDescription` | string | HTTP status description for this individual order, e.g. `HTTP OK` or `400 Bad Request`. |
| `data[].body` | object | Result for this order. It has the same fields as the Single Order response. |
| `data[].body.s` | string | ok / error |
| `data[].body.code` | int | * This is the code to identify specific responses * If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| `data[].body.message` | string | * Message to clarify the request status. * Eg: Order submitted successfully. * Your Order Ref. No.119062829763 |
| `data[].body.id` | string | * The order number of the placed order. * Eg: 119031547242 |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = [{
    "symbol":"NSE:SBIN-EQ",
    "qty":1,
    "type":1,
    "side":1,
    "productType":"INTRADAY",
    "limitPrice":0,
    "stopPrice":0,
    "validity":"DAY",
    "disclosedQty":0,
    "offlineOrder":False,
},
{
    "symbol":"NSE:IDEA-EQ",
    "qty":1,
    "type":1,
    "side":1,
    "productType":"INTRADAY",
    "limitPrice":0,
    "stopPrice":0,
    "validity":"DAY",
    "disclosedQty":0,
    "offlineOrder":False,
},{
    "symbol":"NSE:SBIN-EQ",
    "qty":1,
    "type":1,
    "side":1,
    "productType":"INTRADAY",
    "limitPrice":0,
    "stopPrice":0,
    "validity":"DAY",
    "disclosedQty":0,
    "offlineOrder":False,
},
{
    "symbol":"NSE:IDEA-EQ",
    "qty":1,
    "type":1,
    "side":1,
    "productType":"INTRADAY",
    "limitPrice":0,
    "stopPrice":0,
    "validity":"DAY",
    "disclosedQty":0,
    "offlineOrder":False,
}]

response = fyers.place_basket_orders(data=data)
print(response)
```

```
{
        "s":"ok",
        "code":200,
        "message":"",
        "data":[{"statusCode":200,
              "body":{
                        "s":"ok",
                        "code":1101,
                        "message":"Order submitted successfully. Your Order Ref. No.52104097619",
                        "id":"52104097619"
                    },
        "statusDescription":"HTTP OK"
        },
        {
        "statusCode":200,
        "body":{
        "s":"ok",
        "code":1101,
        "message":"Order submitted successfully. Your Order Ref. No.52104097620",
        "id":"52104097620"
        },
          "statusDescription":"HTTP OK"
        },
        {
        "statusCode":200,
        "body":{
        "s":"ok",
        "code":1101,
        "message":"Order submitted successfully. Your Order Ref. No.52104097621",
        "id":"52104097621"
        },
        "statusDescription":"HTTP OK"
        },
        {
        "statusCode":400,
        "body":{
          "s":"error",
          "code":-392,
          "message":"Price should be in multiples of tick size.",
          "id":""
          },
        "statusDescription":"400 Bad Request"
    }]
 }
```

VIDEO LEARNING

### Video learning

[Place multiple orders at once (REST and cURL)REST and cURL · 5:15](https://www.youtube.com/watch?v=ou7lStADcBs&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)

Go and C video tutorials: coming soon.

## Multi-leg Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-leg-order/ (last updated 2026-10-14)*

This API allows you to place a two-leg or three-leg NSE futures and options order as a single order.

USE CASE

Trade a multi-leg strategy as one order instead of sending each leg separately.

Note

As per exchange mandate, while selecting symbols please check the `stream` key in the [Symbol Master JSON](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-json/) file to ensure both legs belong to the same stream.

* The Multi Leg Order API currently does not support hedge margin benefits. Please use the [Multi Order API](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-order/) to avail of these benefits.

Details

* This allows the user to place an MultiLeg order to NSE via Fyers.
* Placing orders needs an app with the Order Placement permission.
* Only NSE futures and options symbols (NFO) are allowed, and all legs must be on the same underlying. Banned F&O symbols are rejected.
* Set `orderType` to `2L` for two legs or `3L` for three legs, and name the legs `leg1`, `leg2` and `leg3`.
* Each leg must be a limit order (`type` 1). `validity` must be `IOC`, and `productType` must be `INTRADAY` or `MARGIN`.
* The same symbol cannot be used in two legs, and each leg quantity must be a multiple of the lot size.
* The order-per-second limit of 10 orders, covering placing, modifying and cancelling, applies here too.
* Set `offlineOrder` to `true` to place the order as an AMO order, and `false` when the market is open.
* For order types, product types, validations and sync vs async behaviour, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).
* When order rate limiting is triggered, the API returns `429 Too Many Requests`.
* Retry timing is provided through response headers, not in the response body.
* `Retry-After` — Wait time before retrying, in seconds
* `X-Retry-After-Ms` — Wait time before retrying, in milliseconds
* Use the retry interval returned in the response headers before sending another order request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `orderTag` | string | (Optional) Tag you want to assign to the specific order |
| `productType`\* | string | * INTRADAY => Applicable for NFO segments. * MARGIN => Applicable for NFO segments. |
| `offlineOrder`\* | boolean | * False => When market is open * True => When placing AMO order. |
| `orderType`\* | string | * 3L => Applicable for 3 leg order. * 2L => Applicable for 2 leg order. |
| `validity`\* | string | IOC => Immediate or Cancel |
| `legs`\* | json | It represents multiple trading legs in a multi-leg order. Each leg within the legs object corresponds to a specific trading instrument and order details. Each leg is identified by a unique key (leg1, leg2, leg3 ) |

### Leg attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Eg: NSE:SBIN24JUNFUT |
| `qty`\* | int | The quantity should be in multiples of lot size for derivatives. |
| `side`\* | int | * 1 => Buy * -1 => Sell |
| `type`\* | int | * 1 => Limit Order |
| `limitPrice`\* | float | Provide valid price for Limit orders |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | * This is the code to identify specific responses * If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| `message` | string | * Message to clarify the request status. * Eg: Order submitted successfully. * Your Order Ref. No.119062829763 |
| `id` | string | * The order number of the placed order. * Eg: 119031547242 |

### Input Validations

| Error Message | Description |
| --- | --- |
| `The input symbol is invalid.` | Input symbol ticker is not found in the exchange data |
| `Only NFO symbols are allowed` | Options and Future symbols listed in NSE are allowed. |
| `The input symbol is banned for FNO trading.` | The input symbol is banned for trading by the exchange. |
| `All symbols must be related to the same underlying symbol.` | All symbols must be related to same symbol |
| `Quantity should be multiples of the lot size.` | Input qty(Quantity) should be multiples of minimum lot size of that symbol |
| `You cannot add same symbol for two legs.` | Input data should not have same symbol in more than one leg. |
| `Group combination not found` | Input Symbols do not belong to same [stream group.](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-json/) |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "orderTag": "tag1",
    "productType": "MARGIN",
    "offlineOrder": False,
    "orderType": "3L",
    "validity": "IOC",
    "legs": {
        "leg1": {
          "symbol": "NSE:SBIN24JUNFUT",
          "qty": 750,
          "side": 1,
          "type": 1,
          "limitPrice": 800
        },
        "leg2": {
            "symbol": "NSE:SBIN24JULFUT",
            "qty": 750,
            "side": 1,
            "type": 1,
            "limitPrice": 800
        },
        "leg3": {
            "symbol": "NSE:SBIN24JUN900CE",
            "qty": 750,
            "side": 1,
            "type": 1,
            "limitPrice": 3
        }
    }
}
response = fyers.place_multileg_order(data=data)
print(response)
```

```
{
    "s": "ok",
    "code": 1101,
    "message": "Successfully placed order",
    "id":"808058117761"
  }
```

## Single Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/async/single-order/ (last updated 2026-10-14)*

This API allows you to place an order without waiting for the exchange response.

USE CASE

Place orders in quick bursts and get an immediate acknowledgement, then track each one on the General WebSocket or order book.

Note

`stopLoss` and `takeProfit` are not supported with async order placement.

Details

* Same JSON attributes as synchronous **Place order**.
* For `/sync` vs `/async` behavior, queuing, 10 OPS, `id_fyers` and hosts, see the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#overview---sync-and-async-apis).
* Placing orders needs an app with the Order Placement permission. The request attributes are the same as the sync Single Order API.
* An HTTP 200 response only means the request was queued. It does not mean the order was placed or accepted by the exchange.
* The queue sends requests on at most 10 orders per second.
* The response returns `id_fyers` and not `id`. Match `id_fyers` with the order updates on the General WebSocket, which carry both identifiers, or with the order book.
* Price inputs must still be multiples of the symbol tick size, and quantity must follow the lot-size rules.
* To change or cancel this order, use [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-single-order/) or [Cancel Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-single-order/).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - Immediate (async)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `ok` / `error` |
| `code` | int | Response code (same semantics family as sync where applicable) |
| `message` | string | Status message |
| `id_fyers` | string | Fyers queue/async operation id (use for WebSocket and GET correlation). **`id` is not returned here.** |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization: app_id:access_token" -H "Content-Type: application/json" -X POST -d '{
  "symbol":"NSE:SBIN-EQ",
  "qty":1,
  "type":1,
  "side":1,
  "productType":"CNC",
  "limitPrice":0,
  "stopPrice":0,
  "disclosedQty":0,
  "validity":"DAY",
  "offlineOrder":true,
  "stopLoss":0,
  "takeProfit":0
}' https://api-t1.fyers.in/api/v3/orders/async
```

```
{
  "s": "ok",
  "code": 1101,
  "message": "Order queued successfully.",
  "id_fyers": "c6697c04-d9ab-4a7c-a6f4-b0cc4ca698f6"
}
```

## Multi Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/async/multi-order/ (last updated 2026-10-14)*

This API allows you to place multiple orders in a single request without waiting for the exchange response.

USE CASE

Open several positions together in one request and follow each order on the General WebSocket or order book.

Note

* Each order in the array is queued and processed respecting 10 orders per second.
* The HTTP response returns `id_fyers`.
* Exchange `id` and terminal status come from the [General WebSocket](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-connect/) and [Order Book](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/).

`stopLoss` and `takeProfit` are not supported with async order placement.

Details

* Body is an **array** of order objects (same fields as sync multi-order).
* For `/sync` vs `/async` behavior, queuing, 10 OPS, `id_fyers` and hosts, see the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#overview---sync-and-async-apis).
* Placing orders needs an app with the Order Placement permission.
* Send an array of order objects with the same fields as the sync Multi Order API.
* An HTTP 200 response only means the orders were queued. It does not mean they were placed or accepted by the exchange.
* Price inputs must be multiples of the symbol tick size, and quantity must follow the lot-size rules, for every order.
* To change or cancel these orders, use [Modify Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-multi-order/) or [Cancel Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-multi-order/).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Eg: NSE:SBIN-EQ |
| `qty`\* | int | The quantity should be in multiples of lot size for derivatives. |
| `type`\* | int | * 1 => Limit Order * 2 => Market Order (MPP: Market Price Protection ) * 3 => Stop Order (SL-M, MPP: Market Price Protection ) * 4 => Stoplimit Order (SL-L) * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-types/) |
| `side`\* | int | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `productType`\* | string | * CNC => For equity only * INTRADAY => Applicable for all segments. * MARGIN => Applicable only for derivatives * MTF => Approved Symbols Only * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `limitPrice`\* | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN (required for Limit and Stoplimit orders). |
| `stopPrice`\* | float | * Default => 0 * Provide valid price for INTRADAY, CNC, MTF, or MARGIN (required for Stop and Stoplimit orders). |
| `disclosedQty`\* | int | * Default => 0 * Allowed only for Equity |
| `validity`\* | string | * IOC => Immediate or Cancel * DAY => Valid till the end of the day |
| `offlineOrder`\* | boolean | * False => When market is open * True => When placing AMO order |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization: app_id:access_token" -H "Content-Type: application/json" -X POST -d '[
  {"symbol":"NSE:SBIN-EQ","qty":1,"type":1,"side":1,"productType":"INTRADAY","limitPrice":190,"stopPrice":0,"disclosedQty":0,"validity":"DAY","offlineOrder":true,"stopLoss":0,"takeProfit":0},
  {"symbol":"NSE:SBIN-EQ","qty":1,"type":1,"side":1,"productType":"CNC","limitPrice":0,"stopPrice":0,"disclosedQty":0,"validity":"DAY","offlineOrder":true,"stopLoss":0,"takeProfit":0}
]' https://api-t1.fyers.in/api/v3/multi-order/async
```

## Modify Single Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/ (last updated 2026-10-14)*

This API allows you to modify an existing order.

USE CASE

Change the price, quantity or trigger price of an order that is still pending.

Details

* This allows the user to modify a pending order. User can provide parameters which needs to be modified. In case a particular parameter has not been provided, the original value will be considered.
* Modifying orders needs an app with the Order Placement permission.
* Only pending orders can be modified. The `id` of the order and its `type` are always required.
* Prices must be multiples of the symbol tick size, and quantity must follow the lot-size rules.
* Modify requests count towards the limit of 10 orders per second shared with placing and cancelling. Requests beyond it are rejected.
* To change the Take Profit or Stop Loss of a pending order, send the new `takeProfit` or `stopLoss`. To cancel only a linked Take Profit or Stop Loss, pass `null` for it; pass both as `null` to cancel both. See [Modifying TPSL](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#modifying-tpsl) in the Order Placement Guide.
* If the response code is 201, the request was made but not acknowledged. Check the order book before sending it again.
* For order types, product types, validations and sync vs async behaviour, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).
* When order rate limiting is triggered, the API returns `429 Too Many Requests`.
* Retry timing is provided through response headers, not in the response body.
* `Retry-After` — Wait time before retrying, in seconds
* `X-Retry-After-Ms` — Wait time before retrying, in milliseconds
* Use the retry interval returned in the response headers before sending another order request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | * Mandatory. * Eg: 119031547242 |
| `type`\* | int | Mandatory. |
| `limitPrice` | float | Mandatory. Only incase of Limit/ Stoplimit orders |
| `stopPrice` | float | Mandatory. Only incase of Stop/ Stoplimit orders |
| `qty` | int | Mandatory. Incase you want to modify the quantity |
| `disclosedQty` | int | Disclosed quantity (Optional) |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | * This is the code to identify specific responses * If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| `message` | string | * Message to clarify the request status. * Eg: Successfully modified order |
| `id` | string | * The order number of the modified order * Eg: 119031547242 |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

orderId = "8102710298291"
data = {
    "id":orderId,
    "type":1,
    "limitPrice": 61049,
    "qty":1
}

response = fyers.modify_order(data=data)
print(response)
```

```
{
    "s": "ok",
    "code": 1101,
    "message": "Successfully modified order', 'id': '8102710298291"
  }
```

VIDEO LEARNING

### Video learning

[How to modify your orders? (REST and cURL)REST and cURL · 6:34](https://www.youtube.com/watch?v=yWTX6ZNp_vQ&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Modify Multi Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-multi-order/ (last updated 2026-10-14)*

This API allows you to modify multiple orders in a single request.

USE CASE

Update up to 10 pending orders together, for example to move their prices at the same time.

Details

* You can modify upto 10 orders simultaneously via the API.
* While Modifying Multi orders you need to pass an ARRAY containing the orders request attributes
* Modifying orders needs an app with the Order Placement permission.
* Send an array with one object per order. Each object carries the order `id`, its `type` and the fields to change, as in Modify Single Order.
* Only pending orders can be modified. Any field you leave out keeps its original value.
* Prices must be multiples of the symbol tick size, and quantity must follow the lot-size rules.
* Modify requests count towards the limit of 10 orders per second shared with placing and cancelling. Requests beyond it are rejected.
* The response has one entry per order with its own `statusCode`, `message` and `id`. Check every entry.
* For order types, product types, validations and sync vs async behaviour, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).
* When order rate limiting is triggered, the API returns `429 Too Many Requests`.
* Retry timing is provided through response headers, not in the response body.
* `Retry-After` — Wait time before retrying, in seconds
* `X-Retry-After-Ms` — Wait time before retrying, in milliseconds
* Use the retry interval returned in the response headers before sending another order request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | * Mandatory. * Eg: 119031547242 |
| `type`\* | int | Mandatory. |
| `limitPrice` | float | Mandatory. Only incase of Limit/ Stoplimit orders |
| `stopPrice` | float | Mandatory. Only incase of Stop/ Stoplimit orders |
| `qty` | int | Mandatory. Incase you want to modify the quantity |
| `disclosedQty` | int | Disclosed quantity (Optional) |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Overall status of the request: "ok" for success, "error" for failure. |
| `code` | int | Overall response code, e.g. `200` on success. |
| `message` | string | Overall message for the request (empty string on success). |
| `data` | array | List of per-order results, one entry for each order submitted in the request, in the same order they were sent. |
| `data[].statusCode` | int | HTTP-style status code for this specific order's modify request, e.g. `200`. |
| `data[].statusDescription` | string | Status description for this specific order's modify request, e.g. "HTTP OK". |
| `data[].body` | object | Result for this order. It has the same fields as the Modify Single Order response. |
| `data[].body.s` | string | ok / error |
| `data[].body.code` | int | * This is the code to identify specific responses * If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| `data[].body.message` | string | * Message to clarify the request status. * Eg: Successfully modified order |
| `data[].body.id` | string | * The order number of the modified order * Eg: 119031547242 |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = [{
  "id": 8102710298291,
  "type": 1,
  "limitPrice": 61049,
  "qty": 1
},
{
  "id": 8102710298292,
  "type": 1,
  "limitPrice": 61049,
  "qty": 1
}]

response = fyers.modify_basket_orders(data=data)
print(response)
```

```
{
  "s": "ok",
  "code": 200,
  "message": "",
  "data": [{"statusCode": 200,
            "body": {
                        "s": "ok",
                        "code": 200,
                        "message": "Successfully modified order",
                        "id": 8102710298291
                      },
                      "statusDescription": "HTTP OK"
              },
              {
                "statusCode": 200,
                "body": {
                          "s": "ok",
                          "code": 200,
                          "message": "Successfully modified order",
                          "id": 8102710298292
                        },
                        "statusDescription": "HTTP OK"
              }
            ]}

  }
```

VIDEO LEARNING

### Video learning

[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Cancel Single Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/ (last updated 2026-10-14)*

This API allows you to cancel an existing order.

USE CASE

Cancel an order that is still pending or open.

Note

To cancel only the linked Take Profit or Stop Loss without cancelling the parent order, use the [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/) API and pass `null` for the applicable `takeProfit` or `stopLoss` parameter. Pass both parameters as `null` to cancel both.

Details

* Cancel pending orders with a JSON body containing **`id`**. You may alternatively use **`DELETE /api/v3/orders/{orderId}/sync`**, which takes the order id in the path instead of the body.
* Cancelling orders needs an app with the Order Placement permission.
* Only pending orders can be cancelled.
* Cancelling a pending parent order also cancels its linked Take Profit and Stop Loss orders automatically. See [Cancelling TPSL](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#cancelling-tpsl) in the Order Placement Guide.
* Cancel requests count towards the limit of 10 orders per second shared with placing and modifying. Requests beyond it are rejected.
* If the response code is 201, the request was made but not acknowledged. Check the order book before sending it again.
* For order types, product types, validations and sync vs async behaviour, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).
* When order rate limiting is triggered, the API returns `429 Too Many Requests`.
* Retry timing is provided through response headers, not in the response body.
* `Retry-After` — Wait time before retrying, in seconds
* `X-Retry-After-Ms` — Wait time before retrying, in milliseconds
* Use the retry interval returned in the response headers before sending another order request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | * Mandatory for **`DELETE /api/v3/orders/sync`** (JSON body). * Eg: 119031547242 |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | * This is the code to identify specific responses * If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| `message` | string | * Message to clarify the request status. * Eg: Successfully canceled order |
| `id` | string | * The order number of the canceled order. * Eg: 119031547242 |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {"id":'808058117761'}

response = fyers.cancel_order(data=data)
print(response)
```

```
{
  "s": "ok",
  "code": 1103,
  "message": "Successfully cancelled order",
  "id": "808058117761"
}
```

VIDEO LEARNING

### Video learning

[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Cancel Multi Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-multi-order/ (last updated 2026-10-14)*

This API allows you to cancel multiple orders in a single request.

USE CASE

Cancel up to 10 pending orders at once, for example when your strategy needs to pull all its working orders.

Details

* You can cancel upto 10 orders simultaneously via the API.
* While cancelling Multi orders you need to pass an ARRAY containing the orders request attributes
* Cancelling orders needs an app with the Order Placement permission.
* Send an array with one object per order, each carrying the order `id`.
* Only pending orders can be cancelled.
* Cancel requests count towards the limit of 10 orders per second shared with placing and modifying. Requests beyond it are rejected.
* The response has one entry per order with its own `statusCode`, `message` and `id`. Check every entry.
* For order types, product types, validations and sync vs async behaviour, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).
* When order rate limiting is triggered, the API returns `429 Too Many Requests`.
* Retry timing is provided through response headers, not in the response body.
* `Retry-After` — Wait time before retrying, in seconds
* `X-Retry-After-Ms` — Wait time before retrying, in milliseconds
* Use the retry interval returned in the response headers before sending another order request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | * Mandatory. * Eg: 119031547242 |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | Message to clarify the request status |
| `data` | array | Array of individual cancellation results, one entry per order submitted in the request, in the same order |
| `data[].statusCode` | int | HTTP status code for that individual order's cancellation. Eg: 200 |
| `data[].statusDescription` | string | HTTP status description for that individual order's cancellation. Eg: HTTP OK |
| `data[].body` | object | Result for this order. It has the same fields as the Cancel Single Order response. |
| `data[].body.s` | string | ok / error |
| `data[].body.code` | int | * This is the code to identify specific responses * If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| `data[].body.message` | string | * Message to clarify the request status. * Eg: Successfully canceled order |
| `data[].body.id` | string | * The order number of the canceled order. * Eg: 119031547242 |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data =  [{
    "id": '808058117761'
},
{
    "id": '808058117762'
}]

response = fyers.cancel_basket_orders(data=data)
print(response)
```

```
{
   "s":ok,
   "code": 200,
   "message": "",
   "data": [{"statusCode": 200,
               "body":
                     {
                     "s":ok,
                     "code": 1103,
                     "message": "Successfully cancelled order",
                     "id": "808058117761"
                     },"statusDescription": "HTTP OK"
             },
             {
               "statusCode": 200,
               "body":
                     {
                       "s":ok,
                       "code": 1103,
                       "message": "Successfully cancelled order",
                       "id": "808058117762"
                     }, "statusDescription": "HTTP OK"
             }
           ]
 }
```

VIDEO LEARNING

### Video learning

[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Cancel Pending Orders

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-pending-orders/ (last updated 2026-10-14)*

This API allows you to cancel pending opposite orders on your open positions, for all symbols or a single position.

USE CASE

Cancel working opposite orders on a position so you can exit it cleanly.

Details

* This is an added functionality for exit position API. If a user has open positions in particular stocks and also working opposite order of the particular stock, the user can close the working orders and then exit the open positions.
* The following should be passed in the body of the DELETE method of positions to cancel the pending orders:
* It works like Exit Position. A `pending_orders_cancel` value of 1 in the body selects this action.
* It is an add-on to the Exit Position API. The pending orders are cancelled so that the position can be exited.
* To limit it to one symbol, also send the position id in the body, for example `NSE:SBIN-EQ-INTRADAY`.
* Without a position id, pending orders are cancelled for all open positions that have a working opposite order.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

```
{"pending_orders_cancel": 1}
```

If only a single symbol's order and position needs to be cancelled, the position ID should also be sent in the body:

```
{"id": "NSE:SBIN-EQ-INTRADAY","pending_orders_cancel": 1}
```

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `pending_orders_cancel`\* | int | Must be set to `1` in the request body to cancel the pending working order(s) associated with a position before exiting it. Eg: 1 |
| `id` | string | Optional. Position ID to target a single symbol's working order and position for cancellation/exit instead of all. Eg: NSE:SBIN-EQ-INTRADAY |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Status of the request. Eg: ok / error |
| `code` | int | Response code identifying the specific response. Eg: 200 |
| `message` | string | Message describing the result of the request. Eg: The position is closed. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization:app_id:access_token" -H "Content-Type: application/json" -X DELETE -d '{"pending_orders_cancel": 1}' https://api-t1.fyers.in/api/v3/positions
```

```
{
 "s": "ok",
 "code": 200,
 "message": "The position is closed."
}
```

VIDEO LEARNING

### Video learning

[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Modify Single Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-single-order/ (last updated 2026-10-14)*

This API allows you to modify an existing order without waiting for the exchange response.

USE CASE

Modify pending orders in quick succession and confirm each change on the General WebSocket or order book.

Details

* Same JSON attributes as synchronous modify.
* For `/sync` vs `/async` behavior, queuing, 10 OPS, `id_fyers` and hosts, see the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#overview---sync-and-async-apis).
* Modifying orders needs an app with the Order Placement permission. The body rules are the same as the sync Modify Single Order API.
* An HTTP 200 response only means the request was queued. It does not confirm that the order was modified.
* The response returns `id_fyers` and not the order `id`. Use `id_fyers` to match the General WebSocket updates or the order book.
* The queue sends requests on at most 10 orders per second.
* Prices must be multiples of the symbol tick size, and quantity must follow the lot-size rules.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - Immediate (async)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `ok` / `error` |
| `code` | int | Response code |
| `message` | string | Status message |
| `id_fyers` | string | Fyers id for the async modify request. **`id` (order ref) is not returned in this immediate response.** |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization: app_id:access_token" -H "Content-Type: application/json" -X PATCH -d '{
  "id":"52009117318",
  "type":1,
  "limitPrice":200,
  "qty":1
}' https://api-t1.fyers.in/api/v3/orders/async
```

## Modify Multi Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-multi-order/ (last updated 2026-10-14)*

This API allows you to modify multiple orders in a single request without waiting for the exchange response.

USE CASE

Adjust many working orders at once and follow each change on the General WebSocket or order book.

Details

* Body is an **array** of modify payloads (each includes **`id`** and fields to change).
* For `/sync` vs `/async` behavior, queuing, 10 OPS, `id_fyers` and hosts, see the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#overview---sync-and-async-apis).
* Modifying orders needs an app with the Order Placement permission.
* Send an array with one object per order, each carrying the order `id` and the fields to change.
* An HTTP 200 response only means the requests were queued. It does not confirm that the orders were modified.
* The queue sends requests on at most 10 orders per second.
* The response returns `id_fyers`. Use it with the General WebSocket updates and the order book to find the final status of each order.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | * Mandatory. * Eg: 119031547242 |
| `type`\* | int | Mandatory. |
| `limitPrice` | float | Mandatory. Only incase of Limit/ Stoplimit orders |
| `stopPrice` | float | Mandatory. Only incase of Stop/ Stoplimit orders |
| `qty` | int | Mandatory. Incase you want to modify the quantity |
| `disclosedQty` | int | Disclosed quantity (Optional) |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id_fyers` | string / array | Fyers queue/async id(s) for the batch modify request, returned per item or as an envelope depending on implementation. The final exchange `id` and terminal status for each leg are obtained separately via the order WebSocket or the GET order-book APIs, not in this immediate response. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization: app_id:access_token" -H "Content-Type: application/json" -X PATCH -d '[
  {"id":"52009117324","type":1,"limitPrice":196,"offlineOrder":true},
  {"id":"52009117325","type":1,"limitPrice":196,"offlineOrder":true}
]' https://api-t1.fyers.in/api/v3/multi-order/async
```

## Cancel Single Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-single-order/ (last updated 2026-10-14)*

This API allows you to cancel an existing order without waiting for the exchange response.

USE CASE

Cancel pending orders in quick succession and confirm each cancellation on the General WebSocket or order book.

Details

* JSON body with **`id`** of the order to cancel.
* For `/sync` vs `/async` behavior, queuing, 10 OPS, `id_fyers` and hosts, see the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#overview---sync-and-async-apis).
* Cancelling orders needs an app with the Order Placement permission. Send the `id` of the order in the JSON body.
* An HTTP 200 response only means the request was queued. It does not confirm that the order was cancelled.
* The response returns `id_fyers`. Use it to match the General WebSocket updates or the order book.
* The queue sends requests on at most 10 orders per second.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - Immediate (async)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `ok` / `error` |
| `code` | int | Response code |
| `message` | string | Status message |
| `id_fyers` | string | Fyers id for the async cancel request. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization: app_id:access_token" -H "Content-Type: application/json" -X DELETE -d '{
  "id":"52009117318"
}' https://api-t1.fyers.in/api/v3/orders/async
```

## Cancel Multi Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-multi-order/ (last updated 2026-10-14)*

This API allows you to cancel multiple orders in a single request without waiting for the exchange response.

USE CASE

Pull many working orders at once and confirm each cancellation on the General WebSocket or order book.

Details

* Body is an **array** of objects with **`id`**.
* For `/sync` vs `/async` behavior, queuing, 10 OPS, `id_fyers` and hosts, see the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#overview---sync-and-async-apis).
* Cancelling orders needs an app with the Order Placement permission.
* Send an array with one object per order, each carrying the order `id`.
* An HTTP 200 response only means the requests were queued. It does not confirm that the orders were cancelled.
* The queue sends requests on at most 10 orders per second.
* The response returns `id_fyers`. Use it with the General WebSocket updates and the order book to find the final status of each order.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | * Mandatory. * Eg: 119031547242 |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization: app_id:access_token" -H "Content-Type: application/json" -X DELETE -d '[
  {"id":"52009117324"},
  {"id":"52009117325"}
]' https://api-t1.fyers.in/api/v3/multi-order/async
```

## GTT Single Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-single-order/ (last updated 2026-10-14)*

This API allows you to place a single GTT (Good Till Trigger) order that stays active until its trigger price is hit or you cancel it.

USE CASE

Set a target or stop-loss on a holding or position, or queue a new order that is sent only when your trigger price is reached.

Details

* This type is used to create a single GTT order.
* It supports placing orders for CNC, Margin, and MTF.
* It can be applied either as a Target or Stop Loss for your existing holdings/positions.
* Alternatively, it can be used to create a GTT order for a new position/holding.
* It supports Limit and Market order types through `orderInfo.leg1.type`. For Market orders, the order is sent at the market price once the trigger price is hit, so the executed price can differ from the trigger price.
* Market orders are not allowed for BFO symbols. Such requests are rejected with code `-50`.
* A GTT order stays active for up to one year, until its trigger is hit or you cancel it.
* A single GTT uses `leg1` only. `leg2` is used only for OCO orders, which have their own GTT OCO Order page.
* `type` in `leg1` sets the order type: 1 for Limit (the default) and 2 for Market. For a Market order, send `price` as 0 or leave it out.
* Response code `1101` means the order was placed. Code `201` means it is in transit, so confirm it in the GTT Order Book.
* Keep the returned `id`. You need it to modify or cancel the order while it is still pending.
* `orderTag` is optional. FYERS adds `1:GTT` at the start of your tag. Without a tag the order gets `2:GTTUntagged`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `Side` | int | Indicates the side of the order: `1` for buy, `-1` for sell. |
| `symbol`\* | string | The instrument's unique identifier, e.g., "NSE:CHOLAFIN-EQ" |
| `productType`\* | string | The product type for the order. Valid values: "CNC", "MARGIN", "MTF". |
| `orderInfo`\* | object | Contains information about the GTT order leg. |
| `orderInfo.leg1`\* | object | Details for the GTT order leg. |
| `orderInfo.leg1.price`\* | float | Price at which the order should be placed. Required for Limit. For Market, send `0` or leave it out. |
| `orderInfo.leg1.triggerPrice` | float | Trigger price for the GTT order. |
| `orderInfo.leg1.qty`\* | int | Quantity for the GTT order leg. |
| `orderInfo.leg1.type` | int | * Order type for this leg: * `1`: Limit (default if not provided). * `2`: Market. |
| `orderTag` | string | * ordertag provided when placing the order * **Note**: `1:GTT` will be concatenated at the start of tag provided by user. * Default value if tag not provided when order is placed is `2:GTTUntagged` |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | * Status code indicating the outcome of the request: * `1101`: Order placed successfully. * `201`: Order is in transit. Confirm details using the Orderbook API. * Other codes represent specific error conditions. |
| `message`\* | string | Descriptive message about the request status, e.g., "Successfully placed order". |
| `s`\* | string | Request status indicator: "ok" for success, "error" for failure. |
| `id`\* | string | Unique identifier for the placed order, returned when the order is successfully processed. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
      "side": 1,
      "symbol": "NSE:SBIN-EQ",
      "productType":"CNC",
      "orderInfo": {
          "leg1": {
              "price": 1000,
              "triggerPrice": 1000,
              "qty": 3
          }
      }
  }
response = fyers.place_gtt_order(data=data)
print(response)
```

```
{
    "code": 1101,
    "message": "Successfully placed order",
    "s": "ok",
    "id":"25012400002099"
  }
```

## GTT OCO Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-oco-order/ (last updated 2026-10-14)*

This API allows you to place a one-cancels-other (OCO) GTT order with two legs, where the first leg to trigger cancels the other.

USE CASE

Set a target and a stop-loss together on a position you hold, so whichever triggers first cancels the other.

Details

* This type allows you to place both a Stop Loss and a Target order simultaneously. If one order is triggered, the other gets automatically canceled.
* To avoid rejections:
* For Leg1: The trigger price must always be greater than the LTP
* For Leg 2: The trigger price must always be less than the LTP
* Each leg can be a Limit or Market order through `type`, and the two legs can use different order types. For Market orders, the order is sent at the market price once the trigger price is hit, so the executed price can differ from the trigger price.
* Market orders are not allowed for BFO symbols. Such requests are rejected with code `-50`.
* It uses the same endpoint as a single GTT. Sending both `leg1` and `leg2` makes the order an OCO.
* Each leg carries its own `type`, `price`, `triggerPrice` and `qty`. The two legs can use different order types: 1 for Limit (the default) and 2 for Market.
* For a Market leg, send `price` as 0 or leave it out.
* Product type can be CNC, MARGIN or MTF. The order stays active for up to one year unless a leg triggers or you cancel it.
* Response code `1101` means the order was placed. Code `201` means it is in transit, so confirm it in the GTT Order Book.
* In the GTT Order Book an OCO order shows `gtt_oco_ind` as 2, and the second leg appears in `price2_limit`, `price2_trigger`, `qty2` and `ord_type2`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `Side` | int | Indicates the side of the order: `1` for buy, `-1` for sell. |
| `symbol`\* | string | The instrument's unique identifier, e.g., "NSE:CHOLAFIN-EQ" |
| `productType`\* | string | The product type for the order. Valid values: "CNC", "MARGIN", "MTF". |
| `orderInfo`\* | object | Contains information about the GTT/OCO order legs. |
| `orderInfo.leg1`\* | object | Details for GTT order leg. Mandatory for all orders. |
| `orderInfo.leg1.price`\* | float | Price at which the order should be placed. Required for Limit. For Market, send `0` or leave it out. |
| `orderInfo.leg1.triggerPrice` | float | * Trigger price for the GTT order. * NOTE: for OCO order this leg trigger price should be always above LTP |
| `orderInfo.leg1.qty`\* | int | Quantity for the GTT order leg. |
| `orderInfo.leg1.type` | int | * Order type for this leg: * `1`: Limit (default if not provided). * `2`: Market. |
| `orderInfo.leg2`\* | object | Details for OCO order leg. Optional and included only for OCO orders. |
| `orderInfo.leg2.price`\* | float | Price at which the second leg of the OCO order should be placed. Required for Limit. For Market, send `0` or leave it out. |
| `orderInfo.leg2.triggerPrice`\* | float | * Trigger price for the second leg of the OCO order. * NOTE: for OCO order this leg trigger price should be always below LTP |
| `orderInfo.leg2.qty`\* | int | Quantity for the second leg of the OCO order.. |
| `orderInfo.leg2.type` | int | * Order type for this leg: * `1`: Limit (default if not provided). * `2`: Market. The two legs can use different order types. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | * Status code indicating the outcome of the request: * `1101`: Order placed successfully. * `201`: Order is in transit. Confirm details using the Orderbook API. * Other codes represent specific error conditions. |
| `message`\* | string | Descriptive message about the request status, e.g., "Successfully placed order". |
| `s`\* | string | Request status indicator: "ok" for success, "error" for failure. |
| `id`\* | string | Unique identifier for the placed order, returned when the order is successfully processed. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
      "side": 1,
      "symbol": "NSE:SBIN-EQ",
      "productType":"CNC",
      "orderInfo": {
          "leg1": {
              "price": 1000,
              "triggerPrice": 1000,
              "qty": 3
          },
          "leg2": {
              "price": 600,
              "triggerPrice": 600,
              "qty": 3
          }
      }
  }
response = fyers.place_gtt_order(data=data)
print(response)
```

```
{
    "code": 1101,
    "message": "Successfully placed order",
    "s": "ok",
    "id":"25012400002100"
  }
```

## Modify GTT Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/modify-gtt-order/ (last updated 2026-10-14)*

This API allows you to modify the order type, price, trigger price or quantity of a pending GTT order.

USE CASE

Move your target or stop-loss after placing a GTT order, without cancelling it and placing a new one.

Details

* This allows the user to modify pending GTT orders. Send `price`, `triggerPrice` and `qty` for every leg. Send `type` for every Market leg: if `type` is not provided, the leg is modified as a Limit order.
* Send the order `id` and `orderInfo`. `leg1` is mandatory for every modification, and `leg2` is required if the order is an OCO.
* Only the order type, price, trigger price and quantity of each leg can be updated. The request has no field for symbol, side or product type.
* Send `type` for every Market leg. If `type` is not provided, the leg is modified as a Limit order.
* For an OCO order, the `leg1` trigger price must stay above LTP and the `leg2` trigger price must stay below LTP.
* Response code `1102` means the order was modified. Code `201` means it is in transit, so confirm it in the GTT Order Book.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | Unique identifier for the order to be modified, e.g., "25010700000001". |
| `orderInfo`\* | object | Contains updated information about the GTT/OCO order legs. |
| `orderInfo.leg1`\* | object | Details for GTT order leg. Mandatory for all modifications. |
| `orderInfo.leg1.price`\* | float | Updated price at which the order should be placed. Required for Limit. For Market, send `0` or leave it out. |
| `orderInfo.leg1.triggerPrice`\* | float | Updated trigger price for the GTT order. NOTE: for OCO order this leg trigger price should be always above LTP. |
| `orderInfo.leg1.qty`\* | int | Updated quantity for the GTT order leg. |
| `orderInfo.leg1.type` | int | * Order type for this leg: * `1`: Limit (default if not provided). * `2`: Market. If not provided, the leg is modified as a Limit order. |
| `orderInfo.leg2`\* | object | Details for OCO order leg. Required if the order is an OCO type. |
| `orderInfo.leg2.price`\* | float | Updated price for the second leg of the OCO order. Required for Limit. For Market, send `0` or leave it out. |
| `orderInfo.leg2.triggerPrice`\* | float | * Updated trigger price for the second leg of the OCO order. * NOTE: for OCO order this leg trigger price should be always below LTP. |
| `orderInfo.leg2.qty`\* | int | Updated quantity for the second leg of the OCO order. |
| `orderInfo.leg2.type` | int | * Order type for this leg: * `1`: Limit (default if not provided). * `2`: Market. If not provided, the leg is modified as a Limit order. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | * Status code indicating the outcome of the modification request: * 1102: Order modification successful. * 201: Order modification is in transit. Confirm details using the Orderbook API. * Other codes represent specific error conditions. |
| `message` | string | * Descriptive message about the modification request. * e.g., "Successfully modified order". |
| `id` | string | Unique identifier for the modified order, returned if the modification is successful. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "id": "25012400002074",
    "orderInfo": {
        "leg1": {
            "price": 1020,
            "triggerPrice": 1020,
            "qty": 5
        },
        "leg2": {
            "price": 620,
            "triggerPrice": 620,
            "qty": 5
        }
    }
}
response = fyers.modify_gtt_order(data=data)
print(response)
```

```
{
  "code": 1102,
  "message": "Successfully modified order',
  "s": "ok",
  "id": '8102710298291"
  }
```

## Cancel GTT Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/cancel-gtt-order/ (last updated 2026-10-14)*

This API allows you to cancel a pending GTT order.

USE CASE

Cancel a GTT order you no longer need, for example after exiting the position another way.

Details

* You can cancel pending orders before they trigger.
* Send only the `id` of the GTT order. It is returned when you place the order and is also listed in the GTT Order Book.
* Response code `1103` means the cancellation was successful. Other codes are specific error conditions.
* Confirm the result in the GTT Order Book, where a cancelled order shows `ord_status` 1 and `report_type` CANCELLED.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For each order

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id`\* | string | * Unique identifier for the order to be cancelled, * e.g., "25010700000001". |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | * Status code indicating the outcome of the cancellation request: * 1103: Order cancellation successful. * Other codes represent specific error conditions. |
| `message` | string | * Descriptive message about the cancellation request, * e.g., "Successfully cancelled order". |
| `id` | string | Unique identifier for the cancelled order, returned if the cancellation is successful. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {"id":'25012400002099'}

response = fyers.cancel_gtt_order(data=data)
print(response)
```

```
{
  "code": 1103,
  "message": "Successfully cancelled order",
  "s": "ok",
  "id": "25012400002099"
}
```

## Smart Limit Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-limit-order/ (last updated 2026-10-14)*

This API allows you to place a limit order that stays active until an end time you choose on the same trading day.

USE CASE

Place a limit order that is cancelled or converted to a market order automatically if it is not filled by your chosen time.

Note

* Supported product types are CNC, MARGIN, MTF and INTRADAY.
* High-price range (HPR) and low-price range (LPR) apply to NSE and BSE symbols.

* Supports order placement under CNC, MARGIN, MTF, and INTRADAY.

* You can define a price range (HPR/LPR) to restrict execution within your specified limits.

* Supports only NSE & BSE segments, [click here](https://support.fyers.in/portal/en/kb/articles/what-are-the-segment-restrictions-execution-rules-and-validity-conditions-for-smart-orders-in-fyers#Which_Trading_Segments_Support_Smart_Orders) to check allowed and not allowed segments.

Details

* Smart Limit Orders allow you to place limit orders that remain active until the specified end time. Once the end time is reached, the order can be converted to an MPP order or cancelled.
* `endTime` is a Unix timestamp. It must be in the future, within market hours and before midnight of the current day.
* `onExp` sets what happens at `endTime`: `1` cancels the order and `2` turns it into a market order.
* `orderType` is `1` (Limit) or `4` (Stop-Limit). A Stop-Limit order needs `stopPrice`: lower than `limitPrice` for buy, higher for sell.
* `hpr` and `lpr` default to 0, meaning no limit. For a buy, `hpr` must not be below `limitPrice`. For a sell, `lpr` must not be above it.
* `qty` must be 1 to 999999, a multiple of the lot size and within the freeze limit. `limitPrice` must be at least 0.01. `mpp` must be 0 to 3 or -1.
* MTF needs MTF to be enabled and a symbol and exchange that support it. For F&O and currency derivatives only near expiries and strikes close to LTP are allowed.
* Smart orders can be created only on trading days (not special trading days), from 8:00 AM and within regular trading hours. The limit is 100 smart orders per day.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `symbol` | string | Yes | The instrument's unique identifier, e.g., "NSE:SBIN-EQ" |
| `side` | int | Yes | Order side: `1` for Buy, `-1` for Sell (enum: 1, -1) |
| `qty` | int | Yes | Order quantity (Min: 1, Max: 999999; must be a multiple of lot size) |
| `productType` | string | Yes | Must be one of: "CNC", "MARGIN", "INTRADAY", "MTF" |
| `limitPrice` | float | Yes | The price at which the order should be placed (Min: 0.01) |
| `endTime` | int | Yes | Order expiry time as a Unix timestamp (epoch) |
| `orderType` | int | Yes | Order type: `1` for Limit, `4` for Stop-Limit (enum: 1, 4) |
| `onExp` | int | Yes | Action on expiry: `1` = Cancel, `2` = Market (MPP: Market Price Protection ) (enum: 1, 2) |
| `stopPrice` | float | No | Default: 0. Required when orderType is `4` (Stop-Limit) |
| `hpr` | float | No | Default: 0. 0 = no upper price limit. If provided, order executes only below this price |
| `lpr` | float | No | Default: 0. 0 = no lower price limit. If provided, order executes only above this price |
| `mpp` | float | No | Default: 0. 0 = no market protection. Valid values: 0–3 or -1 (disabled) |

### Validations & Error Handling

| Attribute | **Validation Rule** | Error Message |
| --- | --- | --- |
| `symbol` | Must be a valid trading symbol | "The symbol entered is invalid." |
| `symbol` | Must be allowed for smart orders | "The selected symbol is not allowed for placing smart orders. Please try again with a different symbol." |
| `symbol` | Must be allowed for this segment | "The smart order not allowed for this segment" |
| `side` | Must be 1 or -1 (enum) | "The input details entered is invalid." |
| `qty` | Min: 1, Max: 999999, must be multiple of lot size | "Quantity should be multiple of min lot size." |
| `qty` | Must not exceed freeze limit | "Quantity exceeds the allowable freeze limit." |
| `productType` | Must be one of: CNC, MARGIN, INTRADAY, MTF | "productType must be one of the following: CNC, MARGIN, INTRADAY, MTF" |
| `productType` | MTF requires MTF activation | "MTF is not enabled. Please use a different productType" |
| `limitPrice` | Min: 0.01 | "The input details entered is invalid." |
| `orderType` | Must be 1 or 4 (enum) | "orderType must be one of the following: 1, 4" |
| `onExp` | Must be 1 or 2 (enum) | "onExp must be one of the following: 1, 2" |
| `endTime` | Must not be 0 | "EndTime is required and cannot be 0." |
| `endTime` | Must be within market hours | "End time cannot fall within market closed hours." |
| `endTime` | Must not be in the past | "The end time entered is earlier than the current time." |
| `endTime` | Must be within current day | "The end time cannot extend beyond midnight of the current day." |
| `hpr` (buy) | Min: 0, if provided (>0), must be >= limitPrice | "The maximum price must be higher than the limit price." |
| `lpr` (sell) | Min: 0, if provided (>0), must be <= limitPrice | "The minimum price must be lower than the limit price." |
| `stopPrice` (buy) | Min: 0, if orderType=4, must be < limitPrice | "For buy orders, the stop price must be lower than the limit price." |
| `stopPrice` (sell) | Min: 0, if orderType=4, must be > limitPrice | "For sell orders, the stop price must be higher than the limit price." |
| `mpp` | If provided (>0), must be 0-3 or -1 | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |
| `flowtype` | Must be a valid smart order type | "The smart order specified in the URL path is not recognized." |
| User | Must not be banned for smart orders | "You are banned for smart order. Please contact support" |
| Trading day | Must not be market-closed day | "You can't create smart orders on market-closed day" |
| Trading day | Smart orders not allowed on special trading day | "Smart orders are not allowed on special trading day" |
| Trading hours | Must not be after market hours | "Smart orders cannot be created after market hours." |
| Trading hours | Must not be before 8:00 AM | "Smart orders are not allowed to be created before 8:00 AM." |
| Trading hours | Must be within regular trading hours | "You can't place a smart order outside regular trading hours" |
| `productType` (MTF) | Symbol/exchange must support MTF | "This symbol or exchange is not supported for MTF." |
| Derivatives | Expiry must be allowed (F&O/CD) | "The selected contract expiry is not allowed for placing smart orders. Please try again with a near expiry contract." |
| Derivatives | Strike price must be within allowed range (F&O/CD) | "The selected strike price is out of the permitted range. Please try with a strike price closer to the LTP" |
| Daily limit | Max 100 smart orders/day | "You have exceeded the maximum limit of creating 100 smart orders for the day." |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` for success; negative values indicate errors. |
| `message` | string | Describes the response — e.g., "Request sent successfully to place smart order" or an error message. |
| `s` | string | "ok" for success, "error" for failure. |
| `id` | string | Unique identifier for the placed smart order (returned only on success). |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = "YOUR_ACCESS_TOKEN"

fyers = fyersModel.FyersModel(
    client_id=client_id,
    is_async=False,
    token=access_token,
    log_path=""
)

data = {
    "symbol": "NSE:SBIN-EQ",
    "side": 1,                  # Buy
    "qty": 1,
    "productType": "CNC",
    "limitPrice": 1250,
    "stopPrice": 1200,
    "orderType": 1,
    "endTime": 1768987800,
    "hpr": 1300,
    "lpr": 700,
    "mpp": 1,
    "onExp": 2
}

response = fyers.create_smart_order_limit(data=data)
print(response)
```

```
Response structure:
{
  "code": 200,
  "message": "Request sent successfully to place smart order",
  "s": "ok",
  "id": "1bf162b1-6406-407a-911a-5a3309e1aaba"
}
```

## Smart Trail

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-trail/ (last updated 2026-10-14)*

This API allows you to place a trailing stop-loss order whose stop price follows the market as it moves in your favour.

USE CASE

Protect an open position with a stop-loss that moves with the price to lock in gains.

Note

* For sell orders, the stop price moves up as the price rises.
* For buy orders, the stop price moves down as the price falls.

* The order is triggered when the market price hits the trailing stop price.

* You can optionally set a target price to book profits automatically.

* Supports both Limit and Market (MPP) order types for execution.

* Supports only NSE & BSE segments, [click here](https://support.fyers.in/portal/en/kb/articles/what-are-the-segment-restrictions-execution-rules-and-validity-conditions-for-smart-orders-in-fyers#Which_Trading_Segments_Support_Smart_Orders) to check allowed and not allowed segments.

Details

* A Smart Trail Order is a trailing stop-loss that automatically adjusts the stop price as the market moves in your favour. The stop price trails the market by a specified jump price.
* `jump_diff` is how far the stop trails. It must be at least 0.2 and more than 20 times the tick size.
* `stopPrice` must be greater than 0. `productType` can be CNC, MARGIN, INTRADAY or MTF.
* For a Limit order (`orderType` 1) send `limitPrice`. For a Market order (`orderType` 2) leave `limitPrice` out or 0.
* For a Market order, a buy `stopPrice` must be at or above LTP, and a sell `stopPrice` at or below LTP.
* `target_price` is optional. If sent, it must be above LTP for a sell order and below LTP for a buy order.
* `qty` must be 1 to 999999 and a multiple of the lot size. `mpp` must be 0 to 3 or -1.
* Smart orders can be created only on trading days (not special trading days), from 8:00 AM and within regular trading hours. The limit is 100 smart orders per day.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `symbol` | string | Yes | The instrument's unique identifier, e.g., "NSE:SBIN-EQ" |
| `side` | int | Yes | Order side: `1` for Buy, `-1` for Sell (enum: 1, -1) |
| `qty` | int | Yes | Order quantity (Min: 1, Max: 999999; must be a multiple of lot size) |
| `productType` | string | Yes | Must be one of: "CNC", "MARGIN", "INTRADAY", "MTF" |
| `orderType` | int | Yes | Order type: `1` for Limit Order, `2` for Market Order (MPP: Market Price Protection ) (enum: 1, 2) |
| `stopPrice` | float | Yes | Initial stop/trigger price (must be greater than 0) |
| `jump_diff` | float | Yes | Jump price — the value by which the stop price trails (Min: 0.2) |
| `limitPrice` | float | No | Default: 0. If not provided, executes at market price. Required if orderType = 1. |
| `target_price` | float | No | Default: 0 (no target). If provided, must be greater than current LTP. |
| `mpp` | float | No | Default: 0 (no market protection). Valid values: 0–3 or -1 (disabled). |

### Validations & Error Messages

| Attribute | **Validation Rule** | Error Message |
| --- | --- | --- |
| `symbol` | Must be a valid trading symbol | "The symbol entered is invalid." |
| `symbol` | Must be allowed for smart orders | "The selected symbol is not allowed for placing smart orders. Please try again with a different symbol." |
| `symbol` | Must be allowed for this segment | "The smart order not allowed for this segment" |
| `side` | Must be 1 or -1 | "The input details entered is invalid." |
| `qty` | Min: 1, Max: 999999, must be multiple of lot size | "Quantity should be multiple of min lot size." |
| `productType` | Must be one of: CNC, MARGIN, INTRADAY, MTF | "productType must be one of the following: CNC, MARGIN, INTRADAY, MTF" |
| `orderType` | Must be 1 or 2 | "orderType must be one of the following: 1, 2" |
| `stopPrice` | Min: 0, cannot be 0 for placing order | "Stop Price is required to place orders." |
| `jump_diff` | Min: 0.2, must be > 20× tick size | "The jump price must be more than 20 times the tick size." |
| `limitPrice` (buy) | If orderType=1, must be < stopPrice | "For buy orders, the stop price must be lower than the limit price." |
| `limitPrice` (sell) | If orderType=1, must be > stopPrice | "For sell orders, the stop price must be higher than the limit price." |
| `target_price` (sell) | If provided (>0), must be > current LTP | "The target price must be greater than the last traded price for sell orders." |
| `target_price` (buy) | If provided (>0), must be < current LTP | "The target price must be lesser than the last traded price for buy orders." |
| `mpp` | If provided (>0), must be 0-3 or -1 | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |
| `limitPrice` | If orderType=2 (Market), limitPrice must be 0 / not provided | "Limit price is not required." |
| `stopPrice` (buy, orderType=2) | Must be >= current LTP | "For buy orders, the stop price must be greater than the last traded price." |
| `stopPrice` (sell, orderType=2) | Must be <= current LTP | "For sell orders, the stop price must be less than the last traded price." |
| `flowtype` | Must be a valid smart order type | "The smart order specified in the URL path is not recognized." |
| User | Must not be banned for smart orders | "You are banned for smart order. Please contact support" |
| Trading day | Must not be market-closed day | "You can't create smart orders on market-closed day" |
| Trading day | Smart orders not allowed on special trading day | "Smart orders are not allowed on special trading day" |
| Trading hours | Must not be after market hours | "Smart orders cannot be created after market hours." |
| Trading hours | Must not be before 8:00 AM | "Smart orders are not allowed to be created before 8:00 AM." |
| Trading hours | Must be within regular trading hours | "You can't place a smart order outside regular trading hours" |
| Daily limit | Max 100 smart orders/day | "You have exceeded the maximum limit of creating 100 smart orders for the day." |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` indicates success; negative values indicate errors. |
| `message` | string | Descriptive message — e.g., "Request sent successfully to place smart order." or error reason. |
| `s` | string | "ok" for success, "error" for failure. |
| `id` | string | Unique identifier for the placed smart order (returned only on success). |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = "YOUR_ACCESS_TOKEN"

fyers = fyersModel.FyersModel(
    client_id=client_id,
    is_async=False,
    token=access_token,
    log_path=""
)

data = {
    "symbol": "NSE:SBIN-EQ",
    "side": -1,                 # Sell
    "qty": 1,
    "productType": "CNC",
    "stopPrice": 740,
    "jump_diff": 5,
    "orderType": 2,
    "mpp": 1
}

response = fyers.create_smart_order_trail(data=data)
print(response)
```

```
Response structure:
{
  "code": 200,
  "message": "Request sent successfully to place smart order",
  "s": "ok",
  "id": "2cf273c2-7517-518b-a22b-6b4420f2bcbc"
}
```

## Smart Step Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-step-order/ (last updated 2026-10-14)*

This API allows you to build a position gradually by placing orders at price intervals you define.

USE CASE

Average your entry price by buying or selling more quantity at each price step you set.

Note

After execution starts you cannot modify `initQty`, `limitPrice`, or `orderType`.

* Starts with an initial quantity, followed by averaging based on defined step intervals.

* Direction determines whether orders are placed as the price increases or decreases.

* Orders are placed automatically at each step until the total quantity is fulfilled.

* Supports both price-based and time-based step execution.

* Supports only NSE & BSE segments, [click here](https://support.fyers.in/portal/en/kb/articles/what-are-the-segment-restrictions-execution-rules-and-validity-conditions-for-smart-orders-in-fyers#Which_Trading_Segments_Support_Smart_Orders) to check allowed and not allowed segments.

Details

* Smart Step Order lets you average your position by placing orders at predefined price intervals, helping you build the position gradually across multiple price levels.
* `qty` is the total quantity and must be at least `initQty` plus `avgqty`. `initQty` of 0 means nothing is placed immediately.
* `avgqty` is the quantity per step and must be a multiple of the lot size. `avgdiff` must be at least 0.01 and more than 20 times the tick size.
* `direction` 1 averages as the price falls. `direction` -1 averages as the price rises.
* `startTime` and `endTime` are Unix timestamps within market hours. `startTime` must be in the future and before midnight of the current day.
* For a Limit order (`orderType` 1) `limitPrice` is required. `hpr` and `lpr` of 0 mean no limit. `mpp` must be 0 to 3 or -1.
* `productType` can be CNC, MARGIN, INTRADAY or MTF.
* Smart orders can be created only on trading days (not special trading days), from 8:00 AM and within regular trading hours. The limit is 100 smart orders per day.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `symbol` | string | Yes | The instrument's unique identifier, e.g., "NSE:SBIN-EQ" |
| `side` | int | Yes | Order side: `1` for Buy, `-1` for Sell (enum: 1, -1) |
| `qty` | int | Yes | Total order quantity (Min: 1, Max: 999999; must be ≥ initQty + avgqty) |
| `productType` | string | Yes | Must be one of: "CNC", "MARGIN", "INTRADAY", "MTF" |
| `orderType` | int | Yes | Order type: `1` for Limit, `2` for Market (MPP: Market Price Protection ) (enum: 1, 2). If orderType = 1, limitPrice is required. |
| `avgqty` | int | Yes | Quantity to place at each averaging step (Min: 1, Max: 999999) |
| `avgdiff` | float | Yes | Price difference between averaging steps (Min: 0.01) |
| `direction` | int | Yes | `1` for averaging on price decrease, `-1` for averaging on price increase (enum: 1, -1) |
| `startTime` | int | Yes | Unix timestamp (epoch) when the order should start executing |
| `endTime` | int | Yes | Unix timestamp (epoch) when the order should expire |
| `limitPrice` | float | Conditional | Default: 0. Required if orderType = 1. Not needed for market orders. |
| `initQty` | int | No | Default: 0. Quantity to place immediately. 0 = no initial order (Max: 999999) |
| `hpr` | float | No | Default: 0. 0 = no upper price limit. If set, execution allowed only below this price. |
| `lpr` | float | No | Default: 0. 0 = no lower price limit. If set, execution is allowed only above this price. |
| `mpp` | float | No | Default: 0. 0 = no market protection. Valid values: 0–3, or -1 (disabled) |

### Validations & Error Messages

| Attribute | **Validation Rule** | Error Message |
| --- | --- | --- |
| `symbol` | Must be a valid trading symbol | "The symbol entered is invalid." |
| `symbol` | Must be allowed for smart orders | "The selected symbol is not allowed for placing smart orders. Please try again with a different symbol." |
| `symbol` | Must be allowed for this segment | "The smart order not allowed for this segment" |
| `side` | Must be 1 or -1 (enum) | "The input details entered is invalid." |
| `qty` | Min: 1, Max: 999999, must be >= initQty + avgqty | "Total Quantity should be greater than or equal to the sum of Initial Qty and Average Qty." |
| `productType` | Must be one of: CNC, MARGIN, INTRADAY, MTF | "productType must be one of the following: CNC, MARGIN, INTRADAY, MTF" |
| `orderType` | Must be 1 or 2 (enum) | "orderType must be one of the following: 1, 2" |
| `limitPrice` | Required if orderType=1 | "The input details entered is invalid." |
| `avgqty` | Min: 1, Max: 999999, must be multiple of lot size | "Avg quantity should be multiple of min lot size." |
| `avgdiff` | Min: 0.01, must be > 20× tick size | "The average entry price must be more than 20 times the tick size." |
| `direction` | Must be 1 or -1 (enum) | "The input details entered is invalid." |
| `startTime` | Cannot be 0 | "Start Time is required to place orders." |
| `startTime` | Must be within market hours | "Start time cannot fall within market closed hours." |
| `startTime` | Cannot be in the past | "The start time entered is earlier than the current time." |
| `startTime` | Must be within current day | "The start time cannot extend beyond midnight of the current day." |
| `endTime` | Cannot be 0 | "End Time is required to place orders." |
| `endTime` | Must be within market hours | "End time cannot fall within market closed hours." |
| `initQty` | Min: 0, Max: 999999 | "The input details entered is invalid." |
| `hpr` (buy, limit) | Min: 0, if provided must be >= limitPrice | "The limit price cannot be higher than the upper price range." |
| `lpr` (buy, limit) | Min: 0, if provided must be <= limitPrice | "The limit price cannot be lower than the lower price range." |
| `mpp` | If provided (>0), must be 0-3 or -1 | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |
| `flowtype` | Must be a valid smart order type | "The smart order specified in the URL path is not recognized." |
| User | Must not be banned for smart orders | "You are banned for smart order. Please contact support" |
| Trading day | Must not be market-closed day | "You can't create smart orders on market-closed day" |
| Trading day | Smart orders not allowed on special trading day | "Smart orders are not allowed on special trading day" |
| Trading hours | Must not be after market hours | "Smart orders cannot be created after market hours." |
| Trading hours | Must not be before 8:00 AM | "Smart orders are not allowed to be created before 8:00 AM." |
| Trading hours | Must be within regular trading hours | "You can't place a smart order outside regular trading hours" |
| Daily limit | Max 100 smart orders/day | "You have exceeded the maximum limit of creating 100 smart orders for the day." |

**Note:** After the order starts executing, the following fields cannot be modified: `initQty`, `limitPrice`, `orderType`

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` for success; negative values indicate errors. |
| `message` | string | Text message describing the result — e.g., "Request sent successfully" or the error reason. |
| `s` | string | "ok" for success, "error" for failure. |
| `id` | string | Unique identifier for the placed smart order (returned only on success). |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = "YOUR_ACCESS_TOKEN"

fyers = fyersModel.FyersModel(
    client_id=client_id,
    is_async=False,
    token=access_token,
    log_path=""
)

data = {
    "symbol": "NSE:SBIN-EQ",
    "side": 1,
    "qty": 10,
    "productType": "CNC",
    "initQty": 2,
    "avgqty": 2,
    "avgdiff": 5,
    "direction": 1,
    "limitPrice": 750,
    "orderType": 1,
    "startTime": 1768987800,
    "endTime": 1768989000,
    "hpr": 800,
    "lpr": 700,
    "mpp": 1
}

response = fyers.create_smart_order_step(data=data)
print(response)
```

```
Response structure:
{
  "code": 200,
  "message": "Request sent successfully to place smart order",
  "s": "ok",
  "id": "1bf162b1-6406-407a-911a-5a3309e1aaba"
}
```

## Smart SIP

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-sip/ (last updated 2026-10-14)*

This API allows you to automate recurring investments in equity stocks and ETFs on a daily, weekly, monthly or custom schedule.

USE CASE

Invest a fixed amount or quantity in a stock or ETF on a regular schedule.

Note

* Smart SIP is available for equity only.
* You can invest by amount or quantity and optionally enable step-up.

* Available only for **Equity segment** symbols on NSE/BSE CM.

* You can invest using either a fixed amount or a specified quantity.

* Use price range protection (HPR/LPR) to skip execution when prices move beyond your defined range.

* With the step-up option, you can gradually increase the investment amount or quantity over time.

Details

* Smart SIP allows you to automate recurring investments in equity stocks, ETFs, with orders placed automatically at your selected frequency—daily, weekly, monthly, or on custom dates.
* `freq` is 1 (daily), 2 (weekly), 3 (monthly) or 6 (custom). Daily needs `sip_time` within 9:15 AM to 3:30 PM. The others use `sip_day`.
* `sip_day` is 1 to 28. For weekly it must be 1 (Monday) to 5 (Friday). `imd_start` as true starts the SIP now instead of waiting for the schedule.
* Send either `amount` or `qty`, not both. An amount-based SIP cannot be less than LTP. `productType` can be CNC or MTF.
* Send either `endTime` or `exp_qty`, not both. `endTime` must be after today and not on a weekend, at least 4 days away for daily and 30 days for weekly or monthly.
* `step_up_freq` is 3 or 5 and must be at least `freq`. Send `step_up_amount` or `step_up_qty` (matching your SIP mode), not both. Step-up is not allowed for a custom SIP.
* `hpr` must be greater than `lpr`. A custom SIP for today cannot be placed after 11:00 AM.
* There is a daily limit on the number of SIP orders. Going over it is rejected.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `symbol` | string | Yes | The instrument's unique identifier (Equity only), e.g., "NSE:SBIN-EQ" |
| `productType` | string | Yes | Must be one of: "CNC", "MTF" |
| `freq` | int | Yes | SIP frequency (enum: 1, 2, 3, 6) |
| `sip_day` | int | Yes | Day of the month for SIP execution (Min: 1, Max: 28) |
| `qty` OR `amount` | integer/number | Yes | At least one required - Quantity or amount per SIP instalment (Max: 999999) |
| `sip_time` | int | Conditional | Required if freq = 1 (Daily). Unix timestamp for SIP execution time (must be within market hours) |
| `imd_start` | boolean | No | Whether to start SIP immediately. `true` = start now, `false` = wait for schedule |
| `endTime` | int | No | Default: 0 (no end date). Unix timestamp when the SIP should end |
| `hpr` | float | No | Default: 0. Skips SIP if price is above this upper limit |
| `lpr` | float | No | Default: 0. Skips SIP if price is below this lower limit |
| `step_up_freq` | int | No | Frequency of step-up increase (enum: 3, 5). Default: 0 (no step-up) |
| `step_up_qty` | int | No | Quantity to increase at each step-up (Default: 0; Max: 999999) |
| `step_up_amount` | float | No | Amount to increase at each step-up (Default: 0; Max: 999999) |
| `exp_qty` | int | No | Quantity for expiry/final SIP order (Default: 0; Max: 999999) |

### SIP Frequency Values

| **Value** | **Frequency** | **Required Field** | Description |
| --- | --- | --- | --- |
| `1` | Daily | `sip_time` | Invests every trading day at the specified time |
| `2` | Weekly | `sip_day` | Invests once a week on the specified day |
| `3` | Monthly | `sip_day` | Invests once a month on the specified day |
| `6` | Custom | `sip_day` | Invests on selected dates each month |

### Validations & Error Messages

| Attribute | **Validation Rule** | Error Message |
| --- | --- | --- |
| `qty` & `amount` | Provide either amount or qty (exactly one) | "Please enter either the amount or qty to place an order." |
| `symbol` | Must be Equity segment (NSE/BSE CM) | "Equity SIP is not available for the selected symbol. Please choose a different symbol." |
| `productType` | Must be CNC or MTF | "productType must be one of the following: CNC, MTF" |
| `freq` | Must be 1, 2, 3, or 6 (enum) | "The input details entered is invalid." |
| `sip_day` | Min: 1, Max: 28 | "The input details entered is invalid." |
| `sip_time` | Required if freq=1 | "Please select a SIP time." |
| `sip_time` | Must be within 9:15 AM - 3:30 PM | "Please select an SIP time within market hours." |
| `qty` | Max: 999999, must be multiple of lot size | "Quantity should be multiple of min lot size." |
| `amount` | If amount-based SIP, amount must not be < LTP | "The SIP amount cannot be less than the LTP." |
| `step_up_freq` | Must be >= `freq` (enum: 3, 5) | "Step-up frequency should be greater than or equal to the SIP frequency." |
| `step_up_amount` & `step_up_qty` | Only one of step\_up\_amount or step\_up\_qty allowed | "Please provide either step\_up\_amount or step\_up\_qty, not both." |
| `step_up_freq` | Step-up not allowed for custom frequency SIP | "Step-up is not allowed for custom frequency SIP." |
| `step_up_amount` / `step_up_qty` | Step-up field must match SIP mode (amount vs qty) | "Please provide step\_up\_amount for amount based SIP or step\_up\_qty for qty based SIP." |
| `hpr` & `lpr` | HPR must be > LPR | "The high price range must be greater than the low price range." |
| `sip_day` | Required for SIP scheduling | "Please select a SIP day." |
| `endTime` | Must be > current day | "End time must be greater than the current day." |
| `endTime` | Expiry date must not fall on weekend | "The expiry date shouldn't be on a weekend." |
| `endTime` (Daily) | Must be >= 4 days from today | "Please select an expiry date at least 4 days from today." |
| `endTime` (Weekly/Monthly) | Must be >= 30 days from today | "Please select an expiry date at least 30 days from today." |
| Custom SIP | Custom SIP for today not allowed past cutoff | "You can't place a custom SIP for today past 11:00 AM." |
| `sip_time` | SIP time cannot be in the past | "The SIP time cannot be in the past. Please select a future date and time." |
| `sip_day` (weekly) | Weekly SIP day must be Mon–Fri (1–5) | "For weekly SIP, please select a day between 1 (Monday) and 5 (Friday)." |
| `sip_day` (monthly) | Monthly SIP day must be 1–28 | "For monthly SIP, please select a day between 1 and 28." |
| `endTime` & `exp_qty` | Provide either endTime or expired quantity, not both | "Please provide either endTime or expired quantity, not both." |
| Daily limit | Max SIP orders allowed | "You have exceeded the maximum limit of creating X SIP orders for the day." |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` for success; negative values indicate errors. |
| `message` | string | Success or error message. Example: "Your Equity SIP for {symbol} has been successfully initiated" |
| `s` | string | "ok" for success, "error" for failure. |
| `id` | string | Unique identifier for the placed SIP order (returned only on success). |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = "YOUR_ACCESS_TOKEN"

fyers = fyersModel.FyersModel(
    client_id=client_id,
    is_async=False,
    token=access_token,
    log_path=""
)

data = {
    "symbol": "NSE:SBIN-EQ",
    "side": 1,
    "amount": 5000,
    "productType": "CNC",
    "freq": 3,
    "sip_day": 15,
    "imd_start": False,
    "endTime": 1771579800,
    "hpr": 900,
    "lpr": 600,
    "step_up_freq": 3,
    "step_up_amount": 500
}

response = fyers.create_smart_order_sip(data=data)
print(response)
```

```
Response structure:
{
  "code": 200,
  "message": "Your Equity SIP for NSE:SBIN-EQ has been successfully initiated",
  "s": "ok",
  "id": "1bf162b1-6406-407a-911a-5a3309e1aaba"
}
```

## Modify Smart Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/modify-smart-order/ (last updated 2026-10-14)*

This API allows you to modify a pending smart order, such as its quantity, price limits or time settings.

USE CASE

Change the quantity, price limits or end time of a smart order without cancelling it.

Send only the fields you want to change.

Note

* The smart order must be paused before it can be modified, except for SIP.
* Partial updates are supported.

* The order must be in a paused state to be modified (except SIP orders).

* Only include the parameters you want to update. All others will retain their original values.

* Certain parameters cannot be modified once the order has started executing.

Details

* You can modify a pending Smart Order by updating parameters such as quantity, price, and time settings, depending on the order type.
* Send the `flowId` plus the fields to change. The fields you can change depend on the order type: Limit (flowtype 4), Trail (6), Step (3) or SIP (7).
* The usual flow is Pause, then Modify, then Resume. Pausing first is not needed for Smart Limit and SIP orders. Resuming is mandatory after a modification.
* Orders that are already executed, cancelled or cancelled by the system cannot be modified.
* `qty` cannot be lower than the remaining quantity. It must be a multiple of the lot size and within the freeze limit.
* For a Step order, `initQty`, `limitPrice` and `orderType` cannot be changed once the order has started.
* For a Trail order, send `unsetTargetPrice` as true to remove the target price. `limitPrice` is required for a Limit order and must be 0 for a Market order.
* For a SIP, the frequency cannot change, and an amount-based SIP cannot be switched to quantity-based or the other way round.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `flowId` | string | Yes | Unique identifier of the Smart Order to be modified |

### Optional Request Attributes (by Order Type)

#### Limit Order (flowtype: 4)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `qty` | int | To update order quantity |
| `limitPrice` | float | To update limit price |
| `stopPrice` | float | To update stop/trigger price |
| `endTime` | int | To update expiry time (Unix timestamp) |
| `hpr` | float | To update upper price limit (High Price Range) |
| `lpr` | float | To update lower price limit (Low Price Range) |
| `mpp` | float | To update market protection percentage |
| `onExp` | int | To update expiry action (`1` = Cancel, `2` = Market Order, MPP: Market Price Protection ) |

#### Trail Order (flowtype: 6)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `qty` | int | To update order quantity |
| `limitPrice` | float | To update limit price (required if `orderType` = 1; must be `0` if `orderType` = 2) |
| `stopPrice` | float | To update stop/trigger price |
| `jump_diff` | float | To update jump value for trailing stop |
| `target_price` | float | To update target price (optional profit booking) |
| `unsetTargetPrice` | boolean | Set `true` to remove/unset the existing `target_price` |
| `mpp` | float | To update market protection percentage |

#### Step Order (flowtype: 3)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `qty` | int | To update total order quantity |
| `startTime` | int | To update order start time |
| `endTime` | int | To update order end time |
| `hpr` | float | To update upper price limit (High Price Range) |
| `lpr` | float | To update lower price limit (Low Price Range) |
| `mpp` | float | To update market protection percentage |
| `avgqty` | int | To update quantity per averaging step |
| `avgdiff` | float | To update price gap between steps |
| `initQty` | int | To update initial quantity (only before order starts) |
| `limitPrice` | float | To update limit price (only before order starts) |
| `direction` | int | To update direction for averaging (`1` = price drop, `-1` = price rise) |

#### SIP Order (flowtype: 7)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `qty` | int | To update investment quantity per instalment |
| `amount` | float | To update investment amount per instalment |
| `hpr` | float | To update upper price limit (skip if price is above this) |
| `lpr` | float | To update lower price limit (skip if price is below this) |
| `sip_day` | int | To update SIP day (applicable for monthly/custom frequency) |
| `sip_time` | int | To update SIP time (required for daily/custom frequency) |
| `step_up_amount` | float | To update step-up amount (amount-based SIP only) |
| `step_up_qty` | int | To update step-up quantity (qty-based SIP only) |
| `exp_qty` | int | To update expiry quantity (optional) |
| `exp_amount` | float | To update expiry amount (optional) |

### Validations & Error Handling

#### General Validations

| **Scenario** | Error Message |
| --- | --- |
| Invalid flowid | "The provided smart order ID is invalid." |
| Invalid request payload | "The input details entered is invalid." |
| Invalid order type | "Invalid Order type" |
| Order not paused (v3) | "The smart order must be paused before it can be modified." |
| Order already executed | "The modification attempt failed as the smart order was already executed." |
| Order already cancelled | "The modification attempt failed as the smart order was already cancelled." |
| Order cancelled by system | "The modification attempt failed as the smart order cancelled by system" |
| Qty < remaining qty | "Modification attempt failed as the specified quantity is less than the remaining quantity." |
| Qty not multiple of lot size | "Quantity should be multiple of min lot size." |
| Qty exceeds freeze limit | "Quantity exceeds the allowable freeze limit." |
| Field not allowed | "Amount field is not allowed." |
| SIP: changing frequency | "SIP frequency cannot be changed. Please use the same frequency as the existing order." |
| SIP: changing amount->qty | "Cannot change from amount-based SIP to qty-based SIP. Please use amount to modify this order." |
| SIP: changing qty->amount | "Cannot change from qty-based SIP to amount-based SIP. Please use qty to modify this order." |

#### Limit Order Validations (flowtype: 4)

| Attribute | **Validation Rule** | Error Message |
| --- | --- | --- |
| `endTime` | Must be within market hours | "End time cannot fall within market closed hours." |
| `endTime` | Must not be in the past | "The end time entered is earlier than the current time." |
| `endTime` | Must be within current day | "The end time cannot extend beyond midnight of the current day." |
| `hpr` (buy) | If provided (>0), must be >= limitPrice | "The maximum price must be higher than the limit price." |
| `lpr` (sell) | If provided (>0), must be <= limitPrice | "The minimum price must be lower than the limit price." |
| `stopPrice` (buy) | If orderType=4, must be < limitPrice | "For buy orders, the stop price must be lower than the limit price." |
| `stopPrice` (sell) | If orderType=4, must be > limitPrice | "For sell orders, the stop price must be higher than the limit price." |
| `mpp` | Must be 0-3 or -1 (disabled) | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |

#### Trail Order Validations (flowtype: 6)

| Attribute | **Validation Rule** | Error Message |
| --- | --- | --- |
| `stopPrice` | Required for trail orders | "Stop Price is required to place orders." |
| `limitPrice` | Required when orderType=1 (Limit) | "Limit price is required." |
| `limitPrice` (buy) | If orderType=1, must be < stopPrice | "For buy orders, the stop price must be lower than the limit price." |
| `limitPrice` (sell) | If orderType=1, must be > stopPrice | "For sell orders, the stop price must be higher than the limit price." |
| `target_price` | If provided (>0), must be > current LTP | "The target price must be greater than the last traded price." |
| `jump_diff` | Must be > 20× tick size | "The jump price must be more than 20 times the tick size." |
| `mpp` | Must be 0-3 or -1 (disabled) | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |

#### Step Order Validations (flowtype: 3)

| Attribute | **Validation Rule** | Error Message |
| --- | --- | --- |
| `startTime` | Not allowed in modify request | "Start time is not required for modify orders." |
| `startTime` | Must not be in the past | "The start time entered is earlier than the current time." |
| `startTime` | Must be within market hours | "Start time cannot fall within market closed hours." |
| `endTime` | Must not be in the past | "The end time entered is earlier than the current time." |
| `endTime` | Must be within market hours | "End time cannot fall within market closed hours." |
| `avgqty` | Must be multiple of lot size | "Avg quantity should be multiple of min lot size." |
| `initQty` | Cannot modify after order starts | "You cannot modify the initial quantity after the order has been placed." |
| `limitPrice` | Cannot modify after order starts | "You cannot modify the Limit price after the order has been placed." |
| `orderType` | Cannot modify after order starts | "You cannot modify the order type after the order has been placed." |
| `qty` | Total qty >= initQty + avgQty | "Total Quantity should be greater than or equal to the sum of Initial Qty and Average Qty." |
| `mpp` | Must be 0-3 or -1 (disabled) | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` for success; negative values indicate errors. |
| `message` | string | Message indicating success or failure. Example: "Request sent successfully to modify smart order." |
| `s` | string | "ok" for success, "error" for failure. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = ""

## Initialize the FyersModel instance with your clientid, access_token, and enable async mode_
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data ={
  "flowId": "b86ee5e4-df36-47b3-a08f-dfb58e94472c",
  "qty": 5,
  "limitPrice": 760,
  "endTime": 1768989000
}

response = fyers.modify_smart_order(data=data)
print(response)
```

```
Response structure:
{
  "code": 200,
  "message": "Request sent successfully to modify smart order",
  "s": "ok"
}
```

## Cancel Smart Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/cancel-smart-order/ (last updated 2026-10-14)*

This API allows you to cancel a pending smart order.

USE CASE

Cancel a smart order you no longer want. A cancelled order cannot be resumed, so pause it instead if you may need it later.

Details

* Cancel a pending Smart Order. Once cancelled, the order cannot be resumed.
* Send only the `flowId` of the smart order. You can find it in the Smart Order Book.
* Cancellation is rejected if the order is already executed, already cancelled or was cancelled by the system.
* The success message says the request was sent. Check the Smart Order Book for the final state.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `flowId` | string | Yes | Unique identifier of the Smart Order to cancel |

### Validations & Error Handling

| **Scenario** | Error Message |
| --- | --- |
| Invalid flowid | "The provided smart order ID is invalid." |
| Invalid request payload | "The input details entered is invalid." |
| Internal error | "Error in Unmarshal" |
| Order already executed | "The cancellation attempt failed as the smart order was already executed." |
| Order already cancelled | "The cancellation attempt failed as the smart order was already cancelled." |
| Order cancelled by system | "The cancellation attempt failed as the smart order cancelled by system" |
| Invalid cancel request | "Smart order cannot be cancel." |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` for success; negative values indicate errors. |
| `message` | string | "Request sent successfully to cancel smart order" or error description. |
| `s` | string | "ok" for success, "error" for failure. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = "XXXXXXXXXXX"

## Initialize the FyersModel instance with your clientid, access_token, and enable async mode_
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data ={
  "flowId": "b86ee5e4-df36-47b3-a08f-dfb58e94472c"
}
cancel_order = fyers.cancel_smart_order(data=data)
print(cancel_order)
```

```
Response structure:
{
  "code": 200,
  "message": "Request sent successfully to cancel smart order",
  "s": "ok"
}
```

## Pause or Resume Smart Order

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/pause-or-resume-smart-order/ (last updated 2026-10-14)*

This API allows you to pause a running smart order and resume it later.

USE CASE

Pause a smart order temporarily without cancelling it, then resume it when you are ready.

Pause an order before modifying it, then resume it.

Details

* Pause a running smart order. This temporarily stops order execution without cancelling it.
* To modify a Smart Order, it must be paused first (pausing is not mandatory for Smart Limit order modification).
* The order can be resumed later using the Resume API.
* Both calls take only the `flowId` of the smart order.
* Pause is rejected if the order is already executed, cancelled, rejected, already paused or in progress, or if it failed during creation, modification, resume, pause or deletion.
* A Smart Limit order cannot be paused during market hours.
* Resume works only on a paused order. It is rejected if the order is not paused, already running, in progress, executed or cancelled.
* Resuming is mandatory after you modify an order.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `flowId` | string | Yes | Unique identifier of the smart order to pause |

### Validations & Error Handling

| **Scenario** | Error Message |
| --- | --- |
| Invalid flowId | "The provided smart order ID is invalid." |
| Internal error | "Error in Unmarshal" |
| Order already executed | "You are attempting to pause a smart order that has already been executed." |
| Order already cancelled | "You are attempting to pause a smart order that has already been cancelled." |
| Order already paused | "The smart order is already paused and cannot be paused again." |
| Order in progress | "The smart order cannot be paused as it is already in progress." |
| Limit order during market hours | "Pausing is not allowed during market hours for limit orders." |
| Order cancelled by system | "The pause attempt failed as the smart order cancelled by system" |
| Invalid pause request | "Smart order cannot be paused." |
| Failed during creation | "The smart order cannot be paused as it has failed during creation." |
| Failed during modification | "The smart order cannot be paused as it has failed during modification." |
| Failed during resume | "The smart order cannot be paused as it has failed during resume." |
| Failed during pause | "The smart order cannot be paused as it has failed during pause." |
| Failed during deletion | "The smart order cannot be paused as it has failed during deletion." |
| Rejected | "The smart order cannot be paused as it has been rejected." |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` for success, negative values for errors |
| `message` | string | "Request sent successfully to pause smart order." or an error description |
| `s` | string | "ok" for success, "error" for failure |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = ""

## Initialize the FyersModel instance with your clientid, access_token, and enable async mode_
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data ={
  "flowId": "356b4c5c-411b-46e9-9af3-edc2147c98ba"
}
pause_order = fyers.pause_smart_order(data=data)
print(pause_order)
```

```
Response structure:
{
  "code": 200,
  "message": "Request sent successfully to pause smart order",
  "s": "ok"
}
```

Details

* Resume a paused Smart Order. This restarts the order for execution and is mandatory after modifying the order.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `flowId` | string | Yes | Unique identifier of the smart order to resume |

### Validations & Error Handling

| **Scenario** | Error Message |
| --- | --- |
| Invalid flowId | "The provided smart order ID is invalid." |
| Internal error | "Error in Unmarshal" |
| Order not paused | "The smart order must be paused before it can be resumed." |
| Order already executed | "The smart order has already been executed and cannot be resumed." |
| Order already cancelled | "A canceled smart order cannot be resumed." |
| Order already running | "The smart order is already resumed and cannot be resumed again." |
| Order in progress | "The smart order cannot be resumed as it is already in progress." |
| Order cancelled by system | "The resume attempt failed as the smart order cancelled by system" |
| Invalid resume request | "Smart order cannot be resumed." |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` for success, negative for errors |
| `message` | string | "Request sent successfully to resume smart order." or error description |
| `s` | string | "ok" for success, "error" for failure |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = ""

## Initialize the FyersModel instance with your clientid, access_token, and enable async mode_
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "flowId": "356b4c5c-411b-46e9-9af3-edc2147c98ba"
}
resume_order = fyers.resume_smart_order(data=data)
print(resume_order)
```

```
Response structure:
{
  "code": 200,
  "message": "Request sent successfully to resume smart order",
  "s": "ok"
}
```

## Exit Position

*Source: https://fyers.in/api-docs/v3/api/trading/positions/exit-position/ (last updated 2026-10-14)*

This API allows you to exit all or selected open positions in a single request.

USE CASE

Close all your open positions quickly when you want to get out of the market.

Details

* This allows the user to either exit all open positions or any specific open position.
* Send no `id` and every open position is closed. Send a position id, or a list of ids, to exit only those positions.
* The exit is done with counter orders. Response code 201 means a counter order was placed but not filled, because of low liquidity or another reason.
* The response confirms the exit request. Check Get Positions and Get Orders for the final state.
* To cancel pending orders before exiting, send `pending_orders_cancel` as 1 in the DELETE body, and add `id` to limit it to one symbol.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `Id` | string | In case id is not passed, then all the open positions will be closed |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | * This is the code to identify specific responses . * If 201 comes in code it implies that counter order has been placed but not filled due to low liquidity or any other reason |
| `message` | string | * Message to clarify the request status. * Eg:All positions are closed |

Sample Request :

```
  {
    "id": [positionId1,positionId2]
  }
```

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {}

response = fyers.exit_positions(data=data)

print(response)
```

```
{
   "s": "ok",
   "code": 200,
   "message": "The position is closed."
 }
```

Details

* This is an added functionality for exit position API. If a user has open positions in particular stocks and also working opposite order of the particular stock, the user can close the working orders and then exit the open positions.
* The following should be passed in the body of the DELETE method of positions to cancel the pending orders:
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

```
{"pending_orders_cancel": 1}
```

If only a single symbol's order and position needs to be cancelled, the position ID should also be sent in the body:

```
{"id": "NSE:SBIN-EQ-INTRADAY","pending_orders_cancel": 1}
```

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `pending_orders_cancel`\* | int | Must be set to `1` in the request body to cancel the pending working order(s) associated with a position before exiting it. Eg: 1 |
| `id` | string | Optional. Position ID to target a single symbol's working order and position for cancellation/exit instead of all. Eg: NSE:SBIN-EQ-INTRADAY |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Status of the request. Eg: ok / error |
| `code` | int | Response code identifying the specific response. Eg: 200 |
| `message` | string | Message describing the result of the request. Eg: The position is closed. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Authorization:app_id:access_token" -H "Content-Type: application/json" -X DELETE -d '{"pending_orders_cancel": 1}' https://api-t1.fyers.in/api/v3/positions
```

```
{
 "s": "ok",
 "code": 200,
 "message": "The position is closed."
}
```

VIDEO LEARNING

### Video learning

[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Exit Position by ID

*Source: https://fyers.in/api-docs/v3/api/trading/positions/exit-position-by-id/ (last updated 2026-10-14)*

This API allows you to exit specific open positions using their position IDs.

USE CASE

Close one or a few positions while leaving the rest untouched.

Details

* `id` takes one position id, for example `NSE:SBIN-EQ-MARGIN`, or a list such as `["NSE:SBIN-EQ-INTRADAY","NSE:SBIN-EQ-CNC"]`.
* Only the open positions for the ids you pass are exited. Other positions are not affected.
* A position id is the symbol plus the product type, so the same stock held under two product types has two ids. Get them from Get Positions.
* This works like Exit Position. If `id` is left out, all open positions are closed.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id` | string or [string] | * Optional * Eg: NSE:SBIN-EQ-MARGIN * This will only exit the open positions for a particular position id or list of position id provided like ["NSE:SBIN-EQ-INTRADAY","NSE:SBIN-EQ-CNC"] |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status, e.g. `ok` on success. |
| `code` | int | Response status code (e.g. `200` on success). |
| `message` | string | Human-readable message describing the outcome, e.g. "The position is closed." |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "id":"NSE:SBIN-EQ-MARGIN"
}

response = fyers.exit_positions(data=data)
print(response)
```

```
{
   "s": "ok",
   "code": 200,
   "message": "The position is closed."
 }
```

VIDEO LEARNING

### Video learning

[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Exit Positions by Filters

*Source: https://fyers.in/api-docs/v3/api/trading/positions/exit-positions-by-filters/ (last updated 2026-10-14)*

This API allows you to exit open positions that match a segment, side and product type.

USE CASE

Close every position of a chosen segment, side and product type in one request.

Details

* `segment`, `side` and `productType` are all mandatory, and each takes a list. Example: `segment` [10,12], `side` [1,-1], `productType` ["INTRADAY","CNC"].
* `segment` values: 10 (Capital Market), 11 (Equity Derivatives), 12 (Currency Derivatives), 20 (Commodity Derivatives).
* `side` values: 1 (buy side) and -1 (sell side). Pass both to cover both sides.
* `productType` values: "INTRADAY", "CNC", "MARGIN" or "ALL".
* This works like Exit Position. To exit specific positions by id, use Exit Position by ID.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `segment`\* | [ int ] | * **Mandatory** * In the API , to close your position for a specific segment, you need to use the "segment" parameter with one of the following possible values: 10(Capital Market),11(Equity Derivatives),12(Currency Derivatives),20(Commodity Derivatives). Eg: [10,12] |
| `side`\* | [ int] | * **Mandatory** * In the API , to close your position for a specific side, you need to use the "side" parameter with one of the following possible values: 1(Buy side),-1(Sell side). Eg: [1,-1] |
| `productType`\* | [ string ] | * **Mandatory** * In the API , to close your position for a specific orderType, you need to use the "productType" parameter with one of the following possible values: "INTRADAY","CNC","MARGIN","ALL". Eg: ["INTRADAY","CNC"] |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status - `ok` / `error` |
| `code` | int | Code identifying the specific response |
| `message` | string | Message clarifying the request status, e.g. "The position is closed." |

Request

```
from fyers_apiv3 import fyersModel

client_id = "SPXXXXE7-100"
access_token = "eyJ0eXAiOiJK***.eyJpc3MiOiJhcGkuZnllcnM***.IzcuRxg4tnXiULCx3***"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="/home/user/logs")

data = {
    "segment":[10],
    "side":[1,-1],
    "productType":["INTRADAY","CNC"]
   }

response = fyers.exit_positions(data=data)
print(response)
```

```
{
   "s": "ok",
   "code": 200,
   "message": "The position is closed."
 }
```

VIDEO LEARNING

### Video learning

[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Convert Position

*Source: https://fyers.in/api-docs/v3/api/trading/positions/convert-position/ (last updated 2026-10-14)*

This API allows you to convert an open position from one product type to another.

USE CASE

Change the product type of an open position without closing it and placing a new order.

Note

* CNC and MTF positions cannot be converted.
* You also cannot convert positions to MTF.

Details

* This allows the user to convert an open position from one product type to another.
* `symbol` takes the position id, for example `NSE:SBIN-EQ-INTRADAY`. Get it from Get Positions.
* `overnight`: send 1 if the position is a carry forward position. Send 0 if the position was taken today, whatever its product type.
* `positionSide`: 1 for open long positions and -1 for open short positions.
* `convertQty` is the quantity to convert. For derivatives it has to be a multiple of the lot size.
* A request that is not allowed returns an error `message`, for example that a CNC position cannot be converted to INTRADAY or MARGIN.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | * Mandatory. pass the position id here * Eg: NSE:SBIN-EQ-INTRADAY |
| `overnight`\* | int | Mandatory. if the position to be converted is a carry forward position, then send overnight flag as 1. If the position is taken today, irrespective of its product type, then send overnight flag as 0 |
| `positionSide`\* | int | * Mandatory. * 1 => Open long positions * -1 => Open short positions [View Details](https://fyers.in/api-docs/v3/api/appendix/position-sides/) |
| `convertQty`\* | int | Mandatory. Quantity to be converted. Has to be in multiples of lot size for derivatives |
| `convertFrom`\* | string | * Mandatory. Existing productType * (CNC positions cannot be converted) * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `convertTo`\* | string | * Mandatory. The new product type * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |

**Notes**

* CNC and MTF positions cannot be converted.

* You cannot convert positions to MTF.

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | * Message to clarify the request status. * Eg: You cannot convert CNC position to INTRADAY / MARGIN. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "symbol":"MCX:SILVERMIC20NOVFUT",
    "positionSide":1,
    "convertQty":1,
    "convertFrom":"INTRADAY",
    "convertTo":"CNC"
}

response = fyers.convert_position(data=data)
print(response)
```

```
{
  "s": "ok",
  "code": 200,
  "message": "Position Converted Successfully!!",
  "positionDetails": 1101
}
```

VIDEO LEARNING

### Video learning

[Convert open positions easily (REST and cURL)REST and cURL · 3:45](https://www.youtube.com/watch?v=rWqAEW0AkuE&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[All transactions explained (Node.js)Node.js · 8:12](https://www.youtube.com/watch?v=jLUBwogNjT8&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[All transactions explained (C#)C# · 8:33](https://www.youtube.com/watch?v=BCqEo4fmuDM&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[All transactions explained (Java)Java · 6:21](https://www.youtube.com/watch?v=GfbR4rjnYpM&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Set Stop Loss & Target

*Source: https://fyers.in/api-docs/v3/api/trading/positions/set-stop-loss-and-target/ (last updated 2026-10-14)*

This API allows you to add a Stop Loss and Take Profit to an open position.

USE CASE

Set your exit levels on a position after its entry order has traded.

Details

* This allows the user to add Stop Loss and Take Profit to an existing open position.
* `positionId` is mandatory, for example `NSE:KWIL-EQ-INTRADAY`. Send `stopLoss`, `takeProfit` or both.
* `legType` is optional: 1 = offset, 2 = percentage.
* `qty` is optional and its maximum is the position quantity.
* The same API is used to modify and to cancel these levels later.
* This is the Positions API, for an open position. To add Take Profit and Stop Loss to an order that is still pending, see [Creating TPSL](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#creating-tpsl) in the Order Placement Guide.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `positionId`\* | string | * Mandatory. Position id * Eg: NSE:KWIL-EQ-INTRADAY |
| `takeProfit` | float | Take profit value |
| `stopLoss` | float | Stop loss value |
| `qty` | int | Optional. Max qty should be position qty |
| `legType` | int | Optional. `1` = offset, `2` = percentage |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status, `ok` on success or `error` on failure |
| `code` | int | Response code (e.g. `1102` on success) |
| `message` | string | Status message, e.g. "Successfully modified order" |
| `id_fyers` | string | Fyers-generated identifier for the position/order operation the stop-loss/target was attached to |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "positionId": "NSE:TMPV-EQ-CNC",
    "takeProfit": 11,
    "stopLoss": 6
}

response = fyers.attach_position_legs(data=data)
print(response)
```

```
{
  "code": 1102,
  "message": "Successfully modified order",
  "s": "ok",
  "id_fyers": "0ac7e98f-b915-4385-a7d5-fe5cdf555105"
}
```

## Modify Stop Loss & Target

*Source: https://fyers.in/api-docs/v3/api/trading/positions/modify-stop-loss-and-target/ (last updated 2026-10-14)*

This API allows you to modify the Stop Loss and Take Profit of an open position.

USE CASE

Tighten a stop loss as the price moves in your favour.

Details

* This allows the user to modify the Stop Loss and Take Profit for an existing open position. User can provide the parameters that need to be modified. In case a particular parameter has not been provided, the original value will be considered.
* Send only what you want to change. A `stopLoss` or `takeProfit` you leave out keeps its original value.
* `positionId` is mandatory, for example `NSE:KWIL-EQ-INTRADAY`. `qty` is optional and its maximum is the position quantity.
* `legType` is optional: 1 = offset, 2 = percentage.
* To remove a level instead of changing it, pass `null` for it. See [Cancel Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/cancel-stop-loss-and-target/).
* This is the Positions API, for an open position. To change Take Profit and Stop Loss on an order that is still pending, see [Modifying TPSL](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#modifying-tpsl) in the Order Placement Guide.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `positionId`\* | string | * Mandatory. Position id * Eg: NSE:KWIL-EQ-INTRADAY |
| `takeProfit` | float | Take profit value. If not provided, the original value will be considered |
| `stopLoss` | float | Stop loss value. If not provided, the original value will be considered |
| `qty` | int | Optional. Max qty should be position qty |
| `legType` | int | Optional. `1` = offset, `2` = percentage |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Response code returned by the API. `1102` indicates the stop-loss/target modification request was accepted |
| `s` | string | Status of the request, e.g. `ok` |
| `message` | string | Human-readable message describing the result of the request, e.g. "Successfully modified order" |
| `id_fyers` | string | Unique identifier generated by FYERS for this modify stop-loss/target request |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "positionId": "NSE:TMPV-EQ-CNC",
    "takeProfit": 11,
    "stopLoss": 6,
    "legType": 1
}

response = fyers.attach_position_legs(data=data)
print(response)
```

```
{
  "code": 1102,
  "message": "Successfully modified order",
  "s": "ok",
  "id_fyers": "0ac7e98f-b915-4385-a7d5-fe5cdf555105"
}
```

## Cancel Stop Loss & Target

*Source: https://fyers.in/api-docs/v3/api/trading/positions/cancel-stop-loss-and-target/ (last updated 2026-10-14)*

This API allows you to cancel the Stop Loss and Take Profit of an open position.

USE CASE

Remove the exit levels from a position and manage the exit yourself.

Note

Only the parameter passed as `null` is cancelled. If a parameter is not included in the request, its existing value remains unchanged.

Details

* To cancel the Stop Loss or Take Profit added to an open position, use the Modify Stop Loss and Take Profit API and pass `null` for the applicable parameter.
* This uses the same API as **Set stop-loss and target** and **Modify stop-loss and target**.
* **Cancel only Take Profit** - send `{"positionId": "NSE:KWIL-EQ-INTRADAY", "takeProfit": null}`
* **Cancel only Stop Loss** - send `{"positionId": "NSE:KWIL-EQ-INTRADAY", "stopLoss": null}`
* **Cancel both Stop Loss and Take Profit** - send `{"positionId": "NSE:KWIL-EQ-INTRADAY", "takeProfit": null, "stopLoss": null}`
* The position itself stays open. Only the stop loss or take profit you pass as `null` is removed.
* `positionId` is mandatory, for example `NSE:KWIL-EQ-INTRADAY`. Get it from Get Positions.
* This is the Positions API, for an open position. To cancel Take Profit and Stop Loss on an order that is still pending, see [Cancelling TPSL](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/#cancelling-tpsl) in the Order Placement Guide.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `positionId`\* | string | * Mandatory. Position id * Eg: NSE:KWIL-EQ-INTRADAY |
| `takeProfit` | float / null | Pass `null` to cancel the Take Profit. If not included, the existing value remains unchanged |
| `stopLoss` | float / null | Pass `null` to cancel the Stop Loss. If not included, the existing value remains unchanged |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Response status: `ok` / `error` |
| `code` | int | Response code, e.g. `1102` on success |
| `message` | string | Response message, e.g. `Successfully modified order` |
| `id_fyers` | string | Internal Fyers reference id generated for the request |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
## Cancel only Take Profit
curl -H "Authorization:app_id:access_token" -H "Content-Type: application/json" -X PATCH -d '{
  "positionId": "NSE:KWIL-EQ-INTRADAY",
  "takeProfit": null
}' https://api-t1.fyers.in/api/v3/positions

## Cancel only Stop Loss
curl -H "Authorization:app_id:access_token" -H "Content-Type: application/json" -X PATCH -d '{
  "positionId": "NSE:KWIL-EQ-INTRADAY",
  "stopLoss": null
}' https://api-t1.fyers.in/api/v3/positions

## Cancel both Stop Loss and Take Profit
curl -H "Authorization:app_id:access_token" -H "Content-Type: application/json" -X PATCH -d '{
  "positionId": "NSE:KWIL-EQ-INTRADAY",
  "takeProfit": null,
  "stopLoss": null
}' https://api-t1.fyers.in/api/v3/positions
```

## Individual App

*Source: https://fyers.in/api-docs/v3/getting-started/create-an-app/individual-app/*

A FYERS API app connects your application to your FYERS account. Create the app before starting authentication or making API requests.

Individual apps are created for your own personal usage. An individual app can be used only by the creator of the app; no other client can log in and make use of it. To let other FYERS clients log in to your application, use a [Third-Party App](https://fyers.in/api-docs/v3/getting-started/create-an-app/third-party-app/).

### Trading app and non-trading app

There are two types of individual apps. Use a trading app to place orders. Use a non-trading app when you only need data.

| Feature | Trading appPlace orders and fetch data | Non-trading appFetch data only |
| --- | --- | --- |
| Order placement | Allowed | Not allowed |
| Data & User info APIs | Available | Available |
| Number of apps | One per userAs per the [retail algo trading regulations](https://fyers.in/community/t/sebis-new-algo-trading-rules-kick-in-on-april-1-here-is-what-changes-for-you/12267) | Multiple |
| Static IP | RequiredPrimary IP mandatory, Secondary IP optional | Not required |
| Redirect URL | Required | Required |
| How to set it up | [Activate it in My apps](#activate-your-trading-app) | [Create non-trading app](#create-a-non-trading-app) |

To know which APIs are Data & User info APIs, see [Types of APIs](https://fyers.in/api-docs/v3/getting-started/#types-of-apis).

### Activate your trading app

1. Log in to the [API Dashboard](https://fyers.in/web/api-dashboard/user-apps).
2. In **My apps**, select your trading app (Type: **Trading**).
3. Provide the following details:
   * Primary IP address (mandatory)
   * Secondary IP address (optional)
   * Redirect URL
   * Webhook Details (Optional)
4. Accept the API Terms and Conditions and click **Activate**.

![Activate the trading app in the API Dashboard](https://assets.fyers.in/Marcom_Avatar/Images/api-dashboard-activate-trading-app.png)

**Note**

Once you set the static IP addresses, you can’t change them for the next 7 days. Static IPs can be shared within family accounts.

### Create a non-trading app

1. Log in to the [API Dashboard](https://fyers.in/web/api-dashboard/user-apps).
2. Click **Create non-trading app**.
3. Provide the following details:
   * App Name
   * Redirect URL
   * Webhook Details (Optional)
4. Accept the API Terms and Conditions and click **Create**.

![Create a non-trading app in the API Dashboard](https://assets.fyers.in/Marcom_Avatar/Images/api-dashboard-create-non-trading-app.png)

A non-trading app gets Profile details, Transaction info, Historical data, and Quotes and market data. Order placement is not granted.

Securely store the App ID and App Secret the dashboard gives you. You need both for authentication.

### Redirect URI

After a user logs in with their FYERS credentials, they are redirected to the app’s redirect URI with the authorization details. This applies to both trading and non-trading apps.

We recommend the FYERS redirect URL:

```
https://trade.fyers.in/api-login/redirect-uri/index.html
```

You can also use any other redirect URL. If you use your own, it should be an endpoint you control, because the auth code it receives is sensitive information.

### What you will use next

app\_id

#### App ID

Identifies your application during OAuth authentication.

## Third-Party App

*Source: https://fyers.in/api-docs/v3/getting-started/create-an-app/third-party-app/ (last updated 2026-10-14)*

These apps are used by platform providers which would allow end users to login to the app and make use of the functionality. These apps are created by third party application providers to enable FYERS clients to use their applications.

To create a common app, you can get in touch with us at [[email protected]](/cdn-cgi/l/email-protection#e786978eca94929797889593a7819e829594c98e89).

### Redirect URI

After a user logs in with their FYERS credentials, they are redirected to the app’s redirect URI with the authorization details. The redirect URI should be an endpoint you control — since the values it receives are sensitive, never point it at a public or third-party endpoint you don’t own.

## Plans & Limits

*Source: https://fyers.in/api-docs/v3/getting-started/plans-and-limits/ (last updated 2026-10-14)*

Before you build, check whether the Standard plan supports your expected request volume, historical-data requirement and WebSocket subscriptions. The Standard plan is free and includes usage limits to ensure fair access for all users. FYERS Prime is a subscription plan that expands these limits for users with higher data and scale requirements.

### API request limits

| API category | Standard plan | Prime plan |
| --- | --- | --- |
| Data APIs | 5 requests/second 50 requests/minute 5,000 requests/day | 10 requests/second 500 requests/minute 5,00,000 requests/day |
| Transaction + User Info APIs | 10 requests/second 200 requests/minute 1,00,000 requests/day | 10 requests/second 500 requests/minute 5,00,000 requests/day |

### Market-data access

| Feature | Standard plan | Prime plan |
| --- | --- | --- |
| [Quotes API](https://fyers.in/api-docs/v3/api/market-data/quotes/#new) | 50 symbols/request | 1,000 symbols/request |
| Historical data - Daily | Last 5 years | 25+ years |
| Historical data - Intraday | Last 1 year | 5+ years |
| Seconds Data | Not Available | Last 30 days |
| Expired F&O Data - Daily | Last 2 years | 7+ years |
| Expired F&O Data - Intraday | 10 API requests/day | As per Prime API overall rate limits |
| Screeners | 50 API requests/day | As per Prime API overall rate limits |

### WebSocket subscription limits

| Socket | Standard plan | Prime plan |
| --- | --- | --- |
| Data Socket | 100 symbols | 5,000 symbols |
| Tick-by-Tick (TBT) Socket | 1 symbol | 15 symbols |

Symbol limits apply per user, across all your connections to that socket, not per connection. If a subscription would go over the limit, the connection is not established. On the Prime plan the Tick-by-Tick (TBT) Socket allows 15 symbols in total: up to 3 connections with 5 symbols each.

Upgrade plan

### When FYERS Prime is relevant

Take a FYERS Prime subscription through FYERS Web or App → Profile → FYERS Prime, or visit the FYERS Prime page.

* You need significantly higher Data API throughput.
* You need longer daily or intraday historical-data coverage.
* You need Seconds Data or broader Expired F&O Data access.
* You need to subscribe to more symbols through Data Socket or Tick-by-Tick (TBT) Socket.

[Explore Prime details ↗](https://fyers.in/prime)[Join Prime ↗](https://fyers.in/web/profile/prime)

HTTP 429

### When a rate limit is reached

`Error Code -429`The API returns error code -429 when the applicable per-second, per-minute or per-day limit is exceeded.

Stop repeated requests, wait for the applicable limit window to reset and reduce unnecessary calls. FYERS Prime provides higher limits for supported API categories.

Rate-limit error: triggered when the applicable per-second, per-minute or per-day request limit is exceeded.

**User blocking:** if the per-minute rate limit is exceeded more than 3 times in a day, the user is blocked for the rest of the day.

## Individual App Authentication

*Source: https://fyers.in/api-docs/v3/api/authentication/individual-app/ (last updated 2026-10-14)*

This section explains how to authenticate your own FYERS account with an individual app and get an access token for all later requests.

Individual apps are created for your own use. Only the creator can log in with the app; no other client can use it. Create the app in the API [Dashboard](https://fyers.in/web/api-dashboard/user-apps) with a redirect URL that you control. See [Create an app](https://fyers.in/api-docs/v3/getting-started/create-an-app/individual-app/).

* Access tokens expire daily at 6:30 AM. Generate a new token after 6:30 AM for it to remain valid throughout the day.
* Send `app_id:access_token` in the HTTP `Authorization` header on every request after login. See [API Standards](https://fyers.in/api-docs/v3/api/api-standards/#authorization-header).

| Endpoint | Method | Description |
| --- | --- | --- |
| [Authentication Flow](https://fyers.in/api-docs/v3/api/authentication/individual-app/authentication-flow/) | — | This guide explains the steps that turn a FYERS login into an access token for your individual app. |
| [Generate Auth Code](https://fyers.in/api-docs/v3/api/authentication/individual-app/generate-auth-code/) | GET | This API allows you to send a user to the FYERS login page and receive an auth code on your redirect URI. |
| [Validate Auth Code (Generate Access Token)](https://fyers.in/api-docs/v3/api/authentication/individual-app/validate-auth-code/) | POST | This API allows you to exchange an auth code for an access token. |
| [Best Practices](https://fyers.in/api-docs/v3/api/authentication/individual-app/best-practices/) | — | This guide lists the practices that keep your app credentials and tokens secure. |

## Third-Party App Authentication

*Source: https://fyers.in/api-docs/v3/api/authentication/third-party-app/ (last updated 2026-10-14)*

This section explains how to let FYERS clients log in to your platform with their own credentials. Third-party apps are created by platform providers so that FYERS clients can use their applications.

To create a common app, you can get in touch with us at [[email protected]](/cdn-cgi/l/email-protection#81e0f1e8acf2f4f1f1eef3f5c1e7f8e4f3f2afe8ef).

Third-party apps use the OAuth 2.0 authorization code flow. Send the user to the FYERS login page, receive an `auth_code` at your `redirect_uri`, then exchange it from your backend server for an `access_token`. The flow is not recommended for single-page applications.

* `redirect_uri` must be the same URL provided at app creation. Keep it under your control, because the auth token is sensitive.
* `appIdHash` is the SHA-256 hash of `app_id:app_secret`. You can use this [online tool](https://emn178.github.io/online-tools/sha256.html) for reference.
* Access tokens expire daily at 6:30 AM. Generate a new token after 6:30 AM for it to remain valid throughout the day.
* Send `app_id:access_token` in the HTTP `Authorization` header on every request after login. See [API Standards](https://fyers.in/api-docs/v3/api/api-standards/#authorization-header).
* Never store the `app_secret` in front-end code. See the [Best Practices](https://fyers.in/api-docs/v3/api/authentication/third-party-app/best-practices/).

| Endpoint | Method | Description |
| --- | --- | --- |
| [OAuth 2.0 Flow](https://fyers.in/api-docs/v3/api/authentication/third-party-app/oauth-2-0-flow/) | — | This guide explains how your platform logs in FYERS users and gets an access token for each of them. |
| [User Authorization](https://fyers.in/api-docs/v3/api/authentication/third-party-app/user-authorization/) | GET | This API allows you to send a user to the FYERS login page to authorize your app. |
| [Authorization Code](https://fyers.in/api-docs/v3/api/authentication/third-party-app/authorization-code/) | — | This page describes the auth\_code and state that FYERS sends to your redirect\_uri after the user logs in. |
| [Generate Access Token](https://fyers.in/api-docs/v3/api/authentication/third-party-app/generate-access-token/) | POST | This API allows you to exchange an auth code for the access token of a user. |
| [Best Practices](https://fyers.in/api-docs/v3/api/authentication/third-party-app/best-practices/) | — | This guide lists the practices that keep your app credentials and users' tokens secure. |

## API Error Codes

*Source: https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/ (last updated 2026-10-14)*

Standard API error codes with descriptions. Read each code together with the response message.

**What to do when an API returns an error:** Follow the step-by-step workflow in [Handle errors and rate limits](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/). For the request limits that apply to your plan, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### HTTP Status Codes

The HTTP status code on the response indicates the general outcome of the request. Read it together with the response body for the exact condition.

| Status Code | Meaning |
| --- | --- |
| 200 | Request was successful. |
| 400 | Bad request. The request is invalid, or certain other errors. |
| 401 | Authorization error. The user could not be authenticated. |
| 403 | Permission error. The user does not have the necessary permissions. |
| 429 | Rate limit exceeded. The user has been blocked for exceeding the rate limit. |
| 500 | Internal server error. |

### Application Error Codes

Read the error code together with the complete response message. The code identifies the category; the message explains the exact condition returned for the request.

| Code | Description |
| --- | --- |
| -8 | The access token has expired. Generate a valid token before sending the request again. |
| -15 | An invalid access token was provided. Check the token used in the request. |
| -16 | The server could not authenticate the user token. Verify the authentication details and try again after correcting them. |
| -17 | The access token is invalid or has expired. Complete the required authentication flow and use a valid token. |
| -50 | One or more request parameters are invalid. Read the message field for details about the affected input. |
| -51 | The Order ID is invalid while fetching or modifying an order. Check the Order ID and the operation being performed. |
| -53 | The Position ID is invalid. Check the current positions and use the correct Position ID. |
| -99 | The order placement was rejected. Read the rejection message in the API response before taking another action. |
| -300 | The symbol is invalid. Verify it through Appendix → Symbol Master. For direct URLs, URL-encode symbols containing special characters; FYERS SDKs handle this automatically. |
| -352 | The App ID is invalid. Check the App ID configured for the request. |
| -352 | No position is available to exit. Read the response message and request context to identify which -352 condition applies. |
| -360 | A Standard plan user exceeded the API rate limit (per second, minute or day). Upgrade to Prime for higher API limits. To know more, visit [<https://fyers.in/web/profile/prime>](https://fyers.in/web/profile/prime). |
| -429 | The API rate limit was exceeded for the applicable second, minute or day limit. Stop repeated calls, wait for the limit window and then retry. |
| 400 | The multi-leg order request contains invalid input. Review the required fields and values for every leg. |

The same error code may be used for more than one condition. Use the response message and API operation to identify the correct cause before retrying.

## API Standards

*Source: https://fyers.in/api-docs/v3/api/api-standards/ (last updated 2026-10-14)*

Shared rules and conventions for working with FYERS APIs.

Follow these conventions when building requests, handling responses, working with timestamps, interpreting errors, and implementing retries.

### Base URLs

* Use the host documented on the specific API page.
* `REST` APIs and `WebSocket` services use different hosts.
* Do not reuse a REST base URL for a socket connection.

### Authentication

#### Transport security

FYERS APIs are built with security in mind to prevent unauthorised transactions. All API requests and responses are sent and received only over the HTTPS protocol.

#### Authorization header

After authentication you receive an `access_token`. Send your App ID and access token together as `app_id:access_token` in the HTTP `Authorization` header on every subsequent request.

```
curl -H "Authorization: app_id:access_token"
curl -H "Authorization: aaa-99:bbb"
```

Send an active access token on authenticated requests. Keep tokens private — never log them or ship them in client-side or public code. Use the exact format on the API page when a documented header differs.

### Request and response format

* Follow the method, URL, and fields on that API page.
* Send required fields in the documented format.
* Validate the response before using it in a trading workflow.

#### Success response

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `ok` |
| `code` | int | `200` |
| `message` | string | Empty string on success. |
| Additional key | object / list / int / string | Each request returns its own key based on the request. |

#### Failure response

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `error` |
| `code` | int | Negative integer that identifies the specific error. |
| `message` | string | Error message that identifies the error. |
| HTTP header | int | HTTP status code. See [Common API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/#application-error-codes). |

### HTTP status codes

| Status code | Meaning |
| --- | --- |
| `200` | Request was successful. |
| `400` | Bad request — the request is invalid, or another client-side error occurred. |
| `401` | Authorization error — the user could not be authenticated. |
| `403` | Permission error — the user does not have the necessary permissions. |
| `429` | Rate limit exceeded — the user has been blocked for exceeding the rate limit. |
| `500` | Internal server error. |

### Status and error model

Read the response code and message together before deciding the next action. Common cases are success, invalid input, auth failure, rate limit and order rejection.

Use [Appendix → Common API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/#application-error-codes) for the standard description and next action of each app-level error code (the negative `code` values in a failure response).

### Timestamps and timezones

* Use the timestamp format shown on the API page.
* Keep request, storage, and display handling consistent.
* Do not mix timezone assumptions across systems.

### Pagination

* Use the pagination fields documented for that endpoint.
* Continue paging until the required records are retrieved.
* Stop when the page has no further results.

### Rate limits and blocking

Every plan has per-second, per-minute and per-day request limits — see [Plans & Rate Limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/) for the exact numbers per plan and API category. If the per-minute limit is exceeded more than 3 times in a day, the user is blocked from making further requests for the rest of that day.

### Idempotency and retries

**Retry only when it is safe.**

* Confirm account state before repeating order or position actions.
* Check that the earlier request did not already succeed.
* Do not blindly replay requests after timeouts or network errors.

### How API pages are structured

Every API page follows the same structure, so you always know what to expect.

1. **Understand** — What the API does and when to use it.
2. **Check access** — Plan availability and access limits.
3. **Prepare** — Prerequisites and authentication.
4. **Make the request** — Method, URL and request parameters.
5. **Read the response** — Response fields and examples.
6. **Handle errors** — Error codes and recommended actions. See [Common API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/#application-error-codes).

## Sample Code

*Source: https://fyers.in/api-docs/v3/resources/sample-code/ (last updated 2026-10-14)*

You can check the [sample script](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED)) to get started with. More sample code is available in the [fyers-api-sample-code](https://github.com/FyersDev/fyers-api-sample-code) repository.

### Postman Collection

We have also created an extensive Postman collection that makes implementation easier. Import both the Postman collection and the Postman environment variables.

1. Download and import the [Postman collection](https://github.com/FyersDev/fyers-api-sample-code/blob/sample_v3/v3/Postman%20V3/FYERS%20API%20V3.postman_collection.json).
2. Download and import the [Postman environment variables](https://github.com/FyersDev/fyers-api-sample-code/blob/sample_v3/v3/Postman%20V3/FYERS%20API%20V3.postman_environment.json).
3. We have provided dummy data in the environment variables. Update them with the correct values after you import them.

For the full steps, see [Postman Collection](https://fyers.in/api-docs/v3/resources/postman-collection/).

## Postman Collection

*Source: https://fyers.in/api-docs/v3/resources/postman-collection/ (last updated 2026-10-14)*

We have created an extensive Postman collection that makes implementation easier. Import both the Postman collection and the Postman environment variables.

1. Download and import the [Postman collection](https://github.com/FyersDev/fyers-api-sample-code/blob/sample_v3/v3/Postman%20V3/FYERS%20API%20V3.postman_collection.json).
2. Download and import the [Postman environment variables](https://github.com/FyersDev/fyers-api-sample-code/blob/sample_v3/v3/Postman%20V3/FYERS%20API%20V3.postman_environment.json).
3. You can also check the [sample script](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script%28GET%20STARTED%29) to get started with.
4. We have provided dummy data in the environment variables. Update them with the correct values after you import them.

## Quickstart

*Source: https://fyers.in/api-docs/v3/getting-started/quickstart/ (last updated 2026-10-14)*

This quickstart takes you from a configured app to one successful authenticated request. Use the Profile API as your first call to confirm that authentication is complete and the FYERS API connection is working.

### Before you begin

* An active FYERS account
* A configured FYERS API app
* The required app permissions and static IP setup
* A supported language or REST client

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Make your first API call

1. Select REST, Python, Node.js, Web JavaScript, C#, Java, Go or C.
2. Install the SDK when using a supported library.
3. Complete authentication and obtain an access token.
4. Create the client or request headers.
5. Call the Profile API using the access token.
6. Confirm that the API returns the account profile successfully. This verifies that the access token and API connection are working before you move to trading operations.

> Profile API reference: [Open the official Profile API documentation](https://fyers.in/api-docs/v3/api/account/profile/)

Code sample by language: REST | Python | Node.js | Web JavaScript | C# | Java | Go | C

VIDEO LEARNING

### Video learning

[FYERS API playlist (REST and cURL)](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[FYERS API playlist (Node.js)](https://www.youtube.com/playlist?list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)

## How-to Guides

*Source: https://fyers.in/api-docs/v3/getting-started/guides/ (last updated 2026-10-14)*

Getting Started covers the one-time setup required to connect your app. How-to Guides show you how to complete specific trading, market-data and account tasks after your app is ready.

### Choose a Guide

| How-to guide | What it helps you do |
| --- | --- |
| [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/) | Parameters, sync vs async, order types, product types and pre-validations before you place an order. |
| [Place your first order](https://fyers.in/api-docs/v3/getting-started/guides/place-your-first-order/) | Authenticate, submit an order and verify its status. |
| [Stream live market data](https://fyers.in/api-docs/v3/getting-started/guides/stream-live-market-data/) | Connect to Data Socket, subscribe to symbols and process updates. |
| [Monitor orders and positions in real time](https://fyers.in/api-docs/v3/getting-started/guides/monitor-orders-and-positions/) | Use General WebSocket events and recover state after reconnecting. |
| [Work with historical market data](https://fyers.in/api-docs/v3/getting-started/guides/work-with-historical-market-data/) | Select instruments, request candles and validate the returned period. |
| [Manage positions, funds and risk](https://fyers.in/api-docs/v3/getting-started/guides/manage-positions-funds-and-risk/) | Read account state and complete supported position actions safely. |
| [Place basket and multi-leg orders safely](https://fyers.in/api-docs/v3/getting-started/guides/place-basket-and-multi-leg-orders/) | Submit related orders and handle partial or failed execution. |
| [Handle errors and rate limits](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/) | Read error responses, identify the cause and take the correct next action. |
| [Use Symbol Master to find instruments](https://fyers.in/api-docs/v3/getting-started/guides/use-symbol-master/) | Find valid instrument identifiers through the FYERS API Appendix. |

## Trading

*Source: https://fyers.in/api-docs/v3/api/trading/ (last updated 2026-10-14)*

Place and manage orders, read the order book, trade book and positions, and use GTT and smart-order workflows through the FYERS API.

### Overview

Understand synchronous and asynchronous execution, order types, product types, order validations, order tags and Auto Slice before implementing trading operations.

Start with the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/) for those concepts, then use [Place your first order](https://fyers.in/api-docs/v3/getting-started/guides/place-your-first-order/) when you are ready to send a live request.

### In this section

| Endpoint | Method | Description |
| --- | --- | --- |
| [Order Placement](https://fyers.in/api-docs/v3/api/trading/order-placement/) | — | Place orders with sync or async endpoints, and create GTT and smart orders. |
| [Order Management](https://fyers.in/api-docs/v3/api/trading/order-management/) | — | Modify or cancel open orders, one at a time or in bulk, with sync or async endpoints. |
| [Order Book](https://fyers.in/api-docs/v3/api/trading/order-book/) | — | Get all orders for the day, or look up orders by order ID or order tag. |
| [Trade Book](https://fyers.in/api-docs/v3/api/trading/trade-book/) | — | Get the trades executed during the day, or filter them by order tag. |
| [Positions](https://fyers.in/api-docs/v3/api/trading/positions/) | — | Get open positions, exit or convert them, and set, modify or cancel the stop loss and target on a position. |
| [Webhooks / Postbacks](https://fyers.in/api-docs/v3/api/trading/webhooks/) | — | The Postback API sends a POST request with a JSON payload to the registered postback\_url of your app when an order's status changes. |

## Market Data

*Source: https://fyers.in/api-docs/v3/api/market-data/ (last updated 2026-10-14)*

Get quotes, market depth, option and futures chains, and historical candles for live and expired contracts.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Historical Data](https://fyers.in/api-docs/v3/api/market-data/historical-data/) | GET | This API allows you to get historical candle data for a symbol over a date range and resolution. |
| [Quotes](https://fyers.in/api-docs/v3/api/market-data/quotes/) | GET | This API allows you to get the latest quotes for one or more symbols in a single request. |
| [Market Depth](https://fyers.in/api-docs/v3/api/market-data/market-depth/) | GET | This API allows you to get the market depth (bid and ask levels) for a symbol. |
| [Option Chain](https://fyers.in/api-docs/v3/api/market-data/option-chain/) | GET | This API allows you to get the option chain of an underlying, with Call and Put strikes, India VIX and available expiries. |
| [Futures Chain](https://fyers.in/api-docs/v3/api/market-data/futures-chain/) | GET | This API allows you to get the currently available futures contracts for an underlying symbol. |
| [Expired F&O Data](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/) | — | The Expired F&O Contracts Data APIs help you find expired Futures and Options contracts and get their historical data. |
| [Screeners](https://fyers.in/api-docs/v3/api/market-data/screeners/) | — | Screeners run ready-made filters on a set of symbols and return the ones that meet the filter's conditions. |

## Reports

*Source: https://fyers.in/api-docs/v3/api/reports/ (last updated 2026-10-14)*

Pull past orders, trades, charges, profit and loss, and ledger entries for the account as data, instead of exporting reports by hand.

Reports that take a date range default to the current financial year when you send none, and results are paged at 100 records per page by default. Segment and exchange filters are available on most reports, but the segment codes are not the same in every report, so check the request attributes of each one.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Order History](https://fyers.in/api-docs/v3/api/reports/order-history/) | GET | This API allows you to fetch your past orders for a date range, defaulting to the current financial year. |
| [Trade History](https://fyers.in/api-docs/v3/api/reports/trade-history/) | GET | This API allows you to fetch your executed trades for a date range, defaulting to the current financial year. |
| [Charges Report](https://fyers.in/api-docs/v3/api/reports/charges-report/) | GET | This API allows you to fetch the brokerage and other charges you paid over a date range, defaulting to the current financial year. |
| [Realised P&L Report](https://fyers.in/api-docs/v3/api/reports/realised-pnl-report/) | GET | This API allows you to fetch the realised profit and loss on your closed positions for a date range. |
| [Tax P&L Report](https://fyers.in/api-docs/v3/api/reports/tax-pnl-report/) | GET | This API allows you to fetch your tax profit and loss for a financial year, defaulting to the current one. |
| [Ledger Report](https://fyers.in/api-docs/v3/api/reports/ledger-report/) | GET | This API allows you to fetch the ledger entries of your account. |

## Account

*Source: https://fyers.in/api-docs/v3/api/account/ (last updated 2026-10-14)*

Read profile, funds and holdings information, log out the current API session, or pause all trading with Kill Switch.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Profile](https://fyers.in/api-docs/v3/api/account/profile/) | GET | This API allows you to fetch the basic details of the account holder and confirm that your access token is valid. |
| [Funds](https://fyers.in/api-docs/v3/api/account/funds/) | GET | This API allows you to fetch the available balance of your capital and commodity accounts. |
| [Holdings](https://fyers.in/api-docs/v3/api/account/holdings/) | GET | This API allows you to fetch the equity and mutual fund holdings in your demat account. |
| [Logout](https://fyers.in/api-docs/v3/api/account/logout/) | POST | This API allows you to invalidate the access token of your app without affecting other apps or web and mobile sessions. |
| [Kill Switch](https://fyers.in/api-docs/v3/api/account/kill-switch/) | — | Kill Switch lets you pause trading across all segments on your account for the day. |
| [EDIS / DDPI](https://fyers.in/api-docs/v3/api/account/edis-ddpi/) | — | Electronic Delivery Instruction Slip (eDIS) allows you to sell shares if your Power of Attorney (POA) is not submitted or DDPI is not activated. |

## Market Information

*Source: https://fyers.in/api-docs/v3/api/market-information/ (last updated 2026-10-14)*

Check market status and download Symbol Master files for instrument discovery.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Market Status](https://fyers.in/api-docs/v3/api/market-information/market-status/) | GET | This API allows you to check the current trading status of all exchanges and their segments. |
| [Symbol Master](https://fyers.in/api-docs/v3/api/market-information/symbol-master/) | — | Download the Symbol Master in CSV or JSON format to discover instruments and use the exact instrument identifiers in API requests. |

## Margin Calculator

*Source: https://fyers.in/api-docs/v3/api/calculators/ (last updated 2026-10-14)*

Calculate the margin required for your orders and positions before you place them.

| Endpoint | Method | Description |
| --- | --- | --- |
| [SPAN Margin Calculator](https://fyers.in/api-docs/v3/api/calculators/span-margin-calculator/) | POST | This API allows you to calculate the combined SPAN and exposure margin for futures and options, including margin benefits from hedges and individual instrument margin details. |
| [Multi-order Margin Calculator](https://fyers.in/api-docs/v3/api/calculators/multi-order-margin-calculator/) | POST | This API allows you to calculate the approximate margin required for proposed equity and derivative orders, including commodity derivatives, and returns the available account margin. |

## Price Alerts

*Source: https://fyers.in/api-docs/v3/api/price-alerts/ (last updated 2026-10-14)*

Price Alerts are user-configured triggers that notify when a stock or instrument reaches a specific price or meets certain market conditions.

Once an alert is triggered, you can get the notification in the [General WebSocket](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/).

Each alert compares the last traded price, or the open, high, low or close price, of an instrument with a target value you set. An alert is enabled, disabled or triggered, and a triggered or expired alert can no longer be modified or switched on and off. Use these APIs to create, change, pause, list and delete alerts from your own app.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Create Price Alert](https://fyers.in/api-docs/v3/api/price-alerts/create-price-alert/) | POST | This API allows you to create a price alert for an instrument. |
| [Get Price Alerts](https://fyers.in/api-docs/v3/api/price-alerts/get-price-alerts/) | GET | This API allows you to fetch your price alerts by alert name or alert ID, with their current status. |
| [Modify Price Alert](https://fyers.in/api-docs/v3/api/price-alerts/modify-price-alert/) | PUT | This API allows you to modify an existing price alert. |
| [Delete Price Alert](https://fyers.in/api-docs/v3/api/price-alerts/delete-price-alert/) | DELETE | This API allows you to delete a price alert. |
| [Enable / Disable Price Alert](https://fyers.in/api-docs/v3/api/price-alerts/enable-or-disable-price-alert/) | PUT | This API allows you to switch a price alert between enabled and disabled. |

## WebSocket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/websocket-overview/ (last updated 2026-10-14)*

This guide explains the two FYERS WebSockets, when to use each one and how a WebSocket connection differs from REST.

### What are WebSockets?

A WebSocket keeps one persistent, two-way connection open so FYERS can push updates to you as they happen, instead of you polling REST endpoints.

FYERS exposes two WebSocket types: the Data Socket (which includes the Tick-by-Tick (TBT) socket) and the General WebSocket (which carries order, trade, position, price alert and EDIS updates). Pick the socket that matches the data you need.

### Types of WebSockets

| Socket | What it streams |
| --- | --- |
| [Data Socket](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/) | Live market data: symbol (quote) updates, index updates, five-level market depth and lite mode. |
| [Tick-by-Tick (TBT) Socket](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/) | Part of the Data Socket. Streams 50-level market depth for NFO and NSE equity symbols, with Protobuf responses and channels you can pause and resume. |
| [General WebSocket](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/) | Real-time updates for your account’s orders, trades and positions, plus price alert triggers and EDIS updates, over a single connection instead of polling the Order Book. |

### Best practices

**Subscription Limit**

Data Socket symbol limits are per user, across all connections: Standard allows **100** symbols and Prime allows **5,000**. The Tick-by-Tick (TBT) socket has its own limits: Standard allows **1** symbol and Prime allows **15** (up to 3 connections with 5 symbols each). If a subscription would go over the limit, the connection is not established. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

**Connection Instance**

For the Data Socket and General WebSocket, create only one WebSocket instance at a time. The Tick-by-Tick (TBT) Socket has its own connection limits, listed under Rate limits.

**Dedicated Thread**

The WebSocket runs on a dedicated thread, independent of your main application thread, so primary work is not blocked by socket I/O.

**Updating Subscribed Symbols**

To update symbols in an already subscribed socket, it is recommended to unsubscribe from the existing list of symbols and then resubscribe with the updated list.

**Customizable Callbacks**

Tailor your application’s behavior using the callback functions provided by the WebSocket, to define specific actions for events like data updates or error occurrences: `on_connect` `on_message` `on_error` `on_close`.

**Auto-Reconnect**

Enable automatic reconnection on disconnect by setting `reconnect=True` during WebSocket initialization, so your application can recover without manual intervention. You can set a maximum reconnection count of up to **50**.

**Reconnect Retry**

Set a dynamic retry count with `reconnect_retry=10` (max 50). In Node use `fyersdata.autoreconnect(trycount)`.

**Logging to File**

Set `write_to_file=True` to save received data to a log file. `write_to_file` works only when callback functions are not used.

**Disable Logging (Node)**

Pass a logging flag in the Node constructor to disable logs: `new FyersSocket("token", "logpath", true)`

## Appendix

*Source: https://fyers.in/api-docs/v3/api/appendix/ (last updated 2026-10-14)*

Use the reference tables below to validate symbols, interpret request and response fields, and diagnose API errors. Market status and Symbol Master downloads are under [Market Information](https://fyers.in/api-docs/v3/api/market-information/).

| Section | What it contains |
| --- | --- |
| [Fytoken](https://fyers.in/api-docs/v3/api/appendix/fytoken/) | FYERS token structure: exchange, segment, expiry and exchange token fields. |
| [Exchanges](https://fyers.in/api-docs/v3/api/appendix/exchanges/) | Numeric exchange codes for NSE, MCX and BSE. |
| [Segments](https://fyers.in/api-docs/v3/api/appendix/segments/) | Numeric segment codes for capital market, derivatives and commodities. |
| [Exchange-Segment Mapping](https://fyers.in/api-docs/v3/api/appendix/available-exchange-segment-combinations/) | Supported exchange and segment pairings with their codes. |
| [Instrument Types](https://fyers.in/api-docs/v3/api/appendix/instrument-types/) | Instrument type codes by segment (CM, FO, CD and COM). |
| [Symbol Format](https://fyers.in/api-docs/v3/api/appendix/symbology-format/) | Exchange, segment and instrument format rules used in FYERS identifiers. Validate symbols against the latest Symbol Master before requests. |
| [Symbol Values](https://fyers.in/api-docs/v3/api/appendix/symbology-possible-values/) | Placeholder variables and allowed values used in symbology formats. |
| [Product Types](https://fyers.in/api-docs/v3/api/appendix/product-types/) | Product type values such as CNC, INTRADAY, MARGIN and MTF. |
| [Order Types](https://fyers.in/api-docs/v3/api/appendix/order-types/) | Order type values for limit, market and stop orders. |
| [Order Status](https://fyers.in/api-docs/v3/api/appendix/order-status/) | Order status values returned by trading and WebSocket APIs. |
| [Order Sides](https://fyers.in/api-docs/v3/api/appendix/order-sides/) | Buy and sell side values used in order requests. |
| [Position Sides](https://fyers.in/api-docs/v3/api/appendix/position-sides/) | Long, short and closed position side values. |
| [Holding Types](https://fyers.in/api-docs/v3/api/appendix/holding-types/) | T1 and HLD holding type values in account responses. |
| [Order Sources](https://fyers.in/api-docs/v3/api/appendix/order-sources/) | Source channel codes for mobile, web, API and other platforms. |
| [API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/) | Standard API error codes with descriptions. Read each code together with the response message. |

## Troubleshooting

*Source: https://fyers.in/api-docs/v3/getting-started/guides/troubleshooting-guide/ (last updated 2026-10-14)*

Use this guide to resolve common FYERS API issues before reaching out for support.

### In this guide

| Issue | Go to |
| --- | --- |
| Orders are not getting placed | [Order placement issues](#order-placement-issues) |
| Login or authentication is failing | [Authentication issues](#authentication-issues) |
| Unable to update the static IP | [Static IP issues](#static-ip-issues) |
| Request limit reached / `429` | [Rate limit issues](#rate-limit-issues) |
| API is slow or SDK method is not working | [SDK issues](#sdk-issues) |
| Invalid symbol or historical data unavailable | [Symbol & historical data issues](#symbol--historical-data-issues) |
| WebSocket disconnects or no ticks received | [WebSocket issues](#websocket-issues) |
| API returned an error code | [API Error Codes](#api-error-codes) |

---

### Start with these checks

Before going deeper, verify:

* **Use the latest official FYERS SDK**
* **Make sure the access token is valid**
* **Read the complete API error code and message**
* **Refer to Appendix → API Error Codes**
* **Confirm the correct App ID is being used**
* **Verify the request parameters against the API Reference**
* **Check the applicable Plans & Rate Limits**

**Tip**

Updating the SDK, validating the access token, and checking the exact error message can resolve many common API issues.

---

### Order placement issues

#### Orders are not getting placed

**Check**

* App ID ends with `200`
* Static IP is whitelisted
* Request originates from the whitelisted IP
* Correct App ID is being used

**Fix**

Only **App Type 200** supports order placement. Use the trading App ID and ensure orders originate from its whitelisted static IP.

---

### Authentication issues

#### Login or authentication is failing

**Check**

* Access token is valid
* Correct App ID is being used
* Login endpoint is not being called repeatedly

**Fix**

* Generate a new token if the existing token has expired
* Reuse a valid token instead of logging in for every request
* Avoid authentication retry loops

**Note**

The login endpoint allows 10 requests in 2 minutes. Exceeding the limit can temporarily block the IP.

---

### Static IP issues

#### Unable to modify the static IP

**Check**

* When the IP was last modified
* Whether the IP is already mapped to another user

**Fix**

* IP can be modified only once in 7 days
* The same static IP cannot normally be mapped to multiple users
* Eligible family members can share a static IP through the applicable declaration process

---

### Rate limit issues

#### Request limit reached

**Check**

* Repeated API calls
* Retry loops
* Multiple application instances
* REST polling for continuously changing data

**Fix**

* Reduce unnecessary calls
* Implement retry/backoff
* Use WebSockets for live market data
* Refer to [Plans & Rate Limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/)

---

### SDK issues

#### API is slow or an SDK method is not working

**Check**

* SDK version
* API/SDK version compatibility

**Fix**

* Upgrade to the latest official FYERS SDK
* Restart the application
* Ensure the implementation follows the current API documentation

---

### Symbol & historical data issues

#### Invalid symbol or no data

**Check**

* Symbol in Symbol Master
* Exchange and segment
* Date range
* Resolution
* Contract expiry

**Fix**

* Use the latest Symbol Master
* Use the correct date range and resolution
* For expired F&O contracts, use the [Expired F&O Data APIs](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/)

---

### WebSocket issues

#### WebSocket disconnects or no ticks are received

**Check**

* Network stability
* Connection status
* Symbol subscription
* Duplicate subscriptions
* Subscription limits

**Fix**

* Use a stable network
* Enable supported reconnect handling
* Verify symbols are subscribed successfully
* Avoid subscribing repeatedly to the same symbols

---

### API Error Codes

If an API returns an error, read both the error code and message before changing the request.

#### HTTP Status Codes

The HTTP status code on the response indicates the general outcome of the request. Read it together with the response body for the exact condition.

| Status Code | Meaning |
| --- | --- |
| 200 | Request was successful. |
| 400 | Bad request. The request is invalid, or certain other errors. |
| 401 | Authorization error. The user could not be authenticated. |
| 403 | Permission error. The user does not have the necessary permissions. |
| 429 | Rate limit exceeded. The user has been blocked for exceeding the rate limit. |
| 500 | Internal server error. |

#### Application Error Codes

The same error code may be used for more than one condition. Use the response message and API operation to identify the correct cause before retrying.

| Code | Description |
| --- | --- |
| -8 | The access token has expired. Generate a valid token before sending the request again. |
| -15 | An invalid access token was provided. Check the token used in the request. |
| -16 | The server could not authenticate the user token. Verify the authentication details and try again after correcting them. |
| -17 | The access token is invalid or has expired. Complete the required authentication flow and use a valid token. |
| -50 | One or more request parameters are invalid. Read the message field for details about the affected input. |
| -51 | The Order ID is invalid while fetching or modifying an order. Check the Order ID and the operation being performed. |
| -53 | The Position ID is invalid. Check the current positions and use the correct Position ID. |
| -99 | The order placement was rejected. Read the rejection message in the API response before taking another action. |
| -300 | The symbol is invalid. Verify it through Appendix → Symbol Master. For direct URLs, URL-encode symbols containing special characters; FYERS SDKs handle this automatically. |
| -352 | The App ID is invalid. Check the App ID configured for the request. |
| -352 | No position is available to exit. Read the response message and request context to identify which -352 condition applies. |
| -360 | A Standard plan user exceeded the API rate limit (per second, minute or day). Upgrade to Prime for higher API limits. To know more, visit <https://fyers.in/web/profile/prime>. |
| -429 | The API rate limit was exceeded for the applicable second, minute or day limit. Stop repeated calls, wait for the limit window and then retry. |
| 400 | The multi-leg order request contains invalid input. Review the required fields and values for every leg. |

See the full reference at [Appendix → API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/).

## Order Placement

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/ (last updated 2026-10-14)*

Place orders with sync or async endpoints, and create GTT and smart orders.

For details on how to place orders, refer to the [Order Placement Guide](https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/).

| Endpoint | Method | Description |
| --- | --- | --- |
| [Sync](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/) | — | Place single, multiple and multi-leg orders and get the exchange order ID in the response. |
| [Async](https://fyers.in/api-docs/v3/api/trading/order-placement/async/) | — | Place single or multiple orders through a queue processed at up to 10 orders per second. The response returns id\_fyers. |
| [GTT Orders](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/) | — | GTT (Good Till Trigger) is used to create orders with longer validity. It helps you set a Target or Stop-Loss for your open positions or holdings, and you can also use it to take new positions. |
| [Smart Orders](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/) | — | Create Smart Limit, Smart Trail, Smart Step and Smart SIP orders, and modify, cancel, pause, resume and view them. |

## Sync

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/sync/ (last updated 2026-10-14)*

Place single, multiple and multi-leg orders and get the exchange order ID in the response.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Single Order](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/) | POST | This API allows you to place an order to any supported exchange. |
| [Multi Order](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-order/) | POST | This API allows you to place multiple orders in a single request. |
| [Multi-leg Order](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-leg-order/) | POST | This API allows you to place a two-leg or three-leg NSE futures and options order as a single order. |

## Order Placement Guide

*Source: https://fyers.in/api-docs/v3/getting-started/guides/order-placement-guide/ (last updated 2026-10-14)*

**Note:** SEBI’s retail algo trading regulations are now in effect. To check the changes related to the algo trading regulations, refer to the [SEBI algo trading rules](https://fyers.in/community/t/sebis-new-algo-trading-rules-kick-in-on-april-1-here-is-what-changes-for-you/12267).

The order placement process requires you to carefully input several parameters at the time of making the request. There are several validations which are required to be done before sending the request.

### Overview - Sync and Async APIs

#### Sync APIs (`/sync`)

All existing `/sync` order endpoints (single order, multi order, multi-leg order and related `/sync` flows documented under [Sync Order Placement](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/)) remain unchanged in request shape and response shape. They continue to return the exchange order reference `id` (and other fields). Execution is subject to a **10 orders per second (OPS)** limit.

#### Async APIs (`/async`)

Async counterparts use the same request bodies and HTTP methods as sync where applicable, but target:

* `POST https://<host>/api/v3/orders/async` — place order (intraday / margin / CNC, same attributes as sync).
* `PATCH https://<host>/api/v3/orders/async` — modify order (same body rules as sync; `id` in the body is the order reference once known).
* `DELETE https://<host>/api/v3/orders/async` — cancel order (JSON body with `id`, same idea as sync).

**Note:** `stopLoss` and `takeProfit` are not supported with Async Order Placement.

**Queuing:** When you call an async endpoint, the request is accepted and queued immediately. A queuing mechanism drains the queue and sends work downstream at most **10 orders per second** (aligned with the OPS limit). High burst traffic is absorbed in the queue rather than failing fast for rate at the HTTP edge. Final placement, modification or cancellation outcomes are not implied by an HTTP 200 alone.

**Immediate HTTP response:** On success, the async API returns `id_fyers` (the FYERS system identifier for the queued/async operation). It does not return `id` (exchange order number) in this immediate response. Use `id_fyers` to correlate with:

* **General WebSocket** — subscribe to order updates; payloads include identifiers such as `id` and `id_fyers` (see [General WebSocket Overview](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/)).
* **GET APIs** — for example the order book `GET /api/v3/orders` and related transaction GET APIs (see [Order Book](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/)).

**Hosts:** The examples use `https://api-t1.fyers.in`; other environments may use the same path suffixes on a different host (for example `https://api-y1.fyers.in`). Set `<host>` accordingly.

**Reference collection:** Parity with the internal Postman collection *Async apiv3 orders* (place/modify/cancel).

### Order Types

#### Limit Order

* type: `1`
* A limit order allows you to buy or sell an asset at a specific price (`limitPrice`) or better. It will only be executed at the specified price or lower for a buy order, and at the specified price or higher for a sell order.

Sample input:

```
{
  "symbol": "NSE:SBIN-EQ",
  "qty": 100,
  "type": 1,
  "side": 1,
  "productType": "INTRADAY",
  "limitPrice": 100,
  "stopPrice": 0,
  "validity": "DAY",
  "stopLoss": 0,
  "takeProfit": 0,
  "offlineOrder": false,
  "disclosedQty": 0,
  "isSliceOrder" : false
}
```

#### Market Order (MPP)

* type: `2` (MPP: Market Price Protection )
* A market order allows you to buy or sell an asset at the current market price. The `limitPrice` and `stopPrice` should be set to 0, as they are not used in this order type.

Sample input:

```
{
  "symbol": "NSE:SBIN-EQ",
  "qty": 100,
  "type": 2,
  "side": 1,
  "productType": "INTRADAY",
  "limitPrice": 0,
  "stopPrice": 0,
  "validity": "DAY",
  "stopLoss": 0,
  "takeProfit": 0,
  "offlineOrder": false,
  "disclosedQty": 0,
  "isSliceOrder" : false
}
```

#### Stop Order / SL-M (MPP)

* type: `3`
* A stop order is designed to limit losses on a position. It becomes a market order (MPP: Market Price Protection ) when the `stopPrice` is reached. The `stopPrice` is the trigger price at which the market order will be placed.
* The `stopPrice` must not be higher than the Last Traded Price (ltp) for a sell order and not lower than the ltp for a buy order.

Sample input:

```
{
  "symbol": "NSE:SBIN-EQ",
  "qty": 100,
  "type": 3,
  "side": 1,
  "productType": "INTRADAY",
  "limitPrice": 0,
  "stopPrice": 100,
  "validity": "DAY",
  "stopLoss": 0,
  "takeProfit": 0,
  "offlineOrder": false,
  "disclosedQty": 0,
  "isSliceOrder" : false
}
```

#### Stop Limit Order / SL-L

* type: `4`
* A stop-limit order combines features of a stop order and a limit order. It triggers a limit order once the `stopPrice` is reached.
* The `stopPrice` must not be higher than the Last Traded Price (ltp) for a sell order and not lower than the ltp for a buy order.
* The `stopPrice` must be lower than the `limitPrice` for a buy order and higher than the `limitPrice` for a sell order.

Sample input:

```
{
  "symbol": "NSE:SBIN-EQ",
  "qty": 100,
  "type": 4,
  "side": 1,
  "productType": "INTRADAY",
  "limitPrice": 100,
  "stopPrice": 95,
  "validity": "DAY",
  "stopLoss": 0,
  "takeProfit": 0,
  "offlineOrder": false,
  "disclosedQty": 0,
  "isSliceOrder" : false
}
```

### Product Types

* **Intraday**
  + Used to place orders which will be bought and sold the same day.
  + Order type can be anything (Market, Limit, Stop and Stop Limit).
* **CNC**
  + Used to place orders only in stocks which will be carried forward.
  + Order type can be anything (Market, Limit, Stop and Stop Limit).
* **Margin**
  + Used to place orders in derivative contracts which will be carried forward.
  + Order type can be anything (Market, Limit, Stop and Stop Limit).
* **Margin Trading Facility (MTF)**
  + This order type is for placing trades with additional margin.
  + MTF orders require activation.
  + Only stocks from the approved MTF list are allowed.
  + Supported order types: Market, Limit, Stop and Stop Limit.

### Take Profit and Stop Loss (TPSL) orders

Take Profit and Stop Loss (TPSL) orders are linked to a parent order. Which API you use depends on whether the parent order is still pending or has executed into an open position.

* **From order placement (new order):** the parent order is placed but not yet executed. Use the **Orders API** (order modification).
* **From open position:** the parent order has executed and you hold an open position. Use the **Positions API** (position modification), `PATCH /api/v3/positions`.

TPSL is supported for the INTRADAY, CNC, MARGIN and MTF product types.

#### Creating TPSL

**From order placement (new order)**

Use the **Orders API** [Single Order](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/) and send the `takeProfit` and `stopLoss` parameters with the order, using an applicable supported `productType` (INTRADAY, CNC, MARGIN or MTF). TPSL is supported only with sync order placement; async order placement does not support `takeProfit` and `stopLoss`.

**From open position**

Use the **Positions API** [Set Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/set-stop-loss-and-target/). Send the `positionId` with `takeProfit` and/or `stopLoss`. `qty` is optional and can’t be more than the position quantity.

#### Modifying TPSL

**From order placement (new order)**

While the parent order is pending (not yet executed), use the **Orders API** [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/) and send the new `takeProfit` and/or `stopLoss` values.

**Note:** Take Profit and Stop Loss are set as points away from the limit price. If you change only the `limitPrice`, they keep the same points, so their prices move with the new limit price.

Example (buy order): limit price 100, `takeProfit` 5 and `stopLoss` 3 give a Take Profit of 105 and a Stop Loss of 97. Change only the limit price to 102, and they become 107 and 99.

**From open position**

Once the parent order has executed and you have an open position, use the **Positions API** [Modify Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/modify-stop-loss-and-target/). Send only the parameters you want to change; any parameter you leave out keeps its current value.

#### Cancelling TPSL

**From order placement (new order)**

If a pending parent order is cancelled using the **Orders API** [Cancel Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/), its linked Take Profit and Stop Loss orders are cancelled automatically.

To cancel only the linked Take Profit or Stop Loss without cancelling the parent order, use the **Orders API** [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/) and pass `null` for the applicable `takeProfit` or `stopLoss` parameter. Pass both parameters as `null` to cancel both.

**From open position**

Use the **Positions API** [Cancel Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/cancel-stop-loss-and-target/) and pass `null` for the parameter you want to cancel: `takeProfit`, `stopLoss`, or both.

### Price Validations

For all transaction requests (order placement / modification), the price input should be in accordance with the exchange-provided tick size for the particular symbol.

* Tick size is applicable for all price inputs (limit / stop / stopLoss / target).
* Each symbol has its own tick size.
* All price inputs have to be in multiples of the tick size.
* The tick size is available in the [Symbol Master](https://fyers.in/api-docs/v3/api/market-information/symbol-master/).

### Quantity Validations

For all transaction requests (order placement / modification), the quantity input should be in accordance with the exchange-provided minimum lot size.

| Segment | Minimum Quantity Details |
| --- | --- |
| Equities | The quantity will be in multiples of 1 |
| Equity Derivatives | The quantity will be in multiples of the lot size specified by the exchange |
| Currency Derivatives | The quantity will be in multiples of 1 |
| Commodity Derivatives | The quantity will be in multiples of 1 |

### Order Tag

For all order placement requests where tags are passed, they should meet the following requirements:

* The order tag string should be alphanumeric, i.e. no spaces or special characters are allowed.
* The order tag string should not exceed 30 characters and should have a minimum length of 1 character.
* The order tag string cannot be your **clientID** or the string **Untagged**.

### Auto-Order Slice

Use the auto-slice feature to place large orders that exceed the exchange’s freeze-quantity limits.

Enable it by setting `"isSliceOrder": true` in the order request. When enabled, the system automatically splits the order into smaller quantities based on the applicable freeze limit. Each slice is submitted as a separate order with its own Order ID.

**Note:**

* Slicing is only allowed for NSE CM, NFO and BFO.
* Maximum slices per request: 10.

Sample input:

```
{
    "symbol": "NSE:BANKNIFTY25NOV58900PE",
    "qty": 3150,
    "type": 2,
    "side": 1,
    "productType": "MARGIN",
    "limitPrice": 0,
    "stopPrice": 0,
    "disclosedQty": 0,
    "validity": "DAY",
    "offlineOrder": false,
    "stopLoss": 0,
    "takeProfit": 0,
    "IsSliceOrder": true
}
```

Response output:

```
{
  "code": 1101,
  "message": "Order Slice placed successfully",
  "data": [
    {
      "statusCode": 200,
      "body": {
        "code": 1101,
        "message": "Successfully placed order",
        "s": "ok",
        "id": "25120400000372"
      },
      "statusDescription": "OK"
    },
    {
      "statusCode": 200,
      "body": {
        "code": 1101,
        "message": "Successfully placed order",
        "s": "ok",
        "id": "25120400000373"
      },
      "statusDescription": "OK"
    },
    {
      "statusCode": 200,
      "body": {
        "code": 1101,
        "message": "Successfully placed order",
        "s": "ok",
        "id": "25120400000374"
      },
      "statusDescription": "OK"
    }
  ]
}
```

### Related documentation

* [Single Order API](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/)
* [Modify Single Order API](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/)
* [Cancel Single Order API](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/)
* [General WebSocket](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/)
* [Symbol Master](https://fyers.in/api-docs/v3/api/market-information/symbol-master/)

## Order Types

*Source: https://fyers.in/api-docs/v3/api/appendix/order-types/ (last updated 2026-10-14)*

Order type values for limit, market and stop orders.

| Possible Values | Description |
| --- | --- |
| 1 | Limit order |
| 2 | Market order |
| 3 | Stop order (SL-M) |
| 4 | Stoplimit order (SL-L) |

## Order Sides

*Source: https://fyers.in/api-docs/v3/api/appendix/order-sides/ (last updated 2026-10-14)*

Buy and sell side values used in order requests.

| Possible Values | Description |
| --- | --- |
| 1 | Buy |
| -1 | Sell |

## Product Types

*Source: https://fyers.in/api-docs/v3/api/appendix/product-types/ (last updated 2026-10-14)*

Product type values such as CNC, INTRADAY, MARGIN and MTF.

| Possible Values | Description |
| --- | --- |
| CNC | For equity only |
| INTRADAY | Applicable for all segments |
| MARGIN | Applicable only for derivatives |
| MTF | Margin Trading Facility |

## Symbol Master JSON

*Source: https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-json/ (last updated 2026-10-14)*

This API allows you to download the latest Symbol Master as a JSON file for an exchange segment.

USE CASE

Load instrument details into your code to validate symbols and check lot size, tick size and trade status before placing an order.

Details

* You can get all the latest symbols of all the exchanges from the symbol master json files
* Check `tradeStatus` before trading a symbol: 1 means active and 0 means inactive.
* `stream` is the stream group. For multi-leg orders, check that both legs belong to the same stream.
* `isCasEligible` is `true` for CAS-eligible symbols and absent otherwise. `qtyFreeze` is an empty string when not applicable.
* `is_mtf_tradable` is 0 or 1. `mtf_margin` is the margin multiplier for MTF, so 2.9 means 2.9x margin.
* `expiryDate` is a timestamp and applies only to derivative contracts. `lastUpdate` is in YYYY-MM-DD format.
* Key will be the symbol ticker and value will hold the below json object which has symbol master details for that particular symbol ticker.

| **Exchange / Segment** | **Download URL** |
| --- | --- |
| NSE – Currency Derivatives | <https://public.fyers.in/sym_details/NSE_CD_sym_master.json> |
| NSE – Equity Derivatives | <https://public.fyers.in/sym_details/NSE_FO_sym_master.json> |
| NSE – Commodity | <https://public.fyers.in/sym_details/NSE_COM_sym_master.json> |
| NSE – Capital Market | <https://public.fyers.in/sym_details/NSE_CM_sym_master.json> |
| BSE – Capital Market | <https://public.fyers.in/sym_details/BSE_CM_sym_master.json> |
| BSE - Equity Derivatives | <https://public.fyers.in/sym_details/BSE_FO_sym_master.json> |
| MCX - Commodity | <https://public.fyers.in/sym_details/MCX_COM_sym_master.json> |

#### File Format

| Attribute | **Data Type Of Values** | Description |
| --- | --- | --- |
| `fyToken` | string | * Unique token for the security * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `isin` | string | ISIN code for the security |
| `exSymbol` | string | Exchange symbol of the security |
| `symDetails` | string | Full name of the security |
| `symTicker` | string | Unique string to identify the security |
| `exchange` | int | * Exchange mapping * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `segment` | int | * Segment of the security * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `exSymName` | string | Symbol name of the security |
| `exToken` | int | Exchange token |
| `exSeries` | string | Series of the security. This can be used only for CM segments |
| `optType` | string | * CE/PE - For options * XX - For others |
| `underSym` | string | name of underlying symbol |
| `underFyTok` | string | Unique token for the underlying symbol |
| `exInstType` | int | * Exchange instrument type * [View Details](https://fyers.in/api-docs/v3/api/appendix/instrument-types/) |
| `minLotSize` | int | Minimum qty multiplier |
| `tickSize` | float | Minimum price multiplier |
| `tradingSession` | string | Trading session provided in IST |
| `lastUpdate` | string | Date of last update in YYYY-MM-DD format |
| `expiryDate` | string | Date of expiry for a symbol in timestamp.Applicable only for derivative contracts |
| `strikePrice` | float | Strike price |
| `qtyFreeze` | string | * Freeze qty * Empty string in case value is not applicable |
| `tradeStatus` | int | * Flag to check if security is allowed to trade. * Expected values - 0/1 * 1 = Active. 0 = Inactive. |
| `currencyCode` | string | Currency code |
| `upperPrice` | float | Upper circut price |
| `lowerPrice` | float | Lower circut price |
| `faceValue` | float | Face value |
| `qtyMultiplier` | float | Quantity multipler |
| `previousClose` | float | Previous close price |
| `previousOi` | float | Previous OI value |
| `asmGsmVal` | string | Surveillance Indicator message |
| `exchangeName` | string | * Exchange Name * NSE/BSE/MCX |
| `symbolDesc` | string | Full name of the security |
| `originalExpDate` | string | Kindly ignore this field |
| `is_mtf_tradable` | int | * 0: Not MTF tradable. * 1: MTF tradable. |
| `mtf_margin` | float | * Indicates the margin multiplier available for MTF transactions. * For example, a value of 2.9 means you receive 2.9x margin on the stock or security. |
| `stream` | string | Stream Group |
| `isCasEligible` | boolean | Indicates CAS eligibility. `true` means the symbol is CAS eligible; if the field is absent, it is not eligible. |

VIDEO LEARNING

### Video learning

[How to find stock symbols? (REST and cURL)REST and cURL · 5:01](https://www.youtube.com/watch?v=u2qEMgFWjKw&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Symbol format guide (Python)Python · 5:01](https://www.youtube.com/watch?v=1TjugxsnfwY&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Symbol format step by step guide (Node.js)Node.js · 5:00](https://www.youtube.com/watch?v=N7V9YH4e1Kg&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Symbol format guide (C#)C# · 5:01](https://www.youtube.com/watch?v=U95lPkxIk0U&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Symbol format guide (Java)Java · 5:01](https://www.youtube.com/watch?v=ZcPnyUVgZo0&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Async

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/async/ (last updated 2026-10-14)*

Place single or multiple orders through a queue processed at up to 10 orders per second. The response returns id\_fyers.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Single Order](https://fyers.in/api-docs/v3/api/trading/order-placement/async/single-order/) | POST | This API allows you to place an order without waiting for the exchange response. |
| [Multi Order](https://fyers.in/api-docs/v3/api/trading/order-placement/async/multi-order/) | POST | This API allows you to place multiple orders in a single request without waiting for the exchange response. |

## General WebSocket - Connect

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-connect/ (last updated 2026-10-14)*

This guide explains how to connect to the General WebSocket using the endpoint and an authorization header.

USE CASE

Open one connection when your app starts to receive live updates on your orders, trades and positions.

Details

To connect to the General WebSocket, the below two input params are mandate. Based on the programming language chosen, respective socket connection libraries can be used. For reference, the sample code for socket connection is written in Python.

**Mandatory connection parameters**

Pass the websocket endpoint and an authorization header in `<appId:accessToken>` format.

Websocket endpoint: `wss://socket.fyers.in/trade/v3`

Header

Format: `<appId:accessToken>`

Sample header format: `7ABXUX38S-100:eyJ0eXAi**********qiTnzd2lGwS17s`

The connection uses parameters and callback functions `on_message`, `on_error`, `on_close`, and `on_open`, which are required in the Python socket connection library and would change as per the other programming library used. A sample callback function is shared below.

**Note**

Handle accordingly in your programming language.

**Connection response**

On success: returns the socket object.

On failure: possible error status code `403`.

Error: Handshake status 403 Forbidden

Handshake status 403 Forbidden -+-+- {'date': 'Tue, 19 Dec 2023 04:46:45 GMT', 'content-length': '0', 'connection': 'keep-alive', 'cf-cache-status': 'DYNAMIC', 'set-cookie': '\_\_cf\_bm=BOE16LGB7NHpNqW0AJOuFN1rcL3Q9TgnhmtpBfb3.Wk-1702961205-1- AfmECmK9cbVA2XGvkpx+jFuXyRsJET/ZOQYmw3LyZJ68pYLZTgtpbalvNs09ECZZ4GpPiogeYGhhFo+3PCp20nE=; path=/; expires=Tue, 19-Dec-23 05:16:45 GMT; domain=.fyers.in; HttpOnly; Secure', 'server': 'cloudflare', 'cf-ray': '837d00eec8ed17b6-MAA'} -+-+- b''

* Reason: this error will come when your `accessToken` is wrong.
* How to solve: provide the correct accessToken. AccessToken format: `<appID:accesstoken>`.

Error: Handshake status 404 Not Found

Handshake status 404 Not Found -+-+- {'date': 'Tue, 19 Dec 2023 10:04:35 GMT', 'content-type': 'text/plain; charset=utf-8', 'content-length': '0', 'connection': 'keep-alive', 'cf-cache-status': 'DYNAMIC', 'set-cookie': '\_\_cf\_bm=I5oN6zdeKjfGsicqFiXZ57J5SX2IjsFDspaLIEGKPDE-1702980275-1-Ae+ldjrb3WfSuM7yNOzo3ykOIBQ1m+50QqcIqU26A+wqPIHhIEIGSy9kT2OG3OWNI0hwcmh7U+PnJ/aWWhz6fOA=; path=/; expires=Tue, 19-Dec-23 10:34:35 GMT; domain=.fyers.in; HttpOnly; Secure', 'server': 'cloudflare', 'cf-ray': '837ed28169c817ae-MAA'} -+-+- b''

* Reason: socket connection URL would be wrong.
* How to solve: provide a valid URL.

Sample callback function: for more reference, see the `on_open` callback in the Python request sample.

**Good to know**

* This is the General WebSocket endpoint for account events. Live market data uses the separate Data Socket.
* Connecting alone does not deliver any data. Subscribe to the actions you want once the connection is open.
* The Python SDK sends the access token in the `authorization` header. With your own client, send `<appId:accessToken>` in the header.
* With `order_ws.FyersOrderSocket`, the callbacks are `on_connect`, `on_close`, `on_error`, `on_orders`, `on_trades`, `on_positions` and `on_general`. Subscribe inside `on_connect`, then call `keep_running()`.
* The SDK starts its ping loop as soon as the connection opens. With your own client, send `ping` yourself (see Ping method).
* Create only one WebSocket connection instance at a time, as advised in the WebSocket guidance.

RequestPython

```
try:
if self.__ws_object is None:
    if self.write_to_file:
        self.background_flag = True
    header = {"authorization": self.__access_token}
    ws = websocket.WebSocketApp(
        self.__url,
        header=header,
        on_message=lambda ws, msg: self.__on_message(msg),
        on_error=lambda ws, msg: self.On_error(msg),
        on_close=lambda ws, close_code, close_reason: self.__on_close(
            ws, close_code, close_reason
        ),
        on_open=lambda ws: self.__on_open(ws),
    )
    self.t = Thread(target=ws.run_forever)
    self.t.daemon = self.background_flag
    self.t.start()

  #Sample callback function:

    def __on_open(self, ws):
    try:
        if self.__ws_object is None:
        self.__ws_object = ws
        self.ping_thread = threading.Thread(target=self.__ping)
        self.ping_thread.start()
    except Exception as e:
        self.order_logger.error(e)
        self.On_error(e)
```

## Get Orders

*Source: https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/ (last updated 2026-10-14)*

This API allows you to fetch all the orders placed in your account today.

USE CASE

Check the current status of every order placed today.

Note

**Live Streaming** — Receive real-time order updates through the General WebSocket instead of repeatedly polling the Order Book. View [General WebSocket Overview](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/) documentation.

Details

* Fetches all the orders placed by the user across all platforms and exchanges in the current trading day.
* Orders placed from other FYERS platforms also appear, not only API orders. The `source` field tells you where each order was placed.
* `status` values: 1 Cancelled, 2 Traded / Filled, 4 Transit, 5 Rejected, 6 Pending, 7 Expired. Value 3 is not used.
* For a partly filled order, compare `filledQty` with `remainingQuantity`; `tradedPrice` is the average traded price.
* When an order is rejected, `message` carries the error text.
* `orderDateTime` is in IST (DD-MMM-YYYY hh:mm:ss), `slNo` sorts orders by time, and `offlineOrder` is true for AMO orders.
* `orderTag` carries a `1:` prefix for tags you set and `2:` for tags generated by FYERS. Orders without a tag show `2:Untagged`.
* `parentId` is returned only for orders that have a parent order. Take profit and stop loss prices come in `takeProfit` and `stopLoss`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - For each order

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id` | string | The unique order id assigned for each order |
| `exchOrdId` | string | The order id provided by the exchange |
| `id_fyers` | string | Fyers system-generated unique identifier for the order |
| `symbol` | string | The symbol for which order is placed |
| `qty` | int | The original order qty |
| `remainingQuantity` | int | The remaining qty |
| `filledQty` | int | The filled qty after partial trades |
| `status` | int | * 1 => Canceled * 2 => Traded / Filled * 3 => (Not used currently) * 4 => Transit * 5 => Rejected * 6 => Pending * 7 => Expired * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-status/) |
| `slNo` | int | This is used to sort the orders based on the time |
| `message` | string | The error messages are shown here |
| `segment` | int | * 10 => E (Equity) * 11 => D (F&O) * 12 => C (Currency) * 20 => M (Commodity) * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `limitPrice` | float | The limit price for the order |
| `stopPrice` | float | The limit price for the order |
| `productType` | string | The product type |
| `type` | int | * 1 => Limit Order * 2 => Market Order * 3 => Stop Order (SL-M) * 4 => Stoplimit Order (SL-L) |
| `side` | int | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `disclosedQty` | int | Disclosed quantity |
| `orderValidity` | string | * DAY * IOC |
| `orderDateTime` | string | The order time as per DD-MMM-YYYY hh:mm:ss in IST |
| `parentId` | string | The parent order id will be provided only for applicable orders. |
| `tradedPrice` | float | The average traded price for the order |
| `source` | string | * Source from where the order was placed. * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sources/) |
| `fytoken` | string | * Fytoken is a unique identifier for every symbol. * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `offlineOrder` | boolean | * False => When market is open * True => When placing AMO order |
| `pan` | string | PAN of the client |
| `clientId` | string | The client id of the fyers user |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `instrument` | int | * Exchange instrument type * [View Details](https://fyers.in/api-docs/v3/api/appendix/instrument-types/) |
| `discloseQty` | int | Disclosed quantity |
| `orderTag` | string | * ordertag provided when placing the order * **Note**: `1:` will be concatenated at the start of tag provided by user. * `2:` will be concatenated at the start of tag generated internally by Fyers. * Default value if tag not provided when order is placed is `2:Untagged` |
| `takeProfit` | float | Take profit price for the order. |
| `stopLoss` | float | Stop loss price for the order. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

response = fyers.orderbook()
print(response)
```

```
{
    "code":200,
    "message":"",
    "s":"ok",
    "orderBook":[
        {
          "clientId":"XXXXX86",
          "exchange":10,
          "fyToken":"101000000014366",
          "id":"23080444447604",
          "id_fyers": "c6697c04-d9ab-4a7c-a6f4-b0cc4ca698f6",
          "offlineOrder":false,
          "source":"W",
          "status":2,
          "type":1,
          "pan":"",
          "limitPrice":8.1,
          "productType":"INTRADAY",
          "qty":1,
          "disclosedQty":0,
          "remainingQuantity":0,
          "segment":10,
          "symbol":"NSE:IDEA-EQ",
          "description":"VODAFONE IDEA LIMITED",
          "ex_sym":"IDEA",
          "orderDateTime":"02-Aug-2023 13:01:42",
          "side":1,
          "orderValidity":"DAY",
          "stopPrice":0,
          "tradedPrice":8.1,
          "filledQty":1,
          "exchOrdId":"1100000024706527",
          "message":"",
          "ch":-0.35,
          "chp":-4.24,
          "lp":7.9,
          "orderNumStatus":"23080444447604:2",
          "slNo":1,
          "orderTag": "1:Ordertag",
          "takeProfit":0,
          "stopLoss":0
        }
    ]
  }
```

VIDEO LEARNING

### Video learning

[Track your order status (REST and cURL)REST and cURL · 3:02](https://www.youtube.com/watch?v=dsj1QMd_LOY&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)

Go and C video tutorials: coming soon.

## GTT Orders

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/ (last updated 2026-10-14)*

GTT (Good Till Trigger) is used to create orders with longer validity. It helps you set a Target or Stop-Loss for your open positions or holdings, and you can also use it to take new positions.

| Endpoint | Method | Description |
| --- | --- | --- |
| [GTT Single Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-single-order/) | POST | This API allows you to place a single GTT (Good Till Trigger) order that stays active until its trigger price is hit or you cancel it. |
| [GTT OCO Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-oco-order/) | POST | This API allows you to place a one-cancels-other (OCO) GTT order with two legs, where the first leg to trigger cancels the other. |
| [Modify GTT Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/modify-gtt-order/) | PATCH | This API allows you to modify the order type, price, trigger price or quantity of a pending GTT order. |
| [Cancel GTT Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/cancel-gtt-order/) | DELETE | This API allows you to cancel a pending GTT order. |
| [GTT Order Book](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-order-book/) | GET | This API allows you to fetch your GTT orders along with their trigger prices, quantities and current status. |

## Order Management

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/ (last updated 2026-10-14)*

Modify or cancel open orders, one at a time or in bulk, with sync or async endpoints.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Sync](https://fyers.in/api-docs/v3/api/trading/order-management/sync/) | — | Modify or cancel orders, one at a time or in bulk, and get the exchange result in the response. |
| [Async](https://fyers.in/api-docs/v3/api/trading/order-management/async/) | — | Modify or cancel orders through a queue processed at up to 10 orders per second. The response returns id\_fyers. |

## Sync

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/sync/ (last updated 2026-10-14)*

Modify or cancel orders, one at a time or in bulk, and get the exchange result in the response.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/) | PATCH | This API allows you to modify an existing order. |
| [Modify Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-multi-order/) | PATCH | This API allows you to modify multiple orders in a single request. |
| [Cancel Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/) | DELETE | This API allows you to cancel an existing order. |
| [Cancel Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-multi-order/) | DELETE | This API allows you to cancel multiple orders in a single request. |
| [Cancel Pending Orders](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-pending-orders/) | DELETE | This API allows you to cancel pending opposite orders on your open positions, for all symbols or a single position. |

## Async

*Source: https://fyers.in/api-docs/v3/api/trading/order-management/async/ (last updated 2026-10-14)*

Modify or cancel orders through a queue processed at up to 10 orders per second. The response returns id\_fyers.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Modify Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-single-order/) | PATCH | This API allows you to modify an existing order without waiting for the exchange response. |
| [Modify Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/modify-multi-order/) | PATCH | This API allows you to modify multiple orders in a single request without waiting for the exchange response. |
| [Cancel Single Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-single-order/) | DELETE | This API allows you to cancel an existing order without waiting for the exchange response. |
| [Cancel Multi Order](https://fyers.in/api-docs/v3/api/trading/order-management/async/cancel-multi-order/) | DELETE | This API allows you to cancel multiple orders in a single request without waiting for the exchange response. |

## Order Book

*Source: https://fyers.in/api-docs/v3/api/trading/order-book/ (last updated 2026-10-14)*

Get all orders for the day, or look up orders by order ID or order tag.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Get Orders](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/) | GET | This API allows you to fetch all the orders placed in your account today. |
| [Get Order by Order ID](https://fyers.in/api-docs/v3/api/trading/order-book/get-order-by-order-id/) | GET | This API allows you to fetch the details of a single order using its order ID. |
| [Get Orders by Order Tag](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders-by-order-tag/) | GET | This API allows you to fetch the orders placed with a specific order tag. |

## GTT Order Book

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-order-book/ (last updated 2026-10-14)*

This API allows you to fetch your GTT orders along with their trigger prices, quantities and current status.

USE CASE

Check whether your GTT orders are pending, traded, cancelled or rejected.

Details

* You can fetch all pending GTT Orders.
* Orders come back in the `orderBook` array. Use each order's `id` to modify or cancel it.
* `ord_status` shows the state: 1 cancelled, 2 traded or filled, 4 in transit, 5 rejected, 6 pending. `oms_msg` carries the OMS message.
* `gtt_oco_ind` tells the type: 1 for a GTT order and 2 for an OCO order.
* The second-leg fields `price2_limit`, `price2_trigger` and `qty2` apply only to OCO orders.
* `ord_type` is the order type of the first leg and `ord_type2` of the second leg: 1 for Limit and 2 for Market. `ord_type2` is present only for OCO orders.
* Each order also includes the current `ltp`, `ltp_ch` and `ltp_chp` of the symbol.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - For each order

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | * Status code of the API response: * 200: Request successful. * Other codes represent specific error conditions. |
| `message` | string | Optional message about the API request (can be empty for successful requests). |
| `s` | string | Status of the request: "ok" for success, "error" for failure. |
| `orderBook` | array | List of order details. |
| `orderBook[].client_id` | string | Client identifier associated with the order. |
| `orderBook[].exchange` | int | Exchange code where the order is placed, e.g., 10 for NSE. |
| `orderBook[].fy_token` | string | Unique token for the instrument in the order. |
| `orderBook[].id_fyers` | string | Fyers system-generated unique identifier for the order. |
| `orderBook[].id` | string | Order ID provided by the system. |
| `orderBook[].instrument` | int | Instrument type, e.g., 0 for equity. |
| `orderBook[].lot_size` | int | Lot size of the instrument in the order. |
| `orderBook[].multiplier` | int | Multiplier for the instrument (e.g., for derivatives). |
| `orderBook[].ord_status` | int | * Order status code: * 1: Cancelled * 2: Traded / Filled * 3: For future use * 4: Transit * 5: Rejected * 6: Pending |
| `orderBook[].precision` | int | Decimal precision for the instrument's price. |
| `orderBook[].price_limit` | float | Limit price for the first leg of the order. |
| `orderBook[].price2_limit` | float | Limit price for the second leg (if OCO). |
| `orderBook[].price_trigger` | float | Trigger price for the first leg of the order. |
| `orderBook[].price2_trigger` | float | Trigger price for the second leg (if OCO). |
| `orderBook[].product_type` | string | Product type, e.g., "CNC", "MARGIN", "MTF". |
| `orderBook[].qty` | int | Quantity for the first leg of the order. |
| `orderBook[].qty2` | int | Quantity for the second leg (if OCO). |
| `orderBook[].report_type` | string | Status of the order, e.g., "CANCELLED", "PLACED". |
| `orderBook[].segment` | int | Segment code, e.g., 10 for equity. |
| `orderBook[].symbol` | string | Symbol of the instrument, e.g., "NSE:CHOLAFIN-EQ". |
| `orderBook[].symbol_desc` | string | * Full description of the symbol, * e.g., "CHOLAMANDALAM IN & FIN CO". |
| `orderBook[].symbol_exch` | string | Symbol short code on the exchange, e.g., "CHOLAFIN". |
| `orderBook[].tick_size` | float | Minimum price increment for the instrument. |
| `orderBook[].tran_side` | int | Transaction side: 1 for buy, -1 for sell. |
| `orderBook[].gtt_oco_ind` | int | * Indicator for the order type: * 1: GTT order. * 2: OCO order. |
| `orderBook[].create_time` | string | Creation timestamp of the order in human-readable format. |
| `orderBook[].create_time_epoch` | int | Creation timestamp of the order in epoch seconds. |
| `orderBook[].oms_msg` | string | Message from the Order Management System (OMS) about the order's status. |
| `orderBook[].ltp_ch` | float | Last traded price change. |
| `orderBook[].ltp_chp` | float | Last traded price change percentage. |
| `orderBook[].ltp` | float | Last traded price of the instrument. |
| `orderBook[].ord_type` | int | * Order type of the first leg: * 1: Limit. * 2: Market. |
| `orderBook[].ord_type2` | int | * Order type of the second leg: * 1: Limit. * 2: Market. * Present only for OCO orders. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

response = fyers.gtt_orderbook()
print(response)
```

```
Response structure:
{
  "s": "ok",
  "code": 200,
  "message": "",
  "orderBook": [
    {
      "clientId": "X******",
      "exchange": 10,
      "fy_token": "10100000003045",
      "id_fyers": "c6697c04-d9ab-4a7c-a6f4-b0cc4ca698f6",
      "id": "25012400002074",
      "instrument": 0,
      "lot_size": 1,
      "multiplier": 0,
      "ord_status": 1,
      "precision": 2,
      "price_limit": 1020,
      "price2_limit": 620,
      "price_trigger": 1020,
      "price2_trigger": 620,
      "product_type": "CNC",
      "qty": 5,
      "qty2": 5,
      "report_type": "CANCELLED",
      "segment": 10,
      "symbol": "NSE:SBIN-EQ",
      "symbol_desc": "STATE BANK OF INDIA",
      "symbol_exch": "SBIN",
      "tick_size": 0.05,
      "tran_side": 1,
      "gtt_oco_ind": 2,
      "create_time": "24-Jan-2025 16:13:31",
      "create_time_epoch": 1737715411,
      "oms_msg": "GTT/OCO order cancelled successfully.",
      "ltp_ch": 0,
      "ltp_chp": 0,
      "ltp": 0,
      "ord_type": 1,
      "ord_type2": 1
    },
    {
      "clientId": "X******",
      "exchange": 10,
      "fy_token": "10100000003045",
      "id_fyers": "142849a0-d32b-44b5-9108-b7db5ee5e59b",
      "id": "25012400002099",
      "instrument": 0,
      "lot_size": 1,
      "multiplier": 0,
      "ord_status": 1,
      "precision": 2,
      "price_limit": 1000,
      "price2_limit": 600,
      "price_trigger": 1000,
      "price2_trigger": 600,
      "product_type": "MTF",
      "qty": 3,
      "qty2": 3,
      "report_type": "CANCELLED",
      "segment": 10,
      "symbol": "NSE:SBIN-EQ",
      "symbol_desc": "STATE BANK OF INDIA",
      "symbol_exch": "SBIN",
      "tick_size": 0.05,
      "tran_side": -1,
      "gtt_oco_ind": 2,
      "create_time": "24-Jan-2025 16:10:27",
      "create_time_epoch": 1737715227,
      "oms_msg": "GTT/OCO order cancelled successfully.",
      "ltp_ch": 0,
      "ltp_chp": 0,
      "ltp": 0,
      "ord_type": 1,
      "ord_type2": 1
    }
  ]
}
```

## Smart Orders

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/ (last updated 2026-10-14)*

Create Smart Limit, Smart Trail, Smart Step and Smart SIP orders, and modify, cancel, pause, resume and view them.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Smart Limit Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-limit-order/) | POST | This API allows you to place a limit order that stays active until an end time you choose on the same trading day. |
| [Smart Trail](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-trail/) | POST | This API allows you to place a trailing stop-loss order whose stop price follows the market as it moves in your favour. |
| [Smart Step Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-step-order/) | POST | This API allows you to build a position gradually by placing orders at price intervals you define. |
| [Smart SIP](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-sip/) | POST | This API allows you to automate recurring investments in equity stocks and ETFs on a daily, weekly, monthly or custom schedule. |
| [Modify Smart Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/modify-smart-order/) | PATCH | This API allows you to modify a pending smart order, such as its quantity, price limits or time settings. |
| [Cancel Smart Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/cancel-smart-order/) | DELETE | This API allows you to cancel a pending smart order. |
| [Pause Smart Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/pause-or-resume-smart-order/) | PATCH | This API allows you to pause a running smart order and resume it later. |
| [Resume Smart Order](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/pause-or-resume-smart-order/#api-resume-smart-order) | PATCH | This API allows you to pause a running smart order and resume it later. |
| [Smart Order Book](https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-order-book/) | GET | This API allows you to fetch your smart orders along with their current status and filled quantity. |

## Smart Order Book

*Source: https://fyers.in/api-docs/v3/api/trading/order-placement/smart-orders/smart-order-book/ (last updated 2026-10-14)*

This API allows you to fetch your smart orders along with their current status and filled quantity.

USE CASE

Check the status of your smart orders and find the flow ID needed to modify, pause or cancel one.

Details

* Retrieve the list of all smart orders (active, completed, and cancelled).
* **Optional query parameters** (all optional; repeatable parameters may be passed more than once):
* Results are paged. `page_no` defaults to 1 and `page_size` to 15. The default sort is `UpdatedTime`, newest first.
* `sort_by` accepts CreatedTime, UpdatedTime or Alphabet. `ord_by` is 1 for ascending and -1 for descending.
* Filters `flowtype`, `messageType`, `side`, `exchange` (NSE, BSE, MCX) and `product` can each be repeated in the query. `search` matches the symbol name.
* `flowtype` values are 3 (Step), 4 (Limit), 6 (Trail) and 7 (SIP). The filter also lists 5 (Peg).
* `count` is the total number of smart orders before filters, and `filterCount` is the number after filters.
* Each item has `flowId`, `qty`, `filledQty`, `status`, `createdTime` and `updatedTime`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

| Attribute | Data Type | **Default** | Description |
| --- | --- | --- | --- |
| `flowtype` | integer[] | (all types) | Filter by order type (repeatable query param): `3` = Step, `4` = Limit, `5` = Peg, `6` = Trail, `7` = SIP |
| `messageType` | integer[] | (all) | Filter by order status/message type (repeatable query param) |
| `page_no` | int | `1` | Page number for pagination |
| `page_size` | int | 15 | Number of records per page |
| `sort_by` | string | `"UpdatedTime"` | Sort by field: "CreatedTime", "UpdatedTime", "Alphabet" |
| `ord_by` | int | `-1` | Sort order: `1` for ascending, `-1` for descending |
| `side` | integer[] | (all) | Filter by side (repeatable query param): `1` for buy, `-1` for sell |
| `exchange` | string[] | (all) | Filter by exchange (repeatable query param): "NSE", "BSE", "MCX" |
| `product` | string[] | (all) | Filter by product type (repeatable query param): "CNC", "MARGIN", "INTRADAY", "MTF" |
| `search` | string | (none) | Search by symbol name |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Status code: `200` indicates success |
| `s` | string | "ok" indicates success |
| `orderBook` | array | List of smart orders retrieved |
| `count` | int | Total number of smart orders (before filters) |
| `filterCount` | int | Number of smart orders after applying filters |

### Order Book Item Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `flowId` | string | Unique order identifier |
| `flowtype` | int | Order type (`3`=Step, `4`=Limit, `6`=Trail, `7`=SIP) |
| `symbol` | string | Symbol ticker |
| `side` | int | `1`=Buy, `-1`=Sell |
| `qty` | int | Total quantity |
| `filledQty` | int | Executed quantity |
| `status` | int | Order status |
| `productType` | string | Product type |
| `createdTime` | int | Creation timestamp (epoch) |
| `updatedTime` | int | Last update timestamp (epoch) |

Request

```
from fyers_apiv3 import fyersModel

client_id = "AAAAAAAA-100"
access_token = ""

## Initialize the FyersModel instance with your clientid, access_token, and enable async mode_
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

response = fyers.smart_orderbook_with_filter()
print(response)
```

```
Response structure:
{
  "code": 200,
  "s": "ok",
  "orderBook": [
    {
      "flowId": "9076cfa3-af4d-4c73-84f5-0e0371ca1a4a",
      "flowtype": 6,
      "fyId": "FAB24810",
      "timestamp": 1769063695,
      "usertag": "untag",
      "messageType": 13,
      "message": "Cancelled",
      "symbol": "NSE:BSE-EQ",
      "description": "BSE LIMITED",
      "fytoken": "101000000019585",
      "ordtype": 2,
      "price": 0,
      "product": "CNC",
      "side": 1,
      "totqty": 1,
      "mpp": -1,
      "mpp_type": 0,
      "remqty": 1,
      "totplcqty": 0,
      "tradedQty": 0,
      "trigprice": 2821.3,
      "avgPrice": 0,
      "rejQty": 0,
      "canQty": 0,
      "validity": "DAY",
      "created_at": 1769063237,
      "updated_at": 1769063695,
      "ch": 78.1,
      "chp": 2.970937309799148,
      "ltp": 2706.9,
      "openQty": 0,
      "jump_diff": 10,
      "target_price": 0
  }
  ],
  "count": 1,
  "filterCount": 1
}
```

## Positions

*Source: https://fyers.in/api-docs/v3/api/trading/positions/ (last updated 2026-10-14)*

Get open positions, exit or convert them, and set, modify or cancel the stop loss and target on a position.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Get Positions](https://fyers.in/api-docs/v3/api/trading/positions/get-positions/) | GET | This API allows you to fetch your open and closed positions for the current trading day. |
| [Exit Position](https://fyers.in/api-docs/v3/api/trading/positions/exit-position/) | DELETE | This API allows you to exit all or selected open positions in a single request. |
| [Exit Position by ID](https://fyers.in/api-docs/v3/api/trading/positions/exit-position-by-id/) | DELETE | This API allows you to exit specific open positions using their position IDs. |
| [Exit Positions by Filters](https://fyers.in/api-docs/v3/api/trading/positions/exit-positions-by-filters/) | DELETE | This API allows you to exit open positions that match a segment, side and product type. |
| [Convert Position](https://fyers.in/api-docs/v3/api/trading/positions/convert-position/) | POST | This API allows you to convert an open position from one product type to another. |
| [Set Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/set-stop-loss-and-target/) | PATCH | This API allows you to add a Stop Loss and Take Profit to an open position. |
| [Modify Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/modify-stop-loss-and-target/) | PATCH | This API allows you to modify the Stop Loss and Take Profit of an open position. |
| [Cancel Stop Loss & Target](https://fyers.in/api-docs/v3/api/trading/positions/cancel-stop-loss-and-target/) | PATCH | This API allows you to cancel the Stop Loss and Take Profit of an open position. |

## Get Positions

*Source: https://fyers.in/api-docs/v3/api/trading/positions/get-positions/ (last updated 2026-10-14)*

This API allows you to fetch your open and closed positions for the current trading day.

USE CASE

Check the net quantity, average price and profit or loss of each position.

Note

**Live Streaming** — Receive live position updates through the General WebSocket. View [General WebSocket Overview](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/) documentation.

Previous trading day’s closed positions are not shown here.

Details

* Fetches the current open and closed positions for the current trading day. Note that previous trading day’s closed positions will not be shown here.
* Open and closed positions of the current trading day are returned in `netPositions`, and the account totals come in a separate `overall` object.
* `id` is the position id, for example `NSE:SBIN-EQ-INTRADAY` (symbol plus product type). Use it with Exit Position by ID, Convert Position and the stop loss APIs.
* `side` shows whether the position is long or short, and `qty` is the absolute value of `netQty`.
* `realized_profit` is the profit or loss already booked and `pl` is the total. `cfBuyQty` and `cfSellQty` are carry forward quantities; `dayBuyQty` and `daySellQty` are today's.
* For cross currency positions use `rbiRefRate`, and for commodity positions `qtyMulti_com`, when you calculate P&L yourself.
* `slNo` is deprecated. Do not rely on it to sort positions.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - For each position

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `id` | string | The unique value for each position |
| `buyAvg` | float | Average buy price |
| `buyQty` | int | Total buy qty |
| `sellAvg` | float | Average sell price |
| `sellQty` | int | Total sell qty |
| `netAvg` | float | netAvg |
| `netQty` | int | Net qty |
| `side` | int | * The side shows whether the position is long / short * [View Details](https://fyers.in/api-docs/v3/api/appendix/position-sides/) |
| `qty` | int | Absolute value of net qty |
| `productType` | string | * The product type of the position * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `realized_profit` | float | The realized p&l of the position |
| `pl` | float | The total p&l of the position |
| `crossCurrency` | string | * Y => It is cross currency position * N => It is not a cross currency position |
| `rbiRefRate` | float | Incase of cross currency position, the rbi reference rate will be required to calculate the p&l |
| `qtyMulti_com` | float | Incase of commodity positions, this multiplier is required for p&l calculation |
| `segment` | int | * The segment in which the position is taken. * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `exchange` | int | * The exchange in which the position is taken. * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `ltp` | float | LTP is the price from which the next sale of the stocks happens |
| `fytoken` | string | * Fytoken is a unique identifier for every symbol. * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `cfBuyQty` | int | Carry forward buy quantity |
| `cfSellQty` | int | Carry forward sell quantity |
| `dayBuyQty` | int | Day forward buy quantity |
| `daySellQty` | int | Day forward sell quantity |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `slNo` | int | ---Deprecated--- This is used for sorting of positions |

### Response Attributes - Overall Positions

| Attribute | Data Type | Description |
| --- | --- | --- |
| `count_total` | int | Total number of positions present |
| `count_open` | int | Total number of positions opened |
| `pl_total` | float | Total profit and losses |
| `pl_realized` | float | Profit and losses when the owned product is sold |
| `pl_unrealized` | float | Profit and loses when the product is owned , but is not sold |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

response = fyers.positions()
print(response)
```

```
{
    "s": "ok",
    "code": 200,
    "message": "",
    "netPositions":
                [{
                  "netQty":1,
                  "qty":1,
                  "avgPrice":72256.0,
                  "netAvg": 71856.0,
                  "side":1,
                  "productType":"MARGIN",
                  "realized_profit":400.0,
                  "unrealized_profit":461.0,
                  "pl":861.0,
                  "ltp":72717.0,
                  "buyQty":2,
                  "buyAvg":72256.0,
                  "buyVal":144512.0,
                  "sellQty":1,
                  "sellAvg":72656.0,
                  "sellVal":72656.0,
                  "slNo":0,
                  "fyToken":"1120200831217406",
                  "crossCurrency":"N",
                  "rbiRefRate":1.0,
                  "qtyMulti_com":1.0,
                  "segment":20,
                  "symbol":"MCX:SILVERMIC20AUGFUT",
                  "id":"MCX:SILVERMIC20AUGFUT-MARGIN",
                  "cfBuyQty": 0,
                  "cfSellQty": 0,
                  "dayBuyQty": 0,
                  "daySellQty": 1,
                  "exchange": 10,
                }],
     "overall":
                {
                  "count_total":1,
                  "count_open":1,
                  "pl_total":861.0,
                  "pl_realized":400.0,
                  "pl_unrealized":461.0
                }
  }
```

VIDEO LEARNING

### Video learning

[How to manage your portfolio? (Python)Python · 14:13](https://www.youtube.com/watch?v=yFxwZs4cwgI&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to monitor your portfolio? (Node.js)Node.js · 5:08](https://www.youtube.com/watch?v=TLpSSVZZkAg&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[How to monitor your portfolio? (C#)C# · 2:40](https://www.youtube.com/watch?v=9J50HgZU9wo&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[How to monitor your portfolio? (Java)Java · 5:01](https://www.youtube.com/watch?v=NQFLJ7gz45k&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Position Sides

*Source: https://fyers.in/api-docs/v3/api/appendix/position-sides/ (last updated 2026-10-14)*

Long, short and closed position side values.

| Possible Values | Description |
| --- | --- |
| 1 | Long |
| -1 | Short |
| 0 | Closed position |

## Webhooks / Postbacks

*Source: https://fyers.in/api-docs/v3/api/trading/webhooks/ (last updated 2026-10-14)*

The Postback API sends a POST request with a JSON payload to the registered postback\_url of your app when an order’s status changes. This enables you to get orders updates reliably, irrespective of when they happen (Pending, Cancel, Rejected, Traded).

USE CASE

Receive every order status change on your server as it happens, instead of polling Get Orders.

### Things to know

* FYERS sends a POST request with a JSON payload to the postback URL registered for your app.
* Set up the webhook for the app, activate the app by logging in, then read the raw POST body on your server.
* Your server should answer with HTTP status 200. Failed posts can get the URL blacklisted for 30 minutes.

### In this section

| Endpoint | Method | Description |
| --- | --- | --- |
| [Create Webhook](https://fyers.in/api-docs/v3/api/trading/webhooks/create-webhook/) | — | This API allows you to register a webhook URL and a secret to receive order updates for your app. |
| [Activate App](https://fyers.in/api-docs/v3/api/trading/webhooks/activate-app/) | — | This API allows you to activate your app so that order updates start reaching your webhook URL. |
| [Webhook Response](https://fyers.in/api-docs/v3/api/trading/webhooks/webhook-response/) | — | This API allows you to receive order updates as a JSON payload on your webhook URL. |
| [Blacklisting](https://fyers.in/api-docs/v3/api/trading/webhooks/blacklisting/) | — | This API allows you to find out when a webhook URL is blacklisted and for how long. |

## Permission Templates

*Source: https://fyers.in/api-docs/v3/getting-started/create-an-app/permission-templates/ (last updated 2026-10-14)*

You can grant each app a different permission template at creation time. Each template builds on the one before it — pick the narrowest one your app actually needs.

| Permission template | Includes |
| --- | --- |
| **Basic** | Profile details, Logout App, Logout |
| **Transactions Info** | Everything in Basic, plus Orders, Positions, Trades, Holdings, Funds, Market Status |
| **Order Placement** | Everything in Transactions Info, plus Order Placement, Order Modification, Order Cancellation, Exit Positions, Convert Positions |
| **Market Data** | Historical data, Market Depth, Quotes |

Choose the template while creating the app in the [FYERS API dashboard](https://fyers.in/api-docs/v3/getting-started/create-an-app/). You cannot call an API outside your app’s granted permissions — a Basic app cannot place orders even with a valid access token.

## Authentication Flow

*Source: https://fyers.in/api-docs/v3/api/authentication/individual-app/authentication-flow/ (last updated 2026-10-14)*

This guide explains the steps that turn a FYERS login into an access token for your individual app.

USE CASE

Follow the login steps that give your own script or app an access\_token for your FYERS account.

Note

Due to SEBI’s retail algo trading regulations, changes to its usage may take effect on April 1, 2026. Please refer to the [SEBI algo trading rules](https://fyers.in/community/t/sebis-new-algo-trading-rules-kick-in-on-april-1-here-is-what-changes-for-you/12267) for further details.

Details

* The login flow is as follows:
* Navigate to the Login API endpoint
* After successful login, user is redirected to the redirect uri with the auth\_code
* POST the auth\_code and appIdHash (SHA-256 of api\_id + app\_secret) to Validate Authcode API endpoint
* Obtain the access\_token use that for all the subsequent requests
* Individual apps work only for the person who created them; no other FYERS client can log in with your app.
* Step 1: send the user to the login URL with `client_id` (your app ID), `redirect_uri`, `response_type=code` and a random `state`. See [Generate Auth Code](https://fyers.in/api-docs/v3/api/authentication/individual-app/generate-auth-code/).
* `redirect_uri` must match the URL given when the app was created. Keep it under your control, because the `auth_code` sent to it is sensitive.
* After login, check that the returned `state` equals the value you sent, then use the returned `auth_code` in step 2.
* Step 2: POST `grant_type`, `appIdHash` and `code` (the `auth_code`) to [Validate Auth Code (Generate Access Token)](https://fyers.in/api-docs/v3/api/authentication/individual-app/validate-auth-code/).
* `appIdHash` is the SHA-256 hash of `app_id:app_secret`. You can use this [online tool](https://emn178.github.io/online-tools/sha256.html) for reference.
* Send `app_id:access_token` in the HTTP `Authorization` header on every later request; the token expires daily at 6:30 AM.

[](https://assets.fyers.in/myapi-dashboard/docs/authentication_user_flow.webm)

VIDEO LEARNING

### Video learning

[Authentication process (REST and cURL)REST and cURL · 3:27](https://www.youtube.com/watch?v=T-2JZRP7PoM&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Authentication process (Python)Python · 14:41](https://www.youtube.com/watch?v=DYI1NOoY1BE&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Step by step authentication method part 1 (Node.js)Node.js · 3:31](https://www.youtube.com/watch?v=x3T7YpGjv_E&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Step by step authentication part 2 (Node.js)Node.js · 2:41](https://www.youtube.com/watch?v=ZI4rRmD-C3I&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Authentication process (C#)C# · 3:56](https://www.youtube.com/watch?v=fH_wCkp0Pq0&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Authentication process (Java)Java · 6:56](https://www.youtube.com/watch?v=UlQ-bQcRtPg&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Generate Auth Code

*Source: https://fyers.in/api-docs/v3/api/authentication/individual-app/generate-auth-code/ (last updated 2026-10-14)*

This API allows you to send a user to the FYERS login page and receive an auth code on your redirect URI.

USE CASE

Start the login for your own FYERS account and receive an auth\_code on your redirect\_uri.

Details

* Open this URL in the user's browser (a GET request); the user then logs in with their FYERS credentials.
* `redirect_uri` must be the same URL provided at app creation. Example: <https://trade.fyers.in/api-login/redirect-uri/index.html>.
* Send a random `state`. The same value is returned after a successful login, so verify it before using the code.
* The redirect carries an `auth_code`, which you exchange for an access token with [Validate Auth Code (Generate Access Token)](https://fyers.in/api-docs/v3/api/authentication/individual-app/validate-auth-code/).
* Use a `redirect_uri` that is in your control, not a public endpoint such as google.com, because the auth token is sensitive.

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| `client_id` | string | This is the app\_id which you have received after creating the app. Eg: “qwerty-100” |
| `redirect_uri` | string | This is where the user will be redirected after successful login.  Eg: https://trade.fyers.in/api-login/redirect-uri/index.html  **This should be the same as what was provided at the time of app creation** |
| `response_type` | string | This value must always be “code” |
| `state` | string | You send a random value. The same value will be returned after successful login to the redirect uri. Eg: “abcdefg” |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `auth_code` | string | String value which will be used to generate the access\_token |
| `state` | string | This value is returned as is from the first request |

Request

```
## Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

## Replace these values with your actual API credentials
client_id = "SPXXXXE7-100"
secret_key = "N********B"
redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
response_type = "code"
state = "sample_state"

## Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type
)

## Generate the auth code using the session model
response = session.generate_authcode()

## Print the auth code received in the response
print(response)
```

```
https://api-t1.fyers.in/api/v3/generate-authcode?
client_id=SPXXXXE7-100&
redirect_uri=https%3A%2F%2Fdev.fyers.in%2Fredirection%2Findex.html
&response_type=code&state=sample_state&nonce=sample_nonce
```

VIDEO LEARNING

### Video learning

[Authentication process (REST and cURL)REST and cURL · 3:27](https://www.youtube.com/watch?v=T-2JZRP7PoM&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Authentication process (Python)Python · 14:41](https://www.youtube.com/watch?v=DYI1NOoY1BE&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Step by step authentication method part 1 (Node.js)Node.js · 3:31](https://www.youtube.com/watch?v=x3T7YpGjv_E&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Step by step authentication part 2 (Node.js)Node.js · 2:41](https://www.youtube.com/watch?v=ZI4rRmD-C3I&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Authentication process (C#)C# · 3:56](https://www.youtube.com/watch?v=fH_wCkp0Pq0&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Authentication process (Java)Java · 6:56](https://www.youtube.com/watch?v=UlQ-bQcRtPg&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Validate Auth Code (Generate Access Token)

*Source: https://fyers.in/api-docs/v3/api/authentication/individual-app/validate-auth-code/ (last updated 2026-10-14)*

This API allows you to exchange an auth code for an access token.

USE CASE

Get the access\_token that authenticates every later API request, right after login completes.

Note

FYERS API access tokens expire daily at 6:30 AM. Generate a new token after 6:30 AM for it to remain valid throughout the day.

Details

* Send a POST request with a JSON body containing `grant_type` (`authorization_code`), `appIdHash` and `code`, the `auth_code` from the login redirect.
* `appIdHash` is the SHA-256 hash of `app_id:app_secret`; keep the `app_secret` private and never share it.
* Use the returned `access_token` for all later requests, sent as `app_id:access_token` in the `Authorization` header.
* If a token is expired or invalid, API calls return error code -8, -15, -16 or -17. See [API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/).

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| `grant_type` | string | This value must always be “authorization\_code |
| `appIdHash` | string | SHA-256 of api\_id + app\_secret  Eg: SHA-256 of app\_id:app\_secret is 7c7120d2b5004f8de22d8dc2da0453b4d7e6211e37a4108b8371266ecff00498   You can use this [online tool](https://emn178.github.io/online-tools/sha256.html) for reference |
| `code` | string | This is the auth\_code which is received from the first step |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `access_token` | string | This value will be used for all the subsequent requests. |

Request

```
## Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

## Define your Fyers API credentials
client_id = "SPXXXXE7-100"  # Replace with your client ID
secret_key = "N********B"  # Replace with your secret key
redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"  # Replace with your redirect URI
response_type = "code"
grant_type = "authorization_code"

## The authorization code received from Fyers after the user grants access
auth_code = "eyJ0eXAi*******.eyJpc3MiOiJhcGkubG9********.r_65Awa1kGdsNTAgD******"

## Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

## Set the authorization code in the session object
session.set_token(auth_code)

## Generate the access token using the authorization code
response = session.generate_token()

## Print the response, which should contain the access token and other details
print(response)
```

```
{
  's': 'ok',
  'code': 200,
  'message': '',
  'access_token': 'eyJ0eXAiOi***.eyJpc3MiOiJh***.HrSubihiFKXOpUOj_7***',
  'refresh_token': 'eyJ0eXAiO***.eyJpc3MiOiJh***.67mXADDLrrleuEH_EE***'
}
```

VIDEO LEARNING

### Video learning

[Authentication process (REST and cURL)REST and cURL · 3:27](https://www.youtube.com/watch?v=T-2JZRP7PoM&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Authentication process (Python)Python · 14:41](https://www.youtube.com/watch?v=DYI1NOoY1BE&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Step by step authentication method part 1 (Node.js)Node.js · 3:31](https://www.youtube.com/watch?v=x3T7YpGjv_E&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Step by step authentication part 2 (Node.js)Node.js · 2:41](https://www.youtube.com/watch?v=ZI4rRmD-C3I&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Authentication process (C#)C# · 3:56](https://www.youtube.com/watch?v=fH_wCkp0Pq0&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Authentication process (Java)Java · 6:56](https://www.youtube.com/watch?v=UlQ-bQcRtPg&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Best Practices

*Source: https://fyers.in/api-docs/v3/api/authentication/individual-app/best-practices/ (last updated 2026-10-14)*

This guide lists the practices that keep your app credentials and tokens secure.

USE CASE

Check your app against these security rules before you start using it regularly.

Details

* These are the recommended best practises that you should follow while using the APIs
* Never share your app\_secret with anyone
* Never share your access\_token with anyone
* Do not provide trading permissions unless you want to use the app to place orders
* Provide a redirect\_uri which is in your control rather than a public endpoint such as google.com
* You should send a random value in the state parameter and verify whether the same value has been returned to you
* Access tokens expire daily at 6:30 AM. Generate a new token after 6:30 AM for it to remain valid throughout the day.
* Do not provide trading permissions unless you want to use the app to place orders. See [Permission Templates](https://fyers.in/api-docs/v3/getting-started/create-an-app/permission-templates/).
* If a token is expired or invalid, API calls return error code -8, -15, -16 or -17. See [API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/).

## Best Practices

*Source: https://fyers.in/api-docs/v3/api/authentication/third-party-app/best-practices/ (last updated 2026-10-14)*

This guide lists the practices that keep your app credentials and users’ tokens secure.

USE CASE

Review these security rules before you launch your platform to users.

Details

* These are the recommended best practises that you should follow while using the APIs
* Never share your app\_secret with anyone
* Never share your access\_token with anyone
* Do not provide trading permissions unless you want to use the app to place orders
* Provide a redirect\_uri which is in your control rather than a public endpoint such as google.com
* You should send a random value in the state parameter and verify whether the same value has been returned to you
* Do not store the app\_secret in the front end. It should be securely kept without exposing it to third parties.
* Because `appIdHash` is built from the `app_secret`, calculate it and call the token endpoints from your backend, not from front-end code.
* Access tokens expire daily at 6:30 AM. Generate a new token after 6:30 AM for it to remain valid throughout the day.
* Do not provide trading permissions unless you want to use the app to place orders. See [Permission Templates](https://fyers.in/api-docs/v3/getting-started/create-an-app/permission-templates/).
* If a token is expired or invalid, API calls return error code -8, -15, -16 or -17. See [API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/).

## OAuth 2.0 Flow

*Source: https://fyers.in/api-docs/v3/api/authentication/third-party-app/oauth-2-0-flow/ (last updated 2026-10-14)*

This guide explains how your platform logs in FYERS users and gets an access token for each of them.

USE CASE

Set up login for a platform where FYERS clients use your app with their own accounts.

Details

* This is a simple OAuth 2 Authentication Flows.
* This is recommended for applications which have a backend server which can authenticate the second step
* This is **not recommended** for Single Page Applications (SPA)
* The flow has two steps: Step 1, [User Authorization](https://fyers.in/api-docs/v3/api/authentication/third-party-app/user-authorization/) (the redirect returns the `auth_code` and `state` to your `redirect_uri`; see [Authorization Code](https://fyers.in/api-docs/v3/api/authentication/third-party-app/authorization-code/)); Step 2, [Generate Access Token](https://fyers.in/api-docs/v3/api/authentication/third-party-app/generate-access-token/).
* Third-party apps are created for platform providers. To create a common app, contact [[email protected]](/cdn-cgi/l/email-protection#fe9f8e97d38d8b8e8e918c8abe98879b8c8dd09790).
* The user logs in with their own FYERS credentials and is redirected to your `redirect_uri` with an `auth_code`.
* The resulting `access_token` expires daily at 6:30 AM; send it as `app_id:access_token` in the `Authorization` header.
* **Diagram**

[](https://assets.fyers.in/myapi-dashboard/docs/authentication_user_flow.webm)

## User Authorization

*Source: https://fyers.in/api-docs/v3/api/authentication/third-party-app/user-authorization/ (last updated 2026-10-14)*

This API allows you to send a user to the FYERS login page to authorize your app.

USE CASE

Start the login when a user connects their FYERS account to your platform.

Details

* You need to navigate the user to the FYERS login url with the correct get parameters
* Navigate the user to the FYERS login URL with these query parameters (a GET request). The user logs in with their own FYERS credentials.
* Provide a `redirect_uri` you control, not a public endpoint such as google.com; it receives the sensitive `auth_code`.
* Send a random `state` for each login and verify that the same value is returned before using the code.
* After a successful login the user lands on your `redirect_uri` with `auth_code` and `state`; see [Authorization Code](https://fyers.in/api-docs/v3/api/authentication/third-party-app/authorization-code/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `client_id` | string | * This is the app\_id which you have received after creating the app. * Eg: “qwerty-102” |
| `redirect_uri` | string | * This is where the user will be redirected after successful login. * Eg: * <https://trade.fyers.in/api-login/redirect-uri/index.html> * **This should be the same as what was provided at the time of app creation** |
| `response_type` | string | This value must always be “code” |
| `state` | string | * You send a random value. The same value will be returned after successful login to the redirect uri. * Eg: “abcdefg” |

## Authorization Code

*Source: https://fyers.in/api-docs/v3/api/authentication/third-party-app/authorization-code/ (last updated 2026-10-14)*

This page describes the auth\_code and state that FYERS sends to your redirect\_uri after the user logs in.

USE CASE

Read the auth\_code and state sent to your redirect\_uri, and check the state before you use the code.

Details

* After successful login, the user is redirected to the redirect\_uri with the auth\_code and the same state value that was sent in the request.
* `auth_code` is a string you exchange for the `access_token` in [Generate Access Token](https://fyers.in/api-docs/v3/api/authentication/third-party-app/generate-access-token/).
* `state` is returned unchanged; compare it with the value you sent before continuing.
* These values arrive at your `redirect_uri` after a successful login, so it must be a URL that is in your control.

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `auth_code` | string | String value which will be used to generate the access\_token |
| `state` | string | This value is returned as is from the first request |

## Generate Access Token

*Source: https://fyers.in/api-docs/v3/api/authentication/third-party-app/generate-access-token/ (last updated 2026-10-14)*

This API allows you to exchange an auth code for the access token of a user.

USE CASE

Get a user's access\_token from your backend as soon as the redirect returns an auth\_code. Keep the app\_secret on your server.

Details

* POST the auth\_code and appIdHash (SHA-256 of api\_id + app\_secret) to the Validate Authcode API endpoint to obtain the access\_token.
* Send a POST request with a JSON body containing `grant_type` (`authorization_code`), `appIdHash` and `code`, the `auth_code` from the redirect.
* `appIdHash` is the SHA-256 hash of `app_id:app_secret`; keep the `app_secret` on your server and never share it.
* Send `app_id:access_token` in the HTTP `Authorization` header on every later request made for this user.
* If a token is expired or invalid, API calls return error code -8, -15, -16 or -17. See [API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `grant_type` | string | This value must always be “authorization\_code” |
| `appIdHash` | string | * SHA-256 of api\_id + app\_secret * Eg: SHA-256 of app\_id:app\_secret is * 7c7120d2b5004f8de22d8dc2da0453b4d7e6211e37a4108b8371266ecff00498 * You can use this [online tool](https://emn178.github.io/online-tools/sha256.html) for reference |
| `code` | string | This is the auth\_code which is received from the first step |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `access_token` | string | This value will be used for all the subsequent requests. |

**Note:** FYERS API access tokens expire daily at 6:30 AM. Generate a new token after 6:30 AM for it to remain valid throughout the day.

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl -H "Content-Type: application/json" -X POST -d
   '{
         "grant_type":"authorization_code","appIdHash":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","code":"eyJ..."
   }' https://api-t1.fyers.in/api/v3/validate-authcode
```

```
{
   "s": "ok",
   "code": 200,
   "message": "",
   "access_token": "eyJ..."
 }
```

## Handle errors and rate limits

*Source: https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/ (last updated 2026-10-14)*

API errors should be handled as part of the normal workflow. Read the complete response, identify the exact cause and correct it before deciding whether to retry. Do not retry an order or position request until you have checked whether the earlier action succeeded.

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Step-by-step workflow

1. 1

   Capture the complete response

   Record the operation, time, response code and response message. Keep App Secrets, access tokens and other sensitive values out of logs.
2. 2

   Read the error message first

   The response message explains the specific reason returned for that request. Use it to understand the affected field, token, order, position or limit.
3. 3

   Review the error code

   Use the code to identify the error category. Then refer to Appendix → Common API Error Codes for the standard description and recommended action.
4. 4

   Correct the cause before retrying

   Fix invalid inputs, renew an expired token, use the correct App ID or symbol, or wait for the applicable rate-limit window. Do not repeat an unchanged request.
5. 5

   Retry only when it is safe

   Read requests may be retried after a temporary failure. Before retrying an order, exit, conversion or other account-changing request, check the latest account state.
6. 6

   Verify the final state

   Use the relevant Order Book, positions, portfolio or market-data API to confirm the result. Keep the original code and message for troubleshooting if the issue continues.
7. 7

   Verify the result

   Confirm that the corrected request succeeds or that the expected account state is visible. If the request still fails, compare the latest response code and message with the Common API Error Codes table before taking another action.

### Common issues

Reading only the code and ignoring the message400 Bad Request

The numeric or HTTP code names the category. The message explains the exact condition. Read both before deciding the next action.

```
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Retrying an invalid request without correcting it400 Bad Request

Repeating the same payload will return the same error. Fix the stated field or permission, then send a new request.

```
HTTP/1.1 400 Bad Request
{"s":"error","message":"Invalid symbol"}
```

[Review API conventions →](https://fyers.in/api-docs/v3/api/api-standards/)

Retrying an account-changing request too earlyPending

Before placing, modifying or cancelling again, read the latest order or position state. A timeout does not mean the first request failed.

```
{"s":"ok","orderStatus":"6","message":"Pending"}
```

[View Order Book →](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/)

Continuing after a rate limit429 Too Many Requests

Stop the burst, wait, then retry with exponential backoff. Check Plans & limits if the cap is plan-related.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/)

Logging access tokens or App Secrets401 Unauthorized

Never write tokens, App Secrets or passwords to logs, chat, or source control. Rotate credentials if they were exposed.

```
Authorization: appId:access_token
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Related API reference

[API conventions

Review API conventions

View API →](https://fyers.in/api-docs/v3/api/api-standards/)[Common API Error Codes

Look up error codes

View API →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)[Authentication

Generate an access token

View API →](https://fyers.in/api-docs/v3/api/authentication/)[Plans & limits

Review rate limits

View API →](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/)[Troubleshooting & FAQ

Find common solutions

View API →](https://fyers.in/api-docs/v3/resources/)

### Continue with AI

✨

Continue with AI

Want help handling errors and rate limits?

VIDEO LEARNING

### Video learning

[FYERS API playlist (REST and cURL)](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)

## Order Sources

*Source: https://fyers.in/api-docs/v3/api/appendix/order-sources/ (last updated 2026-10-14)*

Source channel codes for mobile, web, API and other platforms.

| Possible Values | Description |
| --- | --- |
| M | Mobile |
| W | Web |
| R | Fyers One |
| A | Admin |
| ITS | API |

## Resources

*Source: https://fyers.in/api-docs/v3/resources/ (last updated 2026-10-14)*

Find implementation help, common answers, direct support and community discussions.

[Troubleshooting Guide

Diagnose authentication, access, order, market-data, WebSocket and rate-limit issues from the API response.

Open guide →](#troubleshooting-guide)[Frequently Asked Questions

Find common answers for FYERS API integrations in the FYERS Help Centre.

Open FAQ →](https://support.fyers.in/portal/en/kb/fyers-api-integrations)[API Support

Contact support with the request details needed to investigate an API issue.

Contact support →](#api-support)[Community

Discuss, share and raise feature requests on FYERS API, and review product or regulatory updates with other API users.

Join community →](#community)

### Troubleshooting Guide

Use the troubleshooting guide to diagnose common integration issues — outdated SDKs, login rate limits, app-type restrictions, WebSocket disconnects and IP whitelisting. For error responses returned directly by an API call, see [Handle errors and rate limits](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/).

[Open troubleshooting guide →](https://fyers.in/api-docs/v3/getting-started/guides/troubleshooting-guide/)

### Frequently Asked Questions

For more frequently asked questions on FYERS API integrations, visit the FYERS Help Centre. You’ll find answers on authentication, orders, market data, WebSockets and related API topics.

[Open FYERS API FAQ ↗](https://support.fyers.in/portal/en/kb/fyers-api-integrations)

### API Support

Hours:9:00 AM – 5:30 PM

Phone:[080-600 01 111](tel:08060001111)

Email:[[email protected]](/cdn-cgi/l/email-protection#7213021b5f010702021d000632140b1700015c1b1c)

When contacting support, include the API category, request time, response code and message, and the relevant request identifier.

Never share passwords, App Secrets or access tokens.

### Community

Use the FYERS Community, a dedicated community to discuss, share and raise feature requests on FYERS API. Discuss implementation approaches, learn from other API users and review related product or regulatory updates. Our goal is to empower the algo trading community in India with the most robust and easy-to-integrate APIs. Search existing discussions before creating a new post, and never include credentials, tokens or sensitive account information.

[Open FYERS Community ↗](https://fyers.in/community/c/api-algo/20)

## Video Tutorials

*Source: https://fyers.in/api-docs/v3/resources/video-tutorials/ (last updated 2026-10-14)*

**Coming soon:**

Documentation for this topic is being prepared and will be published here.

## Profile

*Source: https://fyers.in/api-docs/v3/api/account/profile/ (last updated 2026-10-14)*

This API allows you to fetch the basic details of the account holder and confirm that your access token is valid.

Official reference: [Profile](https://fyers.in/api-docs/v3/api/account/profile/)

USE CASE

Check that your access token works right after login and see which FYERS account it belongs to.

The response also flags whether DDPI and MTF are enabled.

Details

* This allows you to fetch basic details of the client.
* Your app needs the **Basic** permission. It covers Profile Details, Logout App and Logout.
* The request takes no parameters. Send only the `Authorization` header.
* The response gives the account holder details (`name`, `display_name`, `fy_id`, `email_id`, `mobile_number`, `pan`, `image`) and security details (`totp`, `pin_change_date`, `pwd_change_date`, `pwd_to_expire`).
* `ddpi_enabled` and `mtf_enabled` are booleans for the account's DDPI and MTF status.
* Personally identifiable information in the response is masked for privacy and compliance. Report any problem to [[email protected]](/cdn-cgi/l/email-protection).
* An expired or invalid token is rejected with error code -8, -15, -16 or -17. See [API Error Codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `name` | string | Name of the client |
| `display_name` | string | Display name, if any, provided by the client |
| `fy_id` | string | The client id of the fyers user |
| `image` | string | URL link to the user’s profile picture, if any. |
| `email_id` | string | Email address of the client |
| `pan` | string | PAN of the client |
| `pin_change_date` | string | Date when last PIN was updated |
| `pwd_change_date` | string | Date when last password was updated |
| `mobile_number` | string | Registered mobile number |
| `totp` | boolean | Status of TOTP |
| `pwd_to_expire` | int | Number of days until the current password expires |
| `ddpi_enabled` | boolean | Status of DDPI |
| `mtf_enabled` | boolean | Status of MTF |

**Note:** As per our privacy policy and in line with compliance requirements, PII (Personally Identifiable Information) information will be masked to safeguard customer information. If you notice any issues, please report to us at [[email protected]](/cdn-cgi/l/email-protection) for remedial action as may be necessary.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

## Make a request to get the user profile information
response = fyers.get_profile()

## Print the response received from the Fyers API
print(response)
```

```
{
    "s":"ok",
    "code":200,
    "message":"",
    "data":{
        "fy_id":"XXXXX86",
        "name":"JOHN",
        "image":"https://fyers-user-details.s3.amazonaws.com/image/FK0000000001?X-Amz-Algorithm=AWS4-HMAC",
        "display_name":"JD",
        "pin_change_date":"15-12-2022 09:24:05",
        "email_id":"[email protected]",
        "pwd_change_date":"None",
        "PAN": "FYxxxxxx0S",
        "mobile_number": "99xxxxxx99",
        "totp":True,
        "pwd_to_expire":90
        "ddpi_enabled": False,
        "mtf_enabled": False
    }
  }
```

VIDEO LEARNING

### Video learning

[Check account information (REST and cURL)REST and cURL · 2:30](https://www.youtube.com/watch?v=QuY-uymOb1k&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[How to manage your portfolio? (Python)Python · 14:13](https://www.youtube.com/watch?v=yFxwZs4cwgI&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to monitor your portfolio? (Node.js)Node.js · 5:08](https://www.youtube.com/watch?v=TLpSSVZZkAg&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[How to monitor your portfolio? (C#)C# · 2:40](https://www.youtube.com/watch?v=9J50HgZU9wo&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[How to monitor your portfolio? (Java)Java · 5:01](https://www.youtube.com/watch?v=NQFLJ7gz45k&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Place your first order

*Source: https://fyers.in/api-docs/v3/getting-started/guides/place-your-first-order/ (last updated 2026-10-14)*

Go from an authenticated FYERS app to a verified order in six steps.

Follow the examples using the global code switcher — **Python**, **Node.js**, **Java**, or **cURL**.

This guide explains the full sequence without requiring you to assemble the workflow from separate endpoint pages.

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Workflow

01→

Authenticate

Generate a valid access token.

02→

Prepare

Build the order request.

03→

Submit

Send the order request.

04→

Read

Check the API response.

05→

Verify

Confirm the order status.

06→

Handle

Handle rejected or pending orders.

07→

Verify

Confirm the workflow result.

1. 1

   Authenticate

   Complete the authorisation flow and generate a valid access token. Keep the token secure and confirm that the app has the permissions required for order placement.

   [View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

   ```
   Authorization: app_id:access_token
   ```
2. 2

   Prepare your order

   Choose the instrument, side, quantity, product type, order type and price fields required for the trade. Validate the symbol and review the order before submission.

   [View Single Order API →](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/)

   ```
   {
     "symbol": "NSE:SBIN-EQ",
     "qty": 1,
     "type": 1,
     "side": 1,
     "productType": "INTRADAY",
     "limitPrice": 0,
     "stopPrice": 0,
     "validity": "DAY",
     "disclosedQty": 0,
     "offlineOrder": false,
     "orderTag": "tag1",
     "isSliceOrder": false
   }
   ```
3. 3

   Submit the order

   Send the order request once. Record the returned identifier and response so the result can be checked without placing a duplicate order.

   [View Single Order API →](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/)

   **IMPORTANT**

   Order placement changes account state.
   Do not blindly retry a timed-out order request.
   Check the Order Book or Order Details API before submitting another order.

   Application↓

   Single Order API↓

   Order ID / API response↓

   Order Book / Order Details↓

   Order status↓

   Execution confirmation

   ```
   curl -H "Authorization:app_id:access_token" \
     -H "Content-Type:application/json" \
     -X POST -d '{ "symbol":"NSE:SBIN-EQ", "qty":1, "type":1, "side":1, "productType":"INTRADAY" }' \
     https://api-t1.fyers.in/api/v3/orders/sync
   ```
4. 4

   Read the response

   Confirm whether the request was accepted or rejected. Do not treat an accepted API request as a completed trade; execution status must be checked separately.

   ```
   {
     "s": "ok",
     "code": 1101,
     "message": "Order submitted successfully. Your Order Ref. No.808058117761",
     "id": "808058117761"
   }
   ```
5. 5

   Verify the order

   Open the Order Book or request order details using the returned identifier. Check the current status, filled quantity, pending quantity and rejection reason where available.

   [View Order Book / Order Details →](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/)
6. 6

   Handle rejected or pending orders

   For a rejected order, correct the stated issue before trying again. For a pending order, monitor its status or modify or cancel it according to the trading decision.

   [View Modify Single Order →](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/) [View Cancel Single Order →](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/)
7. 7

   Verify the result

   Check the relevant API response and account or market-data state to confirm that the workflow completed successfully. If the result is partial or unsuccessful, review the returned status and message before deciding whether to retry or take another action.

   * Request accepted
   * Order identifier received
   * Order status checked
   * Filled/pending/rejected status understood
   * Execution confirmed where applicable

### Common issues

Authentication failure401 Unauthorized

Check that the access token is valid and that the app has order-placement permission. Generate a new token if it has expired.

```
HTTP/1.1 401 Unauthorized
{"s":"error","code":-8,"message":"Could not authenticate the user"}
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

Invalid request400 Bad Request

Validate symbol, quantity, side, product type and other required order fields against the Single Order documentation before retrying.

```
HTTP/1.1 400 Bad Request
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Rate limit429 Too Many Requests

Respect the API rate limits for your plan. Wait, then retry with exponential backoff instead of sending the same request immediately.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
{"s":"error","message":"Rate limit exceeded"}
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

Pending orderPending

The order was accepted but is not yet complete. Read the current order status from the order book before placing a duplicate.

```
{"s":"ok","orderStatus":"6","message":"Pending"}
```

[View Order Book →](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/)

Network timeoutTimeout

The request may have reached the exchange even if your client timed out. Verify order state before retrying.

```
Error: request timed out
```

[Handle retries safely →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

**Prefer a guided AI workflow?** Use [FYERS MCP](https://fyers.in/api-docs/ai/) or [FYERS GPT](https://fyers.in/api-docs/ai/gpt/) for supported account and trading workflows without starting from REST.

### Related API reference

[Authentication

Generate an access token

View API →](https://fyers.in/api-docs/v3/api/authentication/)[Single Order

Submit a new order

View API →](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/)[Order Book / Order Details

Verify the order

View API →](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/)[Modify Single Order

Modify an existing order

View API →](https://fyers.in/api-docs/v3/api/trading/order-management/sync/modify-single-order/)[Cancel Single Order

Cancel an order

View API →](https://fyers.in/api-docs/v3/api/trading/order-management/sync/cancel-single-order/)

### Continue with AI

✨

Continue with AI

Want help implementing this workflow?

## Stream live market data

*Source: https://fyers.in/api-docs/v3/getting-started/guides/stream-live-market-data/ (last updated 2026-10-14)*

Use Data Socket when your application needs continuous market updates rather than repeated REST requests.

> Plan check
> Data Socket symbol limits are per user, across all connections: Standard supports 100 symbols and Prime supports 5,000. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Step-by-step workflow

1. 1

   Authenticate the socket connection

   Prepare the verified socket authentication value using the active FYERS API session. Do not place credentials directly in logs or client-visible output.
2. 2

   Open a connection

   Create the Data Socket connection and register handlers for connection, message, error and close events.
3. 3

   Subscribe to symbols

   Subscribe only to the symbols and data type required by the workflow. Keep the subscription count within the applicable Standard or Prime limit.
4. 4

   Process incoming updates

   Validate each message type before reading its fields. Update the application state using the latest event rather than assuming every message has the same structure.
5. 5

   Change or remove subscriptions

   Unsubscribe from symbols that are no longer required and update the local subscription list so the application and socket stay aligned.
6. 6

   Reconnect safely after interruption

   Reconnect with controlled backoff, restore only the required subscriptions and avoid opening multiple active connections for the same workflow.
7. 7

   Verify the result

   Check the relevant API response and account or market-data state to confirm that the workflow completed successfully. If the result is partial or unsuccessful, review the returned status and message before deciding whether to retry or take another action.

### Common issues

Authentication or permission failure401 Unauthorized

The access token is missing, expired, or the app does not have the required permission. Generate a fresh token and retry the request.

```
HTTP/1.1 401 Unauthorized
{"s":"error","code":-8,"message":"Could not authenticate the user"}
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

Incorrect request inputs400 Bad Request

A required field is missing or invalid (symbol, quantity, side, or product type). Read the response message, correct the payload, then retry.

```
HTTP/1.1 400 Bad Request
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Plan or rate-limit restriction429 Too Many Requests

The request exceeded the plan’s rate limit or an entitlement. Back off before retrying and confirm the Standard vs Prime limits for the API you are calling.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
{"s":"error","message":"Rate limit exceeded"}
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

Temporary network or socket interruptionTimeout

The connection dropped before a response arrived. Check the latest order, position, or socket state before sending the same request again.

```
Error: socket hang up
ECONNRESET
```

[View WebSocket Overview →](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)

### Related API reference

[WebSocket Overview

WebSocket services overview

View API →](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)[Data Socket - Connect and Subscribe

Subscribe to live symbols

View API →](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-connect-and-subscribe/)[Symbol Update

Process symbol updates

View API →](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-symbol-update/)[Depth Update

Process depth updates

View API →](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-depth-update/)[Unsubscribe and Connection Management

Manage subscriptions and connections

View API →](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-unsubscribe-and-connection-management/)[Advanced Configuration

Tune the queue processing interval

View API →](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/advanced-configuration/)

### Continue with AI

✨

Continue with AI

Want help implementing live market-data streaming?

VIDEO LEARNING

### Video learning

[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[FYERS API playlist (Node.js)](https://www.youtube.com/playlist?list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[FYERS API playlist (Java)](https://www.youtube.com/playlist?list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

## Monitor orders and positions in real time

*Source: https://fyers.in/api-docs/v3/getting-started/guides/monitor-orders-and-positions/ (last updated 2026-10-14)*

This Guide shows how to combine an initial REST snapshot with live events so your application can maintain a reliable view of orders, trades and positions.

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Step-by-step workflow

1. 1

   Read the initial order and position state

   Before opening the socket, read the current Order Book and Positions so the application starts from a known account state.
2. 2

   Connect to General WebSocket

   Open an authenticated General WebSocket connection and register the event handlers required by the workflow.
3. 3

   Subscribe to required event streams

   Subscribe to the supported order, trade, position or general events needed by the application.
4. 4

   Process order events

   Use order events to update status, quantities and rejection information. Match each event to the correct order identifier.
5. 5

   Process trade and position events

   Apply trade and position events to the local account view. Keep order state, executed trades and resulting positions as separate records.
6. 6

   Recover state after reconnect

   After a disconnection, read the latest REST state again before resuming event processing. This prevents missed events from leaving the application out of sync.
7. 7

   Verify the result

   Check the relevant API response and account or market-data state to confirm that the workflow completed successfully. If the result is partial or unsuccessful, review the returned status and message before deciding whether to retry or take another action.

### Common issues

Authentication or permission failure401 Unauthorized

The access token is missing, expired, or the app does not have the required permission. Generate a fresh token and retry the request.

```
HTTP/1.1 401 Unauthorized
{"s":"error","code":-8,"message":"Could not authenticate the user"}
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

Incorrect request inputs400 Bad Request

A required field is missing or invalid (symbol, quantity, side, or product type). Read the response message, correct the payload, then retry.

```
HTTP/1.1 400 Bad Request
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Plan or rate-limit restriction429 Too Many Requests

The request exceeded the plan’s rate limit or an entitlement. Back off before retrying and confirm the Standard vs Prime limits for the API you are calling.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
{"s":"error","message":"Rate limit exceeded"}
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

Temporary network or socket interruptionTimeout

The connection dropped before a response arrived. Check the latest order, position, or socket state before sending the same request again.

```
Error: socket hang up
ECONNRESET
```

[View WebSocket Overview →](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)

### Related API reference

[Order Book and Order Details

Read current orders

View API →](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/)[Trade Book

Read executed trades

View API →](https://fyers.in/api-docs/v3/api/trading/trade-book/get-trades/)[Positions

Read open positions

View API →](https://fyers.in/api-docs/v3/api/trading/positions/get-positions/)[General Socket - Connect

Connect to General WebSocket

View API →](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-connect/)[General Socket - Subscribe

Subscribe to account events

View API →](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-subscribe/)[General Socket - UnSubscribe

Unsubscribe from account events

View API →](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-unsubscribe/)[Ping method

Keep the General WebSocket connection alive

View API →](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/ping-method/)[Order Events

Process order events

View API →](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-order-events/)[Trade Events

Process trade events

View API →](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-trade-events/)[Position Events

Process position events

View API →](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-position-events/)

### Continue with AI

✨

Continue with AI

Want help monitoring orders and positions in real time?

VIDEO LEARNING

### Video learning

[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[FYERS API playlist (Node.js)](https://www.youtube.com/playlist?list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)

## Work with historical market data

*Source: https://fyers.in/api-docs/v3/getting-started/guides/work-with-historical-market-data/ (last updated 2026-10-14)*

Use historical data for charting, research, analysis and backtesting. Start by checking the available history and resolution for your plan.

> Plan check
> Daily, intraday, Seconds Data and Expired F&O Data availability differs between Standard and Prime.

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Step-by-step workflow

1. 1

   Choose the instrument and time range

   Identify the instrument through Symbol Master and define the exact start and end period required for analysis.
2. 2

   Select the required resolution

   Choose daily, intraday or seconds-level data according to the use case and plan availability. Avoid requesting a finer resolution than the analysis needs.
3. 3

   Request historical candles

   Send the historical-data request with the verified symbol, resolution and date fields.
4. 4

   Validate the returned period

   Check that the first and last candle match the requested trading period and that timestamps are interpreted using the documented time-zone rules.
5. 5

   Handle missing or unavailable data

   Separate non-trading periods, unavailable history and invalid requests. Do not fill missing market data without a defined research rule.
6. 6

   Store and reuse data responsibly

   Cache data where appropriate, retain the source and retrieval time, and avoid repeatedly requesting the same historical range.
7. 7

   Verify the result

   Check the relevant API response and account or market-data state to confirm that the workflow completed successfully. If the result is partial or unsuccessful, review the returned status and message before deciding whether to retry or take another action.

### Common issues

Authentication or permission failure401 Unauthorized

The access token is missing, expired, or the app does not have the required permission. Generate a fresh token and retry the request.

```
HTTP/1.1 401 Unauthorized
{"s":"error","code":-8,"message":"Could not authenticate the user"}
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

Incorrect request inputs400 Bad Request

A required field is missing or invalid (symbol, quantity, side, or product type). Read the response message, correct the payload, then retry.

```
HTTP/1.1 400 Bad Request
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Plan or rate-limit restriction429 Too Many Requests

The request exceeded the plan’s rate limit or an entitlement. Back off before retrying and confirm the Standard vs Prime limits for the API you are calling.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
{"s":"error","message":"Rate limit exceeded"}
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

Temporary network or socket interruptionTimeout

The connection dropped before a response arrived. Check the latest order, position, or socket state before sending the same request again.

```
Error: socket hang up
ECONNRESET
```

[View WebSocket Overview →](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)

### Related API reference

[Historical Candles

Download candle data

View API →](https://fyers.in/api-docs/v3/api/market-data/historical-data/)[Symbol Master

Resolve instrument symbols

View API →](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-file/)[Plans & Limits

Review data entitlements

View API →](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/)

### Continue with AI

✨

Continue with AI

Want help working with historical market data?

VIDEO LEARNING

### Video learning

[FYERS API playlist (REST and cURL)](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[FYERS API playlist (Node.js)](https://www.youtube.com/playlist?list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)

## Manage positions, funds and risk

*Source: https://fyers.in/api-docs/v3/getting-started/guides/manage-positions-funds-and-risk/ (last updated 2026-10-14)*

Build account-aware workflows by reading current exposure and available funds before deciding what action to take.

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Step-by-step workflow

1. 1

   Read open positions

   Retrieve current positions and identify net quantity, side, product type and available action for each position.
2. 2

   Read holdings and available funds

   Read holdings and funds separately. Holdings represent owned instruments, while funds show the balances available for account activity.
3. 3

   Check supported margin information

   Use the supported margin calculation before submitting an order when the workflow depends on available margin.
4. 4

   Decide whether to exit or convert a position

   Confirm the position, quantity and intended outcome before choosing exit or conversion. Treat these as separate account-changing actions.
5. 5

   Submit the supported position action

   Send the exit or conversion request with the verified attributes. Store the response and avoid repeating the action while its outcome is uncertain.
6. 6

   Refresh and verify account state

   Read positions and funds again after the action. Confirm that the resulting account state matches the intended change.
7. 7

   Verify the result

   Check the relevant API response and account or market-data state to confirm that the workflow completed successfully. If the result is partial or unsuccessful, review the returned status and message before deciding whether to retry or take another action.

### Common issues

Authentication or permission failure401 Unauthorized

The access token is missing, expired, or the app does not have the required permission. Generate a fresh token and retry the request.

```
HTTP/1.1 401 Unauthorized
{"s":"error","code":-8,"message":"Could not authenticate the user"}
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

Incorrect request inputs400 Bad Request

A required field is missing or invalid (symbol, quantity, side, or product type). Read the response message, correct the payload, then retry.

```
HTTP/1.1 400 Bad Request
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Plan or rate-limit restriction429 Too Many Requests

The request exceeded the plan’s rate limit or an entitlement. Back off before retrying and confirm the Standard vs Prime limits for the API you are calling.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
{"s":"error","message":"Rate limit exceeded"}
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

Temporary network or socket interruptionTimeout

The connection dropped before a response arrived. Check the latest order, position, or socket state before sending the same request again.

```
Error: socket hang up
ECONNRESET
```

[View WebSocket Overview →](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)

**Prefer a guided AI workflow?** Use [FYERS MCP](https://fyers.in/api-docs/ai/) or [FYERS GPT](https://fyers.in/api-docs/ai/gpt/) for supported portfolio and account questions through a conversational interface.

### Related API reference

[Positions

Read open positions

View API →](https://fyers.in/api-docs/v3/api/trading/positions/get-positions/)[Holdings

Read account holdings

View API →](https://fyers.in/api-docs/v3/api/account/holdings/)[Funds

Check available funds

View API →](https://fyers.in/api-docs/v3/api/account/funds/)[Margin Calculator

Calculate required margin

View API →](https://fyers.in/api-docs/v3/api/calculators/multi-order-margin-calculator/)[Exit Positions

Close open positions

View API →](https://fyers.in/api-docs/v3/api/trading/positions/exit-position/)[Convert Position

Convert product type

View API →](https://fyers.in/api-docs/v3/api/trading/positions/convert-position/)

### Continue with AI

✨

Continue with AI

Want help managing positions, funds and risk?

VIDEO LEARNING

### Video learning

[FYERS API playlist (REST and cURL)](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[FYERS API playlist (Node.js)](https://www.youtube.com/playlist?list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)

## Place basket and multi-leg orders safely

*Source: https://fyers.in/api-docs/v3/getting-started/guides/place-basket-and-multi-leg-orders/ (last updated 2026-10-14)*

Basket and multi-leg workflows involve several related orders. The Guide focuses on preparation, validation, execution sequence and post-order verification.

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Step-by-step workflow

1. 1

   Define the complete set of legs

   List every leg with its instrument, side, quantity, order type and role in the overall trade.
2. 2

   Validate instrument, side, quantity and order details

   Validate each symbol and confirm that all quantities and sides match the intended strategy before submitting any order.
3. 3

   Choose basket or multi-leg execution

   Use the supported basket or multi-leg workflow that matches the required execution behaviour. Review any differences in validation and response handling.
4. 4

   Submit the request

   Submit the complete request once and retain the response for every leg.
5. 5

   Check each leg result

   Review each leg independently. A successful request does not guarantee that every leg has the same final status.
6. 6

   Handle partial or failed execution

   Define the action for partial fills or failed legs before execution. Recheck live order and position state before placing corrective orders.
7. 7

   Verify the result

   Check the relevant API response and account or market-data state to confirm that the workflow completed successfully. If the result is partial or unsuccessful, review the returned status and message before deciding whether to retry or take another action.

### Common issues

Authentication or permission failure401 Unauthorized

The access token is missing, expired, or the app does not have the required permission. Generate a fresh token and retry the request.

```
HTTP/1.1 401 Unauthorized
{"s":"error","code":-8,"message":"Could not authenticate the user"}
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

Incorrect request inputs400 Bad Request

A required field is missing or invalid (symbol, quantity, side, or product type). Read the response message, correct the payload, then retry.

```
HTTP/1.1 400 Bad Request
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Plan or rate-limit restriction429 Too Many Requests

The request exceeded the plan’s rate limit or an entitlement. Back off before retrying and confirm the Standard vs Prime limits for the API you are calling.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
{"s":"error","message":"Rate limit exceeded"}
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

Temporary network or socket interruptionTimeout

The connection dropped before a response arrived. Check the latest order, position, or socket state before sending the same request again.

```
Error: socket hang up
ECONNRESET
```

[View WebSocket Overview →](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)

> **Prefer a guided AI workflow?**
> Prefer to automate without maintaining code? Explore FYERS Automate for supported no-code strategy workflows.

### Related API reference

[Multi Order

Submit multiple orders together

View API →](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-order/)[Multi-leg Orders

Submit multi-leg orders

View API →](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/multi-leg-order/)[Order Book and Order Details

Verify order status

View API →](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/)[Positions

Read open positions

View API →](https://fyers.in/api-docs/v3/api/trading/positions/get-positions/)

### Continue with AI

✨

Continue with AI

Want help with basket and multi-leg orders?

VIDEO LEARNING

### Video learning

[FYERS API playlist (REST and cURL)](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[FYERS API playlist (Node.js)](https://www.youtube.com/playlist?list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)

## Use Symbol Master to find instruments

*Source: https://fyers.in/api-docs/v3/getting-started/guides/use-symbol-master/ (last updated 2026-10-14)*

Instrument lookup is a prerequisite for reliable market-data and order workflows. Use the Symbol Master files and symbology guidance in the FYERS API Appendix to select the exact identifier required by the API.

> Official reference: [FYERS API Appendix](https://fyers.in/api-docs/v3/api/appendix/)

### Before you begin

* Create a FYERS API app
* Complete authentication
* Confirm permissions and plan access
* Have connectivity to the API
* Select a supported programming language

[Need authentication? View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

### Step-by-step workflow

1. 1

   Choose the relevant exchange and segment

   Select the exchange and market segment that contains the required instrument.
2. 2

   Download the latest Symbol Master file

   Open the FYERS API Appendix and download the latest Symbol Master file for the required exchange or segment. Use the Appendix as the source of truth for available files and the documented symbology format.
3. 3

   Filter by instrument, expiry, strike or symbol

   Filter the file using the fields relevant to the instrument type, such as trading symbol, expiry, strike, option type or instrument category.
4. 4

   Select the required identifier

   Use the exact identifier required by the target API. Do not construct identifiers from assumptions when Symbol Master provides the official value.
5. 5

   Validate the identifier with a read operation

   Use a quote or other supported read operation to confirm that the selected identifier resolves correctly.
6. 6

   Use it in data or order workflows

   Pass the validated identifier into the required market-data or trading workflow and retain the instrument metadata for display and checks.
7. 7

   Verify the result

   Check the relevant API response and account or market-data state to confirm that the workflow completed successfully. If the result is partial or unsuccessful, review the returned status and message before deciding whether to retry or take another action.

### Common issues

Authentication or permission failure401 Unauthorized

The access token is missing, expired, or the app does not have the required permission. Generate a fresh token and retry the request.

```
HTTP/1.1 401 Unauthorized
{"s":"error","code":-8,"message":"Could not authenticate the user"}
```

[View Authentication →](https://fyers.in/api-docs/v3/api/authentication/)

Incorrect request inputs400 Bad Request

A required field is missing or invalid (symbol, quantity, side, or product type). Read the response message, correct the payload, then retry.

```
HTTP/1.1 400 Bad Request
{"s":"error","code":-50,"message":"Please provide valid order parameters"}
```

[View Error Code Reference →](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/)

Plan or rate-limit restriction429 Too Many Requests

The request exceeded the plan’s rate limit or an entitlement. Back off before retrying and confirm the Standard vs Prime limits for the API you are calling.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
{"s":"error","message":"Rate limit exceeded"}
```

[Learn exponential backoff →](https://fyers.in/api-docs/v3/getting-started/guides/handle-errors-rate-limits/)

Temporary network or socket interruptionTimeout

The connection dropped before a response arrived. Check the latest order, position, or socket state before sending the same request again.

```
Error: socket hang up
ECONNRESET
```

[View WebSocket Overview →](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)

### Related API reference

[Appendix - Symbol Master

Download instrument data

View API →](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-file/)[Quotes

Validate instrument identifiers

View API →](https://fyers.in/api-docs/v3/api/market-data/quotes/)[Historical Candles

Fetch historical prices

View API →](https://fyers.in/api-docs/v3/api/market-data/historical-data/)[Single Order

Submit a new order

View API →](https://fyers.in/api-docs/v3/api/trading/order-placement/sync/single-order/)

### Continue with AI

✨

Continue with AI

Want help working with Symbol Master?

VIDEO LEARNING

### Video learning

[FYERS API playlist (REST and cURL)](https://www.youtube.com/playlist?list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[FYERS API playlist (Python)](https://www.youtube.com/playlist?list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)

## Trade Book

*Source: https://fyers.in/api-docs/v3/api/trading/trade-book/ (last updated 2026-10-14)*

Get the trades executed during the day, or filter them by order tag.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Get Trades](https://fyers.in/api-docs/v3/api/trading/trade-book/get-trades/) | GET | This API allows you to fetch all the trades executed in your account today. |
| [Get Trades by Order Tag](https://fyers.in/api-docs/v3/api/trading/trade-book/get-trades-by-order-tag/) | GET | This API allows you to fetch the trades executed for orders placed with a specific order tag. |

## Historical Data

*Source: https://fyers.in/api-docs/v3/api/market-data/historical-data/ (last updated 2026-10-14)*

This API allows you to get historical candle data for a symbol over a date range and resolution.

USE CASE

Fetch past candles to draw a chart, calculate indicators or backtest a strategy.

Details

The historical API provides archived data (up to date) for symbols across various exchanges within the given range. A historical record is presented in the form of a candle, and the data is available in different resolutions like 1 min, 10 min, 60 min ... 240 min, and daily.

**To Handle Partial Candles**

To receive completed candle data, send a timestamp prior to the current minute. Sending a timestamp for the current minute returns partial data because the minute is not yet finished. Always use a `range_to` timestamp of the previous minute to receive completed candle data.

Current Time (seconds can be 1-59): `12:10:20 PM`

Input Parameters:

`range_from`: `12:08:00 PM`

`range_to`: `12:09:20 PM` (Current Time - 1 minute)

Output Summary: Returns 2 candles (12:08 PM & 12:09 PM). This example is for 1-minute candles; for other resolutions, subtract the resolution time from `range_to` to get completed candles only.

**Good to know**

* Your app needs the Market Data permission (Historical data, Market Depth and Quotes).
* Set date\_format to 0 to pass range\_from and range\_to as epoch values, or to 1 to pass them as yyyy-mm-dd dates.
* Set cont\_flag to 1 for continuous data of futures and options, and oi\_flag to 1 to include open interest in each candle.
* Each candle is an array: epoch time, open, high, low, close and volume (open interest is added when oi\_flag is 1).

**Limits for History**

* Unlimited number of stocks history data can be downloaded in a day.
* Up to 100 days of data per request for resolutions of 1, 2, 3, 5, 10, 15, 20, 30, 45, 60, 120, 180, and 240 minutes (Data available from July 3, 2017).
* For 1D, 1W, and 1M resolutions, up to 366 days of data per request.
* For Seconds Charts, history is available for 30-Trading Days only.

Plan limits

Standard plan

* Daily candles: last 5 years (from 2021); the window moves forward every year
* Intraday candles: last 1 year (from 2025); the window moves forward every year
* Seconds data: not available

Prime plan

* Daily candles: entire available history, 25+ years
* Intraday candles: entire available history, 5+ years
* Seconds data: last 30 days

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | * Mandatory. * Eg: NSE:SBIN-EQ |
| `resolution`\* | string | * The candle resolution. Possible values are: Day : “D” or “1D” * 5 seconds : “5S” * 10 seconds : “10S” * 15 seconds : “15S” * 30 seconds : “30S” * 45 seconds : “45S” * 1 minute : “1” * 2 minute : “2" * 3 minute : "3" * 5 minute : "5" * 10 minute : "10" * 15 minute : "15" * 20 minute : "20" * 30 minute : "30" * 60 minute : "60" * 120 minute : "120" * 240 minute : "240" * 1 Day : "1D" * 1 week : "1W" * 1 month : "1M" |
| `date_format`\* | int | date\_format is a boolean flag. 0 to enter the epoch value. Eg:670073472. 1 to enter the date format as yyyy-mm-dd. |
| `range_from`\* | string | * Indicating the start date of records. Accepts epoch value if date\_format flag is set to 0. Eg: range\_from: 670073472 * Accepts yyyy-mm-dd format if date\_format flag is set to 1. Eg: 2021-01-01 |
| `range_to`\* | string | * Indicating the end date of records. Accepts epoch value if date\_format flag is set to 0. Eg: range\_to: 1622028732 * Accepts yyyy-mm-dd format if date\_format flag is set to 1. Eg:2021-03-01 |
| `cont_flag` | int | set cont flag 1 for continues data and future options. |
| `oi_flag` | int | set flag to "1" enable oi as a part of candle. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `candles` | array | * Candles data containing array of following data for particular time stamp: * 1.Current epoch time * 2. Open Value * 3.Highest Value * 4.Lowest Value * 5.Close Value * 6.Total traded quantity (volume) |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol":"NSE:SBIN-EQ",
    "resolution":"D",
    "date_format":"0",
    "range_from":"1690895316",
    "range_to":"1691068173",
    "cont_flag":"1"
}

response = fyers.history(data=data)
print(response)
```

```
{
  "candles":[
      [
        1690934400,
        609.85,
        610.5,
        594.1,
        598.45,
        14977497
      ],
      [
        1691020800,
        598.7,
        600.85,
        585,
        590.5,
        27774877
      ]
  ],
  "code":200,
  "message":"",
  "s":"ok"
}
```

VIDEO LEARNING

### Video learning

[Fetch historical stock data (Python)Python · 8:39](https://www.youtube.com/watch?v=O_Q4Y37M9mY&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to get historical data (Node.js)Node.js · 7:25](https://www.youtube.com/watch?v=SQITuHvNSfo&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[How to get historical data? (C#)C# · 6:28](https://www.youtube.com/watch?v=gLXWdnpJEA8&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[How to get historical data? (Java)Java · 5:14](https://www.youtube.com/watch?v=evBQp7OazjY&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Quotes

*Source: https://fyers.in/api-docs/v3/api/market-data/quotes/ (last updated 2026-10-14)*

This API allows you to get the latest quotes for one or more symbols in a single request.

USE CASE

Refresh the latest price, change, volume and best bid/ask for your watchlist in one request.

Note

**Live Streaming** — Stream live quote updates through the Data Socket. View [Data Socket - Symbol Update](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-symbol-update/) documentation.

### Quotes (50 symbols support)

GET`/data/quotes`

Note

**Prime plan:** to get quotes for up to 1,000 symbols in one request, use [Quotes (1000 symbols support)](#new).

Details

* The Quotes API retrieves the full market quotes for one or more symbols provided by the user.
* Your app needs the **Market Data** permission. Quotes, Market Depth and Historical Data are part of that permission template.
* Send each symbol in `EXCHANGE:SYMBOL-SERIES` format, for example `NSE:SBIN-EQ`.
* Each symbol comes back as its own entry with `n` (symbol), `s` (ok or error) and `v` (values). Check `s` for every symbol.
* If you call the URL directly, URL-encode symbols with special characters, for example `M&M` as `M%26M`. The SDKs do this for you.
* Where the Call Auction Session does not apply, `imbalance`, `mkt_imbalance` and `reference_price` return 0, and `indicative_price` returns the last traded price.
* The `cmd` field is deprecated. Do not rely on it.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbols`\* | string | Maximum symbol limit is 50. Eg: NSE:SBIN-EQ. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `ch` | float | Change value |
| `chp` | float | Percentage of change between the current value and the previous day's market close |
| `lp` | float | Last traded price |
| `spread` | float | Difference between lowest asking and highest bidding price |
| `ask` | float | Asking price for the symbol |
| `bid` | float | Bidding price for the symbol |
| `open_price` | float | Price at market opening time |
| `high_price` | float | Highest price for the day |
| `low_price` | float | Lowest price for the day |
| `prev_close_price` | float | Previous closing price |
| `atp` | float | Average traded price |
| `imbalance` | int | Order imbalance quantity (total buy quantity minus total sell quantity) during the Call Auction Session. Returns 0 for symbols where CAS is not applicable |
| `mkt_imbalance` | int | Market order imbalance quantity (market buy quantity minus market sell quantity) during the Call Auction Session. Returns 0 for symbols where CAS is not applicable |
| `reference_price` | float | Reference price of the symbol for the Call Auction Session. Returns 0 for symbols where CAS is not applicable |
| `indicative_price` | float | Indicative equilibrium price discovered during the Call Auction Session. For symbols where CAS is not applicable, it returns the last traded price |
| `volume` | int | Volume traded |
| `short_name` | string | Short name for the symbol Eg: “SBIN-EQ” |
| `exchange` | string | Name of the exchange. Eg: “NSE” or “BSE” |
| `description` | string | Description of the symbol |
| `original_name` | string | Original name of the symbol name provided by the use |
| `symbol` | string | Symbol name provided by the user |
| `fyToken` | string | Unique token for each symbol |
| `tt` | int | Today’s time |
| `cmd` | dict | ---Deprecated--- |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "symbols":"NSE:SBIN-EQ,NSE:IDEA-EQ"
}

response = fyers.quotes(data=data)
print(response)
```

```
{
    "code":200,
    "d":[
        {
          "n":"NSE:SBIN-EQ",
          "s":"ok",
          "v":{
              "ask":0,
              "bid":590.5,
              "ch":-7.95,
              "chp":-1.33,
              "description":"NSE:SBIN-EQ",
              "exchange":"NSE",
              "fyToken":"10100000003045",
              "high_price":600.85,
              "low_price":585,
              "lp":590.5,
              "open_price":598.7,
              "original_name":"NSE:SBIN-EQ",
              "prev_close_price":598.45,
              "atp": 428.07,
              "imbalance": -2969,
              "mkt_imbalance": 32522,
              "reference_price": 427.25,
              "indicative_price": 426.9,
              "short_name":"SBIN-EQ",
              "spread":-590.5,
              "symbol":"NSE:SBIN-EQ",
              "tt":"1691020800",
              "volume":27774877
          }
        },
        {
          "n":"NSE:IDEA-EQ",
          "s":"ok",
          "v":{
              "ask":7.85,
              "bid":0,
              "ch":-0.05,
              "chp":-0.63,
              "description":"NSE:IDEA-EQ",
              "exchange":"NSE",
              "fyToken":"101000000014366",
              "high_price":8.05,
              "low_price":7.8,
              "lp":7.85,
              "open_price":7.9,
              "original_name":"NSE:IDEA-EQ",
              "prev_close_price":7.9,
              "atp": 7.5,
              "imbalance": -1250400,
              "mkt_imbalance": 0,
              "reference_price": 7.9,
              "indicative_price": 7.85,
              "short_name":"IDEA-EQ",
              "spread":7.85,
              "symbol":"NSE:IDEA-EQ",
              "tt":"1691020800",
              "volume":78116800
          }
        }
    ],
    "message":"",
    "s":"ok"
  }
```

### Quotes (1000 symbols support)

POST`/data/quotes`

Details

* The Quotes (POST) API retrieves full market quotes for a list of symbols sent in the request body. Use it when you need quotes for more symbols in one request than the [Quotes](https://fyers.in/api-docs/v3/api/market-data/quotes/#quotes-50-symbols-support) GET API allows.
* **Symbol limit per request**

Plan limits

Standard plan

* Up to 50 symbols per request

Prime plan

* Up to 1,000 symbols per request

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

| **Plan** | **Maximum symbols** |
| --- | --- |
| Prime | 1000 |
| Standard | 50 |

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbols`\* | array of strings | List of symbols. Up to 1000 symbols for Prime users and 50 for Standard users. Eg: ["NSE:SBIN-EQ", "NSE:TCS-EQ"] |

### Response Attributes

The response has the same structure and attributes as the [Quotes](https://fyers.in/api-docs/v3/api/market-data/quotes/#quotes-50-symbols-support) GET API.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "symbols": ["NSE:SBIN-EQ", "NSE:IDEA-EQ"]
}

response = fyers.quotes_v2(data=data)
print(response)
```

```
{
 "s": "ok",
 "code": 200,
 "d": [
     {
         "n": "NSE:SBIN-EQ",
         "s": "ok",
         "v": {
             "ch": 1.7,
             "chp": 0.4,
             "lp": 426.9,
             "spread": 0.05,
             "ask": 426.9,
             "bid": 426.85,
             "open_price": 430.5,
             "high_price": 433.65,
             "low_price": 423.6,
             "prev_close_price": 425.2,
             "atp": 428.07,
             "imbalance": -2969,
             "mkt_imbalance": 32522,
             "reference_price": 427.25,
             "indicative_price": 426.9,
             "volume": 38977242,
             "short_name": "SBIN-EQ",
             "exchange": "NSE",
             "description": "NSE:SBIN-EQ",
             "original_name": "NSE:SBIN-EQ",
             "symbol": "NSE:SBIN-EQ",
             "fyToken": "10100000003045",
             "tt": "1622160000"
         }
     }
 ],
 "message": ""
 }
```

VIDEO LEARNING

### Video learning

[Live market data simplified (REST and cURL)REST and cURL · 10:49](https://www.youtube.com/watch?v=dSSdpzQYnu8&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Get live market data (Python)Python · 18:54](https://www.youtube.com/watch?v=BDShdShvBK8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to fetch live market data (Node.js)Node.js · 7:28](https://www.youtube.com/watch?v=vab00pxOnpU&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[How to fetch live market data (C#)C# · 6:03](https://www.youtube.com/watch?v=h-cEAkmFC9I&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[How to fetch live market data (Java)Java · 8:45](https://www.youtube.com/watch?v=mSqX57KimJg&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Market Depth

*Source: https://fyers.in/api-docs/v3/api/market-data/market-depth/ (last updated 2026-10-14)*

This API allows you to get the market depth (bid and ask levels) for a symbol.

USE CASE

Check how much liquidity sits at each bid and ask level before you size an order.

Note

**Live Streaming** — Stream live market-depth updates through the Data Socket. View [Data Socket - Depth Update](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-depth-update/) documentation.

Details

* The Market Depth API returns the complete market data of the symbol provided. It will include the quantity, OHLC values, and Open Interest fields, and bid/ask prices.
* Your app needs the **Market Data** permission. Market Depth is part of that permission template.
* Request one symbol at a time (the maximum is 1), for example `NSE:SBIN-EQ`. Make a separate request for each additional symbol.
* Set `ohlcv_flag` to 1 to get open, high, low, close and volume in the response.
* `bids` and `ask` are arrays with price, volume and number of orders for each level. `totalbuyqty` and `totalsellqty` give the totals.
* `oiflag` is a true or false flag for open-interest data. The OI fields are `oi`, `pdoi` (previous day) and `oipercent`.
* `lower_ckt` and `upper_ckt` give the circuit limits. `ltp`, `ltq` and `ltt` give the last traded price, quantity and time.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Maximum symbol limit is 1. Eg: NSE:SBIN-EQ |
| `ohlcv_flag`\* | int | Set the ohlcv\_flag to 1 to get open, high, low, closing and volume quantity' |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `totalbuyqty` | int | Total buying quantity |
| `totalsellqty` | int | Total selling quantity |
| `bids` | array | Bidding price along with volume and total number of orders |
| `ask` | array | Offer price with volume and total number of orders |
| `o` | float | Price at market opening time |
| `h` | float | Highest price for the day |
| `i` | float | Lowest price for the day |
| `c` | float | Price at the of market closing |
| `chp` | float | Percentage of change between the current value and the previous day's market close |
| `tick_Size` | float | Minimum price multiplier |
| `ch` | float | Change value |
| `ltq` | int | Last traded quantity |
| `ltt` | int | Last traded time |
| `ltp` | float | Last traded price |
| `v` | int | Volume traded |
| `atp` | float | Average traded price |
| `lower_ckt` | float | Lower circuit price |
| `upper_ckt` | float | upper circuit price |
| `expiry` | string | Expiry date |
| `oi` | float | Open interest |
| `oiflag` | boolean | Boolean flag for OI data, true or false |
| `pdoi` | int | previous day open interest |
| `oipercent` | float | Change in open Interest percentage |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
    "symbol":"NSE:SBIN-EQ",
    "ohlcv_flag":"1"
}

response = fyers.depth(data=data)
print(response)
```

```
{
 "s": "ok",
 "d": {
     "NSE:SBIN-EQ": {
         "totalbuyqty": 2396063,
         "totalsellqty": 4990001,
         "bids": [
             {
                 "price": 427.25,
                 "volume": 4738,
                 "ord": 5
             },
             {
                 "price": 427.2,
                 "volume": 2631,
                 "ord": 9
             },
             {
                 "price": 427.15,
                 "volume": 6366,
                 "ord": 19
             },
             {
                 "price": 427.1,
                 "volume": 6344,
                 "ord": 18
             },
             {
                 "price": 427.05,
                 "volume": 8136,
                 "ord": 16
             }
         ],
         "ask": [
             {
                 "price": 427.4,
                 "volume": 2193,
                 "ord": 4
             },
             {
                 "price": 427.45,
                 "volume": 5406,
                 "ord": 19
             },
             {
                 "price": 427.5,
                 "volume": 15311,
                 "ord": 57
             },
             {
                 "price": 427.55,
                 "volume": 11170,
                 "ord": 17
             },
             {
                 "price": 427.6,
                 "volume": 7272,
                 "ord": 25
             }
         ],
         "o": 430.5,
         "h": 433.65,
         "l": 423.6,
         "c": 425.2,
         "chp": 0.48,
         "tick_Size": 0.05,
         "ch": 2.05,
         "ltq": 20,
         "ltt": 1622184920,
         "ltp": 427.25,
         "v": 39163870,
         "atp": 428.07,
         "lower_ckt": 382.7,
         "upper_ckt": 467.7,
         "expiry": "",
         "oi": 0,
         "oiflag": false,
         "pdoi": 0,
         "oipercent": 0.0
     }
 },
  "message": ""
  }
```

VIDEO LEARNING

### Video learning

[Live market data simplified (REST and cURL)REST and cURL · 10:49](https://www.youtube.com/watch?v=dSSdpzQYnu8&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Get live market data (Python)Python · 18:54](https://www.youtube.com/watch?v=BDShdShvBK8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to fetch live market data (Node.js)Node.js · 7:28](https://www.youtube.com/watch?v=vab00pxOnpU&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[How to fetch live market data (C#)C# · 6:03](https://www.youtube.com/watch?v=h-cEAkmFC9I&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[How to fetch live market data (Java)Java · 8:45](https://www.youtube.com/watch?v=mSqX57KimJg&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Option Chain

*Source: https://fyers.in/api-docs/v3/api/market-data/option-chain/ (last updated 2026-10-14)*

This API allows you to get the option chain of an underlying, with Call and Put strikes, India VIX and available expiries.

USE CASE

Fetch the strikes around the current price to build an option-chain screen or pick a strike to trade.

Note

`strikecount` is the number of strikes on each side of ATM (maximum 50). For example, a strike count of 2 returns ATM plus 2 ITM and 2 OTM strikes for both CE and PE.

Details

* The Optionchain API provides important information about options trading, specifically focusing on strike prices, which are predetermined prices at which an option contract can be exercised. This API offers data for both Call (CE) and Put (PE) options, along with values for index, IndiaVIX (Volatility Index) and available expiry dates.
  When using the API, you can specify the number of strike prices you're interested in. For example, if you request a strike count of 2, the API will return data for:
* **At-The-Money (ATM) strike:** The closest strike price to the current market price.
* **Out-of-The-Money (OTM) strikes:** Strike prices higher than the current market price for Calls (CE) and lower than the current market price for Puts (PE). The API will return data for 2 CE and 2 PE OTM strikes.
* **In-The-Money (ITM) strikes:** Strike prices lower than the current market price for Calls (CE) and higher than the current market price for Puts (PE). The API will return data for 2 CE and 2 PE ITM strikes.
* Set `greeks` to 1 to receive `delta`, `gamma`, `theta`, `vega` and `iv`. Each strike then carries them in a nested `greeks` object.
* The first `optionsChain` entry is the underlying itself (`strike_price` -1, empty `option_type`), with its future price in `fp`, `fpch` and `fpchp`.
* `expiryData` lists the available expiries with `date` (DD-MM-YYYY), epoch `expiry` and `expiry_flag`. India VIX is returned in `indiavixData`.
* `callOi` and `putOi` give total open interest for each side. For each strike, `oi`, `oich`, `oichp` and `prev_oi` show open interest and its change.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | * Mandatory. * Eg: NSE:SBIN-EQ |
| `strikecount` | int | Options strike count for symbol(MAX = 50) |
| `timestamp` | string | Options chain data at timestamp |
| `greeks` | string | Set greeks to 1 for greeks data which includes delta, gamma, theta, vega and iv. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `callOi` | int | Total open interest for call options |
| `putOi` | int | Total open interest for put options |
| `date` | string | Expiry date in DD-MM-YYYY |
| `expiry` | string | Expiry timestamp |
| `ask` | float | Ask price |
| `bid` | float | Bid price |
| `description` | string | Description of the stock |
| `ex_symbol` | string | Exchange Symbol |
| `exchange` | int | * The exchange in which order is placed. * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `fytoken` | string | * Fytoken is a unique identifier for every symbol. * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `delta` | float | Sensitivity of option price to a 1-unit change in underlying price |
| `gamma` | float | Rate of change of delta with respect to underlying price |
| `theta` | float | Time decay: change in option price per day as expiry approaches |
| `vega` | float | Sensitivity of option price to a 1% change in implied volatility |
| `iv` | float | Implied volatility: expected future volatility derived from option price |
| `ltp` | float | LTP is the price from which the next sale of the stocks happens |
| `ltpch` | float | Change in last traded price |
| `ltpchp` | float | Percentage change in last traded price |
| `option_type` | string | Type of option (if applicable) |
| `strike_price` | int | Strike price (if applicable) |
| `symbol` | string | Symbol |
| `fp` | float | Future price |
| `fpch` | float | Change in future price |
| `fpchp` | float | Percentage change in future price |
| `oi` | int | Open interest |
| `oich` | int | Change in Open interest |
| `oichp` | float | Percentage change in Open interest |
| `prev_oi` | int | Previous Open interest |
| `volume` | int | Volume traded |

Request

```
from fyers_apiv3 import fyersModel
client_id = "YYYYYYY-100"
access_token = "XXXXXXXXXXXXX"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")
data = {
    "symbol":"NSE:TCS-EQ",
    "strikecount":1,
    "timestamp": "",
    "greeks":"1"
}
response = fyers.optionchain(data=data);
print(response)
```

```
{
  "code": 200,
  "data": {
    "callOi": 10038175,
    "expiryData": [
      {
        "date": "25-04-2024",
        "expiry": "1714039200"
      },
      {
        "date": "30-05-2024",
        "expiry": "1717063200"
      },
      {
        "date": "27-06-2024",
        "expiry": "1719482400"
      }
    ],
    "indiavixData": {
      "ask": 0,
      "bid": 0,
      "description": "INDIAVIX-INDEX",
      "ex_symbol": "INDIAVIX",
      "exchange": "NSE",
      "fyToken": "101000000026017",
      "ltp": 10.55,
      "ltpch": -2.15,
      "ltpchp": -16.93,
      "option_type": "",
      "strike_price": -1,
      "symbol": "NSE:INDIAVIX-INDEX"
    },
    "optionsChain": [
      {
        "ask": 3880.15,
        "bid": 3880.05,
        "description": "TATA CONSULTANCY SERV LT",
        "ex_symbol": "TCS",
        "exchange": "NSE",
        "fp": 3876.65,
        "fpch": 14.2,
        "fpchp": 0.37,
        "fyToken": "101000000011536",
        "ltp": 3880.15,
        "ltpch": 15.55,
        "ltpchp": 0.4,
        "option_type": "",
        "strike_price": -1,
        "symbol": "NSE:TCS-EQ"
      },
      {
        "ask": 34.9,
        "bid": 34.35,
        "fyToken": "1011240425139431",
        "ltp": 34.8,
        "ltpch": 2.7,
        "ltpchp": 8.41,
        "oi": 99575,
        "oich": -3325,
        "oichp": -3.23,
        "option_type": "CE",
        "prev_oi": 102900,
        "strike_price": 3860,
        "symbol": "NSE:TCS24APR3860CE",
        "volume": 202650,
        "greeks": {
            "delta": 0.49,
            "gamma": 0.0007,
            "theta": -28.39,
            "vega": 9.6,
            "iv": 23.42
        }
      },
      {
        "ask": 19.3,
        "bid": 19,
        "fyToken": "1011240425139432",
        "ltp": 19.05,
        "ltpch": -12.4,
        "ltpchp": -39.43,
        "oi": 159075,
        "oich": 28525,
        "oichp": 21.85,
        "option_type": "PE",
        "prev_oi": 130550,
        "strike_price": 3860,
        "symbol": "NSE:TCS24APR3860PE",
        "volume": 304150,
        "greeks": {
            "delta": 0.49,
            "gamma": 0.0007,
            "theta": -28.39,
            "vega": 9.6,
            "iv": 23.42
        }
      },
      {
        "ask": 24.85,
        "bid": 24.55,
        "fyToken": "1011240425133432",
        "ltp": 24.95,
        "ltpch": -0.55,
        "ltpchp": -2.16,
        "oi": 165900,
        "oich": 9975,
        "oichp": 6.4,
        "option_type": "CE",
        "prev_oi": 155925,
        "strike_price": 3880,
        "symbol": "NSE:TCS24APR3880CE",
        "volume": 543025,
        "greeks": {
            "delta": 0.49,
            "gamma": 0.0007,
            "theta": -28.39,
            "vega": 9.6,
            "iv": 23.42
        }
      },
      {
        "ask": 29.35,
        "bid": 28.8,
        "fyToken": "1011240425133433",
        "ltp": 29.2,
        "ltpch": -14.1,
        "ltpchp": -32.56,
        "oi": 98175,
        "oich": 28350,
        "oichp": 40.6,
        "option_type": "PE",
        "prev_oi": 69825,
        "strike_price": 3880,
        "symbol": "NSE:TCS24APR3880PE",
        "volume": 199500,
        "greeks": {
            "delta": 0.49,
            "gamma": 0.0007,
            "theta": -28.39,
            "vega": 9.6,
            "iv": 23.42
        }
      },
      {
        "ask": 17.8,
        "bid": 17.6,
        "fyToken": "1011240425139433",
        "ltp": 17.75,
        "ltpch": -1.4,
        "ltpchp": -7.31,
        "oi": 631050,
        "oich": 23275,
        "oichp": 3.83,
        "option_type": "CE",
        "prev_oi": 607775,
        "strike_price": 3900,
        "symbol": "NSE:TCS24APR3900CE",
        "volume": 981925,
        "greeks": {
            "delta": 0.49,
            "gamma": 0.0007,
            "theta": -28.39,
            "vega": 9.6,
            "iv": 23.42
        }
      },
      {
        "ask": 42.45,
        "bid": 41.85,
        "fyToken": "1011240425139434",
        "ltp": 41.75,
        "ltpch": -14.65,
        "ltpchp": -25.98,
        "oi": 338100,
        "oich": -9975,
        "oichp": -2.87,
        "option_type": "PE",
        "prev_oi": 348075,
        "strike_price": 3900,
        "symbol": "NSE:TCS24APR3900PE",
        "volume": 129325,
        "greeks": {
            "delta": 0.49,
            "gamma": 0.0007,
            "theta": -28.39,
            "vega": 9.6,
            "iv": 23.42
        }
      }
    ],
    "putOi": 3875200
  },
  "message": "",
  "s": "ok"
}
```

## Futures Chain

*Source: https://fyers.in/api-docs/v3/api/market-data/futures-chain/ (last updated 2026-10-14)*

This API allows you to get the currently available futures contracts for an underlying symbol.

USE CASE

Find the futures contracts trading now for an underlying and compare their prices.

Details

* The Futures Chain API gives the list of currently available futures contracts for an underlying symbol, along with the last traded price and the change for each contract.
* The response contains the underlying symbol followed by its available futures contracts. The underlying entry is returned with an empty `expiry`.
* Pass the underlying symbol, for example `NSE:NIFTY50-INDEX`, `NSE:SBIN-EQ`, `BSE:SENSEX-INDEX` or `MCX:CRUDEOIL26SEPFUT`.
* Each entry in `data` returns `symbol`, `fyToken`, `lp`, `ch`, `chp`, `expiry` (epoch value) and `volume`.
* A missing or invalid `symbol` returns an error. Check symbols against [Symbol Master](https://fyers.in/api-docs/v3/getting-started/guides/use-symbol-master/) first.
* Only currently available contracts are listed. For expired contracts, start with [Get Expiry Dates](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expiry-dates/).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Underlying symbol for which the futures chain is required. Eg: NSE:NIFTY50-INDEX, NSE:SBIN-EQ, BSE:SENSEX-INDEX, MCX:CRUDEOIL26SEPFUT |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | Response code |
| `message` | string | Message returned with the response |
| `data` | array | List of the underlying symbol and its available futures contracts |
| `data[].symbol` | string | Symbol name of the underlying or the futures contract |
| `data[].fyToken` | string | Fyers token for the symbol |
| `data[].lp` | float | Last traded price |
| `data[].ch` | float | Change value |
| `data[].chp` | float | Percentage of change between the current value and the previous day's market close |
| `data[].expiry` | string | Expiry of the futures contract as an epoch value. Empty for the underlying symbol. |
| `data[].volume` | int | Volume traded |

**Note**: The API returns an error if an invalid symbol is provided, or if the symbol parameter is missing.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol": "NSE:NIFTY50-INDEX"
}

response = fyers.futures_chain(data)
print(response)
for contract in response["data"]:
    print(contract["symbol"], contract["lp"], contract["expiry"])
```

```
{
    "code": 200,
    "data": [
        {
            "ch": 24.25,
            "chp": 0.1,
            "expiry": "",
            "fyToken": "101000000026000",
            "lp": 23897.7,
            "symbol": "NSE:NIFTY50-INDEX",
            "volume": 0
        },
        {
            "ch": 47.9,
            "chp": 0.2,
            "expiry": "1790676600",
            "fyToken": "101126092968407",
            "lp": 24048,
            "symbol": "NSE:NIFTY26SEPFUT",
            "volume": 1836380
        },
        {
            "ch": 46.4,
            "chp": 0.19,
            "expiry": "1793095800",
            "fyToken": "101126102748704",
            "lp": 24150,
            "symbol": "NSE:NIFTY26OCTFUT",
            "volume": 154440
        }
    ],
    "message": "",
    "s": "ok"
}
```

## Expired F&O Data

*Source: https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/ (last updated 2026-10-14)*

The Expired F&O Contracts Data APIs help you find expired Futures and Options contracts and get their historical data. Use them to research or backtest strategies on contracts that no longer trade: find the expiry, find the contract, then fetch its candles.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Get Expiry Dates](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expiry-dates/) | GET | This API allows you to get the futures and options expiry dates for an underlying symbol within a date range. |
| [Get Expired Contracts](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-contracts/) | GET | This API allows you to get the expired futures and options contract symbols for an underlying symbol and expiry date. |
| [Get Expired F&O Data](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-fo-data/) | GET | This API allows you to get historical candles for an expired futures or options contract. |

### How the APIs work together

1. Use [Get Expiry Dates](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expiry-dates/) to find an available expiry date for an underlying symbol.
2. Use [Get Expired Contracts](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-contracts/) to find the contract symbol for the selected expiry.
3. Use [Get Expired F&O Data](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-fo-data/) to get historical data for the selected contract.

## Screeners

*Source: https://fyers.in/api-docs/v3/api/market-data/screeners/ (last updated 2026-10-14)*

Screeners run ready-made filters on a set of symbols and return the ones that meet the filter’s conditions.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Configuration](https://fyers.in/api-docs/v3/api/market-data/screeners/config/) | GET | Lists every screener and the exact values each one accepts. Call it first. |
| [Standard screeners](https://fyers.in/api-docs/v3/api/market-data/screeners/standard-screeners/) | GET | Runs one of 111 screeners that you can customise: fields, universe, timeframe and sort. |
| [Candlestick screeners](https://fyers.in/api-docs/v3/api/market-data/screeners/candlestick-screeners/) | GET | Runs one of 23 fixed candlestick-pattern screeners. |
| [Technical screeners](https://fyers.in/api-docs/v3/api/market-data/screeners/technical-screeners/) | GET | Runs one of 6 fixed MACD, moving-average and MFI screeners. |

**The order to follow**

1. Call Configuration and pick a screener.
2. Read that screener’s entry to see what it accepts.
3. Call the Standard, Candlestick or Technical API with the screener’s id.

### Before you start

* You need your App ID and an access token (see the Authentication page of these docs). On every call, send them in the Authorization header as `APP_ID:ACCESS_TOKEN`.
* Every Screeners API is a GET call. Parameters go in the URL query string, for example `?screener_id=top_gainers&fields=t0_close_ltp`.
* Terms used on these pages: a **screener** is a ready-made filter; a **universe** is the set of symbols it scans (for example Nifty 50); a **timeframe** is the period over which a change is measured; a **field** is one column of the result.

### Your first call, in three steps

1. Call Configuration and note a screener id from `screeners_standard`, for example `top_gainers`.
2. Call Standard screeners with `screener_id=top_gainers&fields=t0_close_ltp`.
3. Read the result: `header` names the columns (`symbolticker`, then `t0_close_ltp`) and each array in `body` is one stock, in that order.

## Blacklisting

*Source: https://fyers.in/api-docs/v3/api/trading/webhooks/blacklisting/ (last updated 2026-10-14)*

USE CASE

Find out why your webhook stopped receiving updates.

If you missed any, use [Get Orders](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/) to catch up on the day's orders.

### Things to know

* A URL is blacklisted if your server does not answer with HTTP status 200, or if the post to your postback URL fails.
* A blacklisted URL stays blocked for 30 minutes. No webhooks are sent to it during that time.
* A URL is also blacklisted after continuous failures, typically after three retries.

The webhook/postback URL provided by the user can be blacklisted if the response status is not 200 from your web server or if the post request to your PostbackURL fails. These URLs are blacklisted for 30 minutes, and during that time, no webhooks are sent to the blacklisted URL. Additionally, the URL will be blacklisted after continuous failures, typically after three retries.

## Order History

*Source: https://fyers.in/api-docs/v3/api/reports/order-history/ (last updated 2026-10-14)*

This API allows you to fetch your past orders for a date range, defaulting to the current financial year.

USE CASE

Look up past orders by symbol, segment, exchange or status, such as every rejected order in a quarter.

Details

* Fetches all historical orders within the specified date range. If no range is specified, the system automatically defaults to the current financial year.
* Send `from_date` and `to_date` as `YYYY-MM-DD`. Without them the report runs from the start of the current financial year to today.
* Results are paged: `page_size` defaults to 100 and `page_no` to 1. Increase `page_no` to read further pages.
* `status` filters only on Executed (1), Cancelled (2) or Rejected (3), with 0 for all. There is no filter for pending orders, so use [Get Orders](https://fyers.in/api-docs/v3/api/trading/order-book/get-orders/) for open orders.
* In this report `segment_type` is 0 all, 1 equity, 2 equity derivatives, 3 currency derivatives and 4 commodity derivatives. It has no mutual fund option, unlike the other reports.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For each order

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `page_size` | string | The number of records to be fetched in one page (default is 100) |
| `page_no` | string | The page number to fetch (default is 1) |
| `from_date` | string | The start date for fetching orders in “YYYY-MM-DD” format (default is the start of the current financial year) |
| `to_date` | string | The end date for fetching orders in “YYYY-MM-DD” format (default is the current date) |
| `segment_type` | string | * 0 → Includes all Segments [default] * 1 → Includes only Equity * 2 → Includes only Equity Derivatives * 3 → Includes Currency Derivatives * 4 → Includes only Commodity Derivatives |
| `exchange_type` | string | * 0 → Includes all Exchanges [default] * 1 → Includes only NSE * 2 → Includes only BSE * 3 → Includes only MCX |
| `status` | string | * 0 → All Status [default] * 1 → Executed * 2 → Cancelled * 3 → Rejected |

### Response Attributes - For each order

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `clientId` | string | The client id of the fyers user |
| `id_fyers` | string | Fyers system-generated unique identifier for the order |
| `exchOrdId` | string | The order number provided by the exchange |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `segment` | int | * The segment in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `instrument` | int | * Exchange instrument type * [View Details](https://fyers.in/api-docs/v3/api/appendix/instrument-types/) |
| `description` | string | The description of the symbol |
| `trade_date_time` | int | The epoch time when the trade occurred |
| `transaction_type` | string | The type of transaction (BUY/SELL) |
| `trade_date` | string | The time when the trade occurred in “DD-MM-YYYY hh:mm:ss” format in IST |
| `product_type` | string | * The product in which the order was placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `status` | string | The status of the trade (E.g., Executed, Rejected, etc.) |
| `ordertype` | string | The order type (E.g., Market, Limit, etc.) |
| `qty` | int | The quantity of the trade |
| `tradedQty` | int | The total traded qty |
| `traded_price` | float | The traded price |
| `limit_price` | float | The limit price set for the order |
| `ord_source` | string | The source from which the order was placed |
| `rejection_reason` | string | The reason for rejection if the order was rejected |
| `is_symbol_active` | boolean | Indicates if the symbol is currently active for trading |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
      "symbol": "NSE:SBIN-EQ",
  }
response = fyers.orderhistory(data=data)
print(response)
```

```
{
          "s": "ok",
          "data": [
                {
                  "symbol": "NSE:SBIN-EQ",
                  "clientId": "XXXXXX",
                  "id_fyers": "26020100012037",
                  "exchOrdId": "603210324081559",
                  "exchange": 11,
                  "segment": 20,
                  "instrument": 30,
                  "description": "SBI",
                  "trade_date_time": 1769920009000,
                  "trade_date ": "01-02-2026 09:56:49",
                  "transaction_type": "SELL",
                  "product_type": "Overnight",
                  "status": "Executed",
                  "ordertype": "Limit",
                  "qty": 1,
                  "tradedqty": 1,
                  "traded_price": 15013,
                  "limit_price": 15013,
                  "ord_source": "Mobile",
                  "rejection_reason": "",
                  "is_symbol_active": true
                }
          ],
          "message": "Order Book data fetched successfully",
          "code": 200
      }
```

## Trade History

*Source: https://fyers.in/api-docs/v3/api/reports/trade-history/ (last updated 2026-10-14)*

This API allows you to fetch your executed trades for a date range, defaulting to the current financial year.

USE CASE

Pull past trades with trade number, price and quantity to reconcile against your own records.

Details

* Fetches all trades for a specified date range. If no date range is provided, it defaults to the current financial year.
* Send `from_date` and `to_date` as `YYYY-MM-DD`. Without them the report runs from the start of the current financial year to today.
* Results are paged: `page_size` defaults to 100 and `page_no` to 1. Increase `page_no` to read further pages.
* Each row is one trade. `orderNumber` is the order it belongs to, `tradeNumber` and `exchangeOrderNo` come from the exchange, and `side` is 1 for buy and -1 for sell.
* `segment_type` is 0 all, 1 equity, 2 equity derivatives, 3 mutual funds, 4 currency derivatives and 5 commodity derivatives. `exchange_type` is 0 all, 1 NSE, 2 BSE and 3 MCX.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For each order

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `page_size` | string | The number of records to be fetched in one page (default is 100) |
| `page_no` | string | The page number to fetch (default is 1) |
| `from_date` | string | The start date for fetching orders in “YYYY-MM-DD” format (default is the start of the current financial year) |
| `to_date` | string | The end date for fetching orders in “YYYY-MM-DD” format (default is the current date) |
| `segment_type` | string | * 0 → Includes all Segments [default] * 1 → Includes only Equity * 2 → Includes only Equity Derivatives * 3 → Includes Mutal Funds * 4 → Includes only Currency Derivatives * 5 → Includes only Commodity Derivatives |
| `exchange_type` | string | * 0 → Includes all Exchanges [default] * 1 → Includes only NSE * 2 → Includes only BSE * 3 → Includes only MCX |

### Response Attributes - For each trade

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `clientId` | string | The client id of the fyers user |
| `description` | string | The symbol name to display |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `orderDateTime` | int | The epoch time when the trade occurred |
| `orderNumber` | string | The order id for which the trade occurred |
| `tradeNumber` | string | The trade number generated by the exchange |
| `exchangeOrderNo` | string | The order number provided by the exchange |
| `side` | string | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `product_type` | string | * The product in which the order was placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `traded_qty` | int | The quantity of the trade |
| `trade_price` | float | The traded price |
| `segment` | int | * The segment in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `trade_value` | float | The total traded value |
| `is_symbol_active` | boolean | This will show if the symbol is tradable or not |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
      "symbol": "NSE:SBIN-EQ",
  }
response = fyers.tradehistory(data=data)
print(response)
```

```
{
    "s": "ok",
    "data": [
        {
          "symbol": "MCX:GOLDPETAL25JUNFUT",
          "clientId": "XXXXXX",
          "description": "GOLDPETAL25JUNFUT",
          "orderDateTime": "13-Jun-2025 20:05:38",
          "orderNumber": "25061300346219",
          "tradeNumber": "100388805",
          "exchangeOrderNo": "516410327756710",
          "side": 1,
          "exchange": 11,
          "segment": 20,
          "product_type": "Overnight",
          "traded_qty": 1,
          "trade_price": 10007,
          "trade_value": 10007,
          "is_symbol_active": false
        }
    ],
    "message": "Trade Book data fetched successfully"
}
```

## Charges Report

*Source: https://fyers.in/api-docs/v3/api/reports/charges-report/ (last updated 2026-10-14)*

This API allows you to fetch the brokerage and other charges you paid over a date range, defaulting to the current financial year.

USE CASE

Check the brokerage, GST, STT and other charges paid over a period, day by day or summarised by segment.

Details

* Fetches all charges for a specified date range. If no date range is provided, it defaults to the current financial year.
* Set `report_type` to 1 for date-wise rows (default) or 2 for summarised data by segment.
* Send `from_date` and `to_date` as `YYYY-MM-DD`. Without them the report runs from the start of the current financial year to today.
* Results are paged: `page_size` defaults to 100 and `page_no` to 1. The sample response also returns `total_count` and a `summary_data` block with totals such as `ctt_only` and `stt_only`.
* `segment_type` is 0 all, 1 equity, 2 equity derivatives, 3 mutual funds, 4 currency derivatives and 5 commodity derivatives. `exchange_type` is 0 all, 1 NSE, 2 BSE and 3 MCX.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For fetching record

| Attribute | Data Type | Description |
| --- | --- | --- |
| `page_size` | string | Number of records to fetch on single response (default is 100) |
| `page_no` | string | The page number to fetch (default is 1) |
| `from_date` | string | The start date for fetching charges in “YYYY-MM-DD” format (default is the start of the current financial year) |
| `to_date` | string | The end date for fetching charges in “YYYY-MM-DD” format (default is the current date) |
| `segment_type` | string | * 0 → Includes all Segments [default] * 1 → Includes only Equity * 2 → Includes only Equity Derivatives * 3 → Includes Mutal Funds * 4 → Includes only Currency Derivatives * 5 → Includes only Commodity Derivatives |
| `exchange_type` | string | * 0 → Includes all Exchanges [default] * 1 → Includes only NSE * 2 → Includes only BSE * 3 → Includes only MCX |
| `report_type` | string | * 1 → Includes only date wise [default] * 2 → Includes summarised data (segment wise) |

### Response Attributes - For each charge

| Attribute | Data Type | Description |
| --- | --- | --- |
| `brokerage` | float | Brokerage charges for trade execution. |
| `gst` | float | GST levied on profit, brokerage, and transaction charges. |
| `ipft` | float | The IPFT charged for the order. |
| `sebi_toc` | float | Regulatory fee charged by SEBI on turnover. |
| `stamp_duty` | float | The stamp duty charged for the order. |
| `stt` | float | Securities or Commodity Transaction Tax applied on trades. |
| `total` | float | Combined value of all charges and taxes for the day. |
| `trade_date` | int | Date on which the trades were executed. |
| `turnover` | float | Total traded value calculated by the exchange. |
| `transaction_charges` | float | Transaction charges include exchange charges and other charges. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
       "from_date": "2026-04-01",
       "to_date": "2027-03-31",
        "page_size": 1,

  }
response = fyers.charges_history(data=data)
print(response)
```

```
{
    "code": 200,
    "message": "Turnover report data fetched successfully",
    "s": "ok",
    "data": [
      {
        "brokerage": 7.69,
        "transaction_charges": 0.08,
        "gst": 1.4,
        "ipft": 0,
        "sebi_toc": 0,
        "stamp_duty": 0,
        "stt": 0,
        "total": 9.17,
        "trade_date": 1778544000000,
        "turnover": 2575.34,
      }
    ],
    "summary_data": {
      "brokerage": 8.15,
      "ctt_only": 0,
      "gst": 1.49,
      "ipft": 0,
      "sebi_toc": 0,
      "stamp_duty": 0,
      "stt": 0,
      "stt_only": 0,
      "total": 9.770000000000001,
      "turnover": 2915.4400000000005,
      "transaction_charges" : 0.13
    }
  }
```

## Realised P&L Report

*Source: https://fyers.in/api-docs/v3/api/reports/realised-pnl-report/ (last updated 2026-10-14)*

This API allows you to fetch the realised profit and loss on your closed positions for a date range.

USE CASE

Check the profit or loss locked in on closed positions, symbol by symbol, with gross P&L, charges and net P&L.

Details

* Fetches all realised profit & loss for a specified date range. If no date range is provided, it defaults to the current financial year.
* Filter `symbol` by ISIN for equities and mutual funds, for example `INE000A01020`, and by trading symbol for derivatives, for example `BSE:SENSEX2640976500CE`.
* Only positions that are fully closed are counted in `realized_pnl`. For open positions use [Get Positions](https://fyers.in/api-docs/v3/api/trading/positions/get-positions/).
* Send `from_date` and `to_date` as `YYYY-MM-DD`. Results are paged: `page_size` defaults to 100 and `page_no` to 1.
* `segment_type` is 0 all, 1 equity, 2 equity derivatives, 3 mutual funds, 4 currency derivatives and 5 commodity derivatives. `exchange_type` is 0 all, 1 NSE, 2 BSE and 3 MCX.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For each realised profit & loss

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | * For equities and mutual funds, the ISIN is required.Example : INE000A01020 * For derivatives, the trading symbol is required. Example : BSE:SENSEX2640976500CE |
| `page_size` | string | Number of records to fetch on single response (default is 100) |
| `page_no` | string | The page number to fetch (default is 1) |
| `from_date` | string | The start date for fetching realised profit & loss history in “YYYY-MM-DD” format (default is the start of the current financial year) |
| `to_date` | string | The end date for fetching realised profit & loss history in “YYYY-MM-DD” format (default is the current date) |
| `segment_type` | string | * 0 → Includes all Segments [default] * 1 → Includes only Equity * 2 → Includes only Equity Derivatives * 3 → Includes Mutal Funds * 4 → Includes only Currency Derivatives * 5 → Includes only Commodity Derivatives |
| `exchange_type` | string | * 0 → Includes all Exchanges [default] * 1 → Includes only NSE * 2 → Includes only BSE * 3 → Includes only MCX |

### Response data attributes - For each realised profit & loss

| Attribute | Data Type | Description |
| --- | --- | --- |
| `exch_id` | int | The exchange ID |
| `seg_id` | int | The segment ID |
| `segment_name` | string | Market category where the security was traded or invested in. |
| `exchange_name` | string | The name of the exchange |
| `symbol_name` | string | Name of the stock, mutual fund, or F&O contract traded. |
| `realized_pnl` | float | Profit or loss from positions that are fully closed. |
| `buy_qty` | int | Total quantity or units bought. |
| `buy_rate` | float | Price per unit, share, or contract at which it was bought. |
| `sell_qty` | int | Total quantity or units sold. |
| `sell_rate` | float | Price per unit, share, or contract at which it was sold. |
| `is_symbol_active` | boolean | Whether the symbol is active or not |

### Response summary attributes - For the summary of the realised profit & loss

| Attribute | Data Type | Description |
| --- | --- | --- |
| `gross_pnl` | float | The gross profit & loss of the trade |
| `net_pnl` | float | The net profit & loss of the trade |
| `charges` | float | The charges of the trade |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
      "symbol": "INF204KC1402",
      "page_size": 1,
  }
response = fyers.realised_profit_history(data=data)
print(response)
```

```
{
      "code": 200,
      "message": "Global PnL report data fetched successfully",
      "s": "ok",
      "data": [
        {
          "buy_qty": 10,
          "buy_rate": 252.5,
          "exch_id": 10,
          "exchange_name": "NSE",
          "is_symbol_active": true,
          "realized_pnl": 38.5,
          "symbol_name": "NSE:SILVERBEES-EQ",
          "seg_id": 10,
          "segment_name": "NSE_CASH",
          "sell_qty": 10,
          "sell_rate": 256.35
        }
      ],
      "summary_data": {
        "charges": 9.77,
        "gross_pnl": 38.5,
        "net_pnl": 28.73
      }
    }
```

## Tax P&L Report

*Source: https://fyers.in/api-docs/v3/api/reports/tax-pnl-report/ (last updated 2026-10-14)*

This API allows you to fetch your tax profit and loss for a financial year, defaulting to the current one.

USE CASE

Get a financial year's profit and loss grouped for tax filing: trading, short-term, long-term, futures and options.

Details

* Fetches all tax profit & loss for a specified date range. If no date range is provided, it defaults to the current financial year.
* Choose the year with `fin_year`. This report has no `from_date` or `to_date` fields, and without `fin_year` it uses the current financial year.
* Narrow the rows with `transaction_type`: 0 all, 1 TRADING, 2 SHORTTERM, 3 LONGTERM, 4 Future\_Book and 5 Option\_Book.
* The segment filter is called `segment` here: 0 all, 1 equity, 2 equity derivatives, 3 mutual funds, 4 currency derivatives and 5 commodity derivatives. There is no exchange filter.
* Results are paged: `page_size` defaults to 100 and `page_no` to 1. The sample response also returns `total_count`, and its `summary_data` includes `net_ltcg` and `net_stcg`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For fetching tax profit & loss history

| Attribute | Data Type | Description |
| --- | --- | --- |
| `fin_year` | string | The financial year for fetching tax profit & loss history (default is the current financial year) |
| `page_size` | string | The number of records to be fetched in one page (default is 100) |
| `page_no` | string | The page number to fetch (default is 1) |
| `segment` | string | * 0 → Includes all Segments [default] * 1 → Includes only Equity * 2 → Includes only Equity Derivatives * 3 → Includes Mutal Funds * 4 → Includes only Currency Derivatives * 5 → Includes only Commodity Derivatives |
| `transaction_type` | string | * 0 → Includes all Types [default] * 1 → TRADING * 2 → SHORTTERM * 3 → LONGTERM * 4 → Future\_Book * 5 → Option\_Book |

### Response data attributes - For each tax profit & loss

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol_name` | string | Name of the symbol |
| `transaction_type` | string | The type of transaction |
| `segment` | string | Market category where the security was traded or invested in. |
| `buy_date` | string | Date when the stock, contract, or MF units were purchased. |
| `buy_qty` | float | Total quantity or units bought. |
| `buy_rate` | float | Price per unit, share, or contract at which it was bought. |
| `sell_date` | string | Date when the stock, contract, or MF units were sold. |
| `sell_qty` | float | Total quantity or units sold. |
| `sell_rate` | float | Price per unit, share, or contract at which it was sold. |
| `pnl_amount` | float | Profit or loss amount from the specific trade or redemption. |
| `total_days` | int | Number of total calendar days between buy and sell date. |
| `isin` | string | Unique identification number for the stock or mutual fund. |
| `turnover` | float | Trade value considered for tax purposes based on transaction type. |

### Response summary attributes - For the summary of the tax profit & loss

| Attribute | Data Type | Description |
| --- | --- | --- |
| `gross_tax_pnl` | float | The gross tax profit & loss of the trade |
| `net_tax_pnl` | float | The net tax profit & loss of the trade |
| `taxable_intrady` | float | The taxable intraday profit & loss of the trade |
| `taxable_future` | float | The taxable future profit & loss of the trade |
| `taxable_option` | float | The taxable option profit & loss of the trade |
| `realized_pnl` | float | Realised profit or loss from positions that have been fully closed. |
| `turnover_equity` | float | Total turnover from your equity trades. |
| `turnover_fno` | float | Total turnover from your F&O trades. |
| `total_charges` | float | Total charges levied for all transactions in a year. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
      "page_size": 1
  }
response = fyers.tax_pnl_history(data=data)
print(response)
```

```
{
    "code": 200,
    "message": "Tax PnL report data fetched successfully",
    "data": [
      {
        "buy_date": "18 Dec, 2025",
        "buy_qty": 1,
        "buy_rate": 11.4,
        "isin": "INE669E01016",
        "pnl_amount": -1.71,
        "segment": "BSE-Cash",
        "sell_date": "27 Apr, 2026",
        "sell_qty": 1,
        "sell_rate": 9.69,
        "symbol_name": "IDEA      ",
        "total_days": 130,
        "transaction_type": "Short-term",
        "turnover": 0
      }
    ],
    "s": "ok",
    "summary_data": {
      "net_ltcg": 0,
      "net_stcg": 35.68,
      "realized_pnl": 37.01,
      "taxable_future": 0,
      "taxable_intrady": 1.33,
      "taxable_option": 0,
      "total_charges": 9.77,
      "turnover_equity": 3.27,
      "turnover_fno": 0
    }
  }
```

## Ledger Report

*Source: https://fyers.in/api-docs/v3/api/reports/ledger-report/ (last updated 2026-10-14)*

This API allows you to fetch the ledger entries of your account.

USE CASE

Check money movements such as funds added, funds withdrawn and trading entries, with the running balance after each.

Details

* Fetches all ledger for a specified date range. If no date range is provided, it defaults to the current financial year.
* Filter with `transaction_type`: 0 all, 1 BR (funds added), 2 BP (funds withdrawn), 3 SJ (trading), 4 JV (non trading) and 5 MTF.
* The request attributes list no date fields, although the description says the default period is the current financial year.
* Results are paged: `page_size` defaults to 100 and `page_no` to 1. The sample response also returns `total_count` and a `summary_data` block with opening and closing balance.
* `segment_type` is 0 all, 1 equity, 2 equity derivatives, 3 mutual funds, 4 currency derivatives and 5 commodity derivatives. `exchange_type` is 0 all, 1 NSE, 2 BSE and 3 MCX.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For fetching ledger history

| Attribute | Data Type | Description |
| --- | --- | --- |
| `page_size` | string | The number of records to be fetched in one page (default is 100) |
| `page_no` | string | The page number to fetch (default is 1) |
| `segment_type` | string | * 0 → Includes all Segments [default] * 1 → Includes only Equity * 2 → Includes only Equity Derivatives * 3 → Includes Mutal Funds * 4 → Includes only Currency Derivatives * 5 → Includes only Commodity Derivatives |
| `exchange_type` | string | * 0 → Includes all Exchanges [default] * 1 → Includes only NSE * 2 → Includes only BSE * 3 → Includes only MCX |
| `transaction_type` | string | * 0 → Includes all transaction types [default] * 1 → BR(Funds added) * 2 → BP(Funds withdrawn) * 3 → SJ(Trading) * 4 → JV(Non trading) * 5 → MTF(Margin Trading Facility) |

### Response data attributes - For each ledger

| Attribute | Data Type | Description |
| --- | --- | --- |
| `date` | int | Date on which the transaction occurred. |
| `transaction_type` | int | Type of transaction such as fund transfer or charges. |
| `description` | string | Details of the transaction performed on that day. |
| `credit_amount` | string | Amount credited to your account. |
| `debit_amount` | string | Amount debited from your account. |
| `running_balance` | string | Your current account balance. |

### Response summary attributes - For the summary of the ledger

| Attribute | Data Type | Description |
| --- | --- | --- |
| `funds_withdrawn` | float | Total amount withdrawn by you from your trading account. |
| `funds_added` | float | Total amount added by you to your trading account. |
| `opening_balance` | float | Account balance at the beginning of the selected period. |
| `closing_balance` | float | Account balance at the end of the selected period. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"
## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

data = {
      "page_size": 1,
  }
response = fyers.ledger_history(data=data)
print(response)
```

```
{
    "code": 200,
    "message": "Ledger report data fetched successfully",
    "data": [
      {
        "credit_amount": 0,
        "date": 1779840000000,
        "debit_amount": 0.06,
        "description": "Executed trades for the day in equity cash segment",
        "running_balance": 177.61000000000053,
        "transaction_type": "Trading"
      }
    ],
    "s": "ok",
    "summary_data": {
      "closing_balance": 177.61000000000053,
      "funds_added": 650,
      "funds_withdrawn": 2952.9399999999996,
      "opening_balance": 146.74
    }
  }
```

## Technical screeners

*Source: https://fyers.in/api-docs/v3/api/market-data/screeners/technical-screeners/ (last updated 2026-10-14)*

This API returns the Nifty 500 stocks that show a given MACD or moving-average crossover, or an overbought or oversold Money Flow Index (MFI), on end-of-day data.

USE CASE

Find Nifty 500 stocks with a fresh Golden Crossover or an oversold MFI, to build a swing-trading watchlist.

Note

* This API takes only `screener_id`.
* The stocks scanned, the columns returned and the sort are fixed.
* Sending any other parameter returns HTTP 400.

Details

* Send your App ID and access token in the Authorization header as `APP_ID:ACCESS_TOKEN`. Only GET is supported.
* There are 6 Technical screeners: Bullish MACD Crossover (MACD line crosses above the signal line), Bearish MACD Crossover (MACD line crosses below the signal line), Golden Crossover (50-day moving average crosses above the 200-day), Death Crossover (50-day crosses below the 200-day), Overbought by MFI and Oversold by MFI.
* Take the `screener_id` from `screeners_technical` in the Configuration API.
* Every screener scans the Nifty 500 (`iw010`).
* The columns depend on the screener. `symbolticker` is always first, then the columns in the table below.
* Rows are sorted by 1-day change: highest first for Bullish MACD Crossover, Golden Crossover and Oversold by MFI; lowest first for Bearish MACD Crossover, Death Crossover and Overbought by MFI. So Overbought by MFI starts with the stocks that fell the most today, and Oversold by MFI with the stocks that rose the most. The 1-day change itself is not returned.
* The response holds `header` (one object per column: `unique_key`, `description`, `data_type`), `body` (one array per row, values in header order), `total_count` (number of rows returned) and `last_update_time` (Unix epoch seconds). `body` is empty when no stock qualifies.
* How fresh the data is: Technical screeners work on end-of-day data. Until 15:30 IST they return the previous trading day's end-of-day results; these do not change during the session, and `last_update_time` shows 09:15 IST of the current day. At 15:30 IST the results are replaced with the current day's, and `last_update_time` shows 15:30. The exception is `mcap_q`, which follows the live price during the session.

Plan limits

Standard plan

* 50 requests per day

Prime plan

* As per Prime API overall rate limits
* 10 requests per second
* 500 requests per minute
* 5,00,000 requests per day

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `screener_id`\* | string | Mandatory. Screener `id` from the `screeners_technical` array. Only the `screener_id` query parameter is accepted. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `data` | object | Result payload with `header`, `body`, `error`, and `last_update_time` |

### Columns

| Screener | Columns after `symbolticker` |
| --- | --- |
| Bullish MACD Crossover, Bearish MACD Crossover | `today_changes__macd_x_centre` (boolean: MACD crossed the centre line today), `macd` (day MACD), `macdsignal` (day MACD signal line) |
| Golden Crossover, Death Crossover | `sma_50_sma_200_diff` (% distance of the 50-day SMA over the 200-day SMA), `sma_50` (day SMA 50), `sma_200` (day SMA 200), `mcap_q` (market cap, ₹) |
| Overbought by MFI, Oversold by MFI | `mfi` (day MFI), `mcap_q` (market cap, ₹) |

### Screener ids

Take the id from this table or from Configuration.

| Screener | screener\_id |
| --- | --- |
| Bullish MACD Crossover | `macd_crossed_above_signal_line` |
| Bearish MACD Crossover | `macd_crossed_below_signal_line` |
| Golden Crossover | `golden_crossover_end_of_day` |
| Death Crossover | `death_crossover_end_of_day` |
| Overbought by MFI | `mfi_overbought` |
| Oversold by MFI | `mfi_oversold` |

### Example request

`screener_id=mfi_overbought`

### Errors

| HTTP | code | When | message |
| --- | --- | --- | --- |
| 400 | -50 | `screener_id` missing | `screener_id is required` |
| 400 | -50 | `screener_id` unknown, or taken from another Screeners API | `invalid screener_id` |
| 400 | -50 | Any other parameter | `unsupported query parameter: NAME` |
| 401 | -16 | Missing or wrong token | `Could not authenticate the user` |
| 405 | -50 | Method other than GET | `method not allowed; use GET` |
| 429 |  | Rate limit crossed | Wait, then retry |

In the message above, NAME stands for the parameter you sent.

### Notes

* Unlike Standard screeners, the response does not return the applied settings or `fetch_time`.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

data = {
    "screener_id": "mfi_overbought"
}

response = fyers.screeners_technical(data=data)
print(response)
```

```
{
  "code": 200,
  "message": "",
  "s": "ok",
  "data": {
    "body": [
      [
        "NSE:TTML-EQ",
        98.73,
        76691800000
      ],
      [
        "NSE:IGIL-EQ",
        94.62,
        172237200000
      ]
    ],
    "header": [
      {
        "data_type": "string",
        "description": "Symbol",
        "unique_key": "symbolticker"
      },
      {
        "data_type": "double",
        "description": "Day MFI",
        "unique_key": "mfi"
      },
      {
        "data_type": "double",
        "description": "M.Cap (\u20b9)",
        "unique_key": "mcap_q"
      }
    ],
    "last_update_time": 1793159100,
    "total_count": 29
  }
}
```

## Funds

*Source: https://fyers.in/api-docs/v3/api/account/funds/ (last updated 2026-10-14)*

This API allows you to fetch the available balance of your capital and commodity accounts.

USE CASE

Check how much balance is available before placing an order.

Details

* Shows the balance available for the user for capital as well as the commodity market.
* Your app needs the **Transactions Info** permission. Funds is part of that template, along with Orders, Positions, Trades, Holdings and Market Status.
* The request takes no parameters. The response returns a `fund_limit` list with one row per ledger heading.
* Each row has an `id`, a `title`, an `equityAmount` for the capital ledger and a `commodityAmount` for the commodity ledger.
* The sample response lists these titles: Total Balance, Utilized Amount, Clear Balance, Realized Profit and Loss, Collaterals, Fund Transfer, Receivables, Adhoc Limit, Limit at start of the day and Available Balance.
* Look up the row you need, for example Available Balance, by its `title` instead of relying on its position in the list.
* Available Balance = Total Balance - Utilized Amount.
* After you square off all positions, Utilized Amount is not blocked margin any more. It holds the brokerage and the realised loss (less the realised profit) of trades closed today.
* Balances are updated shortly after an order fills. A value read in the first moments after a fill can be out of date.
* To find out the margin a specific order needs, use the [Margin Calculator](https://fyers.in/api-docs/v3/api/calculators/multi-order-margin-calculator/).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `ok` / `error`. |
| `code` | int | API response code. |
| `message` | string | Response or error message. |
| `fund_limit` | array | One row per ledger heading, with the fields below. |
| `id` | int | Unique identity for particular fund |
| `title` | string | Each title represents a heading of the ledger |
| `equityAmount` | float | The amount in the capital ledger for the above-mentioned title |
| `commodityAmount` | float | The amount in the commodity ledger for the above-mentioned title |

### Ledger headings

| **id** | **title** | **Meaning** |
| --- | --- | --- |
| `1` | Total Balance | Total funds in the ledger: Clear Balance plus Collaterals, adjusted for the day's realised profit and loss. |
| `2` | Utilized Amount | Margin blocked for open positions and open orders, plus brokerage and the realised loss (less the realised profit) of trades closed today. |
| `3` | Clear Balance | Cash balance in the ledger, excluding collaterals. |
| `5` | Collaterals | Value of pledged holdings that counts towards margin. |
| `9` | Limit at start of the day | Cash balance at the start of the day. |
| `10` | Available Balance | Total Balance minus Utilized Amount: the amount available to trade. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

## Make a request to get the funds information
response = fyers.funds()
print(response)
```

```
{
    "code":200,
    "message":"",
    "s":"ok",
    "fund_limit":[
        {
          "id":1,
          "title":"Total Balance",
          "equityAmount":58.150000000000006,
          "commodityAmount":0
        },
        {
          "id":2,
          "title":"Utilized Amount",
          "equityAmount":0.3,
          "commodityAmount":0
        },
        {
          "id":3,
          "title":"Clear Balance",
          "equityAmount":58.150000000000006,
          "commodityAmount":0
        },
        {
          "id":4,
          "title":"Realized Profit and Loss",
          "equityAmount":-0.3,
          "commodityAmount":0
        },
        {
          "id":5,
          "title":"Collaterals",
          "equityAmount":0,
          "commodityAmount":0
        },
        {
          "id":6,
          "title":"Fund Transfer",
          "equityAmount":0,
          "commodityAmount":0
        },
        {
          "id":7,
          "title":"Receivables",
          "equityAmount":0,
          "commodityAmount":0
        },
        {
          "id":8,
          "title":"Adhoc Limit",
          "equityAmount":0,
          "commodityAmount":0
        },
        {
          "id":9,
          "title":"Limit at start of the day",
          "equityAmount":58.45,
          "commodityAmount":0
        },
        {
          "id":10,
          "title":"Available Balance",
          "equityAmount":58.150000000000006,
          "commodityAmount":0
        }
    ]
  }
```

VIDEO LEARNING

### Video learning

[Check account information (REST and cURL)REST and cURL · 2:30](https://www.youtube.com/watch?v=QuY-uymOb1k&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[How to manage your portfolio? (Python)Python · 14:13](https://www.youtube.com/watch?v=yFxwZs4cwgI&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to use margin? (Python)Python · 3:10](https://www.youtube.com/watch?v=YN15RDlmDSs&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to monitor your portfolio? (Node.js)Node.js · 5:08](https://www.youtube.com/watch?v=TLpSSVZZkAg&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Margin monitoring explained (Node.js)Node.js · 5:34](https://www.youtube.com/watch?v=vvhigMe2nGk&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[How to monitor your portfolio? (C#)C# · 2:40](https://www.youtube.com/watch?v=9J50HgZU9wo&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[How to monitor your portfolio? (Java)Java · 5:01](https://www.youtube.com/watch?v=NQFLJ7gz45k&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)[Margin monitoring explained (Java)Java · 5:52](https://www.youtube.com/watch?v=_eKzjX1hvW4&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Holdings

*Source: https://fyers.in/api-docs/v3/api/account/holdings/ (last updated 2026-10-14)*

This API allows you to fetch the equity and mutual fund holdings in your demat account.

USE CASE

Show a portfolio view with quantity, cost price, market value and profit or loss for each holding.

Details

* Fetches the equity and mutual fund holdings which the user has in this demat account. This will include T1 and demat holdings.
* Your app needs the **Transactions Info** permission. Holdings is part of that template, along with Orders, Positions, Trades, Funds and Market Status.
* The request takes no parameters. The `holdings` list returns equity and mutual fund holdings, including T1 holdings and holdings already in demat.
* `holdingType` tells the kind of holding. See [Holding Types](https://fyers.in/api-docs/v3/api/appendix/holding-types/) for the values.
* `quantity` is the quantity at the start of the day. `remainingQuantity` is that quantity minus what was sold during the day. `qty_t1` is the T+1 quantity.
* `collateralQuantity` is the pledged quantity and `remainingPledgeQuantity` is the pledged quantity still remaining.
* The `overall` object gives `count_total`, `total_investment`, `total_current_value`, `total_pl` and `pnl_perc` for the whole portfolio.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes - For each holding

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:RCOM-EQ |
| `holdingType` | string | * Identify the type of holding * [View Details](https://fyers.in/api-docs/v3/api/appendix/holding-types/) |
| `quantity` | int | The quantity of the symbol which the user has at the beginning of the day |
| `remainingQuantity` | int | This reflects the quantity - the quantity sold during the day |
| `pl` | float | Profit and loss made |
| `costPrice` | float | The original buy price of the holding |
| `marketVal` | float | The Market value of the current holding |
| `ltp` | float | LTP is the price from which the next sale of the stocks happens |
| `id` | int | The unique value for each holding |
| `fytoken` | string | * Fytoken is a unique identifier for every symbol. * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `exchange` | int | * The exchange in which order is placed. * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `segment` | int | * The segment in which the holding is taken. * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `isin` | string | Unique ISIN provided by exchange for each symbol |
| `qty_t1` | int | Quantity t+1 day |
| `remainingPledgeQuantity` | int | Remaining Pledged quantity |
| `collateralQuantity` | int | Pledged quantity |

### Response Attributes - Overall holdings

| Attribute | Data Type | Description |
| --- | --- | --- |
| `count_total` | int | Total number of holdings present |
| `total_investment` | float | Invested amount for the current holdings |
| `total_current_value` | float | The present value of the holdings |
| `total_pl` | float | Total profit and loss made |
| `pnl_perc` | float | Percentage value of the total pnl |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

response = fyers.holdings()
print(response)
```

```
{
    "code":200,
    "message":"",
    "s":"ok",
    "overall":{
        "count_total":1,
        "pnl_perc":21.9136,
        "total_current_value":23.700000000000003,
        "total_investment":19.44,
        "total_pl":4.26
    },
    "holdings":[
        {
          "costPrice":6.48,
          "id":0,
          "fyToken":"101000000014366",
          "symbol":"NSE:IDEA-EQ",
          "isin":"INE669E01016",
          "quantity":3,
          "exchange":10,
          "segment":10,
          "qty_t1":0,
          "remainingQuantity":3,
          "collateralQuantity":0,
          "remainingPledgeQuantity":3,
          "pl":4.26,
          "ltp":7.9,
          "marketVal":23.700000000000003,
          "holdingType":"HLD"
        }
    ]
  }
```

VIDEO LEARNING

### Video learning

[Check account information (REST and cURL)REST and cURL · 2:30](https://www.youtube.com/watch?v=QuY-uymOb1k&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[How to manage your portfolio? (Python)Python · 14:13](https://www.youtube.com/watch?v=yFxwZs4cwgI&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[How to monitor your portfolio? (Node.js)Node.js · 5:08](https://www.youtube.com/watch?v=TLpSSVZZkAg&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[How to monitor your portfolio? (C#)C# · 2:40](https://www.youtube.com/watch?v=9J50HgZU9wo&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[How to monitor your portfolio? (Java)Java · 5:01](https://www.youtube.com/watch?v=NQFLJ7gz45k&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Logout

*Source: https://fyers.in/api-docs/v3/api/account/logout/ (last updated 2026-10-14)*

This API allows you to invalidate the access token of your app without affecting other apps or web and mobile sessions.

USE CASE

Revoke the access token when a user signs out of your app.

Other apps and FYERS web and mobile sessions stay signed in.

Note

* This revokes the token only for the specific app.
* Other active apps and FYERS web or mobile sessions stay signed in.

Details

* This invalidates the access token, revoking it only for the specific app without affecting other active apps or web and mobile sessions.
* Your app needs the **Basic** permission. It covers Logout and Logout App, along with Profile Details.
* The request takes no body or parameters. Send a POST with only the `Authorization` header.
* After a successful logout the access token is invalid. Get a new one through the [Authentication](https://fyers.in/api-docs/v3/api/authentication/) flow before calling any other API.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status - "ok" when the logout succeeds. |
| `code` | int | Response status code, e.g. 200 on success. |
| `message` | string | Human-readable message confirming the user was successfully logged out. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

##  Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

## Make a request for logout
response = fyers.logout()

## Print the response received from the Fyers API
print(response)
```

```
{
  "s": "ok",
  "code": 200,
  "message": "you are successfully logged out",
}
```

## Kill Switch

*Source: https://fyers.in/api-docs/v3/api/account/kill-switch/ (last updated 2026-10-14)*

Kill Switch lets you pause trading across all segments on your account for the day.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Activate Kill Switch](https://fyers.in/api-docs/v3/api/account/kill-switch/activate-kill-switch/) | POST | This API pauses trading across all segments on your account. |
| [Kill Switch Status](https://fyers.in/api-docs/v3/api/account/kill-switch/kill-switch-status/) | GET | This API lets you check whether Kill Switch is active on your account. |

## EDIS / DDPI

*Source: https://fyers.in/api-docs/v3/api/account/edis-ddpi/ (last updated 2026-10-14)*

Electronic Delivery Instruction Slip (eDIS) allows you to sell shares if your Power of Attorney (POA) is not submitted or DDPI is not activated.

Use these APIs to generate a TPIN, authorise your holdings with CDSL and check the result.

The four APIs work together. The usual order is to generate the TPIN, call Verify DIS to get the CDSL page where the user authorises the holdings with that TPIN, then use EDIS Inquiry to check the result. EDIS Details lists the authorisations already completed. An authorisation is valid till the end of the day, whether or not the sell is completed.

**Note:** You can sell only authorised holdings. To skip this workflow, [activate DDPI](https://support.fyers.in/portal/en/kb/articles/how-do-i-activate-ddpi-for-my-account-on-fyers).

| Endpoint | Method | Description |
| --- | --- | --- |
| [EDIS Details](https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-details/) | GET | This API allows you to fetch the holding authorisations you have already completed. |
| [TPIN Generation](https://fyers.in/api-docs/v3/api/account/edis-ddpi/tpin-generation/) | GET | This API allows you to generate the TPIN used to authorise the sale of holdings through CDSL or NSDL. |
| [Verify DIS](https://fyers.in/api-docs/v3/api/account/edis-ddpi/verify-dis/) | POST | This API allows you to get the CDSL page where the user authorises holdings for sale. |
| [EDIS Inquiry](https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-inquiry/) | POST | This API allows you to check the status of an authorisation using its transaction ID. |

## Market Status

*Source: https://fyers.in/api-docs/v3/api/market-information/market-status/ (last updated 2026-10-14)*

This API allows you to check the current trading status of all exchanges and their segments.

USE CASE

Check whether a market is open before your bot starts sending orders.

Details

* Fetches the current market status of all the exchanges and their segments
* The response has one row for each exchange, segment and `market_type` (NORMAL, ODD\_LOT, CALL\_AUCTION2 or AUCTION). Pick the row that matches your instrument.
* Match rows using the numeric `exchange` and `segment` codes. See [Exchanges](https://fyers.in/api-docs/v3/api/appendix/exchanges/) and [Segments](https://fyers.in/api-docs/v3/api/appendix/segments/).
* The CAS statuses (`CTS_CLOSE`, `CAS_START`, `CAS_MKT_ORD_RESTRICT`, `CAS_END`) apply only to CAS-eligible symbols. Check `isCasEligible` in the [Symbol Master JSON](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-json/).
* Market Status is part of the Transactions Info app permission, which the Order Placement permission also includes.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - For each exchange market segment

| Attribute | Data Type | Description |
| --- | --- | --- |
| `exchange` | int | * The exchange in which the position is taken. * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `segment` | int | * The segment in which the position is taken. * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `market_type` | string | Type of market/session. Possible values: NORMAL, ODD\_LOT, CALL\_AUCTION2, AUCTION. |
| `status` | string | Current market status. Possible values: PREOPEN, OPEN, CLOSE, POSTCLOSE\_START, CTS\_CLOSE, CAS\_START, CAS\_MKT\_ORD\_RESTRICT, CAS\_END. |

### Market Status Definitions

| **Status** | Description |
| --- | --- |
| `PREOPEN` | Pre-open session is active. |
| `OPEN` | Normal trading session is active. |
| `CLOSE` | Trading session is closed. |
| `POSTCLOSE_START` | Post-close session has started. |
| `CTS_CLOSE` | Continuous trading has ended for CAS-eligible symbols. |
| `CAS_START` | Closing Auction Session(CAS) has started. |
| `CAS_MKT_ORD_RESTRICT` | Market orders are restricted during Closing Auction Session(CAS). |
| `CAS_END` | Closing Auction Session(CAS) has ended. |

**Note:** CAS statuses apply to CAS-eligible symbols. CAS eligibility can be identified using the `isCasEligible` field in the [Symbol Master JSON file](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-json/) section.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

response = fyers.market_status()
print(response)
```

```
{
    "code":200,
    "marketStatus":[
        {
          "exchange":10,
          "market_type":"NORMAL",
          "segment":10,
          "status":"POSTCLOSE_CLOSED"
        },
        {
          "exchange":10,
          "market_type":"NORMAL",
          "segment":11,
          "status":"CLOSED"
        },
        {
          "exchange":10,
          "market_type":"NORMAL",
          "segment":12,
          "status":"CLOSED"
        },
        {
          "exchange":10,
          "market_type":"CALL_AUCTION2",
          "segment":10,
          "status":"CLOSED"
        },
        {
          "exchange":10,
          "market_type":"AUCTION",
          "segment":10,
          "status":"CLOSED"
        },
        {
          "exchange":10,
          "market_type":"ODD_LOT",
          "segment":10,
          "status":"CLOSED"
        },
        {
          "exchange":11,
          "market_type":"NORMAL",
          "segment":20,
          "status":"OPEN"
        },
        {
          "exchange":11,
          "market_type":"SPECIAL",
          "segment":20,
          "status":"CLOSED"
        },
        {
          "exchange":12,
          "market_type":"NORMAL",
          "segment":10,
          "status":"POSTCLOSE_CLOSED"
        },
        {
          "exchange":12,
          "market_type":"NORMAL",
          "segment":12,
          "status":"POSTCLOSE_CLOSED"
        },
        {
          "exchange":12,
          "market_type":"AUCTION",
          "segment":10,
          "status":"CLOSED"
        },
        {
          "exchange":12,
          "market_type":"NORMAL",
          "segment":11,
          "status":"POSTCLOSE_CLOSED"
        }
    ],
    "message":"",
    "s":"ok"
  }
```

## Symbol Master

*Source: https://fyers.in/api-docs/v3/api/market-information/symbol-master/ (last updated 2026-10-14)*

Download the Symbol Master in CSV or JSON format to discover instruments and use the exact instrument identifiers in API requests.

| Endpoint | Method | Description |
| --- | --- | --- |
| [Symbol Master File](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-file/) | — | This API allows you to download the latest Symbol Master as a CSV file for an exchange segment. |
| [Symbol Master JSON](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-json/) | — | This API allows you to download the latest Symbol Master as a JSON file for an exchange segment. |

For a walkthrough of reading and filtering the files, see the [Symbol Master Guide](https://fyers.in/api-docs/v3/getting-started/guides/use-symbol-master/).

VIDEO LEARNING

### Video learning

[How to find stock symbols? (REST and cURL)REST and cURL · 5:01](https://www.youtube.com/watch?v=u2qEMgFWjKw&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Symbol format guide (Python)Python · 5:01](https://www.youtube.com/watch?v=1TjugxsnfwY&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Symbol format step by step guide (Node.js)Node.js · 5:00](https://www.youtube.com/watch?v=N7V9YH4e1Kg&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Symbol format guide (C#)C# · 5:01](https://www.youtube.com/watch?v=U95lPkxIk0U&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Symbol format guide (Java)Java · 5:01](https://www.youtube.com/watch?v=ZcPnyUVgZo0&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## EDIS Inquiry

*Source: https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-inquiry/ (last updated 2026-10-14)*

This API allows you to check the status of an authorisation using its transaction ID.

USE CASE

Confirm that an authorisation went through before allowing the sell.

The response counts the holdings that succeeded and failed.

Note

Transaction ID must be base64 encoded.

Transaction ID to be base64 encoded in payload. please refer to the [online tool](https://emn178.github.io/online-tools/base64_encode.html) for conversion.

Details

* This Api is used to get the information/status of the provided transaction Id for the respective holdings you have on your end.
* Send one `transactionId` in the request body, Base64-encoded. Take the value from [EDIS Details](https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-details/) and encode it before sending.
* The response returns `SUCEESS_CNT` and `FAILED_CNT`, the number of holdings that succeeded and failed under that transaction ID. The key `SUCEESS_CNT` is spelled this way in the API.
* The response gives counts only. For the quantities, dates and status text of completed authorisations, call EDIS Details.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `transactionId` | string | The transaction ID to check the status/information for; must be base64 encoded in the payload. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status indicator: "ok" for success, "error" for failure. |
| `code` | int | Response status code. |
| `message` | string | Descriptive message about the response. |
| `FAILED_CNT` | int | Number of holdings/transactions that failed under the given transaction ID. |
| `SUCEESS_CNT` | int | Number of holdings/transactions that succeeded under the given transaction ID. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl --location --request POST 'https://api.fyers.in/api/v2/inquiry'
 --header 'Authorization: app_id:access_Token' --header 'Content-Type: application/json' --data-raw '{"transactionId": "OTE1NDg0MTA4MTc2"}'
```

```
{"s": "ok", "code": 200, "message": "", "data": {"FAILED_CNT": 0, "SUCEESS_CNT": 1}}
```

## SPAN Margin Calculator

*Source: https://fyers.in/api-docs/v3/api/calculators/span-margin-calculator/ (last updated 2026-10-14)*

This API allows you to calculate the combined SPAN and exposure margin for futures and options, including margin benefits from hedges and individual instrument margin details.

USE CASE

Compare hedged and unhedged strategies and understand the margin required for the combined basket.

Note

* A maximum of **20 symbols** is allowed per request.
* Each entry in the `data` array counts towards this limit.
* Zero SPAN margin for bought options does not mean zero premium cost.

Details

* Pass the instrument details inside a `data` array.
* Margin fields are returned inside `data`. Individual instrument details are returned separately in `individual_info`.
* The example buys OTM hedges before selling ATM options.
* The result is based only on the instruments you send. It does not depend on your existing positions, the order of the orders, or the product type. To include your positions and the order sequence, use the [Multi-order Margin Calculator](#margin-calculator-api).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Futures or options symbol in FYERS symbology format. Equity symbols are not supported. |
| `qty` | int | Quantity. For NSE and BSE derivatives, in units, as a multiple of the lot size. For MCX, the number of lots. |
| `side` | int | `1` = Buy; `-1` = Sell. |
| `type` | int | * `1` = Limit * `2` = Market (MPP: Market Price Protection ) * `3` = Stop-market (SL-M, MPP: Market Price Protection ) * `4` = Stop-limit (SL-L)  The order type does not change the calculated margin. |
| `productType` | string | Product type, such as `INTRADAY` or `MARGIN`. It does not change the calculated margin. |
| `limitPrice` | float | Limit price, where applicable. Use `0.0` for market orders. Can be omitted. It does not change the calculated margin. |
| `stopLoss` | float | Stop-loss value, where applicable. Use `0.0` otherwise. Can be omitted. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `ok` / `error`. |
| `code` | int | API response code. `200` on success; `-50`, `-310`, `-209` or `-17` for errors. |
| `message` | string | Response or error message. Empty on success. |
| `latency` | string | Reserved. Returned empty. |
| `data.span` | float | Combined SPAN risk margin for the basket. |
| `data.expo` | float | Combined exposure margin for the basket. |
| `data.total` | float | Combined margin requirement: SPAN plus exposure margin. |
| `data.benefit` | float | Margin saving from combining the legs. It equals the sum of the individual totals minus `total`, and is already reflected in `total`; do not subtract it again. |
| `individual_info` | object | Individual margin details, keyed by FYERS instrument token. |
| `individual_info[token].ltp_info` | float | Instrument’s last traded price reported by the calculator. |
| `individual_info[token].span` | float | Individual SPAN margin. |
| `individual_info[token].expo` | float | Individual exposure margin. |
| `individual_info[token].total` | float | Individual total margin. |

### Errors

| Code | Description |
| --- | --- |
| `-50` | Invalid input. |
| `-310` | Invalid symbol, or more than 20 symbols. |
| `-209` | Token missing. |
| `-17` | Authentication failed. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl --location 'https://api.fyers.in/api/v2/span_margin' \
  --header 'Authorization: <APP_ID>:<ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": [
      {"symbol":"NSE:NIFTY26OCT22650CE","qty":65,"side":1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopLoss":0.0},
      {"symbol":"NSE:NIFTY26OCT22350PE","qty":65,"side":1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopLoss":0.0},
      {"symbol":"NSE:NIFTY26OCT22500CE","qty":65,"side":-1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopLoss":0.0},
      {"symbol":"NSE:NIFTY26OCT22500PE","qty":65,"side":-1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopLoss":0.0}
    ]
  }'
```

```
{
  "code": 200,
  "message": "",
  "data": {
    "span": 10609,
    "expo": 60195.59,
    "total": 70804.59,
    "benefit": 254358.13999999998
  },
  "s": "ok",
  "individual_info": {
    "101126102751325": {
      "ltp_info": 156.95,
      "span": 0,
      "expo": 0,
      "total": 0
    },
    "101126102751330": {
      "ltp_info": 332,
      "span": 139016.15,
      "expo": 30097.79,
      "total": 169113.94
    },
    "101126102751331": {
      "ltp_info": 205.15,
      "span": 125951,
      "expo": 30097.79,
      "total": 156048.79
    },
    "101126102751338": {
      "ltp_info": 245.1,
      "span": 0,
      "expo": 0,
      "total": 0
    }
  },
  "latency": ""
}
```

## Multi-order Margin Calculator

*Source: https://fyers.in/api-docs/v3/api/calculators/multi-order-margin-calculator/ (last updated 2026-10-14)*

This API allows you to calculate the approximate margin required for proposed equity and derivative orders, including commodity derivatives, and returns the available account margin.

USE CASE

Check the funding requirement of an order basket before you submit it, using the intended order sequence and product types.

Note

* A maximum of **50 orders** is allowed per request.
* Order sequence and product types can affect the margin requirement.
* The calculator works through the orders in the sequence you send them. After the orders are placed, the margin blocked on your account is based on your combined positions, so it does not depend on the order in which they were placed.
* `margin_total` is calculated after your existing positions, so it is not a standalone figure for the basket. For a figure that ignores your account, use the [SPAN Margin Calculator](https://fyers.in/api-docs/v3/api/calculators/span-margin-calculator/).
* For hedged strategies, passing hedge BUY orders before SELL orders can reduce the required margin.
* Using different product types for hedge and main legs can increase the margin requirement.
* A hedge with an existing position gets the margin benefit only when it has the same product type.

Details

* Pass the orders inside a `data` array in the intended execution sequence.
* Margin fields are returned inside `data`.
* To check whether the orders can be funded, compare `margin_total` with `margin_avail`. `margin_avail` already excludes the margin in use.
* `limitPrice`, `stopPrice`, `stopLoss` and `takeProfit` can be omitted. If any order has an invalid symbol, the whole request is rejected.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Required | Description |
| --- | --- | --- | --- |
| `symbol` | string | Yes | Instrument symbol in FYERS symbology format. |
| `qty` | int | Yes | Quantity. For NSE and BSE derivatives, in units, as a multiple of the lot size. For MCX, the number of lots. |
| `side` | int | Yes | `1` = Buy; `-1` = Sell. |
| `type` | int | Yes | * `1` = Limit * `2` = Market (MPP: Market Price Protection ) * `3` = Stop-market (SL-M, MPP: Market Price Protection ) * `4` = Stop-limit (SL-L) |
| `productType` | string | Yes | `CNC`, `INTRADAY`, `MARGIN` or `MTF`, in uppercase. The calculator does not check whether the instrument is eligible for the product type. |
| `limitPrice` | float | No | Positive limit price (at least `0.0025`) for limit and stop-limit orders. Must be `0.0` for market and stop-market orders. For a stop-limit sell order it must be below the trigger price. |
| `stopPrice` | float | No | Positive trigger price (at least `0.0025`) for stop-market and stop-limit orders. Use `0.0` otherwise. |
| `stopLoss` | float | No | Reserved. Must be `0.0`. |
| `takeProfit` | float | No | Reserved. Must be `0.0`. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | `ok` / `error`. |
| `code` | int | API response code. `200` on success; `-50` for invalid input; `-16` for authentication errors. |
| `message` | string | Response or error message. Empty on success. |
| `data` | object | Object that holds the margin values below. |
| `margin_total` | float | Approximate additional margin required for the submitted orders, after considering your existing positions. It equals the margin for the orders alone only when `prevMargin` is 0. |
| `margin_new_order` | float | Approximate total margin in use after the submitted orders are placed. It equals `margin_total` + `prevMargin`. |
| `margin_avail` | float | Available margin in your account, the same as Available Balance in the Funds API. It already excludes the margin in use (`prevMargin`). |
| `prevMargin` | float | Margin already in use on your account when the request is made, the same as Utilized Amount in the Funds API. It covers existing positions and open orders, and also includes the brokerage and realised result of trades you have closed today. |

### Errors

| Code | Description |
| --- | --- |
| `-50` | Invalid input. For example: `qty: Must be greater than or equal to 1`, `The input symbol is invalid.:SYMBOL` or `Maximum Items number limit reached`. |
| `-16` | Authentication failed. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl --location 'https://api-t1.fyers.in/api/v3/multiorder/margin' \
  --header 'Authorization: <APP_ID>:<ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
    "data": [
      {"symbol":"NSE:NIFTY26OCT22650CE","qty":65,"side":1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopPrice":0.0,"stopLoss":0.0,"takeProfit":0.0},
      {"symbol":"NSE:NIFTY26OCT22350PE","qty":65,"side":1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopPrice":0.0,"stopLoss":0.0,"takeProfit":0.0},
      {"symbol":"NSE:NIFTY26OCT22500CE","qty":65,"side":-1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopPrice":0.0,"stopLoss":0.0,"takeProfit":0.0},
      {"symbol":"NSE:NIFTY26OCT22500PE","qty":65,"side":-1,"type":2,"productType":"INTRADAY","limitPrice":0.0,"stopPrice":0.0,"stopLoss":0.0,"takeProfit":0.0}
    ]
  }'
```

```
// Sample Success Response
{
  "code": 200,
  "message": "",
  "data": {
    "margin_avail": 294393.5226,
    "margin_total": 138675.84,
    "margin_new_order": 138675.84,
    "prevMargin": 0
  },
  "s": "ok"
}

// Sample Success Response (With an open position)
{
  "code": 200,
  "message": "",
  "data": {
    "margin_avail": 288055.5798,
    "margin_total": 56739.71,
    "margin_new_order": 58725.96,
    "prevMargin": 1986.25
  },
  "s": "ok"
}
```

## General WebSocket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/ (last updated 2026-10-14)*

This WebSocket allows you to receive real-time updates on your orders, positions, trades, price alerts and EDIS status over a single connection.

This guide provides instructions on integrating the General WebSocket into any programming language.

USE CASE

Get your order, trade and position updates pushed to your app instead of polling the Order Book, Trade Book or Positions.

Events

[Order EventsWSSThis WebSocket allows you to receive live updates on the status of your orders, including partial fills and rejections.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-order-events/)[Trade EventsWSSThis WebSocket allows you to receive a live update for every trade executed against your orders.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-trade-events/)[Position EventsWSSThis WebSocket allows you to receive live updates on your positions as your trades execute.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-position-events/)[General EventsWSSThis WebSocket allows you to receive price alert, EDIS and login notifications for your account.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-general-events/)

### Key points

* Connect to `wss://socket.fyers.in/trade/v3` with an authorization header in `appId:accessToken` format.
* Subscribe with `T` set to `SUB_ORD`, `SUB_T` set to `1` and the actions you want in `SLIST`: `orders`, `trades`, `positions`, `edis`, `pricealerts` or `login`. Use `SUB_T` `-1` to unsubscribe.
* Send a `ping` message at regular intervals. A `pong` reply means the connection is alive.
* Read the top-level key of each message (`orders`, `trades`, `positions`, `pricealerts`) to know which event it is. The Python SDK subscribes with `OnOrders`, `OnTrades`, `OnPositions` and `OnGeneral`.
* Keep a single WebSocket connection instance open at a time.

### Connect

Details

To connect to the General WebSocket, the below two input params are mandate. Based on the programming language chosen, respective socket connection libraries can be used. For reference, the sample code for socket connection is written in Python.

**Mandatory connection parameters**

Pass the websocket endpoint and an authorization header in `<appId:accessToken>` format.

Websocket endpoint: `wss://socket.fyers.in/trade/v3`

Header

Format: `<appId:accessToken>`

Sample header format: `7ABXUX38S-100:eyJ0eXAi**********qiTnzd2lGwS17s`

The connection uses parameters and callback functions `on_message`, `on_error`, `on_close`, and `on_open`, which are required in the Python socket connection library and would change as per the other programming library used. A sample callback function is shared below.

**Note**

Handle accordingly in your programming language.

**Connection response**

On success: returns the socket object.

On failure: possible error status code `403`.

Error: Handshake status 403 Forbidden

Handshake status 403 Forbidden -+-+- {'date': 'Tue, 19 Dec 2023 04:46:45 GMT', 'content-length': '0', 'connection': 'keep-alive', 'cf-cache-status': 'DYNAMIC', 'set-cookie': '\_\_cf\_bm=BOE16LGB7NHpNqW0AJOuFN1rcL3Q9TgnhmtpBfb3.Wk-1702961205-1- AfmECmK9cbVA2XGvkpx+jFuXyRsJET/ZOQYmw3LyZJ68pYLZTgtpbalvNs09ECZZ4GpPiogeYGhhFo+3PCp20nE=; path=/; expires=Tue, 19-Dec-23 05:16:45 GMT; domain=.fyers.in; HttpOnly; Secure', 'server': 'cloudflare', 'cf-ray': '837d00eec8ed17b6-MAA'} -+-+- b''

* Reason: this error will come when your `accessToken` is wrong.
* How to solve: provide the correct accessToken. AccessToken format: `<appID:accesstoken>`.

Error: Handshake status 404 Not Found

Handshake status 404 Not Found -+-+- {'date': 'Tue, 19 Dec 2023 10:04:35 GMT', 'content-type': 'text/plain; charset=utf-8', 'content-length': '0', 'connection': 'keep-alive', 'cf-cache-status': 'DYNAMIC', 'set-cookie': '\_\_cf\_bm=I5oN6zdeKjfGsicqFiXZ57J5SX2IjsFDspaLIEGKPDE-1702980275-1-Ae+ldjrb3WfSuM7yNOzo3ykOIBQ1m+50QqcIqU26A+wqPIHhIEIGSy9kT2OG3OWNI0hwcmh7U+PnJ/aWWhz6fOA=; path=/; expires=Tue, 19-Dec-23 10:34:35 GMT; domain=.fyers.in; HttpOnly; Secure', 'server': 'cloudflare', 'cf-ray': '837ed28169c817ae-MAA'} -+-+- b''

* Reason: socket connection URL would be wrong.
* How to solve: provide a valid URL.

Sample callback function: for more reference, see the `on_open` callback in the Python request sample.

**Good to know**

* This is the General WebSocket endpoint for account events. Live market data uses the separate Data Socket.
* Connecting alone does not deliver any data. Subscribe to the actions you want once the connection is open.
* The Python SDK sends the access token in the `authorization` header. With your own client, send `<appId:accessToken>` in the header.
* With `order_ws.FyersOrderSocket`, the callbacks are `on_connect`, `on_close`, `on_error`, `on_orders`, `on_trades`, `on_positions` and `on_general`. Subscribe inside `on_connect`, then call `keep_running()`.
* The SDK starts its ping loop as soon as the connection opens. With your own client, send `ping` yourself (see Ping method).
* Create only one WebSocket connection instance at a time, as advised in the WebSocket guidance.

Full reference and samples: [General WebSocket - Connect](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-connect/).

### Subscribe

Details

Once the connection is established, it is required to subscribe for required actions to get the data. To subscribe for different actions, create a message data, which would be the string format for json node.

**Json node params**

Convert the json to string and send this message to the socket to subscribe for the `action_data` mentioned.

message

`message = json.dumps({ "T": "SUB_ORD", "SLIST": action_data, "SUB_T": 1 })`

`T` Type: String
value: `SUB_ORD` (Fixed)

`action_data` Type: List/Array
Value: `orders` `trades` `positions` `edis` `pricealerts` `login`

Based on the list passed in action\_data, web\_socket data will be received.

`SUB_T` Type: Integer
Value: `1` (value 1 is for subscribing and -1 for unsubscribe)

**Sample response and socket payload**

Once subscribed successfully, for any action triggered, data will be received through the socket. If a callback function is defined, it receives that data. The response is a string in Python and an ArrayBuffer in Node. In another language, convert the payload to a string, then parse it.

Sample response

`{'code': 1605, 'message': 'Successfully subscribed', 's': 'ok'}`

Type: string

Value

{"orders":{"client\_id":"XP0001","exchange":10,"fy\_token":"10100000001628","id":"23121800292158","id\_fyers":"df013f50-6925-4e2d-ba0f-0becf1229298","instrument":0,"lot\_size":1,"offline\_flag":false,"oms\_flag":"K:1","ord\_source":"W","ord\_status":20,"ord\_type":2,"ordertag":"2:Untagged","org\_ord\_status":4,"pan":"FYxxxxxx0S","precision":2,"price\_multiplier":1,"product\_type":"CNC","qty":1,"qty\_multiplier":1,"qty\_remaining":1,"report\_type":"New Ack","segment":10,"status\_msg":"New Ack","symbol":"NSE:BECTORFOOD-EQ","symbol\_desc":"MRS BECTORS FOOD SPE LTD","symbol\_exch":"BECTORFOOD","tick\_size":0.05,"time\_epoch\_oms":1702887690,"time\_exch":"NA","time\_oms":"18-Dec-2023 13:51:30","tran\_side":1,"update\_time\_epoch\_oms":1702887690,"update\_time\_exch":"01-Jan-1970 05:30:00","validity":"DAY"},"s":"ok"}

**Note**

1. The response is a string in Python and an `arraybuffer` in Node. Check the format you receive from the websocket library for your language.
2. Convert the data to a string if it is not already a string, then parse that string to JSON. The JSON will contain one of these keys: `orders`, `trades`, or `positions`.
3. The key identifies the update type. `orders` is an order update, `trades` is a trades update, and `positions` is a positions update.
4. In the FYERS SDK, the raw socket response is parsed to keep required keys and remove unnecessary keys.

Parsed Data

```
{
  "s": "ok",
  "orders": {
    "clientId": "XP03754",
    "id": "23121800388066",
    "qty": 1,
    "remainingQuantity": 1,
    "type": 2,
    "fyToken": "10100000002705",
    "exchange": 10,
    "segment": 10,
    "symbol": "NSE:PRAJIND-EQ",
    "instrument": 0,
    "offlineOrder": false,
    "orderDateTime": "18-Dec-2023 16:33:24",
    "orderValidity": "DAY",
    "productType": "CNC",
    "side": 1,
    "status": 4,
    "source": "W",
    "ex_sym": "PRAJIND",
    "description": "PRAJ INDUSTRIES LTD",
    "orderNumStatus": "23121800388066:4"
  }
}
```

* All the keys information for orders updates are available there: [orders event keys](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-order-events/)
* All the keys information for trades updates are available there: [trades event keys](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-trade-events/)
* All the keys information for positions updates are available there: [positions event keys](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-position-events/)

Internal mapping from raw keys to the final parsed data:

```
{
  "position_mapper": {
    "symbol": "symbol",
    "id": "id",
    "buy_avg": "buyAvg",
    "buy_qty": "buyQty",
    "buy_val": "buyVal",
    "sell_avg": "sellAvg",
    "sell_qty": "sellQty",
    "sell_val": "sellVal",
    "net_avg": "netAvg",
    "net_qty": "netQty",
    "tran_side": "side",
    "qty": "qty",
    "product_type": "productType",
    "pl_realized": "realized_profit",
    "rbirefrate": "rbiRefRate",
    "fy_token": "fyToken",
    "exchange": "exchange",
    "segment": "segment",
    "day_buy_qty": "dayBuyQty",
    "day_sell_qty": "daySellQty",
    "cf_buy_qty": "cfBuyQty",
    "cf_sell_qty": "cfSellQty",
    "qty_multiplier": "qtyMulti_com",
    "pl_total": "pl",
    "cross_curr_flag": "crossCurrency",
    "pl_unrealized": "unrealized_profit"
  },
  "order_mapper": {
    "client_id": "clientId",
    "id": "id",
    "id_parent": "parentId",
    "id_exchange": "exchOrdId",
    "qty": "qty",
    "qty_remaining": "remainingQuantity",
    "qty_filled": "filledQty",
    "price_limit": "limitPrice",
    "price_stop": "stopPrice",
    "tradedPrice": "price_traded",
    "ord_type": "type",
    "fy_token": "fyToken",
    "exchange": "exchange",
    "segment": "segment",
    "symbol": "symbol",
    "instrument": "instrument",
    "oms_msg": "message",
    "offline_flag": "offlineOrder",
    "time_oms": "orderDateTime",
    "validity": "orderValidity",
    "product_type": "productType",
    "tran_side": "side",
    "org_ord_status": "status",
    "ord_source": "source",
    "symbol_exch": "ex_sym",
    "symbol_desc": "description"
  },
  "trade_mapper": {
    "id_fill": "tradeNumber",
    "id": "orderNumber",
    "qty_traded": "tradedQty",
    "price_traded": "tradePrice",
    "traded_val": "tradeValue",
    "product_type": "productType",
    "client_id": "clientId",
    "id_exchange": "exchangeOrderNo",
    "ord_type": "orderType",
    "tran_side": "side",
    "symbol": "symbol",
    "fill_time": "orderDateTime",
    "fy_token": "fyToken",
    "exchange": "exchange",
    "segment": "segment"
  }
}
```

**Good to know**

* Subscribe only after the connection is open. You receive data only for the actions you pass in `SLIST`, and you can list several actions in one message.
* A message with `code` `1605` and `s` set to `ok` confirms the subscription.
* In the Python SDK, subscribe with `data_type` values `OnOrders`, `OnTrades`, `OnPositions` and `OnGeneral`. Join several with commas, for example `OnOrders,OnTrades`. The SDK converts them into `SLIST`.
* Price alert, EDIS and login messages are general events and arrive under their own top-level key, for example `pricealerts`. See General Events.
* The raw message and the SDK-parsed message use different key names, for example `org_ord_status` becomes `status` and `tran_side` becomes `side`. Use the key mappers above to translate between them.
* `SUB_T` `1` subscribes and `-1` unsubscribes. See General Socket - UnSubscribe.

Full reference and samples: [General WebSocket - Subscribe](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-subscribe/).

### Unsubscribe

Details

To Unsubscribe for different actions, create a message data, which would be the string format for json node.

**Json node params**

Convert the json to string and send this message to the socket to unsubscribe for the `action_data` mentioned.

message

`message = json.dumps({ "T": "SUB_ORD", "SLIST": action_data, "SUB_T": -1 })`

`T` Type: String
value: `SUB_ORD` (Fixed)

`action_data` Type: List/Array
Value: `orders` `trades` `positions` `edis` `pricealerts` `login`

Based on the list passed in action\_data, web\_socket data will be received.

`SUB_T` Type: Integer
Value: `-1` (value -1 is for unsubscribing and 1 for subscribe)

**Good to know**

* The message is the same as the subscribe message. Only `SUB_T` changes: `-1` unsubscribes and `1` subscribes.
* Put the actions you want to stop in `SLIST`, using the same names as when subscribing: `orders`, `trades`, `positions`, `edis`, `pricealerts`, `login`.
* In the Python SDK, `unsubscribe(data_type)` takes the same comma-separated names as `subscribe` and sends this message for you.

Full reference and samples: [General WebSocket - Unsubscribe](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-unsubscribe/).

### Ping

Details

To check whether the websocket connection is alive or not, we have to send a periodically `ping` message. If we get a `pong` from websocket, it means it is alive else dead. Find how we are doing in Python Code.

**Ping interval**

Here there is one while loop with sleep of `10` seconds and we send a `ping` message to websocket to know that websocket is alive or not.

message

`self.__ws_object.send("ping")`

`ping` Type: String
value: `ping` (Fixed)

`sleep` Type: Integer
Value: `10` seconds

**Good to know**

* The message is the plain text `ping`, not JSON. A `pong` reply means the connection is alive. If none comes, treat the connection as dead.
* The sample loop sends `ping` and then sleeps for 10 seconds, and keeps going only while the socket is still connected.
* The Python SDK starts this ping loop in its own thread as soon as the connection opens. If you use your own client, run the loop yourself.
* Connection, subscribe and unsubscribe each have mandatory fields. See the table below.

### Mandatory fields

| Method | Fields | Reason |
| --- | --- | --- |
| WebSocket Connection | `WebSocket Connection URL(Endpoint)` | To make a connection |
| WebSocket Connection | `Headers` | To authorize |
| Subscribe Method | `action_data` | To subscribe for particular actions |
| Subscribe Method | `"SUB_T": 1` | While subscribing to any action |
| UnSubscribe Method | `"SUB_T": -1` | While unsubscribing any action |

Full reference and samples: [General WebSocket - Ping and Mandatory Fields](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/ping-method/).

### In this section

| Endpoint | Method | Description |
| --- | --- | --- |
| [Connect](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-connect/) | WSS | This guide explains how to connect to the General WebSocket using the endpoint and an authorization header. |
| [Subscribe](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-subscribe/) | WSS | This guide explains how to subscribe to orders, trades, positions, EDIS, price alerts and login updates on the General WebSocket. |
| [Unsubscribe](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-unsubscribe/) | WSS | This guide explains how to stop receiving selected updates on the General WebSocket without closing the connection. |
| [Ping and Mandatory Fields](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/ping-method/) | WSS | This guide explains how to send ping messages to check that the General WebSocket connection is alive. |
| [Order Events](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-order-events/) | WSS | This WebSocket allows you to receive live updates on the status of your orders, including partial fills and rejections. |
| [Trade Events](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-trade-events/) | WSS | This WebSocket allows you to receive a live update for every trade executed against your orders. |
| [Position Events](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-position-events/) | WSS | This WebSocket allows you to receive live updates on your positions as your trades execute. |
| [General Events](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-general-events/) | WSS | This WebSocket allows you to receive price alert, EDIS and login notifications for your account. |

## Create Price Alert

*Source: https://fyers.in/api-docs/v3/api/price-alerts/create-price-alert/ (last updated 2026-10-14)*

This API allows you to create a price alert for an instrument.

USE CASE

Get notified when an instrument, such as NSE:SBIN-EQ, crosses a price you choose.

FYERS watches the price, so your app does not have to poll quotes.

Details

* You can create a new price alert using this API. Alerts can be configured based on the following parameters.
* Send `alert-type` as `1` (price-based alert). `comparisonType` picks the price that is checked: `LTP`, `OPEN`, `HIGH`, `LOW` or `CLOSE`.
* `condition` accepts `GT`, `GTE`, `LT`, `LTE` or equality. The reference lists equality as `E` in the Condition table and as `==` in the request attributes.
* `symbol` must be the full trading symbol, for example `NSE:SBIN-EQ`. `name` is only your own label for the alert.
* A successful call returns code `120` and a confirmation message only. Read the `alertId` for later calls from [Get Price Alerts](https://fyers.in/api-docs/v3/api/price-alerts/get-price-alerts/).
* Triggered alerts arrive on the [General WebSocket](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/) under `pricealerts`, which also pushes a message when an alert is created.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

#### Comparison Type

| **Possible Values** | Description |
| --- | --- |
| `LTP` | LTP |
| `HIGH` | High Price |
| `LOW` | Low Price |
| `OPEN` | Open Price |
| `CLOSE` | Close Price |

#### Condition

| **Possible Values** | Description |
| --- | --- |
| `GT` | Greater than (>) |
| `GTE` | Greater than equal to (>=) |
| `LT` | Less than |
| `LTE` | Less than equal to (<=) |
| `E` | Equal to |

#### Alert Type

| **Possible Values** | Description |
| --- | --- |
| `1` | v / LTP |

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `agent` | string | Source of alert creation. Eg: "fyers-api" |
| `alert-type` | int | Type of alert. 1 price-based alert. |
| `name` | string | User-provided label for alert. |
| `symbol` | string | Full trading symbol (e.g., "NSE:SBIN-EQ") |
| `comparisonType` | string | price metric. Allowed: "OPEN", "HIGH", "LOW", "CLOSE", "LTP" |
| `condition` | string | comparison operator. Allowed: "GT" (greater), "GTE" (greater or equal), "LT" (lesser), "LTE" (lesser or equal), "==" (equal) |
| `value` | float | Target price for comparison. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Numeric response/status code returned by the API (e.g. 120 on successful alert creation). |
| `message` | string | Human-readable message describing the result of the alert creation request. |
| `s` | string | Status of the response. Possible value: "ok" for a successful request. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

data = {
    "agent": "fyers-api",
    "alert-type": 1,
    "name": "SBIN Alert",
    "symbol": "NSE:SILVERMIC25DECFUT",
    "comparisonType": "CLOSE",
    "condition": "LT",
    "value": 45
}

response = fyers.create_alert(data=data)
print(response)
```

```
{
  "code": 120,
  "message": "A price alert for NSE:SILVERMIC25DECFUT at â¹45 is created.",
  "s": "ok"
}
```

## Get Price Alerts

*Source: https://fyers.in/api-docs/v3/api/price-alerts/get-price-alerts/ (last updated 2026-10-14)*

This API allows you to fetch your price alerts by alert name or alert ID, with their current status.

USE CASE

Check which alerts are enabled, triggered or disabled, and get the alert IDs that Modify, Delete and Enable / Disable need.

Details

* You can retrieve alerts using:
* Alert Name
* Alert Id
* This returns both active and triggered alerts.
* The `data` object in the response is keyed by alert ID. Each entry holds `fyToken`, `alert` and `symbol`.
* Read `status` before changing an alert: `1` is enabled, `0` is triggered and `2` is disabled. Triggered alerts cannot be modified or switched.
* Times come both as text, for example `04-Dec-2025 12:20:03`, and as epoch seconds in `createdEpoch`, `triggeredEpoch` and `modifiedEpoch`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `fyToken` | string | Fytoken is a unique identifier for every symbol. |
| `alert` | object | Detailed alert configuration. |
| `symbol` | string | Trading symbol for the alert. |

### alert Object Fields

| Attribute | Data Type | Description |
| --- | --- | --- |
| `comparisonType` | string | metric compared (e.g., "OPEN", "CLOSE"). |
| `condition` | string | Comparison operator (GT, LT, EQ). |
| `name` | string | user label. |
| `type` | string | Alert type.(e.g,"V"= LTP) |
| `value` | float/int | Target value. |
| `triggeredAt` | string | Time of trigger (if any). |
| `createdAt` | string | creation timestamp. |
| `modifiedAt` | string | Last updated timestamp. |
| `notes` | string | Additional notes or description. |
| `status` | int | Alert status: 1 = Enabled, 0 = triggered, 2 = Disabled |
| `triggeredEpoch` | int | Trigger time (epoch) (0 = not triggered). |
| `createdEpoch` | int | Created timestamp (epoch format) . |
| `modifiedEpoch` | int | Last modified timestamp in epoch format (0 = never modified). |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

response = fyers.get_alert()
print(response)
```

```
{
  "code": 200,
  "message": "",
  "data": {
    "5682484": {
      "fyToken": "10100000008080",
      "alert": {
        "comparisonType": "LTP",
        "condition": "LT",
        "name": "Silver alert ",
        "type": "V",
        "value": 130,
        "triggeredAt": "",
        "createdAt": "09-Dec-2025 11:49:06",
        "modifiedAt": "",
        "notes": "",
        "status": 2,
        "triggeredEpoch": 0,
        "createdEpoch": 1765280946,
        "modifiedEpoch": 0
      },
      "symbol": "NSE:SILVERBEES-EQ"
    }
  },
  "s": "ok"
}
```

## Modify Price Alert

*Source: https://fyers.in/api-docs/v3/api/price-alerts/modify-price-alert/ (last updated 2026-10-14)*

This API allows you to modify an existing price alert.

USE CASE

Move the target price or change the compared price of an alert without deleting and re-creating it.

Details

* Allows you to modify alerts.
* Only active alerts can be modified.
* Expired or triggered alerts cannot be modified.
* The symbol associated with an alert cannot be changed; all other fields can be updated.
* Send the whole alert definition, not only the changed field: `alertId`, `alert-type`, `name`, `symbol`, `comparisonType` and `value` are mandatory.
* `name` can be at most 50 characters and `value` can have up to 6 decimal places.
* Send `symbol` exactly as the alert was created. It cannot be changed, so to watch another instrument create a new alert.
* A successful call returns code `123` and a message saying the alert for that symbol at the new value is updated.
* Check the alert `status` in [Get Price Alerts](https://fyers.in/api-docs/v3/api/price-alerts/get-price-alerts/) first: `1` is enabled, `0` is triggered and `2` is disabled.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `alertId`\* | string | Mandatory. Unique alert ID |
| `agent` | string | Identifier of client (e.g., "fyers-api") |
| `alert-type` | int | Mandatory. 1 → Price alert (LTP) |
| `name` | string | Mandatory. Max 50 characters |
| `symbol` | string | Mandatory. Trading symbol (e.g., NSE:GOLDBEES-EQ) |
| `comparisonType` | string | Mandatory. comparision type Allowed: "OPEN", "HIGH", "LOW", "CLOSE", "LTP" |
| `condition` | string | comparison operator. Allowed: "GT" (greater), "GTE" (greater or equal), "LT" (lesser), "LTE" (lesser or equal), "==" (equal) |
| `value` | float | Mandatory. Up to 6 decimal places |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status. Possible values: `"ok"` or `"error"` |
| `code` | int | Response status code |
| `message` | string | Message describing the result of the price alert modification |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

data = {
    "alertId": "3870995",
    "agent": "fyers-api",
    "alert-type": 1,
    "name": "Updated Alert",
    "symbol": "NSE:SILVERMIC25DECFUT",
    "comparisonType": "CLOSE",
    "condition": "LT",
    "value": 50
}

response = fyers.update_alert(data=data)
print(response)
```

```
{
  "code": 123,
  "message": "A price alert for NSE:SILVERMIC25DECFUT at â¹50 is updated.",
  "s": "ok"
}
```

## Delete Price Alert

*Source: https://fyers.in/api-docs/v3/api/price-alerts/delete-price-alert/ (last updated 2026-10-14)*

This API allows you to delete a price alert.

USE CASE

Remove an alert you no longer need, such as after the price level has passed.

Details

* Delete a price alert.
* `alertId` is mandatory. Read it from [Get Price Alerts](https://fyers.in/api-docs/v3/api/price-alerts/get-price-alerts/), where results are keyed by alert ID.
* Send `alertId` and `agent` as a JSON body with the DELETE request, not in the URL.
* A successful call returns code `121` and a message saying the alert for that symbol at that value is deleted.
* To pause an alert and keep its settings, use [Enable / Disable Price Alert](https://fyers.in/api-docs/v3/api/price-alerts/enable-or-disable-price-alert/) instead of deleting it.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `alertId` | string | Mandatory. Alert ID from creation |
| `agent` | string | Client calling the API (e.g., "fyers-api") |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status. Value is `ok` on success. |
| `code` | int | Response code returned by the API (e.g., `121`). |
| `message` | string | Human-readable message describing the result of the delete operation (e.g., which alert was deleted). |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

data = {
    "alertId": "3870995",
    "agent": "fyers-api"
}

response = fyers.delete_alert(data=data)
print(response)
```

```
{
  "code": 121,
  "message": "A price alert for NSE:GOLDBEES-EQ at â¹185 is deleted.",
  "s": "ok"
}
```

## Enable / Disable Price Alert

*Source: https://fyers.in/api-docs/v3/api/price-alerts/enable-or-disable-price-alert/ (last updated 2026-10-14)*

This API allows you to switch a price alert between enabled and disabled.

USE CASE

Pause an alert and switch it on again later without losing its condition or target price.

Details

* This API allows you to change the alert state between enabled and disabled.
* Only active alerts are allowed to change state; expired or triggered alert states cannot be changed.
* The request has only `alertId` and `agent`. There is no field to choose the state: the call changes the alert between enabled and disabled.
* The success response has code `123` and says whether the alert is now enabled or disabled, so read the message to confirm the new state.
* You can also confirm it from `status` in [Get Price Alerts](https://fyers.in/api-docs/v3/api/price-alerts/get-price-alerts/): `1` is enabled, `2` is disabled and `0` is triggered.
* Send `alertId` and `agent` as a JSON body with the PUT request.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `alertId` | string | Mandatory. Alert ID from creation |
| `agent` | string | Client calling the API (e.g., "fyers-api") |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `code` | int | Response code returned by the API (e.g. `123` on success). |
| `message` | string | Human-readable message confirming the alert was enabled or disabled. |
| `s` | string | Status of the request, e.g. `"ok"` for success. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

data = {
    "alertId": "3870995",
    "agent": "fyers-api",
}

response = fyers.toggle_alert(data=data)
print(response)
```

```
// Sample Success Response
{
  "code": 123,
  "message": "Your alert has been successfully enabled",
  "s": "ok"
}

// Sample Success Response for Disabled Alert
{
  "code": 123,
  "message": "Your alert has been successfully disabled",
  "s": "ok"
}
```

## WebSocket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/ (last updated 2026-10-14)*

Redirecting to [WebSocket Overview](https://fyers.in/api-docs/v3/api/websockets/websocket-overview/)…

## Data Socket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/ (last updated 2026-10-14)*

This WebSocket allows you to stream live symbol, index and market-depth updates over a single connection.

USE CASE

Stream live prices for a watchlist, chart or strategy without polling the Quotes API.

Data streams

[Symbol UpdateWSSThis WebSocket allows you to stream live price updates for equity and option symbols.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-symbol-update/)[Indices UpdateWSSThis WebSocket allows you to stream live index values such as NIFTY 50 and NIFTY Bank.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-indices-update/)[Market Depth UpdateWSSThis WebSocket allows you to stream live five-level market depth for a symbol.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-depth-update/)[Lite ModeWSSThis WebSocket allows you to receive only the last traded price of a symbol.Samples: Python · Node · Web · C# · Java · Go · C](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-lite-mode/)

### Key points

* Every message has a `type`: `cn` for connection, `sub` for subscribe, `sf` for equity and option data, `if` for index data and `dp` for market depth.
* Need 50 levels of depth? Use the [Tick-by-Tick (TBT) Socket](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/).

### Connect and subscribe

* Your plan sets how many symbols you can subscribe to, counted across all your Data Socket connections. See [Subscription limits](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/#subscription-limits).
* Pass the access token in the format `appid:accesstoken`.
* Subscribe from the on-connect callback so symbols are requested as soon as the connection opens. In Python, call `keep_running()` afterwards to keep receiving data.
* Use FYERS symbology, for example `NSE:SBIN-EQ` for a stock or `NSE:NIFTY50-INDEX` for an index. In Python, `data_type` is `SymbolUpdate` for prices and indices, or `DepthUpdate` for market depth.
* Each message has a `type`: `cn` connection, `sub` subscribe, `sf` equity and option data, `if` index data, `dp` market depth.
* To receive only the last traded price, set `litemode=True` when you create the socket in Python, or call `mode(LiteMode)` in Node and Web JS. See [Lite Mode](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-lite-mode/).
* With auto-reconnect on, previous symbols are resubscribed automatically after a reconnect.

Full reference and samples: [Data Socket - Connect and Subscribe](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-connect-and-subscribe/).

### Unsubscribe and connection management

* In Python, call `unsubscribe` with the symbols and the same `data_type` you used to subscribe, for example `SymbolUpdate`.
* A successful unsubscribe returns `type` `unsub`, `code` 200 and `s` `ok`. The `message` text differs by SDK (Python: `Unsubscribed`; Node: `successful`).
* You can run the call from the message callback, for example to drop a symbol once your condition is met.
* For a changed symbol list, unsubscribe from the current list and subscribe again.
* Set `reconnect=True` so a dropped connection recovers on its own. `reconnect_retry` sets the retry count, up to 50.
* Handle disconnects and errors in the on-close and on-error callbacks.

Full reference and samples: [Data Socket - Unsubscribe and Connection Management](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-unsubscribe-and-connection-management/).

### Subscription limits

Plan limits

Standard plan

* Up to 100 symbols, counted per user across all connections

Prime plan

* Up to 5,000 symbols, counted per user across all connections

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

* Your plan sets how many symbols you can subscribe to.
* The limit counts all your Data Socket connections together, not each connection on its own.
* If a subscription would take you over the limit, the connection is not established.
* **Example:** your limit is 100 symbols and one connection already has 90. If you open another connection with 20 symbols, it isn’t established, because 90 + 20 = 110 is over the limit.
* **Tip:** use the latest SDK version. Older versions may not show a clear error when you reach the limit, and they miss the latest improvements. The current symbol limits need at least Python v3.1.0, Node v1.1.1 or Web JS v1.1.0. See [SDKs & Libraries](https://fyers.in/api-docs/v3/getting-started/sdks-and-libraries/).

### Best practices

* The WebSocket runs on a dedicated thread, independent of your main application thread, so primary work is not blocked by socket I/O.
* To update symbols in an already subscribed socket, unsubscribe from the existing list of symbols and then subscribe again with the updated list.
* Use the callbacks to define what happens on data updates and errors: `on_connect`, `on_message`, `on_error` and `on_close`.
* Enable automatic reconnection with `reconnect=True` when you create the socket. Set the retry count with `reconnect_retry` (up to 50). In Node, use `fyersdata.autoreconnect(trycount)`.
* Set `write_to_file=True` to save received data to a log file. It works only when callback functions are not used.
* In Node, pass a logging flag in the constructor to disable logs: `new FyersSocket("token", "logpath", true)`.

### Advanced configuration

Details

The WebSocket queue processing interval is an `Optional` setting that allows you to customize how frequently data in the subscription queue is handled. By default, this interval is set to `1` millisecond, but it can be adjusted to better suit your application's specific needs and performance preferences.

**Queue processing interval**

You can set the processing interval anywhere between `1ms` and `2000ms` (2 seconds). Call `setQueueProcessInterval` before or during an active WebSocket session.

setQueueProcessInterval

Range: `1ms` to `2000ms`
Default: `1ms`
Example: `setQueueProcessInterval(200)`

**Configuration options**

* Customizable Interval: You can set the processing interval anywhere between 1ms to 2000ms (2 seconds), giving you flexibility to optimize performance and responsiveness.
* Dynamic Adjustment: The interval setting can be changed at any time during an active WebSocket session.
* Performance Optimization: Shorter intervals (`1-10ms`) are ideal for high-frequency trading scenarios that benefit from rapid data processing, while slightly longer intervals (`100-500ms`) work well for general market data streaming.
* Resource Management: You can tune the interval based on how your application handles incoming data, helping to maintain smooth operation across different environments.

**Recommended ranges**

Use `1-10ms` when you need rapid queue processing, and `100-500ms` for general market data streaming.

**Availability**

Customizing the queue processing interval was added on 09 Jun 2025 (the Change Log lists Node Js `fyers-web-sdk-v3` `v1.4.2`). The sample on this page uses the Node SDK. Check the [Change Log](https://fyers.in/api-docs/v3/changelog/) for other SDKs.

Full reference and samples: [Data Socket - Advanced Configuration](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/advanced-configuration/).

### In this section

| Endpoint | Method | Description |
| --- | --- | --- |
| [Connect and Subscribe](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-connect-and-subscribe/) | WSS | This WebSocket allows you to connect to the Data Socket and subscribe to live updates for your symbols. |
| [Unsubscribe and Connection Management](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-unsubscribe-and-connection-management/) | WSS | This WebSocket allows you to unsubscribe from symbols and manage your Data Socket connection. |
| [Advanced Configuration](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/advanced-configuration/) | WSS | This setting lets you control how often the Node SDK processes queued Data Socket messages. |
| [Symbol Update](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-symbol-update/) | WSS | This WebSocket allows you to stream live price updates for equity and option symbols. |
| [Indices Update](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-indices-update/) | WSS | This WebSocket allows you to stream live index values such as NIFTY 50 and NIFTY Bank. |
| [Market Depth Update](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-depth-update/) | WSS | This WebSocket allows you to stream live five-level market depth for a symbol. |
| [Lite Mode](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-lite-mode/) | WSS | This WebSocket allows you to receive only the last traded price of a symbol. |

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Tick-by-Tick (TBT) Socket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/ (last updated 2026-10-14)*

This WebSocket allows you to stream 50 levels of market depth for NSE equity and NFO symbols.

USE CASE

Track order flow or run high-frequency strategies on full 50-level market depth.

### Introduction

Tick-by-tick data is the most detailed market data, recording every trade and order book update in real-time. Each tick includes the price, volume, and timestamp of individual trades, as well as changes to buy and sell orders. This granular data is crucial for analyzing market microstructure, tracking order flow, and developing high-frequency trading strategies.

### Key Points

**Supported Instruments**

Exclusively available for NFO (NSE Futures & Options) and NSE (Equity) instruments.

NFONSE Equity

**Data Formats & Transmission**

Requests are sent in JSON format. Responses are received in Protobuf format — a compact, efficient binary stream.

JSONProtobuf

**Incremental Data Updates**

The server sends only delta changes (differences) between the last packet and the current one. Apply those changes onto the previous state to reconstruct the book. Official [FYERS SDKs](https://fyers.in/api-docs/v3/getting-started/sdks-and-libraries/) handle this process automatically.

**Snapshot Data on New Subscriptions**

Packet #1 returns a complete initial snapshot of the market data at subscribe time. Subsequent packets stream real-time updates and differences that you apply to that snapshot.

Details

* The only feature on this socket today is TBT 50 Market Depth, requested with mode `depth`.
* Connect to `wss://rtsocket-api.fyers.in/versova` with the header `Authorization: appId:accessToken`. See [TBT WebSocket Connection](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/tbt-websocket-connection/).
* See [Ratelimits](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/concept-of-channels/#ratelimits) for connection and channel limits.
* Subscribing to symbols on a channel does not start the stream. Resume the channel to receive data. See [Concept of channels](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/concept-of-channels/).
* Send the string `ping` to keep the connection alive.
* Requests are JSON strings. Responses are protobuf, defined by the [.proto file](https://public.fyers.in/tbtproto/1.0.0/msg.proto).
* SDK support: TBT 50 depth was added in the Python SDK `v3.1.7` (04 Mar 2025) and the Node SDK `v1.4.1` (26 Mar 2025). NSE equity support was added on 23 Jun 2025. See the [Change Log](https://fyers.in/api-docs/v3/changelog/).

Plan limits

Standard plan

* 1 symbol, counted per user across all connections
* 1 active connection

Prime plan

* 15 symbols, counted per user across all connections
* Up to 3 active connections with 5 symbols each

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Connection

Connect to `wss://rtsocket-api.fyers.in/versova` with the header `Authorization: appId:accessToken`, subscribe with mode `depth` and a channel number, then resume that channel to start the stream.

Full reference and samples: [Tick-by-Tick (TBT) Socket - Connection (50 Market Depth)](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/tbt-websocket-connection/).

### Channels and message types

With the Tick-by-Tick (TBT) WebSocket, we are introducing the concept of channels. A channel acts as a logical grouping for different subscribed symbols, making it easier to manage data streams efficiently.

#### How Channels Work

* When subscribing to market data, you need to specify both the symbols and a channel number.
* Simply subscribing to a channel does not start the data stream—you must also resume the channel to begin receiving updates.

#### Example Usage

Let's say you organize your subscriptions as follows:

* Channel 1: All Nifty-related symbols
* Channel 2: All BankNifty-related symbols

Now, depending on what data you need, you can control the channels dynamically:

* Receive only Nifty data → Pause Channel 2 and Resume Channel 1
* Receive only BankNifty data → Pause Channel 1 and Resume Channel 2
* Receive both Nifty and BankNifty data → Resume both channels

This approach provides greater flexibility and control over market data streaming, allowing you to filter and manage real-time data efficiently.

Details

* Every subscribe and unsubscribe request carries a channel number. A connection supports 50 channels (1 to 50). See [Rate limits](#ratelimits) for symbol and connection limits by plan.
* Subscribing to a channel does not start the stream. Send a switch-channel request (`type` 2) with the channel in `resumeChannels` to start it.
* Use `pauseChannels` and `resumeChannels` in the same request to switch between groups. Both lists hold channel numbers as strings; the sample sends an empty `pauseChannels` list.
* Subscribe uses `subs` 1 and unsubscribe uses `subs` -1, both with `type` 1 and `mode` `depth`.
* Responses are protobuf. `snapshot` is true for the first full packet and false for diff packets. When `error` is true, `feeds` is empty.
* Each depth level has `price`, `qty`, `nord` and `num`. For 50 levels, `num` runs from 0 to 49.

### Request Message Types

| Type | Purpose | Encoding Format | Data Format |
| --- | --- | --- | --- |
| `Ping` | Ping message to keep connection alive | `String` | ``` "ping" ``` |
| `Subscribe` | Subscribe to the symbols for which data is required | `Json string` | ``` {   "type": 1,   "data": {     "subs": 1,     "symbols": [       "NSE:IOC25FEBFUT",       "NSE:NIFTY25FEBFUT",       "NSE:BANKNIFTY25FEBFUT",       "NSE:FINNIFTY25FEBFUT",       "NSE:TCS25FEBFUT"     ],     "mode": "depth",     "channel": "1"   } } ``` |
| `Unsubscribe` | Unsubscribe to the symbols for which data is NOT required | `Json string` | ``` {   "type": 1,   "data": {     "subs": -1,     "symbols": [       "NSE:IOC25FEBFUT",       "NSE:NIFTY25FEBFUT",       "NSE:BANKNIFTY25FEBFUT",       "NSE:FINNIFTY25FEBFUT",       "NSE:TCS25FEBFUT"     ],     "mode": "depth",     "channel": "1"   } } ``` |
| `Switch Channel` | Switch between active and paused channels | `Json string` | ``` {   "type": 2,   "data": {     "resumeChannels": ["1"],     "pauseChannels": []   } } ``` |

### Response Message Types

We use Protocol Buffers (protobuf) as the response format for all market data. The .proto file, which defines the data structure, is available at:

<https://public.fyers.in/tbtproto/1.0.0/msg.proto>

Protobuf is a widely used data format, and compilers are available to generate code in different programming languages.

#### How to install and use Protobuf

* Protobuf Compiler Installation: <https://protobuf.dev/getting-started/>
* Using Protobuf with Python: <https://protobuf.dev/reference/python/python-generated/>
* Using Protobuf with Node.js: <https://www.npmjs.com/package/protobufjs>

We have uploaded the compiled files also for python, nodejs, and golang. Download from: <https://public.fyers.in/tbtproto/1.0.0/protogencode.zip>

Copy the required file directly in your project and use it.

#### Proto versions & links

| Proto Version | Proto URL | Compiled files URL | Updated on |
| --- | --- | --- | --- |
| `1.0.0` | <https://public.fyers.in/tbtproto/1.0.0/msg.proto> | <https://public.fyers.in/tbtproto/1.0.0/protogencode.zip> | 20-02-2025 |

#### Response structures

| Type | Data Format | Field Explanation |
| --- | --- | --- |
| `SocketMessage` | * `type`: value will always be `MessageType.depth` * `feeds`: string (key) will be the symbol ticker and value will be the [`MarketFeed`](#mfeed) datastructure. This value will have the actual 50 depth values. * `snapshot`: true if it's a snapshot and false if it's a diff packet. * `msg`: will mostly contain error msgs when error = true. * `error`: true if it is an error, else false. In case of true, feeds will be nil/empty. | ``` message SocketMessage {   MessageType type = 1;   map<string, MarketFeed> feeds = 2;   bool snapshot = 3;   string msg = 4;   bool error = 5; } ``` |
| `MarketFeed` | * `depth`: [`Depth`](#depth) datastructure. This field will have the actual market depth value. * `feed_time`: time of packet in unix epoch. * `send_time`: time of packet at the time of sending from server. * `token`: fytoken for symbol. * `snapshot`: true if snapshot, false if diff packet. * `ticker`: symbol ticker. * **Note:** other fields can be ignored | ``` message MarketFeed {   Quote quote = 1;   ExtendedQuote eq = 2;   DailyQuote dq = 3;   OHLCV ohlcv = 4;   Depth depth = 5;   google.protobuf.UInt64Value feed_time = 6;   google.protobuf.UInt64Value send_time = 7;   string token = 8;   uint64 sequence_no = 9;   bool snapshot = 10;   string ticker = 11;   SymDetail symdetail = 12; } ``` |
| `Depth` | * `tbq`: total bid qty * `tsq`: total sell qty * `asks`: array of asks of type [`MarketLevel`](#mlevel) datastructure * `bids`: array of bids of type [`MarketLevel`](#mlevel) datastructure | ``` message Depth {   google.protobuf.UInt64Value tbq = 1;   google.protobuf.UInt64Value tsq = 2;   repeated MarketLevel asks = 3;   repeated MarketLevel bids = 4; } ``` |
| `MarketLevel` | * `price`: price * `qty`: qty in the market depth for the price * `nord`: number of orders in market depth for the price * `num`: depth number, for 50 depth will be between 0 and 49 [0 based array indexing] | ``` message MarketLevel {   google.protobuf.Int64Value price = 1;   google.protobuf.UInt32Value qty = 2;   google.protobuf.UInt32Value nord = 3;   google.protobuf.UInt32Value num = 4; } ``` |

### Rate limits

Following ratelimits apply for TBT Websocket. The symbol limit is per user, across all connections: Standard allows 1 symbol and Prime allows 15 symbols, which is up to 3 connections with 5 symbols each. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

| Description | Standard plan | Prime plan |
| --- | --- | --- |
| Symbols per user, across all connections [Market Depth] | 1 | 15 |
| Active Connections Per App Per User | 1 | 3 |
| Symbols per connection [Market Depth] | 1 | 5 |
| Channels per connection | 50 (1-50) | 50 (1-50) |

Full reference and samples: [Tick-by-Tick (TBT) Socket - Channels and Message Types](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/concept-of-channels/).

### In this section

| Endpoint | Method | Description |
| --- | --- | --- |
| [Connection (50 Market Depth)](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/tbt-websocket-connection/) | WSS |  |
| [Channels and Message Types](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/concept-of-channels/) | WSS |  |

## Data Socket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/ (last updated 2026-10-14)*

Redirecting to [Data Socket Overview](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/)…

## Fytoken

*Source: https://fyers.in/api-docs/v3/api/appendix/fytoken/ (last updated 2026-10-14)*

FYERS token structure: exchange, segment, expiry and exchange token fields.

| **Indicator** | **Format** | Description |
| --- | --- | --- |
| Exchange | 2 Digits | Exchange of the symbol |
| Segment | 2 Digits | Segment of the symbol |
| Expiry | 6 Digits | * Format: YYMMDD * Eg: 200827 |
| Exchange Token | From 2 upto 6 Digits | * The token assigned for the symbol by the exchange * Eg:22 |

## Exchanges

*Source: https://fyers.in/api-docs/v3/api/appendix/exchanges/ (last updated 2026-10-14)*

Numeric exchange codes for NSE, MCX and BSE.

| Possible Values | Description |
| --- | --- |
| 10 | NSE (National Stock Exchange) |
| 11 | MCX (Multi Commodity Exchange) |
| 12 | BSE (Bombay Stock Exchange) |

## Segments

*Source: https://fyers.in/api-docs/v3/api/appendix/segments/ (last updated 2026-10-14)*

Numeric segment codes for capital market, derivatives and commodities.

| Possible Values | Description |
| --- | --- |
| 10 | Capital Market |
| 11 | Equity Derivatives |
| 12 | Currency Derivatives |
| 20 | Commodity Derivatives |

## Exchange-Segment Mapping

*Source: https://fyers.in/api-docs/v3/api/appendix/available-exchange-segment-combinations/ (last updated 2026-10-14)*

Supported exchange and segment pairings with their codes.

| Exchange | Segment | Exchange Code | Segment Code |
| --- | --- | --- | --- |
| NSE | Capital Market | 10 | 10 |
| NSE | Equity Derivatives | 10 | 11 |
| NSE | Currency Derivatives | 10 | 12 |
| NSE | Commodity Derivatives | 10 | 20 |
| BSE | Capital Market | 12 | 10 |
| BSE | Equity Derivatives | 12 | 11 |
| BSE | Currency Derivatives | 12 | 12 |
| MCX | Commodity Derivatives | 11 | 20 |

## Instrument Types

*Source: https://fyers.in/api-docs/v3/api/appendix/instrument-types/ (last updated 2026-10-14)*

Instrument type codes by segment (CM, FO, CD and COM).

| Possible Values | Description |
| --- | --- |
| **CM segment** | |
| 0 | EQ (EQUITY) |
| 1 | PREFSHARES |
| 2 | DEBENTURES |
| 3 | WARRANTS |
| 4 | MISC (NSE, BSE) |
| 5 | SGB |
| 6 | G - Secs |
| 7 | T - Bills |
| 8 | MF |
| 9 | ETF |
| 10 | INDEX |
| 50 | MISC (BSE) |
| **FO segment** | |
| 11 | FUTIDX |
| 12 | FUTIVX |
| 13 | FUTSTK |
| 14 | OPTIDX |
| 15 | OPTSTK |
| **CD segment** | |
| 16 | FUTCUR |
| 17 | FUTIRT |
| 18 | FUTIRC |
| 19 | OPTCUR |
| 20 | UNDCUR |
| 21 | UNDIRC |
| 22 | UNDIRT |
| 23 | UNDIRD |
| 24 | INDEX\_CD |
| 25 | FUTIRD |
| **COM segment** | |
| 11 | FUTIDX |
| 30 | FUTCOM |
| 31 | OPTFUT |
| 32 | OPTCOM |
| 33 | FUTBAS |
| 34 | FUTBLN |
| 35 | FUTENR |
| 36 | OPTBLN |
| 37 | OPTFUT (NCOM) |

## Symbol Format

*Source: https://fyers.in/api-docs/v3/api/appendix/symbology-format/ (last updated 2026-10-14)*

Exchange, segment and instrument format rules used in FYERS identifiers. Validate symbols against the latest Symbol Master before requests.

| **Segment** | **Format** | **Examples** |
| --- | --- | --- |
| Equity | {Ex}:{Ex\_Symbol}-{Series} | NSE:SBIN-EQ, NSE:ACC-EQ,  NSE:MODIRUBBER-BE  BSE:SBIN-A, BSE:ACC-A,  BSE:MODIRUBBER-T |
| Equity Futures | {Ex}:{Ex\_UnderlyingSymbol}{YY}{MMM}FUT | NSE:NIFTY20OCTFUT,  NSE:BANKNIFTY20NOVFUT,   BSE:SENSEX23AUGFUT |
| Equity Options (Monthly Expiry) | {Ex}:{Ex\_UnderlyingSymbol}{YY}{MMM}{Strike}{Opt\_Type} | NSE:NIFTY20OCT11000CE,  NSE:BANKNIFTY20NOV25000PE ,   BSE:SENSEX23AUG60400CE |
| Equity Options (Weekly Expiry) | {Ex}:{Ex\_UnderlyingSymbol}{YY}{M}{dd}{Strike}{Opt\_Type}   [refer here for possible values of {M}](https://fyers.in/api-docs/v3/api/appendix/symbology-possible-values/) | NSE:NIFTY2010811000CE,  NSE:NIFTY20O0811000CE,  BSE:SENSEX2381161000CE,   NSE:NIFTY20D1025000CE |
| Currency Futures | {Ex}:{Ex\_CurrencyPair}{YY}{MMM}FUT | NSE:USDINR20OCTFUT,  NSE:GBPINR20NOVFUT |
| Currency Options (Monthly Expiry) | Ex}:{Ex\_CurrencyPair}{YY}{MMM}{Strike}{Opt\_Type} | NSE:USDINR20OCT75CE,  NSE:GBPINR20NOV80.5PE |
| Currency Options (Weekly Expiry) | {Ex}:{Ex\_CurrencyPair}{YY}{M}{dd}{Strike}{Opt\_Type} | NSE:USDINR20O0875CE,  NSE:GBPINR20N0580.5PE  NSE:USDINR20D1075CE |
| Commodity Futures | {Ex}:{Ex\_Commodity}{YY}{MMM}FUT | MCX:CRUDEOIL20OCTFUT,  MCX:GOLD20DECFUT |
| Commodity Options (Monthly Expiry) | {Ex}:{Ex\_Commodity}{YY}{MMM}{Strike}{Opt\_Type} | MCX:CRUDEOIL20OCT4000CE,  MCX:GOLD20DEC40000PE |

## Symbol Values

*Source: https://fyers.in/api-docs/v3/api/appendix/symbology-possible-values/ (last updated 2026-10-14)*

Placeholder variables and allowed values used in symbology formats.

| **Variable** | Description | **Possible Values** |
| --- | --- | --- |
| {Ex} | This is the exchange on which the symbol is trading | NSE, BSE, MCX |
| {YY} | This is the last 2 digits of the year | 2019 will be 19 2020 will be 2020 2021 will be 21 2022 will be 22 |
| {MMM} | For monthly expiries such as futures and options,  this value is the 3 characters of the month. The month  will always be denoted in uppercase. | JAN  FEB  MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC |
| {M} | For weekly expiries, this value represents the month  of expiry but with only 1 character. This is a mix  of numbers as well as characters. | Jan => 1   Feb => 2   Mar => 3   Apr => 4   May => 5   Jun => 6   Jul => 7   Aug => 8   Sep => 9   Oct => O (Letter)   Nov => N   Dec => D |
| {dd} | This is used in weekly expiries. This represents  the date of the month on which the contract is  going to expire. This value will always be 2 characters. | 01   06   10   25   30 |
| {Opt\_Type} | This represents whether the contract is call or put | Call Option => CE,  Put Option => PE |
| {Strike} | This is the strike price of the option contract | 11000  75.5 |

## Order Status

*Source: https://fyers.in/api-docs/v3/api/appendix/order-status/ (last updated 2026-10-14)*

Order status values returned by trading and WebSocket APIs.

| Possible Values | Description |
| --- | --- |
| 1 | Cancelled |
| 2 | Traded / Filled |
| 3 | For future use |
| 4 | Transit |
| 5 | Rejected |
| 6 | Pending |

## Holding Types

*Source: https://fyers.in/api-docs/v3/api/appendix/holding-types/ (last updated 2026-10-14)*

T1 and HLD holding type values in account responses.

| Possible Values | Description |
| --- | --- |
| T1 | The shares are purchased but not yet delivered to the demat account. |
| HLD | The shares are purchased and are available in the demat account. |

## General Socket - General Events

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-general-events/ (last updated 2026-10-14)*

This WebSocket allows you to receive price alert, EDIS and login notifications for your account.

USE CASE

Receive a notification when a price alert triggers or an EDIS update arrives.

Details

* The WebSocket API for receiving order, position, trade, price alerts, and EDIS updates is a real-time communication protocol designed to provide seamless access to various critical elements of a trading and EDIS system. This API allows traders and developers to establish a persistent, bidirectional connection with the server, enabling them to receive real-time updates on their orders, current positions, executed trades, price alerts, and EDIS status.
* Subscribe with the `edis`, `pricealerts` and `login` actions on the raw socket, or `OnGeneral` in the Python SDK (callback `on_general`).
* To receive everything in one call in the SDK, use `OnOrders,OnTrades,OnPositions,OnGeneral`. On the raw socket, list several actions in `SLIST`.
* Each message has a top-level key that tells you its type: `orders`, `trades`, `positions` or, for price alerts, `pricealerts`.
* A price alert message carries `title`, `body` and `notification_data` with fields such as `action`, `alertId`, `symbol`, `condition`, `value` and `triggeredValue`. Creating an alert sends "Alert created".

Request

```
from fyers_apiv3.FyersWebsocket import order_ws

def onTrade(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Trade Response:", message)

def onOrder(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Order Response:", message)

def onPosition(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Position Response:", message)

def onGeneral(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("General Response:", message)
def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    # data_type = "OnOrders"
    # data_type = "OnTrades"
    # data_type = "OnPositions"
    # data_type = "OnGeneral"
    data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"

    fyers.subscribe(data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "AAAAAAAA-100:YYYYYYYYYYYY"

## Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
    access_token=access_token,  # Your access token for authenticating with the Fyers API.
    write_to_file=False,        # A boolean flag indicating whether to write data to a log file or not.
    log_path="",                # The path to the log file if write_to_file is set to True (empty string means current directory).
    on_connect=onopen,          # Callback function to be executed upon successful WebSocket connection.
    on_close=onclose,           # Callback function to be executed when the WebSocket connection is closed.
    on_error=onerror,           # Callback function to handle any WebSocket errors that may occur.
    on_general=onGeneral,       # Callback function to handle general events from the WebSocket.
    on_orders=onOrder,          # Callback function to handle order-related events from the WebSocket.
    on_positions=onPosition,    # Callback function to handle position-related events from the WebSocket.
    on_trades=onTrade           # Callback function to handle trade-related events from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
    "s":"ok",
    "orders":{
        "clientId":"FY****",
        "id":"23080400089344",
        "exchOrdId":"1100000009596016",
        "qty":1,
        "filledQty":1,
        "limitPrice":7.95,
        "type":1,
        "fyToken":"101000000014366",
        "exchange":10,
        "segment":10,
        "symbol":"NSE:IDEA-EQ",
        "instrument":0,
        "offlineOrder":false,
        "orderDateTime":"04-Aug-2023 10:12:58",
        "orderValidity":"DAY",
        "productType":"INTRADAY",
        "side":-1,
        "status":90,
        "source":"W",
        "ex_sym":"IDEA",
        "description":"VODAFONE IDEA LIMITED",
        "orderNumStatus":"23080400089344:2",
        "id_fyers": "1b30241e-2819-4ec9-a3e4-69b6155cacab"
    }
  }
```

## Symbol Master File

*Source: https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-file/ (last updated 2026-10-14)*

This API allows you to download the latest Symbol Master as a CSV file for an exchange segment.

USE CASE

Look up the exact symbol, lot size or expiry of an instrument before calling a quote, history or order API.

Details

* You can get all the latest symbols of all the exchanges from the symbol master files
* There is one file per exchange segment. For example, NSE equity derivatives are in `NSE_FO.csv` and the NSE cash market is in `NSE_CM.csv`.
* Copy the `Symbol ticker` value exactly as it appears in the file when you use a symbol in other API requests. See [Symbol Format](https://fyers.in/api-docs/v3/api/appendix/symbology-format/).
* `Option type` is CE or PE for options and XX for other segments. `Expiry date` applies only to derivative contracts.
* The last three columns are reserved for future use and can be ignored.
* Fields such as `tradeStatus`, `qtyFreeze`, `upperPrice`, `lowerPrice`, `isCasEligible` and `stream` are in the [Symbol Master JSON](https://fyers.in/api-docs/v3/api/market-information/symbol-master/symbol-master-json/) file only.

| **Exchange / Segment** | **Download URL** |
| --- | --- |
| NSE – Currency Derivatives | <https://public.fyers.in/sym_details/NSE_CD.csv> |
| NSE – Equity Derivatives | <https://public.fyers.in/sym_details/NSE_FO.csv> |
| NSE – Commodity | <https://public.fyers.in/sym_details/NSE_COM.csv> |
| NSE – Capital Market | <https://public.fyers.in/sym_details/NSE_CM.csv> |
| BSE – Capital Market | <https://public.fyers.in/sym_details/BSE_CM.csv> |
| BSE - Equity Derivatives | <https://public.fyers.in/sym_details/BSE_FO.csv> |
| MCX - Commodity | <https://public.fyers.in/sym_details/MCX_COM.csv> |

#### File Headers

| Attribute | Data Type | Description |
| --- | --- | --- |
| `Fytoken` | string | * Unique token for each symbol * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `Symbol Details` | string | Name of the symbol |
| `Exchange Instrument type` | int | * Exchange instrument type * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `Minimum lot size` | int | Minimum qty multiplier |
| `Tick size` | float | Minimum price multiplier |
| `ISIN` | string | Unique ISIN provided by exchange for each symbol |
| `Trading Session` | string | Trading session provided in IST |
| `Last update date` | date | Date of last update |
| `Expiry date` | string | Date of expiry for a symbol.Applicable only for derivative contracts |
| `Symbol ticker` | string | Unique string to identify the symbol |
| `Exchange` | int | * Exchange mapping * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `Segment` | int | * Segment of the symbol * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `Scrip code` | int | Token of the Exchange |
| `Underlying symbol` | string | name of underlying symbol |
| `Underlying scrip code` | int | Scrip code of underlying symbol |
| `Strike price` | float | Strike price |
| `Option type` | string | * CE/PE - For options * XX - For other segments |
| `Underlying FyToken` | string | Unique token for the underlying symbol |
| `Reserved column` | string | Reserved for future, kindly ignore |
| `Reserved column` | int | Reserved for future, kindly ignore |
| `Reserved column` | float | Reserved for future, kindly ignore |

VIDEO LEARNING

### Video learning

[How to find stock symbols? (REST and cURL)REST and cURL · 5:01](https://www.youtube.com/watch?v=u2qEMgFWjKw&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)[Symbol format guide (Python)Python · 5:01](https://www.youtube.com/watch?v=1TjugxsnfwY&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Symbol format step by step guide (Node.js)Node.js · 5:00](https://www.youtube.com/watch?v=N7V9YH4e1Kg&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Symbol format guide (C#)C# · 5:01](https://www.youtube.com/watch?v=U95lPkxIk0U&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Symbol format guide (Java)Java · 5:01](https://www.youtube.com/watch?v=ZcPnyUVgZo0&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## General WebSocket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/ (last updated 2026-10-14)*

Redirecting to [General WebSocket Overview](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/)…

## General WebSocket - Subscribe

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-subscribe/ (last updated 2026-10-14)*

This guide explains how to subscribe to orders, trades, positions, EDIS, price alerts and login updates on the General WebSocket.

USE CASE

Choose which updates you want, such as orders, trades or positions, right after the connection opens.

Details

Once the connection is established, it is required to subscribe for required actions to get the data. To subscribe for different actions, create a message data, which would be the string format for json node.

**Json node params**

Convert the json to string and send this message to the socket to subscribe for the `action_data` mentioned.

message

`message = json.dumps({ "T": "SUB_ORD", "SLIST": action_data, "SUB_T": 1 })`

`T` Type: String
value: `SUB_ORD` (Fixed)

`action_data` Type: List/Array
Value: `orders` `trades` `positions` `edis` `pricealerts` `login`

Based on the list passed in action\_data, web\_socket data will be received.

`SUB_T` Type: Integer
Value: `1` (value 1 is for subscribing and -1 for unsubscribe)

**Sample response and socket payload**

Once subscribed successfully, for any action triggered, data will be received through the socket. If a callback function is defined, it receives that data. The response is a string in Python and an ArrayBuffer in Node. In another language, convert the payload to a string, then parse it.

Sample response

`{'code': 1605, 'message': 'Successfully subscribed', 's': 'ok'}`

Type: string

Value

{"orders":{"client\_id":"XP0001","exchange":10,"fy\_token":"10100000001628","id":"23121800292158","id\_fyers":"df013f50-6925-4e2d-ba0f-0becf1229298","instrument":0,"lot\_size":1,"offline\_flag":false,"oms\_flag":"K:1","ord\_source":"W","ord\_status":20,"ord\_type":2,"ordertag":"2:Untagged","org\_ord\_status":4,"pan":"FYxxxxxx0S","precision":2,"price\_multiplier":1,"product\_type":"CNC","qty":1,"qty\_multiplier":1,"qty\_remaining":1,"report\_type":"New Ack","segment":10,"status\_msg":"New Ack","symbol":"NSE:BECTORFOOD-EQ","symbol\_desc":"MRS BECTORS FOOD SPE LTD","symbol\_exch":"BECTORFOOD","tick\_size":0.05,"time\_epoch\_oms":1702887690,"time\_exch":"NA","time\_oms":"18-Dec-2023 13:51:30","tran\_side":1,"update\_time\_epoch\_oms":1702887690,"update\_time\_exch":"01-Jan-1970 05:30:00","validity":"DAY"},"s":"ok"}

**Note**

1. The response is a string in Python and an `arraybuffer` in Node. Check the format you receive from the websocket library for your language.
2. Convert the data to a string if it is not already a string, then parse that string to JSON. The JSON will contain one of these keys: `orders`, `trades`, or `positions`.
3. The key identifies the update type. `orders` is an order update, `trades` is a trades update, and `positions` is a positions update.
4. In the FYERS SDK, the raw socket response is parsed to keep required keys and remove unnecessary keys.

Parsed Data

```
{
  "s": "ok",
  "orders": {
    "clientId": "XP03754",
    "id": "23121800388066",
    "qty": 1,
    "remainingQuantity": 1,
    "type": 2,
    "fyToken": "10100000002705",
    "exchange": 10,
    "segment": 10,
    "symbol": "NSE:PRAJIND-EQ",
    "instrument": 0,
    "offlineOrder": false,
    "orderDateTime": "18-Dec-2023 16:33:24",
    "orderValidity": "DAY",
    "productType": "CNC",
    "side": 1,
    "status": 4,
    "source": "W",
    "ex_sym": "PRAJIND",
    "description": "PRAJ INDUSTRIES LTD",
    "orderNumStatus": "23121800388066:4"
  }
}
```

* All the keys information for orders updates are available there: [orders event keys](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-order-events/)
* All the keys information for trades updates are available there: [trades event keys](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-trade-events/)
* All the keys information for positions updates are available there: [positions event keys](https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-position-events/)

Internal mapping from raw keys to the final parsed data:

```
{
  "position_mapper": {
    "symbol": "symbol",
    "id": "id",
    "buy_avg": "buyAvg",
    "buy_qty": "buyQty",
    "buy_val": "buyVal",
    "sell_avg": "sellAvg",
    "sell_qty": "sellQty",
    "sell_val": "sellVal",
    "net_avg": "netAvg",
    "net_qty": "netQty",
    "tran_side": "side",
    "qty": "qty",
    "product_type": "productType",
    "pl_realized": "realized_profit",
    "rbirefrate": "rbiRefRate",
    "fy_token": "fyToken",
    "exchange": "exchange",
    "segment": "segment",
    "day_buy_qty": "dayBuyQty",
    "day_sell_qty": "daySellQty",
    "cf_buy_qty": "cfBuyQty",
    "cf_sell_qty": "cfSellQty",
    "qty_multiplier": "qtyMulti_com",
    "pl_total": "pl",
    "cross_curr_flag": "crossCurrency",
    "pl_unrealized": "unrealized_profit"
  },
  "order_mapper": {
    "client_id": "clientId",
    "id": "id",
    "id_parent": "parentId",
    "id_exchange": "exchOrdId",
    "qty": "qty",
    "qty_remaining": "remainingQuantity",
    "qty_filled": "filledQty",
    "price_limit": "limitPrice",
    "price_stop": "stopPrice",
    "tradedPrice": "price_traded",
    "ord_type": "type",
    "fy_token": "fyToken",
    "exchange": "exchange",
    "segment": "segment",
    "symbol": "symbol",
    "instrument": "instrument",
    "oms_msg": "message",
    "offline_flag": "offlineOrder",
    "time_oms": "orderDateTime",
    "validity": "orderValidity",
    "product_type": "productType",
    "tran_side": "side",
    "org_ord_status": "status",
    "ord_source": "source",
    "symbol_exch": "ex_sym",
    "symbol_desc": "description"
  },
  "trade_mapper": {
    "id_fill": "tradeNumber",
    "id": "orderNumber",
    "qty_traded": "tradedQty",
    "price_traded": "tradePrice",
    "traded_val": "tradeValue",
    "product_type": "productType",
    "client_id": "clientId",
    "id_exchange": "exchangeOrderNo",
    "ord_type": "orderType",
    "tran_side": "side",
    "symbol": "symbol",
    "fill_time": "orderDateTime",
    "fy_token": "fyToken",
    "exchange": "exchange",
    "segment": "segment"
  }
}
```

**Good to know**

* Subscribe only after the connection is open. You receive data only for the actions you pass in `SLIST`, and you can list several actions in one message.
* A message with `code` `1605` and `s` set to `ok` confirms the subscription.
* In the Python SDK, subscribe with `data_type` values `OnOrders`, `OnTrades`, `OnPositions` and `OnGeneral`. Join several with commas, for example `OnOrders,OnTrades`. The SDK converts them into `SLIST`.
* Price alert, EDIS and login messages are general events and arrive under their own top-level key, for example `pricealerts`. See General Events.
* The raw message and the SDK-parsed message use different key names, for example `org_ord_status` becomes `status` and `tran_side` becomes `side`. Use the key mappers above to translate between them.
* `SUB_T` `1` subscribes and `-1` unsubscribes. See General Socket - UnSubscribe.

RequestPython

```
def subscribe(self, data_type: str) -> None:
"""
Subscribes to real-time updates of a specific data type.

Args:
    data_type (str): The type of data to subscribe to, such as orders, position, or holdings.

"""

try:
    if self.__ws_object is not None:
        self.data_type = []
        for elem in data_type.split(","):
            if isinstance(self.socket_type[elem], list):
                self.data_type.extend(self.socket_type[elem])
            else:
                self.data_type.append(self.socket_type[elem])

        print("Data type is ", self.data_type)
        print("Data type is ", type(self.data_type))
        message = json.dumps(
            {"T": "SUB_ORD", "SLIST": self.data_type, "SUB_T": 1}
        )
        self.__ws_object.send(message)

except Exception as e:
    self.order_logger.error(e)
```

## Get Order by Order ID

*Source: https://fyers.in/api-docs/v3/api/trading/order-book/get-order-by-order-id/ (last updated 2026-10-14)*

This API allows you to fetch the details of a single order using its order ID.

USE CASE

Check the latest status of one order after you place, modify or cancel it.

Details

* You can query for a particular order id by passing the id in the get parameters
* Pass the order id as the `id` query parameter.
* The value to pass is the order `id` assigned by FYERS (the `id` field of an order). `exchOrdId` is a different value, the id given by the exchange.
* The response uses the same `orderBook` list and order fields as Get Orders, so one parser can handle both.
* `status` values: 1 Cancelled, 2 Traded / Filled, 4 Transit, 5 Rejected, 6 Pending, 7 Expired. For partial fills compare `filledQty` with `remainingQuantity`.
* When the order is rejected, `message` carries the error text.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `clientId` | string | The client id of the fyers user |
| `id` | string | The unique order id assigned for each order |
| `exchOrdId` | string | The order id provided by the exchange |
| `qty` | int | The original order qty |
| `remainingQuantity` | int | The remaining qty |
| `filledQty` | int | The filled qty after partial trades |
| `discloseQty` | int | Disclosed quantity |
| `limitPrice` | float | The limit price for the order |
| `stopPrice` | float | The stop price for the order |
| `tradedPrice` | float | The average traded price for the order |
| `type` | int | Order type — 1: Limit Order, 2: Market Order, 3: Stop Order (SL-M), 4: Stoplimit Order (SL-L) |
| `fyToken` | string | Fytoken is a unique identifier for every symbol |
| `exchange` | int | The exchange in which the order is placed |
| `segment` | int | The segment of the order — 10: Equity, 11: F&O, 12: Currency, 20: Commodity |
| `symbol` | string | The symbol for which the order is placed |
| `instrument` | int | Exchange instrument type |
| `message` | string | The error message, if any, for this order |
| `offlineOrder` | boolean | `false` when placed during market hours, `true` when placed as an AMO order |
| `orderDateTime` | string | The order time as DD-MMM-YYYY hh:mm:ss in IST |
| `orderValidity` | string | Order validity — `DAY` or `IOC` |
| `pan` | string | PAN of the client |
| `productType` | string | The product type of the order |
| `side` | int | Order side — `1`: Buy, `-1`: Sell |
| `status` | int | Order status code |
| `source` | string | Source from where the order was placed |
| `ex_sym` | string | The exchange symbol (trading symbol without the exchange/segment prefix) |
| `description` | string | The description of the traded symbol |
| `ch` | float | Change in LTP compared to the previous close |
| `chp` | float | Percentage change in LTP compared to the previous close |
| `lp` | float | Last traded price of the symbol |
| `slNo` | int | Used to sort the orders based on time |
| `dqQtyRem` | int | Remaining disclosed quantity |
| `orderNumStatus` | string | The order id concatenated with its status code |
| `disclosedQty` | int | Disclosed quantity |
| `orderTag` | string | Order tag provided when placing the order |
| `takeProfit` | float | Take profit price for the order |
| `stopLoss` | float | Stop loss price for the order |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

orderId = "23080444447604"
data = {"id":orderId}

response = fyers.orderbook(data=data)
print(response)
```

```
{
    "code":200,
    "message":"",
    "s":"ok",
    "orderBook": [{
              "clientId":"XXXXX86",
              "exchange":10,
              "fyToken":"101000000014366",
              "id":"23080444447604",
              "offlineOrder":false,
              "source":"W",
              "status":2,
              "type":1,
              "pan":"",
              "limitPrice":8.1,
              "productType":"INTRADAY",
              "qty":1,
              "disclosedQty":0,
              "remainingQuantity":0,
              "segment":10,
              "symbol":"NSE:IDEA-EQ",
              "description":"VODAFONE IDEA LIMITED",
              "ex_sym":"IDEA",
              "orderDateTime":"02-Aug-2023 13:01:42",
              "side":1,
              "orderValidity":"DAY",
              "stopPrice":0,
              "tradedPrice":8.1,
              "filledQty":1,
              "exchOrdId":"1100000024706527",
              "message":"",
              "ch":-0.35,
              "chp":-4.24,
              "lp":7.9,
              "orderNumStatus":"23080444447604:2",
              "slNo":1,
              "orderTag": "1:Ordertag",
              "takeProfit":0,
              "stopLoss":0
          }]
  }
```

VIDEO LEARNING

### Video learning

[Track your order status (REST and cURL)REST and cURL · 3:02](https://www.youtube.com/watch?v=dsj1QMd_LOY&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)

Go and C video tutorials: coming soon.

## Get Orders by Order Tag

*Source: https://fyers.in/api-docs/v3/api/trading/order-book/get-orders-by-order-tag/ (last updated 2026-10-14)*

This API allows you to fetch the orders placed with a specific order tag.

USE CASE

List only the orders placed by one strategy, using its order tag.

Details

* You can query for a particular orderTag by passing the orderTag in the get parameters
* Pass the tag in the GET parameters. The sample request uses `order_tag=1:Ordertag`, which includes the `1:` prefix.
* A tag you set when placing an order is stored with `1:` in front; tags generated by FYERS get `2:`. Orders without a tag show `2:Untagged`.
* Tag rules at order placement: letters and digits only (no spaces or special characters), 1 to 30 characters, and it cannot be your client ID or `Untagged`.
* The response uses the same `orderBook` fields as Get Orders, including `status`, `filledQty` and `tradedPrice`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - For each order in `orderBook`

| Attribute | Data Type | Description |
| --- | --- | --- |
| `clientId` | string | The client id of the fyers user |
| `id` | string | The unique order id assigned for each order |
| `exchOrdId` | string | The order id provided by the exchange |
| `qty` | int | The original order qty |
| `remainingQuantity` | int | The remaining qty |
| `filledQty` | int | The filled qty after partial trades |
| `discloseQty` | int | Disclosed quantity |
| `limitPrice` | float | The limit price for the order |
| `stopPrice` | float | The stop price for the order |
| `tradedPrice` | float | The average traded price for the order |
| `type` | int | * The order type, e.g. * 1 => Limit Order * 2 => Market Order * 3 => Stop Order (SL-M) * 4 => Stoplimit Order (SL-L) |
| `fyToken` | string | Fytoken is a unique identifier for every symbol |
| `exchange` | int | The exchange in which the order is placed |
| `segment` | int | * The segment in which the order is placed, e.g. * 10 => Equity * 11 => F&O * 12 => Currency * 20 => Commodity |
| `symbol` | string | The symbol for which the order is placed. Eg: NSE:IDEA-EQ |
| `instrument` | int | Exchange instrument type |
| `message` | string | The error messages are shown here |
| `offlineOrder` | boolean | False when market is open, True when placed as an AMO order |
| `orderDateTime` | string | The order time as per DD-MMM-YYYY hh:mm:ss in IST |
| `orderValidity` | string | DAY or IOC |
| `pan` | string | PAN of the client |
| `productType` | string | The product type of the order, e.g. CNC |
| `side` | int | * The order side, e.g. * 1 => Buy * -1 => Sell |
| `status` | int | The order status code, e.g. 2 => Traded / Filled |
| `source` | string | Source from where the order was placed, e.g. W (Web) |
| `ex_sym` | string | The short exchange symbol/ticker name, e.g. IDEA |
| `description` | string | The full descriptive name of the traded instrument |
| `ch` | float | The absolute change in the last traded price |
| `chp` | float | The percentage change in the last traded price |
| `lp` | float | The last traded price (LTP) of the symbol |
| `slNo` | int | Used to sort the orders based on the time |
| `dqQtyRem` | int | The remaining disclosed quantity |
| `orderNumStatus` | string | Concatenation of the order id and status code, e.g. `23030900015105:2` |
| `disclosedQty` | int | Disclosed quantity |
| `orderTag` | string | The order tag provided when placing the order, prefixed with `1:` for user-provided tags or `2:` for internally generated tags |
| `takeProfit` | float | Take profit price for the order |
| `stopLoss` | float | Stop loss price for the order |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
Curl Request Method
curl -H "Authorization:app_id:access_token"  https://api-t1.fyers.in/api/v3/orders??order_tag=1:Ordertag
```

```
{
  "s": "ok",
  "code": 200,
  "message": "",
  "orderBook": [{
      "clientId": "X******",
      "id": "23030900015105",
      "exchOrdId": "1100000001089341",
      "qty": 1,
      "remainingQuantity": 0,
      "filledQty": 1,
      "discloseQty": 0,
      "limitPrice": 6.95,
      "stopPrice": 0,
      "tradedPrice": 6.95,
      "type": 1,
      "fyToken": "101000000014366",
      "exchange": 10,
      "segment": 10,
      "symbol": "NSE:IDEA-EQ",
      "instrument": 0,
      "message": "",
      "offlineOrder": false,
      "orderDateTime": "09-Mar-2023 09:34:38",
      "orderValidity": "DAY",
      "pan": "",
      "productType": "CNC",
      "side": -1,
      "status": 2,
      "source": "W",
      "ex_sym": "IDEA",
      "description": "VODAFONE IDEA LIMITED",
      "ch": -0.1,
      "chp": -1.44,
      "lp": 6.85,
      "slNo": 1,
      "dqQtyRem": 0,
      "orderNumStatus": "23030900015105:2",
      "disclosedQty": 0,
      "orderTag": "1:Ordertag",
      "takeProfit":0,
      "stopLoss":0
  }]
}
```

VIDEO LEARNING

### Video learning

[Track your order status (REST and cURL)REST and cURL · 3:02](https://www.youtube.com/watch?v=dsj1QMd_LOY&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)

Go and C video tutorials: coming soon.

## Get Trades by Order Tag

*Source: https://fyers.in/api-docs/v3/api/trading/trade-book/get-trades-by-order-tag/ (last updated 2026-10-14)*

This API allows you to fetch the trades executed for orders placed with a specific order tag.

USE CASE

Review the fills of a single strategy, using its order tag.

Details

* You can query for a particular orderTag by passing the orderTag in the get parameters.
* Pass the tag in the GET parameters. The sample request uses `order_tag=1:Ordertag`, which includes the `1:` prefix.
* A tag you set when placing an order is stored with `1:` in front; tags generated by FYERS get `2:`. Trades without a tag show `1:Untagged`.
* Tag rules at order placement: letters and digits only (no spaces or special characters), 1 to 30 characters, and it cannot be your client ID or `Untagged`.
* The response uses the same trade fields as Get Trades, such as `tradePrice`, `tradedQty` and `orderNumber`.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Trading symbol of the instrument, e.g. `NSE:SBIN-EQ` |
| `row` | int | Unique value used to sort the trades |
| `orderDateTime` | string | Time the trade occurred, in `DD-MMM-YYYY hh:mm:ss` format (IST) |
| `orderNumber` | string | The order ID for which the trade occurred |
| `exchangeOrderNo` | string | The order number provided by the exchange |
| `tradeNumber` | string | The trade number generated by the exchange |
| `tradePrice` | float | The traded price |
| `tradeValue` | float | The total traded value |
| `tradedQty` | int | The total traded quantity |
| `orderType` | int | The type of order that generated the trade (e.g. Limit, Market) |
| `side` | int | * 1 => Buy * -1 => Sell |
| `productType` | string | The product type in which the order was placed, e.g. CNC or INTRADAY |
| `segment` | int | The segment in which the order was placed |
| `exchange` | int | The exchange in which the order was placed |
| `fyToken` | string | Fytoken — a unique identifier for the symbol |
| `clientId` | string | The FYERS client ID of the account the trade belongs to |
| `orderTag` | string | The order tag matched by the `order_tag` filter; a `1:` prefix denotes a user-supplied tag and a `2:` prefix denotes a tag generated internally by FYERS (default is `1:Untagged`) |

Python is not available for this example. Showing cURL instead.

Request

```
Curl Request Method
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/tradebook?order_tag=1:Ordertag
```

```
{
  "s": "ok",
  "code": 200,
  "message": "",
  "tradeBook":
              [{
                "clientId":"FXXXXX",
                "orderDateTime":"07-Aug-2020 13:51:12",
                "orderNumber":"120080789075",
                "exchangeOrderNo": "1200000009204725",
                "exchange":10,
                "side":1,
                "segment":10,
                "orderType":2,
                "fyToken":"101000000010666",
                "productType":"CNC",
                "tradedQty":10,
                "tradePrice":32.7,
                "tradeValue":327.0,
                "tradeNumber":"52605023",
                "row":52605023,
                "symbol":"NSE:PNB-EQ",
                "orderTag": "1:Ordertag"
              },
              {
                "clientId":"FXXXXX",
                "orderDateTime":"07-Aug-2020 13:48:12",
                "orderNumber":"120080789139",
                "exchangeOrderNo": "1000000012031528",
                "exchange":10,
                "side":1,
                "segment":10,
                "orderType":2,
                "fyToken":"101000000010454",
                "productType":"CNC",
                "tradedQty":19,
                "tradePrice":14.1,
                "tradeValue":267.9,
                "tradeNumber":"3281523",
                "row":3281523,
                "symbol":"NSE:CENTRUM-EQ",
                "orderTag": "1:Ordertag"
              },
              {
                "clientId":"FXXXXX1",
                "orderDateTime":"07-Aug-2020 13:47:22",
                "orderNumber":"120080797993",
                "exchangeOrderNo": "1100000008047027",
                "exchange":10,
                "side":1,
                "segment":10,
                "orderType":2,
                "fyToken":"101000000018783",
                "productType":"CNC",
                "tradedQty":4,
                "tradePrice":115.5,
                "tradeValue":462.0,
                "tradeNumber":"27945307",
                "row":27945307,
                "symbol":"NSE:IDFNIFTYET-EQ",
                "orderTag": "1:Ordertag"
              }]
}
```

VIDEO LEARNING

### Video learning

[How to check trade history? (REST and cURL)REST and cURL · 5:27](https://www.youtube.com/watch?v=mVp4kUapEMA&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)

Go and C video tutorials: coming soon.

## Create Webhook

*Source: https://fyers.in/api-docs/v3/api/trading/webhooks/create-webhook/ (last updated 2026-10-14)*

USE CASE

Register a URL and choose the order statuses you want pushed to your server.

### Things to know

* Log in to the [API Dashboard](https://fyers.in/web/api-dashboard/user-apps).
* When creating or editing a Trading App or Non-Trading App, go to the **Webhook details** section and click **Add**. In the Add Webhook pop-up, enter the webhook URL and secret, then select the order status updates you want to receive: Pending, Rejected, Cancelled and Traded. Click **Save** to add the webhook.
* After entering the required details, click **Create App** and accept the terms and conditions.
* You can add more than one webhook to an app.
* ![Create webhooks](https://assets.fyers.in/myapi-dashboard/docs/create-webhooks.png)
* The app must be activated by logging in before order data reaches the webhook URL. See [Activate App](https://fyers.in/api-docs/v3/api/trading/webhooks/activate-app/).

Postbacks are configured while creating your app:

1. Set a webhook URL, a webhook secret, and the webhook preference (Cancel, Rejected, Pending, Traded). You can add multiple webhooks.
2. Finish creating the app by accepting the terms and conditions.

## Activate App

*Source: https://fyers.in/api-docs/v3/api/trading/webhooks/activate-app/ (last updated 2026-10-14)*

USE CASE

Log in through a new app once, so order updates start reaching your webhook.

### Things to know

* Activation means completing the [Authentication & Login](https://fyers.in/api-docs/v3/api/authentication/) flow for the app.
* Order data is delivered to the webhook URL only after that login succeeds.

After successful creation of the App, you need to activate the App by following the [Authentication & Login](https://fyers.in/api-docs/v3/api/authentication/) mechanism. After successfully logging in via the App, you will be able to get the order data over the webhook URL.

## Webhook Response

*Source: https://fyers.in/api-docs/v3/api/trading/webhooks/webhook-response/ (last updated 2026-10-14)*

USE CASE

Read the status, filled quantity and error message of an order from the posted payload.

### Things to know

* The JSON payload is posted as a raw HTTP POST body. Your server has to read the raw body.
* `status` values: 1 Cancelled, 2 Traded / Filled, 4 Transit, 5 Rejected, 6 Pending, 7 Expired. Value 3 is not used.
* `filledQty` and `remainingQuantity` show how much of the order has traded, which covers partial fills. `tradedPrice` is the average traded price.
* `message` carries the error text, for example when an order is rejected.
* `offlineOrder` is true when the order was placed as an AMO order.
* Reply with HTTP status 200 to every post. Other responses or failed posts can get the URL blacklisted. See [Blacklisting](https://fyers.in/api-docs/v3/api/trading/webhooks/blacklisting/).

The JSON payload is posted as a raw HTTP POST body. You will have to read the raw body.

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| id | string | The unique order ID assigned for each order |
| exchOrdId | string | The order ID provided by the exchange |
| symbol | string | The symbol for which the order is placed |
| qty | int | The original order quantity |
| remainingQuantity | int | The remaining quantity |
| filledQty | int | The filled quantity after partial trades |
| status | int | 1 => Canceled, 2 => Traded / Filled, 3 => (Not used currently), 4 => Transit, 5 => Rejected, 6 => Pending, 7 => Expired. |
| message | string | The error messages are shown here |
| segment | int | 10 (Equity), 11 (F&O), 12 (Currency), 20 (Commodity). [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| limitPrice | float | The limit price for the order |
| stopPrice | float | The stop price for the order |
| productType | string | The product type |
| type | int | 1 => Limit Order, 2 => Market Order, 3 => Stop Order (SL-M), 4 => Stop Limit Order (SL-L). [View Details](https://fyers.in/api-docs/v3/api/appendix/order-types/) |
| side | int | Disclosed quantity: 1 => Buy, -1 => Sell. [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| disclosedQty | int | Disclosed quantity |
| dqQtyRem | int | Remaining disclosed quantity |
| orderValidity | string | DAY, IOC |
| orderDateTime | string | The datetime object here will be in epoch timestamp |
| tradedPrice | float | The average traded price for the order |
| source | string | Source from where the order was placed. [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sources/) |
| fytoken | string | Fytoken is a unique identifier for every symbol. [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| offlineOrder | boolean | False => When the market is open, True => When placing AMO order |
| pan | string | PAN of the client |
| clientId | string | The client ID of the Fyers user |
| exchange | int | The exchange in which the order is placed. [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| instrument | string | Exchange instrument type. [View Details](https://fyers.in/api-docs/v3/api/appendix/instrument-types/) |

#### Sample response

```
{
  "orderDateTime": "18-Jul-2023 11:44:29",
  "id": "23071800238607",
  "exchOrdId": "2500000061319029",
  "side": -1,
  "segment": 11,
  "instrument": 15,
  "productType": "MARGIN",
  "status": 2,
  "qty": 5400,
  "remainingQuantity": 0,
  "filledQty": 5400,
  "limitPrice": 2.15,
  "stopPrice": 0,
  "type": 2,
  "discloseQty": 0,
  "dqQtyRem": 0,
  "orderValidity": "DAY",
  "source": "M",
  "fyToken": "101123072754619",
  "offlineOrder": false,
  "message": "Completed",
  "orderNumStatus": "23071800238607:2",
  "tradedPrice": 2.15,
  "exchange": 10,
  "pan": "",
  "clientId": "xxxx",
  "symbol": "NSE:ABCAPITAL23JUL190CE"
}
```

## Learn Algo Trading with FYERS

*Source: https://fyers.in/api-docs/v3/learning/*

Learn algo trading from experienced algo traders and mentors who have built trading systems using FYERS API. Learn from scratch — where to start, how to build and test a strategy, and how to turn your trading ideas into automated trading systems.

Choose a course based on your interest and experience. Explore our paid and free courses, along with FYERS YouTube playlists and tutorials, to learn algo trading, understand FYERS API, and build your own trading systems.

### Paid courses

Explore courses and partner programs to build with FYERS APIs.

Featured courses

[![Udemy](https://fyers.in/api-docs/v3/learning/udemy.svg)

UdemyPaid course

#### Complete Algorithmic Trading on FYERS Platform

A structured FYERS API course for guided learning and practical implementation.

View course →](https://www.udemy.com/course/complete-algorithmic-trading-on-fyers-platform/)

Learning partners

![IIQF](https://fyers.in/api-docs/v3/learning/iiqf.svg)

#### IIQF

Coming soon

## Change Log

*Source: https://fyers.in/api-docs/v3/changelog/ (last updated 18 NOV 202)*

Release history for FYERS APIv3 documentation and official SDKs. Filter by year, search keywords, or show SDK version bumps only.

[**What's new on FYERS**Product features and platform updates for the FYERS app and web — separate from this API changelog.Visit What's New](https://fyers.in/whats-new)

All years2026202520242023UndatedSDK releases only

Showing **62** of 62 entries

| Date | Changes |
| --- | --- |
| 18 NOV 2026 | * [GTT Single](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-single-order/) and [GTT OCO](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-oco-order/) orders now support Market orders through the `type` field in each leg (`1`: Limit, `2`: Market). The two legs of an OCO order can use different order types. * [Modify GTT Order](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/modify-gtt-order/) now accepts `type` for each leg. If `type` is not provided, the leg is modified as a Limit order. * [GTT Order Book](https://fyers.in/api-docs/v3/api/trading/order-placement/gtt-orders/gtt-order-book/) now returns `ord_type` and `ord_type2`, the order type of each leg. * Market GTT orders are not allowed for BFO symbols. |
| 30 OCT 2026 | Published the [Screeners](https://fyers.in/api-docs/v3/api/market-data/screeners/) APIs under `/api/v3/screeners` — Config, Standard Screen, Candlestick Screeners and Technical Screeners.  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.2.1` | | Node | `fyers-api-v3` | `v2.4.1` | | Web Js | `fyers-web-sdk-v3` | `v2.2.1` | | Java | `fyers-api-v3` | `v2.1.1` | | C# | `fyers-api-v3` | `v1.6.0` | | Go | `fyers-api-v3` | `v1.7.0` | | C | `fyers-api-v3` | `v1.5.0` | |
| 16 OCT 2026 | * Added the [API Prime Benefits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/) section, comparing Prime and Standard rate limits (for Data APIs and for Transaction & User Info APIs) and feature access. * Introduced the [new API docs](https://fyers.in/api-docs/introduction/) at `https://fyers.in/api-docs/`. * Added the [Quotes (POST)](https://fyers.in/api-docs/v3/api/market-data/quotes/#new) API, which returns quotes for up to 1,000 symbols per request for Prime users and 50 for Standard users. |
| 01 OCT 2026 | * [Get Expired F&O Data](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-fo-data/) API now supports Greeks via the `include_greeks` parameter. * [Quotes](https://fyers.in/api-docs/v3/api/market-data/quotes/) API now provides CAS data points: `imbalance`, `mkt_imbalance`, `reference_price` and `indicative_price`. |
| 06 SEP 2026 | * Added Expired F&O Contracts Data APIs under `/data/history/fno/expired` under the new [Expired F&O Contracts Data](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/) section — Get Expiry Dates, Get Expired Contracts, and Get Expired F&O Data endpoints. * Documented the [Futures Chain](https://fyers.in/api-docs/v3/api/market-data/futures-chain/) API under `/data/futures-chain`, which lists the available futures contracts for an underlying symbol.  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.17` | | Node | `fyers-api-v3` | `v2.2.0` | | Web Js | `fyers-web-sdk-v3` | `v2.1.0` | | Java | `fyers-api-v3` | `v2.1.0` | | C# | `fyers-api-v3` | `v1.5.0` | | Go | `fyers-api-v3` | `v1.6.0` | | C | `fyers-api-v3` | `v1.4.0` | |
| 13 AUG 2026 | Added **Market Status Definitions** table under [Market Status](https://fyers.in/api-docs/v3/api/market-information/market-status/), describing each `status` value including the Closing Auction Session (CAS) states: `CTS_CLOSE`, `CAS_START`, `CAS_MKT_ORD_RESTRICT` and `CAS_END`. CAS statuses apply only to CAS-eligible symbols, identified by the `isCasEligible` field in the Symbol Master JSON. |
| 07 AUG 2026 | Added Manage Positions option to cancel Stop Loss and Take Profit on an open position via `PATCH /api/v3/positions` by passing `null` for the applicable parameter(s). |
| 02 AUG 2026 | CO & BO Deprecated ,Added modify the Stop Loss and Take Profit for an existing open position.  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.15` | | Node | `fyers-api-v3` | `v2.1.0` | | Web Js | `fyers-web-sdk-v3` | `v2.0.0` | | Java | `fyers-api-v3` | `v2.0.0` | | Go | `fyers-api-v3` | `v1.5.0` | | C | `fyers-api-v3` | `v1.3.0` | |
| 05 JUN 2026 | Added APIv3 support for Charges, Tax Profit & Loss, Ledger and Realised Profit & Loss history under Reports API.  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.13` | | Node | `fyers-api-v3` | `v1.9.0` | | Web Js | `fyers-web-sdk-v3` | `v1.8.0` | | Java | `fyers-api-v3` | `v1.8.0` | | Go | `fyers-api-v3` | `v1.3.0` | | C | `fyers-api-v3` | `v1.3.0` | |
| 20 APR 2026 | Added Support for Smart Orders in APIv3. |
| 13 APR 2026 | Added Greeks param for sdk under option chain.  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.12` | | Node | `fyers-api-v3` | `v1.8.0` | | Web Js | `fyers-web-sdk-v3` | `v1.7.0` | | Java | `fyers-api-v3` | `v1.7.0` | | Go | `fyers-api-v3` | `v1.2.0` | | C | `fyers-api-v3` | `v1.2.0` | | C# | `fyers-api-v3` | `v1.1.2` | |
| 10 APR 2026 | Added Order Tagging support for GTT Orders |
| 09 APR 2026 | Added APIv3 support for Greeks under option chain |
| 31 MAR 2026 | Documented **async order placement** endpoints: `/api/v3/orders/async` and `/api/v3/multi-order/async` (queued execution, 10 OPS dispatch, immediate response returns `id_fyers` only; outcomes via order WebSocket and GET APIs). `/sync` order APIs remain as documented. See [Async Order Placement](https://fyers.in/api-docs/v3/api/trading/order-placement/async/). |
| 27 MAR 2026 | Added support for Week and Month resolution in History API. |
| 09 MAR 2026 | Added regulatory changes in documentation for APIv3. |
| 04 MAR 2026 | Added APIv3 support for Order History and Trade History.  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.11` | | Node | `fyers-api-v3` | `v1.7.0` | | Web Js | `fyers-web-sdk-v3` | `v1.6.0` | | Java | `fyers-api-v3` | `v1.6.0` | | Go | `fyers-api-v3` | `v1.1.0` | | C | `fyers-api-v3` | `v1.1.0` | |
| 28 FEB 2026 | Added APIv3 support for C.  | Lang | Package | Ver | | --- | --- | --- | | C | `fyers-api-v3` | `v1.0.0` | |
| 21 JAN 2026 | **Version:** All Added Price Alerts feature. |
| 04 DEC 2025 | Added the order slicing feature for single-order placements. |
| 17 NOV 2025 | Added id\_fyers key in the OrderBook response. |
| 09 Sep 2025 | Masked PII (Personally Identifiable Information) in Profile API response. Fields masked: Mobile number, Email ID, PAN number. |
| 22 Aug 2025 | * Fixed missing symbol key in market data indices update. * Updated WebSocket reconnection logic. * Fixed rate limiting issue caused by internet connectivity checks.  | Lang | Package | Ver | | --- | --- | --- | | Java | `fyers-api-v3` | `v1.3.0` | |
| 23 Jun 2025 | Added support for NSE equity segment on TBT (Tick by tick) Socket. [Click here for reference](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/) |
| 09 Jun 2025 | Added optional support for customizing WebSocket queue processing interval  | Lang | Package | Ver | | --- | --- | --- | | Node Js | `fyers-web-sdk-v3` | `v1.4.2` | |
| 16 Apr 2025 | Added support for logout API in Web Js SDK and Java SDK  | Lang | Package | Ver | | --- | --- | --- | | Web Js | `fyers-web-sdk-v3` | `v1.3.1` | | Java | `fyers-apiv3` | `v1.2.0` | |
| 26 Mar 2025 | * Added support for TBT 50 depth in Node SDK * Added support for logout API in node SDK  | Lang | Package | Ver | | --- | --- | --- | | Node | `fyers-api-v3` | `v1.4.1` | |
| 20 Mar 2025 | Updated Instrument Types |
| 04 Mar 2025 | * Added support for TBT 50 depth in python SDK * Added [sample code](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/tbt-websocket-connection/) for TBT 50 depth * Added support for logout API in python SDK  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.7` | |
| 20 Feb 2025 | [TBT 50 depth](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/) websocket documentation |
| 13 Feb 2025 | Added keys for DDPI and MTF Activation Status in Profile API |
| 05 Feb 2025 | * Introduced Logout API [Logout API reference](https://fyers.in/api-docs/v3/api/account/logout/) * Added MTF and GTT Order Placement  | Lang | Package | Ver | | --- | --- | --- | | Node | `fyers-api-v3` | `v1.4.0` | | Web Js | `fyers-web-sdk-v3` | `v1.3.0` | | CDN | `fyers-web-sdk-v3` | `v1.3.0` | | Java | `fyers-apiv3` | `v1.1.0` | |
| 01 Feb 2025 | Added MTF and GTT Order Placement  | Lang | Package | Ver | | --- | --- | --- | | C# | `fyers-apiv3` | `v1.0.6` | |
| 30 Jan 2025 | Added MTF and GTT Order Placement  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.5` | |
| 20 Jan 2025 | Introduced MTF and GTT Order Placement APIs |
| 13 Jan 2025 | Added key for DisclosedQty in modify order  | Lang | Package | Ver | | --- | --- | --- | | C# | `fyers-api-v3` | `v1.0.5` | | Java | `fyers-apiv3` | `v1.0.2` | |
| 27 Dec 2024 | Improved compatibility with symbols containing special characters  | Lang | Package | Ver | | --- | --- | --- | | Node | `fyers-api-v3` | `v1.3.3` | | Web Js | `fyers-web-sdk-v3` | `v1.2.4` | | CDN | `fyers-web-sdk-v3` | `v1.2.1` | |
| 26 Dec 2024 | Fixed Data Socket Issue for Sensex Symbol  | Lang | Package | Ver | | --- | --- | --- | | C# | `fyers-api-v3` | `v1.0.4` | | Java | `fyers-apiv3` | `v1.0.1` | |
| 10 Oct 2024 | Minor bug fixes within websocket package  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.4` | |
| 09 Oct 2024 | Added Multileg order feature  | Lang | Package | Ver | | --- | --- | --- | | C# | `fyers-api-v3` | `v1.0.3` | |
| 03 Oct 2024 | Introduced API V3 Java SDK  | Lang | Package | Ver | | --- | --- | --- | | Java | `fyers-api-v3` | `v1.0.0` | |
| 17 Sep 2024 | Added Option Chain API  | Lang | Package | Ver | | --- | --- | --- | | C# | `fyers-api-v3` | `v1.0.2` | |
| 22 Aug 2024 | **Version:** All   * Increased API rate limit from 10,000 requests per day to 1 Lakh requests per day (10x increase from the previous daily rate limit), view the [current rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/). **Note:** There are no change in per-second and per-minute rate limits * Updated API document with API Error Codes [API error codes](https://fyers.in/api-docs/v3/api/appendix/common-api-error-codes/) |
| 03 Jul 2024 | Added Multileg order feature  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.2` | | Node | `fyers-api-v3` | `v1.3.0` | |
| 12 Jun 2024 | Optimized package with bug fixes  | Lang | Package | Ver | | --- | --- | --- | | C# | `fyers-api-v3` | `v1.0.1` | |
| 07 Jun 2024 | Optimized package  | Lang | Package | Ver | | --- | --- | --- | | Web Js | `fyers-web-sdk-v3` | `v1.2.2` | |
| 30 May 2024 | **Version:** All Added description for fyers 201 code(order placement) |
| 29 May 2024 | Improvised logging  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.0` | |
| 14 May 2024 | Improvised in internal package import logic  | Lang | Package | Ver | | --- | --- | --- | | Web Js | `fyers-web-sdk-v3` | `v1.2.1` | |
| 25 Apr 2024 | Introduced API V3 C# SDK  | Lang | Package | Ver | | --- | --- | --- | | C# | `fyers-api-v3` | `v1.0.0` | |
| 23 Apr 2024 | Added option chain API  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.0` | | Node | `fyers-api-v3` | `v1.2.0` | | Web Js | `fyers-web-sdk-v3` | `v1.2.0` | | CDN | `fyers-web-sdk-v3` | `v1.2.0` | |
| 22 Mar 2024 | **Version:** All Added 2 new reserved columns in Symbol Master CSV files, will be used for future development, kindly ignore |
| 04 Apr 2024 | **Version:** All Deprecated **cmd** attribute in Quotes API response [read the notice-board announcement](https://fyers.in/notice-board/action-required-cmd-field-in-api-to-be-deprecated) for more details |
| 26 Mar 2024 | * **Symbol Subscription Enhancement**   + Optimised symbol subscription   + Increased symbol subscription limit from **200** to **5000** in a single connection  | Lang | Package | Ver | | --- | --- | --- | | Python | `fyers-apiv3` | `v3.1.0` | | Node | `fyers-api-v3` | `v1.1.1` | | Web Js | `fyers-web-sdk-v3` | `v1.1.0` | | CDN | `fyers-web-sdk-v3` | `v1.1.0` | |
| 22 Mar 2024 | **Version:** All Added 2 new reserved columns in Symbol Master CSV files, will be used for future development, kindly ignore |
| 15 Mar 2024 | **Version:** fyers-web-sdk-v3 - v1.0.0 Introduced Browser Compatible SDK. |
| 14 Mar 2024 | **Version:** Python SDK - v3.0.9   * **Logging Enhancement**   + In the FyersModel class, the log\_level parameter has been introduced to control the verbosity of logging. By default, the logging level is set to 'ERROR',only errors will be logged. However, users have the flexibility to set the log\_level parameter to 'DEBUG', allowing for more detailed logging. Logs are written **fyersApi.log** file.   + Added **fyersRequest.log** file where requested endpoints and status code are logged (can be used to analyse the API requests made). * **Compatible with Python v3.12**   + Updated aiohttp to version 3.9.3 (latest release) to ensure compatibility with Python 3.12. |
| 13 Mar 2024 | **Version:** All Added support for seconds candles |
| 05 Dec 2023 | **Version:** All   * **Order Placement**   + OrderTagging functionality added. * **Orderbook**   + Orderbook returns Ordertag in response   + Query orderbook by Ordertag * **Tradebook**   + Orderbook returns Ordertag in response   + Query tradebook by Ordertag |
| 18 Aug 2023 | **Version:** API Version 3  **New Features and Updates**   * **Performance**   + Fast Order Placement: Achieving placement within < 75 ms   + Fast get APIs: Achieving response times within < 75 ms * **New Data Socket:**   + Improved tick update speed, ensuring swift and efficient market data updates.   + Introducing Lite mode for targeted last traded price (LTP) change updates.   + SymbolUpdate: Real-time symbol-specific updates for instant parameter changes.   + DepthUpdate: Real-time market depth changes for selected symbols.   + Increased subscription capacity, accommodating tracking of 200 symbols.   + Strengthened error handling callbacks for seamless issue resolution. * **New Order Socket**   + Real-time updates for orders   + Real-time updates for positions   + Real-time updates for trades   + Real-time updates for eDIS   + Real-time updates for price alerts   + Improved error handling callbacks * **URL update for various APIs**   + Enhanced History API available at: <https://api-t1.fyers.in/data/history>   + New Market Status API introduced at: <https://api-t1.fyers.in/data/marketStatus>   + Enhanced Quotes API available at: <https://api-t1.fyers.in/data/quotes>   + Enhanced Market Depth API available at: <https://api-t1.fyers.in/data/depth> * **Documentation and Sample Code Updates**   + Added sample code for NodeJS and Python in the documentation   + Updated sample code in the GitHub repository for both Python and NodeJS |
| 04 May 2023 | **Version:** All   * **Quotes**   + URL updated to **https://api-t1.fyers.in/data/quotes?symbols=NSE:SBIN-EQ**   + ip updated to lp   + Removed fyToken & prev\_close\_price from response   + Text updation: "Symbols" changed to "symbol" * **Market Depth**   + URL updated to **https://api-t1.fyers.in/data/depth?symbol=NSE:SBIN-EQ&ohlcv\_flag=1**   + itt updated to ltt   + Removed tick\_Size & oi from response |
| — | **Version:** API Version 2   * **App Related**   + Introduced common apps for third party app developers   + Different authentication methods such as OAuth2, PKCE and OIDC   + Permission templates at the time of app creation * **Authentication**   + Authentication flow has been changed to improve security   + Authorization header value has been changed * **Order placement**   + Multi order placement   + Multi order modification   + Multi order cancellation * **Other**   + Market status API * **Realtime Data Rest API**   + Quotes api to get realtime data for list of symbols via Rest API   + Market Depth API to get bid ask data for a particular symbol * **Websocket**   + Get realtime price info for a list of symbols   + Get realtime market depth for a particular symbol   + Get realtime order updates   + Background and Foreground process enabled for websocket.   + User can subscribe to only Index symbols   + Added sample scripts to get started with websocket   + Object initialization method changed a bit (instead of fyers\_api.websocket it is fyers\_api.Websocket)   + No More Pong received message on the console. The data will be continuous * **Postback (Webhooks)**   + Get realtime order updates via postbacks / webhooks * **Transactions**   + eDIS flow |

## Data Socket - Connect and Subscribe

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-connect-and-subscribe/ (last updated 2026-10-14)*

This WebSocket allows you to connect to the Data Socket and subscribe to live updates for your symbols.

USE CASE

Subscribe to the stocks on your watchlist and receive every price update in your callback.

Details

* The Data Socket provides real-time market data with low latency over a persistent, bidirectional connection, such as symbol updates and depth updates.
* Subscription limits and best practices (single instance, thread handling, updating symbols, callbacks, auto-reconnect, reconnect retry and logging) are on the [Data Socket Overview](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/).
* Your plan sets how many symbols you can subscribe to, counted across all your Data Socket connections. See [Subscription limits](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/#subscription-limits).
* Pass the access token in the format `appid:accesstoken`.
* Subscribe from the on-connect callback so symbols are requested as soon as the connection opens. In Python, call `keep_running()` afterwards to keep receiving data.
* Use FYERS symbology, for example `NSE:SBIN-EQ` for a stock or `NSE:NIFTY50-INDEX` for an index. In Python, `data_type` is `SymbolUpdate` for prices and indices, or `DepthUpdate` for market depth.
* Each message has a `type`: `cn` connection, `sub` subscribe, `sf` equity and option data, `if` index data, `dp` market depth.
* To receive only the last traded price, set `litemode=True` when you create the socket in Python, or call `mode(LiteMode)` in Node and Web JS. See [Lite Mode](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-lite-mode/).
* With auto-reconnect on, previous symbols are resubscribed automatically after a reconnect.

Plan limits

Standard plan

* Up to 100 symbols, counted per user across all connections

Prime plan

* Up to 5,000 symbols, counted per user across all connections

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

Request

```
from fyers_apiv3.FyersWebsocket import data_ws

fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage,            # Callback function to handle incoming messages from the WebSocket.
    reconnect_retry=10               # Number of times reconnection will be attepmted in case
)
```

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Data Socket - Symbol Update

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-symbol-update/ (last updated 2026-10-14)*

This WebSocket allows you to stream live price updates for equity and option symbols.

USE CASE

React to every price change on a stock or option, such as a watchlist update or a strategy trigger.

Details

* The WebSocket API for receiving stock data is a real-time communication protocol designed to provide seamless and low-latency access to live stock market data. This API allows developers and traders to establish a persistent, bidirectional connection with the server, enabling them to receive continuous updates on stock prices, trading volumes, and other relevant market information.
* To quickly get started with the WebSocket API and start receiving real-time stock data, you can explore our sample scripts and code examples in our GitHub repository:
  [Data WebSocket Sample Scripts](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED)/websocket%20sample%20script)
* To update symbols in an already subscribed socket, it is recommended to unsubscribe from the existing list of symbols and then resubscribe with the updated list.
* Subscribe with `data_type` set to `SymbolUpdate` and symbols in FYERS format, for example `NSE:SBIN-EQ`.
* Check `type` on every message: `sf` carries equity and option data. `cn` and `sub` are connection and subscribe messages.
* Price fields such as `high_price`, `low_price`, `open_price`, `ch`, `chp` and `vol_traded_today` are for the current trading day.
* Use lite mode (`litemode=True` in Python, `mode(LiteMode)` in Node and Web JS) to get only `symbol`, `ltp` and `type`. See [Lite Mode](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-lite-mode/).
* Index symbols arrive as index messages with fewer fields. See [Indices Update](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-indices-update/).

Plan limits

Standard plan

* Up to 100 symbols, counted per user across all connections

Prime plan

* Up to 5,000 symbols, counted per user across all connections

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes (Market Data Update)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | The symbol in fyers symbology format whose data is received on socket. |
| `ltp` | float | Last traded price of security or asset. |
| `prev_close_price` | float | Previous day's close of security or asset. |
| `high_price` | float | Current day's high of security or asset. |
| `low_price` | float | Current day's low of security or asset. |
| `open_price` | float | Current day's open of security or asset. |
| `ch` | float | Change in price of security or asset today. |
| `chp` | float | Change in price in % of security or asset today. |
| `vol_traded_today` | int | Volume traded for security or asset today. |
| `last_traded_time` | int | Last traded time of security or asset. |
| `bid_size` | int | The bid size key represents the quantity or volume of the security or asset that buyers are willing to purchase at a specific bid price level. |
| `ask_size` | int | The ask size key represents the quantity or volume of the security or asset that sellers are willing to sell at a specific ask price level. |
| `ask_price` | float | The ask price key represents the lowest price at which sellers are willing to sell a particular security or asset. |
| `bid_price` | float | The bid price key represents the highest price at which buyers are willing to purchase a particular security or asset. |
| `last_traded_qty` | int | Last traded quantity of security or asset. |
| `tot_buy_qty` | int | Total buy quantity of security or asset. |
| `tot_sell_qty` | int | Total sell quantity of security or asset. |
| `avg_trade_price` | float | Average trade price of security or asset. |
| `type` | string | * cn - connection message * sub - subscribe message * if - index data message * dp - market depth data message * sf - Equity and option data message |

Request

```
from fyers_apiv3.FyersWebsocket import data_ws

def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Response:", message)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "SymbolUpdate"

    # Subscribe to the specified symbols and data type
    symbols = ['NSE:SBIN-EQ', 'NSE:ADANIENT-EQ']
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "XC4XXXXXXM-100:eXXXXXXXXXXXXfZNSBoLo"

## Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
    "ltp":606.4,
    "vol_traded_today":3045212,
    "last_traded_time":1690953622,
    "exch_feed_time":1690953622,
    "bid_size":2081,
    "ask_size":903,
    "bid_price":606.4,
    "ask_price":606.45,
    "last_traded_qty":5,
    "tot_buy_qty":749960,
    "tot_sell_qty":1092063,
    "avg_trade_price":608.2,
    "low_price":605.85,
    "high_price":610.5,
    "open_price":609.85,
    "prev_close_price":620.2,
    "type":"sf",
    "symbol":"NSE:SBIN-EQ",
    "ch":-13.8,
    "chp":-2.23
  }
```

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Data Socket - Market Depth Update

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-depth-update/ (last updated 2026-10-14)*

This WebSocket allows you to stream live five-level market depth for a symbol.

USE CASE

Build a live order book showing the best five bids and asks as they change.

Details

* The WebSocket API for receiving stock data is a real-time communication protocol designed to provide seamless and low-latency access to live stock market data. This API allows developers and traders to establish a persistent, bidirectional connection with the server, enabling them to receive continuous updates on stock prices, trading volumes, and other relevant market information.
* To quickly get started with the WebSocket API and start receiving real-time stock data, you can explore our sample scripts and code examples in our GitHub repository:
   [Data WebSocket Sample Scripts](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED)/websocket%20sample%20script)
* Depth covers 5 levels on each side, for example `bid_price1` to `bid_price5`. For 50 levels use the [Tick-by-Tick (TBT) Socket](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/).
* Subscribe with `data_type` set to `DepthUpdate` in Python. In Node, pass `true` as the second argument of `subscribe`.
* Depth messages have `type` set to `dp`.
* Each level has a price, a size and an order count, for example `bid_price1`, `bid_size1` and `bid_order1`.
* In the sample response, levels with no quantity show 0.

Plan limits

Standard plan

* Up to 100 symbols, counted per user across all connections

Prime plan

* Up to 5,000 symbols, counted per user across all connections

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes (Depth Update)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | The symbol in fyers symbology format whose data is received on socket. |
| `bid_price1-bid_price5` | float | The bid price key represents the highest price at which buyers are willing to purchase a particular security or asset. |
| `ask_price1-ask_price5` | float | The ask price key represents the lowest price at which sellers are willing to sell a particular security or asset. |
| `bid_size1-bid_size5` | int | The bid size key represents the quantity or volume of the security or asset that buyers are willing to purchase at a specific bid price level. |
| `ask_size1-ask_size5` | int | The ask size key represents the quantity or volume of the security or asset that sellers are willing to sell at a specific ask price level. |
| `bid_order1-bid_order5` | int | The number of bid order. |
| `ask_order1-ask_order5` | int | The number of ask order. |
| `type` | string | * cn - connection message * sub - subscribe message * if - index data message * dp - market depth data message * sf - Equity and option data message |

Request

```
from fyers_apiv3.FyersWebsocket import data_ws

def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Response:", message)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "DepthUpdate"

    # Subscribe to the specified symbols and data type
    symbols = ['NSE:SBIN-EQ', 'NSE:ADANIENT-EQ']
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "XXDHHIOKS-100:eajoljXXXXXXXXXX"

## Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
  "bid_price1":606.25,
  "bid_price2":606.2,
  "bid_price3":606.15,
  "bid_price4":606.1,
  "bid_price5":606.05,
  "ask_price1":606.3,
  "ask_price2":606.35,
  "ask_price3":606.4,
  "ask_price4":606.45,
  "ask_price5":606.5,
  "bid_size1":20,
  "bid_size2":902,
  "bid_size3":111,
  "bid_size4":110,
  "bid_size5":979,
  "ask_size1":282,
  "ask_size2":568,
  "ask_size3":2910,
  "ask_size4":1676,
  "ask_size5":2981,
  "bid_order1":1,
  "bid_order2":3,
  "bid_order3":2,
  "bid_order4":2,
  "bid_order5":9,
  "ask_order1":4,
  "ask_order2":2,
  "ask_order3":12,
  "ask_order4":9,
  "ask_order5":17,
  "type":"dp",
  "symbol":"NSE:SBIN-EQ"
}
```

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Data Socket - Unsubscribe and Connection Management

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-unsubscribe-and-connection-management/ (last updated 2026-10-14)*

This WebSocket allows you to unsubscribe from symbols and manage your Data Socket connection.

USE CASE

Stop updates for symbols you no longer track, for example when a watchlist is closed or a position is exited.

Details

* To stop receiving real-time data updates for a specific stock symbol or a group of symbols, you can utilize the "unsubscribe" action in the WebSocket API. Sending an "unsubscribe" message will remove the specified symbol(s) from your active subscriptions, and you will no longer receive updates for those symbols.
  You can check the sample code to know how to unsubscribe to already subscribed symbols.
* After a reconnect, previous symbols are resubscribed through auto-reconnect. To then update your symbol list, it is recommended to unsubscribe from the existing list and resubscribe with the updated list. See **Updating subscribed symbols** under [Web Socket Introduction](https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/data-socket-connect-and-subscribe/).
* In Python, call `unsubscribe` with the symbols and the same `data_type` you used to subscribe, for example `SymbolUpdate`.
* A successful unsubscribe returns `type` `unsub`, `code` 200 and `s` `ok`. The `message` text differs by SDK (Python: `Unsubscribed`; Node: `successful`).
* You can run the call from the message callback, for example to drop a symbol once your condition is met.
* For a changed symbol list, unsubscribe from the current list and subscribe again.
* Set `reconnect=True` so a dropped connection recovers on its own. `reconnect_retry` sets the retry count, up to 50.
* Handle disconnects and errors in the on-close and on-error callbacks.

Request

```
from fyers_apiv3.FyersWebsocket import data_ws

def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Response:", message)
    # After processing or when you decide to unsubscribe for specific symbol and data_type
    # you can use the fyers.unsubscribe() method

    # Example of condition: Unsubscribe when a certain condition is met
    if message['symbol']== 'NSE:SBIN-EQ' and message['ltp'] > 610:
        # Unsubscribe from the specified symbols and data type
        data_type = "SymbolUpdate"
        symbols_to_unsubscribe = ['NSE:SBIN-EQ']
        fyers.unsubscribe(symbols=symbols_to_unsubscribe, data_type=data_type)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "SymbolUpdate"

    # Subscribe to the specified symbols and data type
    symbols = ['NSE:SBIN-EQ', 'NSE:ADANIENT-EQ']
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "XXDHHIOKS-100:eajoljXXXXXXXXXX"

## Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{'type': 'unsub', 'code': 200, 'message': 'Unsubscribed', 's': 'ok'}
```

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Data Socket - Advanced Configuration

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/overview/advanced-configuration/ (last updated 2026-10-14)*

This setting lets you control how often the Node SDK processes queued Data Socket messages.

USE CASE

Set a short interval for fast, tick-driven logic, or around 100 to 500 ms for general streaming.

Details

The WebSocket queue processing interval is an `Optional` setting that allows you to customize how frequently data in the subscription queue is handled. By default, this interval is set to `1` millisecond, but it can be adjusted to better suit your application's specific needs and performance preferences.

**Queue processing interval**

You can set the processing interval anywhere between `1ms` and `2000ms` (2 seconds). Call `setQueueProcessInterval` before or during an active WebSocket session.

setQueueProcessInterval

Range: `1ms` to `2000ms`
Default: `1ms`
Example: `setQueueProcessInterval(200)`

**Configuration options**

* Customizable Interval: You can set the processing interval anywhere between 1ms to 2000ms (2 seconds), giving you flexibility to optimize performance and responsiveness.
* Dynamic Adjustment: The interval setting can be changed at any time during an active WebSocket session.
* Performance Optimization: Shorter intervals (`1-10ms`) are ideal for high-frequency trading scenarios that benefit from rapid data processing, while slightly longer intervals (`100-500ms`) work well for general market data streaming.
* Resource Management: You can tune the interval based on how your application handles incoming data, helping to maintain smooth operation across different environments.

**Recommended ranges**

Use `1-10ms` when you need rapid queue processing, and `100-500ms` for general market data streaming.

**Availability**

Customizing the queue processing interval was added on 09 Jun 2025 (the Change Log lists Node Js `fyers-web-sdk-v3` `v1.4.2`). The sample on this page uses the Node SDK. Check the [Change Log](https://fyers.in/api-docs/v3/changelog/) for other SDKs.

Python is not available for this example. Showing Node instead.

RequestNode

```
const FyersSocket = require("fyers-api-v3").fyersDataSocket

var fyersdata= new FyersSocket("xxxxx-1xx:ey....","logpath",true/*flag to enable disable logging*/)
fyersdata.setQueueProcessInterval(200)  // 200ms - more reasonable interval for queue processing
fyersdata.connect()
```

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Get Trades

*Source: https://fyers.in/api-docs/v3/api/trading/trade-book/get-trades/ (last updated 2026-10-14)*

This API allows you to fetch all the trades executed in your account today.

USE CASE

Check the price and quantity at which your orders were filled today.

Note

**Live Streaming** — Receive trade execution updates in real time through the General WebSocket. View [General WebSocket Overview](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/) documentation.

Details

* Fetches all the trades for the current day across all platforms and exchanges in the current trading day.
* Each row is one executed trade. `orderNumber` links it to the order it filled and `tradeNumber` is the number generated by the exchange.
* Orders that were never executed (pending, rejected or cancelled) do not appear here. Use Get Orders to see them.
* `orderDateTime` is the time the trade occurred, in IST. `row` is a unique value you can use to sort trades.
* `orderTag` carries a `1:` prefix for tags you set and `2:` for tags generated by FYERS. Trades without a tag show `1:Untagged`.
* `exchangeOrderNo` is the order number provided by the exchange, and `fyToken` is the unique identifier of the symbol.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes - For each trade

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `row` | int | The unique value to sort the trades |
| `orderDateTime` | string | The time when the trade occurred in “DD-MM-YYYY hh:mm:ss” format in IST |
| `orderNumber` | string | The order id for which the trade occurred |
| `tradeNumber` | string | The trade number generated by the exchange |
| `tradePrice` | float | The traded price |
| `tradeValue` | float | The total traded value |
| `tradedQty` | int | The total traded qty |
| `side` | int | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `productType` | string | * The product in which the order was placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `exchangeOrderNo` | string | The order number provided by the exchange |
| `segment` | int | * The segment in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `fyToken` | string | Fytoken is a unique identifier for every symbol. |
| `orderTag` | string | * ordertag provided when placing the order * **Note**: `1:` will be concatenated at the start of tag provided by user. * `2:` will be concatenated at the start of tag generated internally by Fyers. * Default value if tag not provided when order is placed is `1:Untagged` |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

response = fyers.tradebook()
print(response)
```

```
{
  "s": "ok",
  "code": 200,
  "message": "",
  "tradeBook":
              [{
                "clientId":"FXXXXX",
                "orderDateTime":"07-Aug-2020 13:51:12",
                "orderNumber":"120080789075",
                "exchangeOrderNo": "1200000009204725",
                "exchange":10,
                "side":1,
                "segment":10,
                "orderType":2,
                "fyToken":"101000000010666",
                "productType":"CNC",
                "tradedQty":10,
                "tradePrice":32.7,
                "tradeValue":327.0,
                "tradeNumber":"52605023",
                "row":52605023,
                "symbol":"NSE:PNB-EQ"
                "orderTag": "1:Ordertag"
              },
              {
                "clientId":"FXXXXX",
                "orderDateTime":"07-Aug-2020 13:48:12",
                "orderNumber":"120080789139",
                "exchangeOrderNo": "1000000012031528",
                "exchange":10,
                "side":1,
                "segment":10,
                "orderType":2,
                "fyToken":"101000000010454",
                "productType":"CNC",
                "tradedQty":19,
                "tradePrice":14.1,
                "tradeValue":267.9,
                "tradeNumber":"3281523",
                "row":3281523,
                "symbol":"NSE:CENTRUM-EQ"
                "orderTag": "1:Ordertag"
              },
              {
                "clientId":"FXXXXX1",
                "orderDateTime":"07-Aug-2020 13:47:22",
                "orderNumber":"120080797993",
                "exchangeOrderNo": "1100000008047027",
                "exchange":10,
                "side":1,
                "segment":10,
                "orderType":2,
                "fyToken":"101000000018783",
                "productType":"CNC",
                "tradedQty":4,
                "tradePrice":115.5,
                "tradeValue":462.0,
                "tradeNumber":"27945307",
                "row":27945307,
                "symbol":"NSE:IDFNIFTYET-EQ"
                "orderTag": "1:Ordertag"
              }]
}
```

VIDEO LEARNING

### Video learning

[How to check trade history? (REST and cURL)REST and cURL · 5:27](https://www.youtube.com/watch?v=mVp4kUapEMA&list=PLgzB28RH71Ju9iCF-a8MPuroWb-a_uP60)

Go and C video tutorials: coming soon.

## General WebSocket - Unsubscribe

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-unsubscribe/ (last updated 2026-10-14)*

This guide explains how to stop receiving selected updates on the General WebSocket without closing the connection.

USE CASE

Stop receiving updates you no longer need, such as price alerts, while keeping the connection open.

Details

To Unsubscribe for different actions, create a message data, which would be the string format for json node.

**Json node params**

Convert the json to string and send this message to the socket to unsubscribe for the `action_data` mentioned.

message

`message = json.dumps({ "T": "SUB_ORD", "SLIST": action_data, "SUB_T": -1 })`

`T` Type: String
value: `SUB_ORD` (Fixed)

`action_data` Type: List/Array
Value: `orders` `trades` `positions` `edis` `pricealerts` `login`

Based on the list passed in action\_data, web\_socket data will be received.

`SUB_T` Type: Integer
Value: `-1` (value -1 is for unsubscribing and 1 for subscribe)

**Good to know**

* The message is the same as the subscribe message. Only `SUB_T` changes: `-1` unsubscribes and `1` subscribes.
* Put the actions you want to stop in `SLIST`, using the same names as when subscribing: `orders`, `trades`, `positions`, `edis`, `pricealerts`, `login`.
* In the Python SDK, `unsubscribe(data_type)` takes the same comma-separated names as `subscribe` and sends this message for you.

RequestPython

```
def unsubscribe(self, data_type: str) -> None:
  """
    Unsubscribes from real-time updates of a specific data type.

  Args:
  data_type (str): The type of data to unsubscribe from, such as orders, position, holdings or general.

  """

  try:
    if self.__ws_object is not None:
      self.data_type = [
        self.socket_type[(type)] for type in data_type.split(",")
      ]
      message = json.dumps(
        {"T": "SUB_ORD", "SLIST": self.data_type, "SUB_T": -1}
      )
      self.__ws_object.send(message)

except Exception as e:
  self.order_logger.error(e)
```

## General WebSocket - Ping and Mandatory Fields

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/ping-method/ (last updated 2026-10-14)*

This guide explains how to send ping messages to check that the General WebSocket connection is alive.

USE CASE

Send a ping at regular intervals and treat the connection as dead if no pong comes back.

Details

To check whether the websocket connection is alive or not, we have to send a periodically `ping` message. If we get a `pong` from websocket, it means it is alive else dead. Find how we are doing in Python Code.

**Ping interval**

Here there is one while loop with sleep of `10` seconds and we send a `ping` message to websocket to know that websocket is alive or not.

message

`self.__ws_object.send("ping")`

`ping` Type: String
value: `ping` (Fixed)

`sleep` Type: Integer
Value: `10` seconds

**Good to know**

* The message is the plain text `ping`, not JSON. A `pong` reply means the connection is alive. If none comes, treat the connection as dead.
* The sample loop sends `ping` and then sleeps for 10 seconds, and keeps going only while the socket is still connected.
* The Python SDK starts this ping loop in its own thread as soon as the connection opens. If you use your own client, run the loop yourself.
* Connection, subscribe and unsubscribe each have mandatory fields. See the table below.

RequestPython

```
def __ping(self) -> None:
  """
  Sends periodic ping messages to the server to maintain the WebSocket connection.

  The method continuously sends "__ping" messages to the server at a regular interval
  as long as the WebSocket connection is active.

  """

  while (
      self.__ws_object is not None
      and self.__ws_object.sock
      and self.__ws_object.sock.connected
  ):
      self.__ws_object.send("ping")
      time.sleep(10)
```

### Mandatory fields

| Method | Fields | Reason |
| --- | --- | --- |
| WebSocket Connection | `WebSocket Connection URL(Endpoint)` | To make a connection |
| WebSocket Connection | `Headers` | To authorize |
| Subscribe Method | `action_data` | To subscribe for particular actions |
| Subscribe Method | `"SUB_T": 1` | While subscribing to any action |
| UnSubscribe Method | `"SUB_T": -1` | While unsubscribing any action |

## General Socket - Order Events

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-order-events/ (last updated 2026-10-14)*

This WebSocket allows you to receive live updates on the status of your orders, including partial fills and rejections.

USE CASE

Receive an update the moment one of your orders is placed, modified, traded or rejected.

Details

* The WebSocket API for receiving order, position, trade, price alerts, and EDIS updates is a real-time communication protocol designed to provide seamless access to various critical elements of a trading and EDIS system. This API allows traders and developers to establish a persistent, bidirectional connection with the server, enabling them to receive real-time updates on their orders, current positions, executed trades, price alerts, and EDIS status.
* Subscribe with the `orders` action on the raw socket, or `OnOrders` in the Python SDK (callback `on_orders`). Nothing is delivered until you subscribe.
* Match each update to your order with `id`. `exchOrdId` is the exchange order id and `id_fyers` is the FYERS-generated unique identifier.
* Read `status` to track the order: 1 canceled, 2 traded, 4 transit, 5 rejected, 6 pending, 7 expired (3 is not used). `message` carries error text.
* `filledQty` and `remainingQuantity` show how much has traded and what is left after partial trades. `tradedPrice` is the average traded price.
* `offlineOrder` is true for an AMO order and false when the market is open. `parentId` is sent only for orders where it applies.
* `orderDateTime` is in IST as `DD-MMM-YYYY hh:mm:ss`, for example `04-Aug-2023 10:12:58`.
* The raw socket message uses different key names. The SDK renames them, for example `org_ord_status` to `status` and `qty_remaining` to `remainingQuantity`. See the key mappers on [General WebSocket - Subscribe](https://fyers.in/api-docs/v3/api/websockets/general-socket/overview/general-socket-subscribe/).

### Response Attributes - For order updates

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id` | string | The unique order id assigned for each order |
| `exchOrdId` | string | The order id provided by the exchange |
| `symbol` | string | The symbol for which order is placed |
| `qty` | int | The original order qty |
| `remainingQuantity` | int | The remaining qty |
| `filledQty` | int | The filled qty after partial trades |
| `status` | int | * 1 => Canceled * 2 => Traded / Filled * 3 => (Not used currently) * 4 => Transit * 5 => Rejected * 6 => Pending * 7 => Expired * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-status/) |
| `message` | string | The error messages are shown here |
| `segment` | int | * 10 => E (Equity) * 11 => D (F&O) * 12 => C (Currency) * 20 => M (Commodity) * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `limitPrice` | float | The limit price for the order |
| `stopPrice` | float | The limit price for the order |
| `productType` | string | The product type |
| `type` | int | * 1 => Limit Order * 2 => Market Order * 3 => Stop Order (SL-M) * 4 => Stoplimit Order (SL-L) |
| `side` | int | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `orderValidity` | string | * DAY * IOC |
| `orderDateTime` | string | The order time as per DD-MMM-YYYY hh:mm:ss in IST |
| `parentId` | string | The parent order id will be provided only for applicable orders. |
| `tradedPrice` | float | The average traded price for the order |
| `source` | string | * Source from where the order was placed. * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sources/) |
| `fytoken` | string | * Fytoken is a unique identifier for every symbol. * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `offlineOrder` | boolean | * False => When market is open * True => When placing AMO order |
| `pan` | string | PAN of the client |
| `clientId` | string | The client id of the fyers user |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `instrument` | int | * Exchange instrument type * [View Details](https://fyers.in/api-docs/v3/api/appendix/instrument-types/) |
| `id_fyers` | string | Fyers system-generated unique identifier for the order. |

Request

```
from fyers_apiv3.FyersWebsocket import order_ws

def onOrder(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Order Response:", message)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "OnOrders"
    # data_type = "OnTrades"
    # data_type = "OnPositions"
    # data_type = "OnGeneral"
    # data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"

    fyers.subscribe(data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "AAAAAAAA-100:eyJ..."

## Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
    access_token=access_token,  # Your access token for authenticating with the Fyers API.
    write_to_file=False,        # A boolean flag indicating whether to write data to a log file or not.
    log_path="",                # The path to the log file if write_to_file is set to True (empty string means current directory).
    on_connect=onopen,          # Callback function to be executed upon successful WebSocket connection.
    on_close=onclose,           # Callback function to be executed when the WebSocket connection is closed.
    on_error=onerror,           # Callback function to handle any WebSocket errors that may occur.
    on_orders=onOrder,          # Callback function to handle order-related events from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
  "s":"ok",
  "orders":{
      "clientId":"FY****",
      "id":"23080400089344",
      "exchOrdId":"1100000009596016",
      "qty":1,
      "filledQty":1,
      "limitPrice":7.95,
      "type":1,
      "fyToken":"101000000014366",
      "exchange":10,
      "segment":10,
      "symbol":"NSE:IDEA-EQ",
      "instrument":0,
      "offlineOrder":false,
      "orderDateTime":"04-Aug-2023 10:12:58",
      "orderValidity":"DAY",
      "productType":"INTRADAY",
      "side":-1,
      "status":90,
      "source":"W",
      "ex_sym":"IDEA",
      "description":"VODAFONE IDEA LIMITED",
      "orderNumStatus":"23080400089344:2",
      "id_fyers":"1b30241e-2819-4ec9-a3e4-69b6155cacab"
  }
}
```

## General Socket - Trade Events

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-trade-events/ (last updated 2026-10-14)*

This WebSocket allows you to receive a live update for every trade executed against your orders.

USE CASE

Receive each execution of your orders the moment it happens, with its price and quantity.

Details

* Subscribe with the `trades` action on the raw socket, or `OnTrades` in the Python SDK (callback `on_trades`). Nothing is delivered until you subscribe.
* Each message carries a `tradeNumber` (generated by the exchange) with the traded quantity and price. `orderNumber` is the id of the order the trade occurred for.
* `tradedQty`, `tradePrice` and `tradeValue` describe that execution. Use `id` to sort trades.
* `exchangeOrderNo` is the order number provided by the exchange.
* `orderDateTime` is in IST as `DD-MM-YYYY hh:mm:ss`, which differs from the `DD-MMM-YYYY` format used in order events.
* The raw socket message uses different key names. The SDK renames them, for example `id_fill` to `tradeNumber`, `id` to `orderNumber`, `qty_traded` to `tradedQty` and `price_traded` to `tradePrice`.

### Response Attributes - For trade update

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `id` | string | The unique id to sort the trades |
| `orderDateTime` | string | The time when the trade occurred in “DD-MM-YYYY hh:mm:ss” format in IST |
| `orderNumber` | string | The order id for which the trade occurred |
| `tradeNumber` | string | The trade number generated by the exchange |
| `tradePrice` | float | The traded price |
| `tradeValue` | float | The total traded value |
| `tradedQty` | int | The total traded qty |
| `side` | int | * 1 => Buy * -1 => Sell * [View Details](https://fyers.in/api-docs/v3/api/appendix/order-sides/) |
| `productType` | string | * The product in which the order was placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `exchangeOrderNo` | string | The order number provided by the exchange |
| `segment` | int | * The segment in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `fyToken` | string | Fytoken is a unique identifier for every symbol. |
| `id_fyers` | string | Fyers system-generated unique identifier for the order. |

Request

```
from fyers_apiv3.FyersWebsocket import order_ws

def onTrade(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Trade Response:", message)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "OnTrades"

    # data_type = "OnOrders"
    # data_type = "OnPositions"
    # data_type = "OnGeneral"
    # data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"

    fyers.subscribe(data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "AAAAAAAA-100:eyJ..."

## Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
    access_token=access_token,  # Your access token for authenticating with the Fyers API.
    write_to_file=False,        # A boolean flag indicating whether to write data to a log file or not.
    log_path="",                # The path to the log file if write_to_file is set to True (empty string means current directory).
    on_connect=onopen,          # Callback function to be executed upon successful WebSocket connection.
    on_close=onclose,           # Callback function to be executed when the WebSocket connection is closed.
    on_error=onerror,           # Callback function to handle any WebSocket errors that may occur.
    on_trades=onTrade           # Callback function to handle trade-related events from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
    "s":"ok",
    "trades":{
        "tradeNumber":"23080400089344-21726639",
        "orderNumber":"23080400089344",
        "tradedQty":1,
        "tradePrice":7.95,
        "tradeValue":7.95,
        "productType":"INTRADAY",
        "clientId":"FY****",
        "exchangeOrderNo":"1100000009596016",
        "orderType":2,
        "side":-1,
        "symbol":"NSE:IDEA-EQ",
        "orderDateTime":"04-08-2023 10:12:58",
        "fyToken":"101000000014366",
        "exchange":10,
        "segment":10,
        "id_fyers":"1b30241e-2819-4ec9-a3e4-69b6155cacab"
    }
  }
```

## General Socket - Position Events

*Source: https://fyers.in/api-docs/v3/api/websockets/general-socket/general-socket-position-events/ (last updated 2026-10-14)*

This WebSocket allows you to receive live updates on your positions as your trades execute.

USE CASE

Track your net quantity, average prices and realised P&L live as trades execute.

Details

* Subscribe with the `positions` action on the raw socket, or `OnPositions` in the Python SDK (callback `on_positions`). Nothing is delivered until you subscribe.
* `id` is unique for each position, for example `NSE:IDEA-EQ-INTRADAY`. `slNo` is used to sort positions.
* `netQty` is the net quantity and `qty` is its absolute value. A squared-off position is sent with `netQty` 0, as in the sample response.
* `dayBuyQty` and `daySellQty` are today's quantities. `cfBuyQty` and `cfSellQty` are carry-forward quantities.
* For cross-currency positions (`crossCurrency` is Y), use `rbiRefRate` to calculate P&L. For commodity positions, use `qtyMulti_com`.
* The raw socket message uses different key names. The SDK renames them, for example `pl_realized` to `realized_profit`, `tran_side` to `side`, `pl_total` to `pl` and `pl_unrealized` to `unrealized_profit`.

### Response Attributes - For position updates

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | Eg: NSE:SBIN-EQ |
| `id` | string | The unique value for each position |
| `buyAvg` | float | Average buy price |
| `buyQty` | int | Total buy qty |
| `sellAvg` | float | Average sell price |
| `sellQty` | int | Total sell qty |
| `netAvg` | float | netAvg |
| `netQty` | int | Net qty |
| `side` | int | * The side shows whether the position is long / short * [View Details](https://fyers.in/api-docs/v3/api/appendix/position-sides/) |
| `qty` | int | Absolute value of net qty |
| `productType` | string | * The product type of the position * [View Details](https://fyers.in/api-docs/v3/api/appendix/product-types/) |
| `realized_profit` | float | The realized p&l of the position |
| `crossCurrency` | string | * Y => It is cross currency position * N => It is not a cross currency position |
| `rbiRefRate` | float | Incase of cross currency position, the rbi reference rate will be required to calculate the p&l |
| `qtyMulti_com` | float | Incase of commodity positions, this multiplier is required for p&l calculation |
| `segment` | int | * The segment in which the position is taken. * [View Details](https://fyers.in/api-docs/v3/api/appendix/segments/) |
| `exchange` | int | * The exchange in which the position is taken. * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `slNo` | int | This is used for sorting of positions |
| `fytoken` | string | * Fytoken is a unique identifier for every symbol. * [View Details](https://fyers.in/api-docs/v3/api/appendix/fytoken/) |
| `cfBuyQty` | int | Carry forward buy quantity |
| `cfSellQty` | int | Carry forward sell quantity |
| `dayBuyQty` | int | Day forward buy quantity |
| `daySellQty` | int | Day forward sell quantity |
| `exchange` | int | * The exchange in which order is placed * [View Details](https://fyers.in/api-docs/v3/api/appendix/exchanges/) |
| `buyVal` | float | Total buy value of the position. |
| `sellVal` | float | Total sell value of the position. |

Request

```
from fyers_apiv3.FyersWebsocket import order_ws

def onPosition(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Position Response:", message)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "OnPositions"

    # data_type = "OnOrders"
    # data_type = "OnTrades"
    # data_type = "OnGeneral"
    # data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"

    fyers.subscribe(data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "AAAAAAAA-100:eyJ..."

## Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
    access_token=access_token,  # Your access token for authenticating with the Fyers API.
    write_to_file=False,        # A boolean flag indicating whether to write data to a log file or not.
    log_path="",                # The path to the log file if write_to_file is set to True (empty string means current directory).
    on_connect=onopen,          # Callback function to be executed upon successful WebSocket connection.
    on_close=onclose,           # Callback function to be executed when the WebSocket connection is closed.
    on_error=onerror,           # Callback function to handle any WebSocket errors that may occur.
    on_positions=onPosition,    # Callback function to handle position-related events from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
    "s":"ok",
    "positions":{
        "symbol":"NSE:IDEA-EQ",
        "id":"NSE:IDEA-EQ-INTRADAY",
        "buyAvg":8,
        "buyQty":1,
        "buyVal":8,
        "sellAvg":7.95,
        "sellQty":1,
        "sellVal":7.95,
        "netAvg":0,
        "netQty":0,
        "side":0,
        "qty":0,
        "productType":"INTRADAY",
        "realized_profit":-0.04999999999999982,
        "rbiRefRate":1,
        "fyToken":"101000000014366",
        "exchange":10,
        "segment":10,
        "dayBuyQty":1,
        "daySellQty":1,
        "cfBuyQty":0,
        "cfSellQty":0,
        "qtyMulti_com":1
    }
  }
```

## Get Expiry Dates

*Source: https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expiry-dates/ (last updated 2026-10-14)*

This API allows you to get the futures and options expiry dates for an underlying symbol within a date range.

USE CASE

Find the expiry dates that existed for an underlying before you look up its expired contracts.

Details

* The Get Expiry Dates API gives the available Futures and Options expiry dates for an underlying symbol within a specified date range.
* Futures and Options expiry dates are returned separately.
* Use this API when the underlying symbol is known but the expiry date is not. Once you select an expiry date, use the underlying symbol and expiry date with the [Get Expired Contracts](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-contracts/) API to get the available expired contract symbols.
* You can request up to 366 days at a time.
* Use an underlying symbol such as `NSE:NIFTY50-INDEX`, `NSE:SBIN-EQ` or `BSE:SENSEX-INDEX`.
* Dates in `range_from` and `range_to` are epoch values when `date_format` is 0, or `yyyy-mm-dd` when it is 1.
* Futures expiries are returned in `data.expiry_dates.futures` and options expiries in `data.expiry_dates.options`.
* Pass a returned expiry date to [Get Expired Contracts](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-contracts/) as `expiry_date`.
* Expiry data is available from different dates for each exchange.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

#### Data Availability

| **Exchange** | **Data Available From** |
| --- | --- |
| `NSE` | 10 October 2018 |
| `BSE` | 07 August 2023 |
| `MCX` | 11 October 2018 |

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Underlying symbol for which the expiry dates are required. Eg: NSE:NIFTY50-INDEX, NSE:SBIN-EQ, BSE:SENSEX-INDEX |
| `range_from`\* | string | Indicating the start date of records. Accepts epoch value if date\_format flag is set to 0. Accepts yyyy-mm-dd format if date\_format flag is set to 1. |
| `range_to`\* | string | Indicating the end date of records. Accepts epoch value if date\_format flag is set to 0. Accepts yyyy-mm-dd format if date\_format flag is set to 1. |
| `date_format`\* | int | date\_format is a boolean flag. 0 to enter the epoch value. 1 to enter the date format as yyyy-mm-dd. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | Response code |
| `message` | string | Message returned with the response |
| `data.symbol` | string | Underlying symbol for which the expiry dates are returned |
| `data.from_date` | string | Start of the requested range |
| `data.to_date` | string | End of the requested range |
| `data.expiry_dates.futures` | array | Futures expiry dates available within the requested range |
| `data.expiry_dates.options` | array | Options expiry dates available within the requested range |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol": "NSE:SBIN-EQ",
    "range_from": "2025-01-01",
    "range_to": "2025-03-31",
    "date_format": "1"
}

response = fyers.expiry_dates(data)
print(response)
print(response["data"]["expiry_dates"]["futures"])
print(response["data"]["expiry_dates"]["options"])
```

```
{
    "code": 200,
    "data": {
        "symbol": "SBIN",
        "from_date": "2025-01-01",
        "to_date": "2025-03-31",
        "expiry_dates": {
            "futures": ["2025-01-30", "2025-02-27", "2025-03-27"],
            "options": ["2025-01-30", "2025-02-27", "2025-03-27"]
        }
    },
    "message": "",
    "s": "ok"
}
```

## Get Expired Contracts

*Source: https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-contracts/ (last updated 2026-10-14)*

This API allows you to get the expired futures and options contract symbols for an underlying symbol and expiry date.

USE CASE

Find the exact symbol of an expired futures contract or option strike for a given expiry.

Details

* The Get Expired Contracts API gives the expired Futures and Options contract symbols available for a specified underlying symbol and expiry date.
* Futures and Options contract symbols are returned separately.
* If the expiry date is not known, use the [Get Expiry Dates](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expiry-dates/) API first.
* Once you find the required expired contract symbol, use it with the [Get Expired F&O Data](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-fo-data/) API to get historical data.
* Send `expiry_date` in `yyyy-mm-dd` format, using a date returned by [Get Expiry Dates](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expiry-dates/).
* Futures symbols are returned in `data.contracts.futures` and options symbols in `data.contracts.options`.
* Copy a contract symbol exactly as returned into [Get Expired F&O Data](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-fo-data/).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Underlying symbol for which the expired contracts are required. Eg: NSE:NIFTY50-INDEX, NSE:SBIN-EQ, BSE:SENSEX-INDEX |
| `expiry_date`\* | string | Expiry date of the contracts in yyyy-mm-dd format. Use an expiry date returned by the Get Expiry Dates API. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | Response code |
| `message` | string | Message returned with the response |
| `data.symbol` | string | Underlying symbol for which the contracts are returned |
| `data.expiry_date` | string | Expiry date of the returned contracts |
| `data.contracts.futures` | array | Expired Futures contract symbols for the requested expiry |
| `data.contracts.options` | array | Expired Options contract symbols for the requested expiry |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol": "NSE:SBIN-EQ",
    "expiry_date": "2025-03-27"
}

response = fyers.history_underlying_symbols(data)
print(response)
print(response["data"]["contracts"]["futures"])
print(response["data"]["contracts"]["options"])
```

```
{
    "code": 200,
    "data": {
        "symbol": "SBIN",
        "expiry_date": "2025-03-27",
        "contracts": {
            "futures": ["NSE:SBIN25MARFUT"],
            "options": ["NSE:SBIN25MAR320PE", "NSE:SBIN25MAR320CE", "NSE:SBIN25MAR340PE", "NSE:SBIN25MAR340CE"]
        }
    },
    "message": "",
    "s": "ok"
}
```

## Get Expired F&O Data

*Source: https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-fo-data/ (last updated 2026-10-14)*

This API allows you to get historical candles for an expired futures or options contract.

USE CASE

Fetch candles, open interest and option Greeks for an expired contract to backtest a strategy on past expiries.

Note

* Greeks are not available for MCX.

* NCOM does not have historical F&O data.

Details

* The Get Expired F&O Data API gives historical data for expired Futures and Options contracts.
* This API supports expired contracts only. It does not provide historical data for active Futures and Options contracts.
* To get historical data, provide the expired contract symbol, required date range, and resolution.
* If the expired contract symbol is not known, use the [Get Expired Contracts](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expired-contracts/) API first. If the expiry date is also not known, use the [Get Expiry Dates](https://fyers.in/api-docs/v3/api/market-data/expired-fo-data/get-expiry-dates/) API to find it.
* **Historical Data Limits**
  The amount of historical data you can request depends on the selected resolution.
* Intraday, daily and weekly timeframes are available. The monthly timeframe will be coming soon.
* For 1, 2, 3, 5, 10, 15, 20, 30, 45, 60, 120, 180, and 240-minute resolutions, you can request up to 100 days of data at a time.
* For seconds data, in a single request 30 days data can be fetched.
* Pass `resolution` as `5S` for seconds, or as a minute value such as `1`, `5` or `60`.
* Set `include_oi` to 1 to add `open_interest`. Set `include_greeks` to 1 to add `implied_volatility`, `delta`, `gamma`, `theta` and `vega` to each candle.
* `include_greeks=1` works only for CE and PE contracts. A futures request with it returns a validation error.
* Invalid input returns HTTP `422` with code `-50`. For example, `include_greeks=2` is rejected because it must be 0 or 1.
* A valid request with no candles returns `s` as `no_data` and an empty `candles` array. Treat this as an empty result, not a failure.
* Greek values can be `null` for a candle. The API does not copy the previous candle or use zero, so handle `null` before calculating.
* Read optional columns by name from `columns`. Only the first six (timestamp, open, high, low, close, volume) are fixed.
* If data is not available for the contract, exchange or date range, the API returns an error.
* Historical data is available from different dates for each exchange.
* Historical data before the availability date for an exchange cannot be retrieved. The requested date range must also be within the limit for the selected resolution.

Plan limits

Standard plan

* Daily candles: last 2 years
* Intraday candles: 10 API requests per day

Prime plan

* Daily candles: 7+ years
* Intraday candles: as per Prime API overall rate limits

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

#### Historical Data Availability

| **Exchange** | **Historical Data Available From** |
| --- | --- |
| `NSE` | 10 October 2018 |
| `BSE` | 07 August 2023 |
| `MCX` | 11 October 2018 |

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol`\* | string | Expired Futures or Options contract symbol. Eg: NSE:NIFTY25MAR23000CE |
| `resolution`\* | string | * The candle resolution. Supported values are: 5 seconds : "5S" * 1 minute : "1" * 2 minute : "2" * 3 minute : "3" * 5 minute : "5" * 10 minute : "10" * 15 minute : "15" * 20 minute : "20" * 30 minute : "30" * 45 minute : "45" * 60 minute : "60" * 120 minute : "120" * 180 minute : "180" * 240 minute : "240" * 1 Day : "1D" * 1 week : "1W" * 1 month : "1M" |
| `date_format`\* | int | date\_format is a boolean flag. 0 to enter the epoch value. 1 to enter the date format as yyyy-mm-dd. |
| `range_from`\* | string | Indicating the start date of records. Accepts epoch value if date\_format flag is set to 0. Accepts yyyy-mm-dd format if date\_format flag is set to 1. |
| `range_to`\* | string | Indicating the end date of records. Accepts epoch value if date\_format flag is set to 0. Accepts yyyy-mm-dd format if date\_format flag is set to 1. |
| `include_oi` | int | set flag to "1" to enable oi as a part of the response. |
| `include_greeks` | int | set flag to "1" to enable greeks as a part of the response. |

#### How the two flags change the rows

| **include\_oi** | **include\_greeks** | **Fields after core OHLCV** |
| --- | --- | --- |
| 0 / empty | 0 / empty | None |
| 1 | 0 / empty | `open_interest` |
| 0 / empty | 1 | `implied_volatility`, `delta`, `gamma`, `theta`, `vega` |
| 1 | 1 | `open_interest`, then all five Greek fields |

**Note:** Options only: `include_greeks=1` is accepted only for CE or PE contracts. A Futures request with this flag returns a validation error.

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / no\_data / error |
| `symbol` | string | Expired contract symbol for which the data is returned |
| `resolution` | string | Resolution of the returned candles |
| `columns` | array | Column names for each candle, in the order returned: timestamp, open, high, low, close, volume. An `open_interest` column is appended when `include_oi` is set to 1. The `iv`, `delta`, `gamma`, `theta` and `vega` columns are appended (after `open_interest`, if present) when `include_greeks` is set to 1. |
| `candles` | array | * Candles data containing array of following data for particular time stamp: * 1.Current epoch time * 2. Open Value * 3.Highest Value * 4.Lowest Value * 5.Close Value * 6.Total traded quantity (volume) * 7.Open interest (only when `include_oi` is 1) * 8.Implied volatility (only when `include_greeks` is 1) * 9.Delta (only when `include_greeks` is 1) * 10.Gamma (only when `include_greeks` is 1) * 11.Theta (only when `include_greeks` is 1) * 12.Vega (only when `include_greeks` is 1) |
| `schema_version` | int | Version of the response schema |

**Note**: The API returns an error if historical data is not available for the specified contract, exchange, or date range.

#### Stable core columns

| **Index** | **Column** | **Meaning** |
| --- | --- | --- |
| 0 | `timestamp` | Candle time as UNIX epoch seconds. |
| 1 | `open` | First price in the candle. |
| 2 | `high` | Highest price in the candle. |
| 3 | `low` | Lowest price in the candle. |
| 4 | `close` | Last price in the candle. |
| 5 | `volume` | Volume for the candle. |

Optional values are appended after index 5. Clients should use `columns` instead of hard-coding optional indexes.

#### OI and Greek fields

| **Column** | **Returned when** | **Simple meaning** |
| --- | --- | --- |
| `open_interest` | `include_oi=1` | Open Interest stored for the candle. |
| `implied_volatility` | `include_greeks=1` | Calculated IV in percent. Example: 11.87 means 11.87%. |
| `delta` | `include_greeks=1` | Estimated option-price change for a one-point change in the underlying. |
| `gamma` | `include_greeks=1` | Estimated Delta change for a one-point change in the underlying. |
| `theta` | `include_greeks=1` | Estimated one-day time effect on the option price. |
| `vega` | `include_greeks=1` | Estimated option-price change for a one-percentage-point IV change. |

#### No data, null Greeks, and errors

**Valid request with no candles**

`s` is `no_data`. The requested column layout is still returned, but `candles` is empty.

```
{
  "s": "no_data",
  "schema_version": 1,
  "symbol": "NSE:BANKNIFTY2342042600PE",
  "resolution": "1",
  "greeks_at": "candle_close",
  "columns": [
    "timestamp", "open", "high", "low", "close", "volume",
    "open_interest", "implied_volatility", "delta", "gamma",
    "theta", "vega"
  ],
  "candles": []
}
```

**Greek unavailable for one candle**

The five Greek positions are `null`. The API does not copy values from the previous candle and does not replace missing values with zero.

```
"columns": [
  "timestamp", "open", "high", "low", "close", "volume",
  "implied_volatility", "delta", "gamma", "theta", "vega"
],
"candles": [
  [1681357500, 1080.45, 1080.50, 1080.45, 1080.50, 76,
   null, null, null, null, null]
]
```

**Validation error**

Invalid input returns HTTP `422`. Here, `include_greeks=2` is rejected.

```
{
  "code": -50,
  "data": {
    "include_greeks": "include_greeks should be either 0 or 1"
  },
  "message": "Invalid input",
  "s": "error"
}
```

**Safe client handling**
1. Check `s`.
2. For `ok`, map every candle row using `columns`.
3. For `no_data`, treat `candles: []` as a valid empty result.
4. For `error`, read `code`, `message`, and optional `data`.
5. Handle `null` OI or Greek values before calculations.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol": "NSE:NIFTY25MAR23000CE",
    "resolution": "60",
    "date_format": "1",
    "range_from": "2025-03-26",
    "range_to": "2025-03-27",
    "include_oi": "1",
    "include_greeks": "1"
}

response = fyers.fno_historical_data(data)
print(response)
for candle in response["candles"]:
    print(candle)
```

```
{
    "candles": [
        [1742960700, 730.00, 750.00, 645.00, 706.00, 359100, 5131225, 17.84, 0.8127, 0.0006, -38.52, 4.21],
        [1742964300, 706.00, 760.00, 651.30, 680.50, 246225, 5019500, 18.36, 0.7612, 0.0007, -41.07, 4.88],
        [1742967900, 680.50, 708.85, 608.00, 640.00, 146025, 4987175, 18.92, 0.7245, 0.0008, -43.66, 5.23],
        [1742971500, 636.90, 670.35, 594.50, 606.50, 376875, 4776350, 19.47, 0.6883, 0.0008, -45.19, 5.61]
    ],
    "columns": ["timestamp", "open", "high", "low", "close", "volume", "open_interest", "iv", "delta", "gamma", "theta", "vega"],
    "resolution": "60",
    "s": "ok",
    "schema_version": 1,
    "symbol": "NSE:NIFTY25MAR23000CE"
}
```

## Configuration

*Source: https://fyers.in/api-docs/v3/api/market-data/screeners/config/ (last updated 2026-10-14)*

This API returns the list of all screeners and the exact values each screener accepts. Every id you send to the other three Screeners APIs comes from this response.

USE CASE

Load the list of screeners once, to build a screener menu or to check a request before you run a Standard, Candlestick or Technical screener.

Note

* This API takes no parameters.
* Sending any parameter returns HTTP 400.

Details

* Send your App ID and access token in the Authorization header as `APP_ID:ACCESS_TOKEN`.
* Only GET is supported. Any other method returns HTTP 405.
* The response holds the keys listed in the table below.
* Every screener has: `id` (send it as `screener_id`), `name`, `category`, `description`, `conditions` (the rule a row must meet), `order_by` and `order` (the default sort), `default_universe` and `supported_params` (the only parameters it accepts besides `screener_id`).
* Standard screeners also have `universe_group`, `column_group`, `default_timeframe` and `allowed_timeframes`. For a screener that takes no timeframe, `default_timeframe` is null and `allowed_timeframes` is empty.
* Candlestick and Technical screeners have an empty `supported_params`, because they take only `screener_id`.
* The `screeners_standard` array contains the following screener categories:
* Each object in `screeners_standard`, `screeners_technical`, and `screeners_candlestick` represents an available screener.
* **Columns**
* Price & Volume
* Returns
* F&O
* Valuation Ratios
* Growth
* Margin & Profitability
* P&L – Annual
* Quarterly
* Balance Sheet
* Solvency & Liquidity
* Cash Flow
* Others
* The column `id` can also appear in the `order_by` field of a screener object.
* The `timeframes` array contains the supported periods for measuring price changes.
* **Universes**
* Broad indices
* Sector indices
* NSE, BSE, and F&O stocks
* Sector and industry groups
* ETFs and other instruments
* ETF instrument classifications

The `columns` array contains the fields supported in screener results. Columns are grouped into categories such as:
A universe defines the group of instruments on which a screener is applied.

#### Cash-market universes

The `universes` array includes:

#### Futures universes

Returned in `universes\_futures`.

#### Options universes

Returned in `universes\_options`.

Plan limits

Standard plan

* 50 requests per day

Prime plan

* As per Prime API overall rate limits
* 10 requests per second
* 500 requests per minute
* 5,00,000 requests per day

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

#### Screener types

| **Screener type** | Description |
| --- | --- |
| `Standard Screeners` | Includes predefined screeners based on price movement, volume, breakouts, futures, options, commodities, fundamentals, ETFs, and other market conditions. These screeners are returned in the `screeners_standard` array. |
| `Technical Crossovers and Momentum` | Includes screeners based on technical indicators, moving-average crossovers, and momentum conditions such as MACD, Golden Crossover, Death Crossover, and Money Flow Index signals. These screeners are returned in the `screeners_technical` array. |
| `Candlestick Screeners – EOD` | Includes end-of-day candlestick pattern screeners used to identify bullish, bearish, reversal, and continuation patterns. These screeners are returned in the `screeners_candlestick` array. |

#### Standard screener categories

| **Category** | Description |
| --- | --- |
| `Intraday Screeners` | Identifies intraday price movement, volume activity, gaps, reversals, circuit activity, and stocks trading near their daily highs or lows. |
| `Breakout with Volume` | Identifies stocks reaching new highs or lows across different periods with higher-than-average trading volume. |
| `Technical Crossovers and Momentum` | Identifies consecutive higher highs, lower lows, higher closes, and lower closes based on recent price movement. |
| `Commodities Futures` | Identifies commodity futures based on price movement, premium, open interest, position buildup, and expiry. |
| `Futures Scan` | Identifies futures contracts based on price movement, premium, open interest, and long or short position activity. |
| `Options Trading` | Identifies options contracts based on premium movement, open-interest changes, and long or short position activity. |
| `Fresh Breakouts` | Identifies stocks reaching new periodic highs or lows or crossing key support and resistance levels. |
| `Near Breakouts` | Identifies stocks trading close to their periodic or all-time highs and lows. |
| `Fundamentals` | Identifies companies based on valuation, growth, profitability, debt, dividend, and cash-flow conditions. |
| `ETF` | Identifies exchange-traded funds based on price movement, proximity to yearly highs or lows, and instrument classification. |

#### Screener object

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of the screener. Use this value when requesting results for a specific screener. |
| `name` | string | Display name of the screener. |
| `category` | string | Category under which the screener is grouped. |
| `description` | string | Brief explanation of the market condition identified by the screener. |
| `conditions` | string | Conditions used to identify matching instruments. This field can be empty for system-defined technical or candlestick screeners. |
| `order_by` | string | Column identifier used to sort the screener results. |
| `order` | string | Sorting direction applied to the results. Supported values are `asc` and `desc`. |

#### Column object

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of the column. |
| `name` | string | Display name of the column. |
| `category` | string | Category under which the column is grouped. |

#### Timeframes

| **Timeframe** | Description |
| --- | --- |
| `1 minute` | Percentage change over one minute. |
| `5 minutes` | Percentage change over five minutes. |
| `15 minutes` | Percentage change over 15 minutes. |
| `30 minutes` | Percentage change over 30 minutes. |
| `1 hour` | Percentage change over one hour. |
| `1 day` | Percentage change for the current trading day. |
| `1 week` | Percentage change over one week. |
| `1 month` | Percentage change over one month. |
| `3 months` | Percentage change over three months. |
| `6 months` | Percentage change over six months. |
| `Year to date` | Percentage change from the beginning of the current calendar year. |
| `52 weeks` | Percentage change over the previous 52 weeks. |
| `2 years` | Percentage change over two years. |
| `3 years` | Percentage change over three years. |
| `5 years` | Percentage change over five years. |
| `All time` | Percentage change across the complete available trading history. |

#### Timeframe object

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of the timeframe. |
| `name` | string | Display name of the timeframe. |

| **Universe** | Description |
| --- | --- |
| `Index Based Futures` | Includes futures contracts based on supported market indices. |
| `Stock Based Futures` | Includes futures contracts based on individual stocks. |
| `Commodity Based Futures` | Includes supported commodity futures contracts. |

| **Universe** | Description |
| --- | --- |
| `Index Based Options` | Includes options contracts based on supported market indices. |
| `Stock Based Options` | Includes options contracts based on individual stocks. |
| `Commodity Based Options` | Includes supported commodity options contracts. |

#### Universe object

| Attribute | Data Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of the universe. |
| `name` | string | Display name of the universe. |
| `category` | string | Category under which the universe is grouped. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `data` | object | Contains `screeners_standard`, `screeners_technical`, `screeners_candlestick`, `columns`, `timeframes`, `universes`, `universes_futures`, and |
| `universes_options` | array | s |

### Sorting behaviour

Screener results are sorted using the values returned in `order\_by` and `order`.

* `order_by` identifies the column used for sorting.

* `asc` sorts the values from lowest to highest.

* `desc` sorts the values from highest to lowest.

For example, the `top_gainers` screener uses `t0_per_change` with the sorting order `desc`, which displays instruments with the highest one-day percentage change first.

### Response keys

| Attribute | What it holds | Use it for |
| --- | --- | --- |
| `screeners_standard` | 111 Standard screeners | `screener_id` of the Standard API |
| `screeners_candlestick` | 23 Candlestick screeners | `screener_id` of the Candlestick API |
| `screeners_technical` | 6 Technical screeners | `screener_id` of the Technical API |
| `columns` | The 118 Standard fields: `id`, `name` (display label) and `category` | `fields` and `order_by` |
| `column_groups` | Which field ids each group allows: `equity` (103), `fno` (45), `commodity` (45) | The fields a screener accepts |
| `universes`, `universes_futures`, `universes_options` | Universe ids and names (97, 3 and 3) | `universe` |
| `universe_groups` | Which universe ids each group allows | The universes a screener accepts |
| `timeframes` | The 16 timeframe ids, from `t0_1min` (1 minute) to `alltime` (all time) | `timeframe` |
| `option_types`, `expiry_types` | `CE`, `PE` and `W` (weekly), `M` (monthly) | `option_type`; reading expiries |
| `expiries` | Upcoming expiries of `fw001`, `fw002`, `ow001` and `ow002`, each with `epoch`, `date` and `display` | `expiry` |

### How to build a valid Standard request

* Find the screener in `screeners_standard`. Note its `id`, `universe_group`, `column_group`, `allowed_timeframes` and `supported_params`.
* `fields`: pick up to 10 ids from `column_groups[column_group]`.
* `universe`: pick one id from `universe_groups[universe_group]`. Leave it out to use `default_universe`.
* `timeframe`: pick one of `allowed_timeframes`. Leave it out to use `default_timeframe`.
* `expiry`: only if `expiry` is in `supported_params` and the universe is `fw001`, `fw002`, `ow001` or `ow002`. Use an epoch from `expiries[universe]`.
* Send only the parameters listed in `supported_params`.

### Notes

* The expiry lists change as contracts expire, so call this API at least once a day.
* `supported_params` can list `expiry` for a screener that also runs on commodity universes. Commodity universes do not accept an expiry, so check `expiries` for the universe before you send one.
* A field's `id` and `name` here are the `unique_key` and `description` of the same field in a screener's response header.
* The `conditions` field describes the default logic used by a predefined screener. It can be empty for technical, candlestick, expiry-based or instrument-classification screeners whose calculation logic is managed internally.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

response = fyers.screeners_config()
print(response)
```

```
{
  "code": 200,
  "message": "",
  "s": "ok",
  "data": {
    "screeners_standard": [
      {
        "id": "top_gainers",
        "name": "Top Gainers",
        "category": "Intraday Screeners",
        "description": "Stocks with the biggest price increases in the selected timeframe.",
        "conditions": "Selected Time Frame Chg % > 0 AND Day's Volume > 0",
        "order_by": "t0_per_change",
        "order": "desc",
        "default_universe": "iw010",
        "universe_group": "equity",
        "column_group": "equity",
        "supported_params": [
          "fields",
          "universe",
          "order_by",
          "order",
          "timeframe"
        ],
        "default_timeframe": "t0",
        "allowed_timeframes": [
          "t0",
          "c1_week",
          "c1_month",
          "c3_month",
          "c6_month",
          "ytd",
          "c52_week",
          "c2_year",
          "c3_year",
          "c5_year",
          "alltime"
        ]
      }
    ],
    "screeners_technical": [
      {
        "id": "mfi_overbought",
        "name": "Overbought by MFI",
        "category": "Technical Crossovers and Momentum",
        "description": "Stocks that may be overbought, according to the money flow index.",
        "conditions": "",
        "order_by": "t0_per_change",
        "order": "asc",
        "default_universe": "iw010",
        "supported_params": []
      }
    ],
    "screeners_candlestick": [
      {
        "id": "hammer",
        "name": "Hammer",
        "category": "Candlestick Screeners - EOD",
        "description": "A bullish reversal pattern where prices recover after dipping significantly lower during the day.",
        "conditions": "",
        "order_by": "t0_per_change",
        "order": "desc",
        "default_universe": "iw010",
        "supported_params": []
      }
    ],
    "columns": [
      {
        "id": "symbolticker",
        "name": "Symbol",
        "category": "Others"
      },
      {
        "id": "t0_close_ltp",
        "name": "Price",
        "category": "Price & Volume"
      }
    ],
    "universes": [
      {
        "id": "iw001",
        "name": "Nifty 50",
        "category": "Broad Indices"
      },
      {
        "id": "iw002",
        "name": "Nifty Next 50",
        "category": "Broad Indices"
      }
    ],
    "timeframes": [
      {
        "id": "t0_1min",
        "name": "1 min"
      },
      {
        "id": "t0_5min",
        "name": "5 min"
      }
    ]
  }
}
```

## Standard screeners

*Source: https://fyers.in/api-docs/v3/api/market-data/screeners/standard-screeners/ (last updated 2026-10-14)*

This API runs a Standard screener and returns the stocks, contracts or ETFs that meet its conditions, with the fields you choose.

USE CASE

Find today's top gainers in a universe, stock futures with long build-up in the last 15 minutes, or stocks near their 52-week high, and get the values you need for each one in a single call.

Note

* One call returns at most 500 rows and 10 fields.
* There is no paging: to see other rows, change the sort or narrow the universe.

Details

* Send your App ID and access token in the Authorization header as `APP_ID:ACCESS_TOKEN`. Only GET is supported.
* There are 111 Standard screeners in 10 categories: Intraday Screeners, Breakout with Volume, Fresh Breakouts, Near Breakouts, Technical Crossovers and Momentum, Fundamentals, Futures Scan, Options Trading, Commodities Futures and ETF. Take ids, rules and defaults from the Configuration API.
* Parameters are sent in the URL query string (names are case-sensitive, values are not). See Request Attributes below.
* A parameter works only if it is in the screener's `supported_params`. Any other parameter returns HTTP 400, including `limit`, `offset` and `page`.
* `symbolticker` is always returned first and does not count towards the 10 fields.
* The timeframe sets the period of Selected Time Frame in the screener's conditions and of its default sort field, for example `t0_5min_per_change_oi` becomes `t0_15min_per_change_oi`. For a screener whose conditions use only Day's values, it changes the default sort field only.
* Every returned row meets the screener's conditions. The sort decides the row order and, when more than 500 rows match, which 500 are returned. The default sorts put the strongest matches first.
* The response holds `header` (one object per column: `unique_key`, `description`, `data_type` and, for most fields, `tool_tip`) and `body` (one array per row, values in header order). `body` is empty when nothing matches.
* The response also returns the settings that were applied, including defaults: `universe`, `timeframe`, `expiry`, `option_type`, `order_by` and `order`. A setting is null when the screener does not use it, or when all expiries or both option types are returned.
* `fetch_time` is when the response was built and `last_update_time` is when the screener's data was last refreshed, both in Unix epoch seconds.
* How fresh the data is: during market hours results are real time, so both times equal the time of your call and move with the clock. After the close, `last_update_time` shows the last refresh: 15:30 IST for equity and ETF screeners and 15:40 IST for F&O screeners. Commodity screeners keep refreshing while MCX is open.

Plan limits

Standard plan

* 50 requests per day

Prime plan

* As per Prime API overall rate limits
* 10 requests per second
* 500 requests per minute
* 5,00,000 requests per day

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `screener_id`\* | string | Mandatory. Screener `id` from the `screeners_standard` array in the config response. Eg: `top_gainers` |
| `fields` | string | Optional. Comma-separated list of column or timeframe `id`s. Maximum 10 fields. `symbolticker` is always included in the response. |
| `universe` | string | Optional. Cash-market universe `id` from the `universes` array only. Default: `iw010` (Nifty 500). |
| `order_by` | string | Optional. Column or timeframe `id` used to sort results. |
| `order` | string | Optional. Sorting direction. Allowed values: `asc`, `desc`. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `data` | object | Result payload |
| `data.header` | array | Column metadata for the result set |
| `data.body` | array | Result rows |
| `data.error` | string | Error detail when applicable |
| `data.last_update_time` | int | Epoch timestamp of the last data update |

### Finding a field and its meaning

* Look the field up in `columns` of the Configuration API. Each entry gives `id` (what you send in `fields` and `order_by`), `name` (the label) and `category`.
* The 118 fields fall in 12 categories: Others, Price & Volume, Returns, F&O, Valuation Ratios, Growth, Margin & Profitability, P&L - Annual, Quarterly, Balance Sheet, Solvency & Liquidity and Cash Flow.
* A screener accepts only the fields of its `column_group`. Take them from `column_groups[column_group]` in the same response.
* The `header` of a Standard response repeats each field: `unique_key` is the field id and `description` is its name. Most fields also carry a `tool_tip` with a short explanation; where `tool_tip` is missing, the name is the only description.

### Timeframe ids

The full list is in `timeframes` of the Configuration API. A screener accepts only its `allowed_timeframes`.

| timeframe | Meaning | timeframe | Meaning |
| --- | --- | --- | --- |
| `t0_1min` | 1 min | `c3_month` | 3 months |
| `t0_5min` | 5 min | `c6_month` | 6 months |
| `t0_15min` | 15 min | `ytd` | YTD |
| `t0_30min` | 30 min | `c52_week` | 52 weeks |
| `t0_60min` | 1 hour | `c2_year` | 2 years |
| `t0` | 1 day | `c3_year` | 3 years |
| `c1_week` | 1 week | `c5_year` | 5 years |
| `c1_month` | 1 month | `alltime` | All time |

### Universe ids used on this page

All ids and names are in `universes`, `universes_futures` and `universes_options` of the Configuration API.

| universe | Attribute |
| --- | --- |
| `iw001` | Nifty 50 |
| `iw010` | Nifty 500 |
| `cs001` | All Stocks |
| `fw001` | Index Based Futures |
| `fw002` | Stock Based Futures |
| `ow001` | Index Based Options |
| `ow002` | Stock Based Options |
| `cw001` | Commodity Based Futures |

### Example requests

The query string is shown here; the endpoint is above.

* Top gainers over one week, with last price: `screener_id=top_gainers&timeframe=c1_week&fields=t0_close_ltp`
* Futures OI gainers on universe `fw002`: `screener_id=fut_oi_gainers&universe=fw002&fields=t0_close_ltp`
* Options OI gainers for one expiry, calls only: `screener_id=top_oi_gainers&universe=ow001&expiry=EPOCH&option_type=CE&fields=t0_close_ltp`, where `EPOCH` is a value from `expiries.ow001`

### Errors

| HTTP | code | When | message |
| --- | --- | --- | --- |
| 400 | -50 | `screener_id` missing | `screener_id is required` |
| 400 | -50 | `screener_id` unknown | `invalid screener_id` |
| 400 | -50 | More than 10 fields | `maximum 10 fields are allowed` |
| 400 | -50 | A value the screener does not accept | `invalid field FIELD for screener ID; see column_groups.GROUP in /config`, and the same for universe, timeframe and expiry |
| 400 | -50 | A parameter the screener does not support | `PARAMETER is not supported for screener ID` or `unsupported query parameter: NAME` |
| 401 | -16 | Missing or wrong token | `Could not authenticate the user` |
| 404 | -50 | Wrong path | `endpoint not found` |
| 405 | -50 | Method other than GET | `method not allowed; use GET` |
| 429 |  | Rate limit crossed | Wait, then retry |

A failed call returns `"s": "error"`; a successful one returns `"s": "ok"`. In the messages above, FIELD, ID, GROUP, PARAMETER and NAME stand for the values in your request.

### Notes

* A parameter sent with a blank value counts as not sent, but only if the screener supports that parameter.
* Prices and money values (`ttv`, `market_cap`, balance-sheet and P&L fields) are in rupees, not crore. Fields named (%) are percentages: 2.5 means 2.5%. The `conditions` text writes amounts in crore (cr) and rupees (Rs).
* Some money values carry long decimals, for example 40574899902.34375. Round them for display.
* `leverage` (MTF Leverage) is text, such as 2.5x, or - when the stock is not eligible for MTF.
* `expiry` is returned in Unix epoch seconds; `expiry_type` is W (weekly) or M (monthly).
* `pnl_1pct_move` (Near Expiry - Commodities) is the profit or loss on one lot for a 1% price move: LTP × units per lot × 1%, rounded.
* An empty `body` is a valid answer: it means no row meets the conditions at that moment.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

data = {
    "screener_id": "top_gainers",
    "fields": "t0_close_ltp,t0_per_change,t0_volume"
}

response = fyers.screeners_standard(data=data)
print(response)
```

```
{
  "code": 200,
  "message": "",
  "s": "ok",
  "data": {
    "body": [
      [
        "NSE:PPLPHARMA-EQ",
        232.8,
        17.15,
        118072228
      ],
      [
        "NSE:SYNGENE-EQ",
        410.85,
        12.19,
        32965479
      ]
    ],
    "expiry": null,
    "fetch_time": 1793183914,
    "header": [
      {
        "data_type": "string",
        "description": "Symbol",
        "unique_key": "symbolticker"
      },
      {
        "data_type": "double",
        "description": "Price",
        "tool_tip": "Latest traded price of the stock or contract.",
        "unique_key": "t0_close_ltp"
      },
      {
        "data_type": "double",
        "description": "1D Chg (%)",
        "tool_tip": "Percentage change in price from the previous trading session's close.",
        "unique_key": "t0_per_change"
      },
      {
        "data_type": "double",
        "description": "Volume",
        "tool_tip": "Total quantity traded during the current trading session.",
        "unique_key": "t0_volume"
      }
    ],
    "last_update_time": 1793181600,
    "option_type": null,
    "order": "desc",
    "order_by": "t0_per_change",
    "timeframe": "t0",
    "universe": "iw010"
  }
}
```

## Candlestick screeners

*Source: https://fyers.in/api-docs/v3/api/market-data/screeners/candlestick-screeners/ (last updated 2026-10-14)*

This API returns the Nifty 500 stocks that formed a given candlestick pattern on the previous trading session’s daily candle.

USE CASE

Shortlist Nifty 500 stocks that formed a Hammer, Morning Star or Bullish Engulfing pattern, as reversal candidates for the next session.

Note

* This API takes only `screener_id`.
* The stocks scanned, the columns returned and the sort are fixed.
* Sending any other parameter returns HTTP 400.

Details

* Send your App ID and access token in the Authorization header as `APP_ID:ACCESS_TOKEN`. Only GET is supported.
* There are 23 Candlestick screeners. 13 bullish: Dragonfly Doji, Inverted Hammer, Hammer, White Marubozu, Bullish Harami, Bullish Harami Cross, Bullish Engulfing Pattern, Piercing Line, Upside Tasuki Gap, Morning Star, Three White Soldiers, Bullish Kicking, Bullish Abandoned Baby. 10 bearish: Black Marubozu, Hanging Man, Shooting Star, Bearish Harami, Bearish Engulfing, Dark Cloud Cover, Bearish Harami Cross, Bearish Abandoned Baby, Identical Three Crows, Downside Tasuki Gap.
* Take the `screener_id` from `screeners_candlestick` in the Configuration API.
* Every screener scans the Nifty 500 (`iw010`).
* Every screener returns the same 7 columns: `symbolticker` (symbol), `week_change_p` (week change %), `sma_5` (day SMA 5), `ema_5` (day EMA 5), `sma_10` (day SMA 10), `net_bullish_candlestick` (day candlestick strength: bullish minus bearish) and `prev_close` (previous day close).
* Rows are sorted by 1-day change: highest first for bullish patterns, lowest first for bearish patterns. The 1-day change itself is not returned.
* The response holds `header` (one object per column: `unique_key`, `description`, `data_type`), `body` (one array per row, values in header order), `total_count` (number of rows returned) and `last_update_time` (Unix epoch seconds). `body` is empty when no stock formed the pattern.
* How fresh the data is: patterns are found on the previous trading session's daily candle. Results are computed once, at 09:15 IST, and stay the same until 09:15 of the next trading day. `last_update_time` shows 09:15 of the current day. `prev_close` is the close of that candle, that is, the previous trading day's close.

Plan limits

Standard plan

* 50 requests per day

Prime plan

* As per Prime API overall rate limits
* 10 requests per second
* 500 requests per minute
* 5,00,000 requests per day

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `screener_id`\* | string | Mandatory. Screener `id` from the `screeners_candlestick` array. Only the `screener_id` query parameter is accepted. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | ok / error |
| `code` | int | This is the code to identify specific responses |
| `message` | string | This is the message to identify the specific error responses |
| `data` | object | Result payload with `header`, `body`, `error`, and `last_update_time` |

### Screener ids

The id is not always the name in lower case (for example Bullish Abandoned Baby is `abandoned_baby_bottom`), so take it from this table or from Configuration.

| Screener | screener\_id | Data Type |
| --- | --- | --- |
| Dragonfly Doji | `dragonfly_doji` | Bullish |
| Inverted Hammer | `inverted_hammer` | Bullish |
| Hammer | `hammer` | Bullish |
| White Marubozu | `white_marubozu` | Bullish |
| Bullish Harami | `bullish_harami` | Bullish |
| Bullish Harami Cross | `bullish_harami_cross` | Bullish |
| Bullish Engulfing Pattern | `bullish_engulfing_pattern` | Bullish |
| Piercing Line | `piercing_line` | Bullish |
| Upside Tasuki Gap | `upside_tasuki_gap` | Bullish |
| Morning Star | `morning_star` | Bullish |
| Three White Soldiers | `three_white_soldiers` | Bullish |
| Bullish Kicking | `bullish_kicking` | Bullish |
| Bullish Abandoned Baby | `abandoned_baby_bottom` | Bullish |
| Black Marubozu | `black_marubozu` | Bearish |
| Hanging Man | `hanging_man` | Bearish |
| Shooting Star | `shooting_star` | Bearish |
| Bearish Harami | `bearish_harami` | Bearish |
| Bearish Engulfing | `bearish_engulfing` | Bearish |
| Dark Cloud Cover | `dark_cloud_cover` | Bearish |
| Bearish Harami Cross | `bearish_harami_cross` | Bearish |
| Bearish Abandoned Baby | `abandoned_baby_top` | Bearish |
| Identical Three Crows | `identical_three_crows` | Bearish |
| Downside Tasuki Gap | `downside_tasuki_gap` | Bearish |

### Example request

`screener_id=hammer`

### Errors

| HTTP | code | When | message |
| --- | --- | --- | --- |
| 400 | -50 | `screener_id` missing | `screener_id is required` |
| 400 | -50 | `screener_id` unknown, or taken from another Screeners API | `invalid screener_id` |
| 400 | -50 | Any other parameter | `unsupported query parameter: NAME` |
| 401 | -16 | Missing or wrong token | `Could not authenticate the user` |
| 405 | -50 | Method other than GET | `method not allowed; use GET` |
| 429 |  | Rate limit crossed | Wait, then retry |

In the message above, NAME stands for the parameter you sent.

### Notes

* Unlike Standard screeners, the response does not return the applied settings or `fetch_time`.

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

data = {
    "screener_id": "hammer"
}

response = fyers.screeners_candlestick(data=data)
print(response)
```

```
{
  "code": 200,
  "message": "",
  "s": "ok",
  "data": {
    "body": [
      [
        "NSE:ICICILIFE-EQ",
        -7.52,
        421.52,
        420.54,
        433.16,
        1,
        409.55
      ],
      [
        "NSE:AEGISLOG-EQ",
        -9.82,
        1273.1,
        1269.54,
        1335.57,
        1,
        1200.1
      ]
    ],
    "header": [
      {
        "data_type": "string",
        "description": "Symbol",
        "unique_key": "symbolticker"
      },
      {
        "data_type": "double",
        "description": "Week change %",
        "unique_key": "week_change_p"
      },
      {
        "data_type": "double",
        "description": "Day SMA5",
        "unique_key": "sma_5"
      },
      {
        "data_type": "double",
        "description": "Day EMA5",
        "unique_key": "ema_5"
      },
      {
        "data_type": "double",
        "description": "Day SMA10",
        "unique_key": "sma_10"
      },
      {
        "data_type": "double",
        "description": "Day Candlestick Strength [Bullish minus Bearish]",
        "unique_key": "net_bullish_candlestick"
      },
      {
        "data_type": "double",
        "description": "Prev Day Close",
        "unique_key": "prev_close"
      }
    ],
    "last_update_time": 1793159100,
    "total_count": 3
  }
}
```

## Activate Kill Switch

*Source: https://fyers.in/api-docs/v3/api/account/kill-switch/activate-kill-switch/ (last updated 2026-10-14)*

This API pauses trading across all segments on your account.

USE CASE

Use this API when you want to stop the trading for the day.

Details

* Before activating Kill Switch, you need to close all open positions and cancel pending orders. You can keep your pending GTT orders.
* Once Kill Switch is active, you cannot take any new positions across all trading segments.
* When you activate Kill Switch through the API, Web or App, it applies across all platforms. You can check its status using the [Kill Switch Status](https://fyers.in/api-docs/v3/api/account/kill-switch/kill-switch-status/) API.
* Trading resumes automatically on the next trading day.
* If your account is blocked, debarred or has a pending closure request, Kill Switch cannot be activated.
* If the request fails due to a network issue or timeout, the API returns HTTP 502 or 504 with `code` -99 and the message "Something went wrong. Please contact support". You can try again after some time.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status - "ok" on success, "error" on failure. |
| `code` | int | Response status code. 200 on success. On a failure it is the error code, for example 1500. |
| `message` | string | Human-readable message about the result. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

## Make a request to activate the kill switch
## Note: this blocks trading on the account
response = fyers.activate_killswitch()

## Print the response received from the Fyers API
print(response)
```

```
{
  "code": 200,
  "message": "Client placed on Break. ",
  "s": "ok"
}
```

## Kill Switch Status

*Source: https://fyers.in/api-docs/v3/api/account/kill-switch/kill-switch-status/ (last updated 2026-10-14)*

This API lets you check whether Kill Switch is active on your account.

USE CASE

Check Kill Switch status before placing orders or after activating it through the FYERS API, Web or App.

Details

* The `killswitch` field returns `true` when Kill Switch is active and `false` when it is inactive. The `openPositions` and `pendingOrders` fields show the number of open positions and pending orders in your FYERS account.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `killswitch` | boolean | `true` when Kill Switch is active, `false` when it is not. |
| `openPositions` | int | Number of open positions on your account. |
| `pendingOrders` | int | Number of pending orders on your account. |
| `message` | string | Human-readable status, for example "Kill Switch is activated." |
| `code` | int | Response status code. 200 on success. |
| `s` | string | Request status - "ok" on success, "error" on failure. |

Request

```
from fyers_apiv3 import fyersModel

client_id = "XC4XXXXM-100"
access_token = "eyJ0eXXXXXXXX2c5-Y3RgS8wR14g"

## Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, is_async=False, log_path="")

## Make a request to get the kill switch status
response = fyers.get_killswitch_status()

## Print the response received from the Fyers API
print(response)
```

```
// Kill Switch not active
{
    "killswitch": false,
    "openPositions": 0,
    "pendingOrders": 0,
    "message": "Kill Switch is not activated.",
    "code": 200,
    "s": "ok"
}

// Kill Switch active
{
    "killswitch": true,
    "openPositions": 0,
    "pendingOrders": 0,
    "message": "Kill Switch is activated.",
    "code": 200,
    "s": "ok"
}
```

## EDIS Details

*Source: https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-details/ (last updated 2026-10-14)*

This API allows you to fetch the holding authorisations you have already completed.

USE CASE

Check which holdings are authorised for sale, with the quantity authorised and the quantity already used.

Details

* This API provides information about holding authorizations that have been successfully completed.
* The request takes no parameters. Send only the `Authorization` header.
* Only authorisations that were completed successfully are listed. You can sell only authorised holdings.
* `qty` is the quantity authorised and `qtyUtlize` is the part of it already used.
* `startDate`, `endDate` and `noOfDays` show how long the authorisation stays valid. The CDSL page states that an authorisation is valid till the end of the day, whether or not the sell is completed.
* `status` and `reason` describe the outcome of the transaction. `errCode` is `NA` when there is no error and `errorCount` gives the number of errors.
* `transactionId` is the ID to use with [EDIS Inquiry](https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-inquiry/). `source` is a code for where the transaction was started (`W` in the sample response).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `clientId` | string | Client ID of the account for which the holding authorization was processed. |
| `isin` | string | ISIN of the security for which the holding authorization was completed. |
| `qty` | float | Quantity of the security authorized. |
| `qtyUtlize` | float | Quantity of the authorized holding that has been utilized. |
| `entryDate` | string | Date and time on which the authorization entry was created. |
| `startDate` | string | Start date of the authorization's validity period. |
| `endDate` | string | End date of the authorization's validity period. |
| `noOfDays` | int | Number of days for which the authorization remains valid. |
| `source` | string | Source through which the authorization was initiated (e.g. `W` for web). |
| `status` | string | Status of the authorization transaction, e.g. `SUCCESS`. |
| `reason` | string | Description of the outcome of the authorization transaction. |
| `internalTxnId` | string | Internal transaction ID generated by FYERS for the authorization. |
| `dpTxnId` | string | Depository Participant (DP) transaction ID associated with the authorization. |
| `errCode` | string | Error code returned for the transaction, if any (`NA` when none). |
| `errorCount` | string | Count of errors encountered while processing the transaction. |
| `transactionId` | string | Unique transaction ID for the holding authorization, usable to query status via the Inquiry API. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl --location --request GET 'https://api.fyers.in/api/v2/details' \
 --header 'Authorization: app_id:access_token'
```

```
{"s": "ok", "code": 200, "message": "", "data": [{"clientId": "DXXXX4", "isin": "INE313D01013", "qty": 1.0, "qtyUtlize": 0.0, "entryDate": "07/06/2021 13:58:56", "startDate": "07/06/2021", "endDate": "07/06/2021", "noOfDays": 1, "source": "W", "status": "SUCCESS", "reason": "eDIS Transaction done successfully", "internalTxnId": "915485", "dpTxnId": "0706202171316317", "errCode": "NA", "errorCount": "0", "transactionId": "915484108176"}]
```

## TPIN Generation

*Source: https://fyers.in/api-docs/v3/api/account/edis-ddpi/tpin-generation/ (last updated 2026-10-14)*

This API allows you to generate the TPIN used to authorise the sale of holdings through CDSL or NSDL.

USE CASE

Get a TPIN before authorising a sell when POA is not submitted or DDPI is not activated.

Details

* TPIN is an authorization code generated by CDSL/NSDL respectively, using which the customer validates/authorises the transaction.
* The request takes no parameters. Send only the `Authorization` header.
* The TPIN is an authorisation code generated by CDSL or NSDL. The customer uses it to validate and authorise the transaction.
* The response does not contain the TPIN. On success `data` is an empty string and `message` confirms that the request was sent.
* Use [Verify DIS](https://fyers.in/api-docs/v3/api/account/edis-ddpi/verify-dis/) next, where the user authorises the holdings with the TPIN.
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Request status, e.g. "ok" on success. |
| `code` | int | Response status code, e.g. 200 on success. |
| `message` | string | Status message describing the result of the TPIN generation request. |
| `data` | string | Empty string on success; this API does not return additional payload data. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl --location --request GET 'https://api.fyers.in/api/v2/tpin'
--header 'Authorization: app_id:access_token'
```

```
{"s": "ok", "code": 200, "message": "Successfully sent request for BO Tpin generation", "data": ""}
```

## Verify DIS

*Source: https://fyers.in/api-docs/v3/api/account/edis-ddpi/verify-dis/ (last updated 2026-10-14)*

This API allows you to get the CDSL page where the user authorises holdings for sale.

USE CASE

Send the ISIN, quantity and symbol of the holdings to sell, and show the returned page for the user to authorise them.

Details

* This Api will provide you with the CDSL page to login where you can submit your Holdings information and accordingly you can provide the same to exchange to Sell your holdings.
* Send the holdings in `recordLst`. Each record needs `isin_code`, `qty` and `symbol`, for example `NSE:SAIL-EQ`.
* The `data` field of the response is HTML for the CDSL eDIS page. It contains a form that posts to CDSL, so render it for the user to log in and authorise the sell.
* The user needs the CDSL TPIN. The page has a Forgot CDSL TPIN link, and [TPIN Generation](https://fyers.in/api-docs/v3/api/account/edis-ddpi/tpin-generation/) requests a TPIN.
* The authorisation is valid till the end of the day, whether or not you complete the sell.
* You can sell only authorised holdings. Check the result with [EDIS Inquiry](https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-inquiry/) or [EDIS Details](https://fyers.in/api-docs/v3/api/account/edis-ddpi/edis-details/).
* Rate limits differ between the Standard and Prime plans. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Request Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `recordLst` | array | List of holding records to be authorized for the sell transaction via the CDSL eDIS page. |
| `recordLst[].isin_code` | string | ISIN code of the holding/security to be authorized. |
| `recordLst[].qty` | string | Quantity of the holding to be authorized for sale. |
| `recordLst[].symbol` | string | Trading symbol of the holding, e.g. `NSE:SAIL-EQ`. |

### Response Attributes

| Attribute | Data Type | Description |
| --- | --- | --- |
| `s` | string | Status of the request. Possible values: `ok`, `error`. |
| `code` | int | Response code returned by the API, e.g. `200`. |
| `message` | string | Response message (empty string on success). |
| `data` | string | HTML markup for the CDSL eDIS authorization page, containing an auto-submitting form (`action="https://eDIS.cdslindia.com/eDIS/VerifyDIS"`) that the client renders/loads so the user can log in and authorize the sell transaction (TPIN) for the holdings supplied in the request. |

Python is not available for this example. Showing cURL instead.

RequestcURL

```
curl --location --request POST 'https://api.fyers.in/api/v2/index' --header 'Authorization: app_id:accessToken' --header 'Content-Type: application/json'
 --data-raw '{"recordLst": [{"isin_code": "INE114A01011","qty": "1","symbol": "NSE:SAIL-EQ"}]}'
```

```
{"s": "ok", "code": 200, "message": "", "data": "<table width=\"100%\"><tr><td><table align=\"center\"><tr><td><table  align=\"center\"><tr><th><img src=\"https://clib.fyers.in/fy_images/320x132.png\" alt=\"Fyers\" width=\"220\" /></th></tr><tr style=\"color:#7c7e7f;\"><th class=\"sansserif\">&nbsp; &nbsp; &nbsp; Free Investment Zone</th></tr></table></td></tr></table><table align=\"center\" bgcolor=\"#ffffff\"  style=\"Margin: 0 auto;max-width: 600px;min-width: 320px; border-style:solid;border-left-width:10px;padding:5px; border-color:#ffffff;\"><tr style=\"color:#3e4751;\"><th><img src=\"https://mockedis.cdslindia.com/images/CDSL-Logo.png\"></th> </tr><tr><th><hr  style=\" border:1px solid\" width=\"12%\"><br></th></tr><br><tr align=\"left\" style=\"color:#7c7e7f;\"><td class=\"sansserif\" id=\"tpinDescp\">As per new regulations, clients are required to authorise sell transactions by providing specific instrument details along with quantites at the CDSL portal prior to executing any sell transactions from their demat account.<br><br> The autorisation will be valid till the end of the day irrespective of whether you have completed the sell transaction or not. <br><br></td></tr><tr align=\"left\" style=\"color:#7c7e7f;\"><td class=\"sansserif\"><br></td></tr><tr align=\"left\" style=\"color:#7c7e7f;\"><td class=\"sansserif\" style=\"text-align:center\"><br><br>       <form name= \"frmDIS\" method = \"post\" action= \"https://eDIS.cdslindia.com/eDIS/VerifyDIS\" >        <input type= \"hidden\" name= \"DPId\" value= \"89400\" />        <input type= \"hidden\" name= \"ReqId\" value= \"917177108176\" />        <input type= \"hidden\" name= \"Version\" value= \"1.1\" />        <input type= \"hidden\" name= \"TransDtls\" value= \"LD9WAIJCL2jgSj1hY2DABqfayzA6iInmBvh9ub+Ftqy0P+V/Qy4kRf9dsBHElVwcDdAhTx5a6+9g3y/TcVh1zEdMbslVXAcMi913u+YwHNp5IWUS6XAOCAx9UY01XZ+OVAgAez/9m+7cP6TjOeOBCqw57MWZ1y5N6OsPyzh+ecLUD2e6G5hJMc/ZKRw1dl5FvzJGpfmr1MGpM5jwtpzpbksmAIiAUMyx+zqfT5dX27ZLp0P4MRCl/QNyLnMCNwbhoPx7TEp6fN23UD8T3Y1742Kb1mVz3b4Aw6Kt+maXsjM12jP2bHZuM+rYKkjQWBK+AejT3Uk9vAZmFbd+Y1xeqKJFXAoKRA+cQXiCp8gjpm6RaZ04p8V7MMTWrIhpKAXNCCpCb+suxO74mjfW18AfZMKxX0UK/JjVomEoHz0GaIAKq4z3KAfwwcpqhtcNZv8u68DyeMmCFwojJ0Y+SBLjwUlJV3SWqpYhBnXxni5YsmvOK5NQLfWxd+KjuWK4gXgONgxWIcPMWsjY++JkYwtAlAhI43khxe0Y0SjntmZTZ4A=\" />        <input type= \"submit\" value=\"Submit\">         </form></td></tr><tr><td style=\"text-align: center;\" class=\"like-anchor\"><div id=\"forgetTpinDiv\"><a href=\"#\" id=\"forgetTpin\" onclick=\"tpin()\">Forgot CDSL TPIN</a></div></td></tr></tbody></table></td></tr></tbody></table>"}
```

## Data Socket - Indices Update

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-indices-update/ (last updated 2026-10-14)*

This WebSocket allows you to stream live index values such as NIFTY 50 and NIFTY Bank.

USE CASE

Show live index levels in a market header, or compare a stock's move with its index.

Details

* The WebSocket API for receiving stock data is a real-time communication protocol designed to provide seamless and low-latency access to live stock market data. This API allows developers and traders to establish a persistent, bidirectional connection with the server, enabling them to receive continuous updates on stock prices, trading volumes, and other relevant market information.
* To quickly get started with the WebSocket API and start receiving real-time stock data, you can explore our sample scripts and code examples in our GitHub repository:
  [Data WebSocket Sample Scripts](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED)/websocket%20sample%20script)
* Subscribe with `data_type` set to `SymbolUpdate` and index symbols such as `NSE:NIFTY50-INDEX` or `NSE:NIFTYBANK-INDEX`.
* Index messages have `type` set to `if`.
* An index message has only `symbol`, `ltp`, `prev_close_price`, `high_price`, `low_price`, `open_price`, `ch`, `chp` and `type`. Volume and bid or ask fields are not sent.
* A missing `symbol` key in index updates was fixed on 22 Aug 2025 (Java v1.3.0). Use a recent SDK version. See the [Change Log](https://fyers.in/api-docs/v3/changelog/).

Plan limits

Standard plan

* Up to 100 symbols, counted per user across all connections

Prime plan

* Up to 5,000 symbols, counted per user across all connections

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

### Response Attributes (Index Update)

| Attribute | Data Type | Description |
| --- | --- | --- |
| `symbol` | string | The symbol in fyers symbology format whose data is received on socket. |
| `ltp` | float | Last traded price of security or asset. |
| `prev_close_price` | float | Previous day's close of security or asset. |
| `high_price` | float | Current day's high of security or asset. |
| `low_price` | float | Current day's low of security or asset. |
| `open_price` | float | Current day's open of security or asset. |
| `ch` | float | Change in price of security or asset today. |
| `chp` | float | Change in price in % of security or asset today. |
| `type` | string | * cn - connection message * sub - subscribe message * if - index data message * dp - market depth data message * sf - Equity and option data message |

Request

```
from fyers_apiv3.FyersWebsocket import data_ws

def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Response:", message)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "SymbolUpdate"

    # Subscribe to the specified symbols and data type
    symbols = ["NSE:NIFTY50-INDEX" , "NSE:NIFTYBANK-INDEX"]
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "XC4XXXXXXM-100:eXXXXXXXXXXXXfZNSBoLo"

## Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
     "symbol":"NSE:NIFTY50-INDEX",
      "ch":"-27.95",
      "high_price":"26277.35",
      "ltp":"26188.1",
      "exch_feed_time":"1727428424",
      "chp":"-0.11",
      "low_price":"26166.95",
      "open_price":"26248.25",
      "type":"if",
      "prev_close_price":"26216.05"
  }
```

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Data Socket - Lite Mode

*Source: https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-lite-mode/ (last updated 2026-10-14)*

This WebSocket allows you to receive only the last traded price of a symbol.

USE CASE

Stream just the latest price for a ticker strip or a simple price trigger.

Details

* The WebSocket API provides a lightweight and efficient "Lite Mode" for receiving only the Last Traded Price (LTP) updates of specific stock symbols. This mode is designed for users who require real-time access to LTP data without the additional overhead of subscribing to other stock data fields. The Lite Mode allows for seamless integration into applications where only the latest stock prices are needed.
* In Python, set `litemode=True` when you create the socket; `litemode=False` gives the full update. In Node and Web JS, call `mode(LiteMode)`; Web JS can switch back with `mode(FullMode)`.
* In the sample, a lite message has only `symbol`, `ltp` and `type` (`sf`).
* Volume, day open, high and low, change and best bid and ask are not sent in lite mode. Use full mode for them. See [Symbol Update](https://fyers.in/api-docs/v3/api/websockets/data-socket/data-socket-symbol-update/).
* Subscribe as usual, for example with `data_type` set to `SymbolUpdate`.

Plan limits

Standard plan

* Up to 100 symbols, counted per user across all connections

Prime plan

* Up to 5,000 symbols, counted per user across all connections

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

Request

```
from fyers_apiv3.FyersWebsocket import data_ws

def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Response:", message)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "SymbolUpdate"

    # Subscribe to the specified symbols and data type
    symbols = ['NSE:SBIN-EQ', 'NSE:ADANIENT-EQ']
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "XC4XXXXXXM-100:eXXXXXXXXXXXXfZNSBoLo"

## Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=True,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)

## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
{
    symbol: 'NSE:SBIN-EQ',
    ltp: 500.55,
    type: 'sf'
  }
```

VIDEO LEARNING

### Video learning

[Web-socket set-up explained (Python)Python · 10:47](https://www.youtube.com/watch?v=hfDvcqc_1o8&list=PLgzB28RH71JuwC9ftCsXCgU6OWeWagIGw)[Web-socket setup explained (Node.js)Node.js · 7:15](https://www.youtube.com/watch?v=OXJ61uef7AY&list=PLgzB28RH71JuZHp0mQLdX0eB-gLU3Leda)[Web-socket set-up explained (C#)C# · 6:59](https://www.youtube.com/watch?v=eYSFj_9gf2M&list=PLgzB28RH71JsQyZu5KtSsgPxwYOHOVpla)[Web-socket set-up explained (Java)Java · 9:41](https://www.youtube.com/watch?v=57jZVvl0dHo&list=PLgzB28RH71JvDkJKfwrIy2_wQqdMeo2p6)

Go and C video tutorials: coming soon.

## Tick-by-Tick (TBT) Socket Overview

*Source: https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/ (last updated 2026-10-14)*

Redirecting to [Tick-by-Tick (TBT) Socket Overview](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/)…

## Tick-by-Tick (TBT) Socket - Connection (50 Market Depth)

*Source: https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/tbt-websocket-connection/ (last updated 2026-10-14)*

This WebSocket allows you to connect to the Tick-by-Tick socket and subscribe to 50-level market depth.

USE CASE

Stream 50-level depth for the few symbols you trade closely, such as a Nifty or Bank Nifty futures contract.

Currently, these are the features available on the socket:

| Feature | Description | Status |
| --- | --- | --- |
| TBT 50 Market Depth | TBT 50 Market Depth provides users with 50 levels of market depth. [Learn more](https://fyers.in/community/t/50-market-depth-a-game-changer-for-options-scalpers/12229) | Available |

### Mandatory connection parameters

To connect to the TBT WebSocket, the below input parameters are mandatory:

| Parameter | Value |
| --- | --- |
| Endpoint | `wss://rtsocket-api.fyers.in/versova` |
| Header Key | `Authorization` |
| Header Format | `<appId:accessToken>` |
| Sample Header | `7ABXUX38S-100:eyJ0eXAi**********qiTnzd2lGwS17s` |

Details

* Tick-by-tick data is available only for NFO (NSE Futures & Options) and NSE equity symbols.
* See [Rate limits](https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/concept-of-channels/#ratelimits) for connection and channel limits.
* A subscribe request needs the symbols, the mode (`depth`) and a channel number. Data starts only after you resume that channel.
* The first packet for a subscription is a snapshot. Later packets hold only the differences, which you apply to the snapshot. The SDKs do this for you.
* Server errors come through the error-message callback (`on_error_message` in Python, `servererror` in Node). In a response, `error` is true, `feeds` is empty and `msg` mostly holds the error message.
* In the Node SDK, call `autoreconnect()` before `connect()` to reconnect automatically after a disconnect. Send the string `ping` to keep the connection alive.
* SDK support: TBT 50 depth is available from the Python SDK `v3.1.7` (04 Mar 2025) and the Node SDK `v1.4.1` (26 Mar 2025). See the [Change Log](https://fyers.in/api-docs/v3/changelog/).

Plan limits

Standard plan

* 1 symbol, counted per user across all connections
* 1 active connection

Prime plan

* 15 symbols, counted per user across all connections
* Up to 3 active connections with 5 symbols each

For rate limits and all other plan details, see [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

WSSwss://rtsocket-api.fyers.in/versova

Authorization: <appId:accessToken>

```
from fyers_apiv3.FyersWebsocket.tbt_ws import FyersTbtSocket, SubscriptionModes

def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    print("Connection opened")
    # Specify the data type and symbols you want to subscribe to
    mode = SubscriptionModes.DEPTH
    Channel = '1'
    # Subscribe to the specified symbols and data type
    symbols = ['NSE:NIFTY25MARFUT', 'NSE:BANKNIFTY25MARFUT']

    fyers.subscribe(symbol_tickers=symbols, channelNo=Channel, mode=mode)
    fyers.switchChannel(resume_channels=[Channel], pause_channels=[])

    # Keep the socket running to receive real-time data
    fyers.keep_running()

def on_depth_update(ticker, message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        ticker (str): The ticker symbol of the received message.
        message (Depth): The received message from the WebSocket.

    """
    print("ticker", ticker)
    print("depth response:", message)
    print("total buy qty:", message.tbq)
    print("total sell qty:", message.tsq)
    print("bids:", message.bidprice)
    print("asks:", message.askprice)
    print("bidqty:", message.bidqty)
    print("askqty:", message.askqty)
    print("bids ord numbers:", message.bidordn)
    print("asks ord numbers:", message.askordn)
    print("issnapshot:", message.snapshot)
    print("tick timestamp:", message.timestamp)

def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.

    """
    print("Error:", message)

def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)

def onerror_message(message):
    """
    Callback function for error message events from the server

    Parameters:
        message (dict): The error message received from the Server.

    """
    print("Error Message:", message)

## Replace the sample access token with your actual access token obtained from Fyers
access_token = "XCXXXXXXM-100:eyJ0tHfZNSBoLo"

fyers = FyersTbtSocket(
    access_token=access_token,  # Your access token for authenticating with the Fyers API.
    write_to_file=False,        # A boolean flag indicating whether to write data to a log file or not.
    log_path="",                # The path to the log file if write_to_file is set to True (empty string means current directory).
    on_open=onopen,          # Callback function to be executed upon successful WebSocket connection.
    on_close=onclose,           # Callback function to be executed when the WebSocket connection is closed.
    on_error=onerror,           # Callback function to handle any WebSocket errors that may occur.
    on_depth_update=on_depth_update, # Callback function to handle depth-related events from the WebSocket
    on_error_message=onerror_message         # Callback function to handle server-related erros from the WebSocket.
)
## Establish a connection to the Fyers WebSocket
fyers.connect()
```

```
const { SubscriptionModes } = require("../tbtsocket/models.js")

var fyersOrderSocket= require("../index.js").fyersTbtSocket

var skt=new fyersOrderSocket("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3********************************************")

skt.on("error",function (errmsg) {
    console.log(errmsg)
})
skt.on('open', function() {
    skt.subscribe(['NSE:NIFTY25FEBFUT', 'NSE:IOC25FEBFUT', 'NSE:BANKNIFTY25FEBFUT', 'NSE:FINNIFTY25FEBFUT', 'NSE:TCS25FEBFUT'], '1', SubscriptionModes.DEPTH)
    skt.switchChannel([], ['1'])
})
skt.on('depth',function (ticker, data) {
    console.log('depth',ticker, data)
})
skt.on('close',function () {
    console.log('closed')
})
skt.on('servererror',function (msg) {
    console.log('serverr', msg)
})
skt.autoreconnect()
skt.connect()
```

## Tick-by-Tick (TBT) Socket - Channels and Message Types

*Source: https://fyers.in/api-docs/v3/api/websockets/tick-by-tick-socket/overview/concept-of-channels/ (last updated 2026-10-14)*

This guide explains how to group Tick-by-Tick symbols into channels and pause or resume their streams.

USE CASE

Group your Nifty and Bank Nifty symbols into channels and switch each group on or off with one message.

With the Tick-by-Tick (TBT) WebSocket, we are introducing the concept of channels. A channel acts as a logical grouping for different subscribed symbols, making it easier to manage data streams efficiently.

### How Channels Work

* When subscribing to market data, you need to specify both the symbols and a channel number.
* Simply subscribing to a channel does not start the data stream—you must also resume the channel to begin receiving updates.

### Example Usage

Let's say you organize your subscriptions as follows:

* Channel 1: All Nifty-related symbols
* Channel 2: All BankNifty-related symbols

Now, depending on what data you need, you can control the channels dynamically:

* Receive only Nifty data → Pause Channel 2 and Resume Channel 1
* Receive only BankNifty data → Pause Channel 1 and Resume Channel 2
* Receive both Nifty and BankNifty data → Resume both channels

This approach provides greater flexibility and control over market data streaming, allowing you to filter and manage real-time data efficiently.

Details

* Every subscribe and unsubscribe request carries a channel number. A connection supports 50 channels (1 to 50). See [Rate limits](#ratelimits) for symbol and connection limits by plan.
* Subscribing to a channel does not start the stream. Send a switch-channel request (`type` 2) with the channel in `resumeChannels` to start it.
* Use `pauseChannels` and `resumeChannels` in the same request to switch between groups. Both lists hold channel numbers as strings; the sample sends an empty `pauseChannels` list.
* Subscribe uses `subs` 1 and unsubscribe uses `subs` -1, both with `type` 1 and `mode` `depth`.
* Responses are protobuf. `snapshot` is true for the first full packet and false for diff packets. When `error` is true, `feeds` is empty.
* Each depth level has `price`, `qty`, `nord` and `num`. For 50 levels, `num` runs from 0 to 49.

### Request Message Types

| Type | Purpose | Encoding Format | Data Format |
| --- | --- | --- | --- |
| `Ping` | Ping message to keep connection alive | `String` | ``` "ping" ``` |
| `Subscribe` | Subscribe to the symbols for which data is required | `Json string` | ``` {   "type": 1,   "data": {     "subs": 1,     "symbols": [       "NSE:IOC25FEBFUT",       "NSE:NIFTY25FEBFUT",       "NSE:BANKNIFTY25FEBFUT",       "NSE:FINNIFTY25FEBFUT",       "NSE:TCS25FEBFUT"     ],     "mode": "depth",     "channel": "1"   } } ``` |
| `Unsubscribe` | Unsubscribe to the symbols for which data is NOT required | `Json string` | ``` {   "type": 1,   "data": {     "subs": -1,     "symbols": [       "NSE:IOC25FEBFUT",       "NSE:NIFTY25FEBFUT",       "NSE:BANKNIFTY25FEBFUT",       "NSE:FINNIFTY25FEBFUT",       "NSE:TCS25FEBFUT"     ],     "mode": "depth",     "channel": "1"   } } ``` |
| `Switch Channel` | Switch between active and paused channels | `Json string` | ``` {   "type": 2,   "data": {     "resumeChannels": ["1"],     "pauseChannels": []   } } ``` |

### Response Message Types

We use Protocol Buffers (protobuf) as the response format for all market data. The .proto file, which defines the data structure, is available at:

<https://public.fyers.in/tbtproto/1.0.0/msg.proto>

Protobuf is a widely used data format, and compilers are available to generate code in different programming languages.

#### How to install and use Protobuf

* Protobuf Compiler Installation: <https://protobuf.dev/getting-started/>
* Using Protobuf with Python: <https://protobuf.dev/reference/python/python-generated/>
* Using Protobuf with Node.js: <https://www.npmjs.com/package/protobufjs>

We have uploaded the compiled files also for python, nodejs, and golang. Download from: <https://public.fyers.in/tbtproto/1.0.0/protogencode.zip>

Copy the required file directly in your project and use it.

#### Proto versions & links

| Proto Version | Proto URL | Compiled files URL | Updated on |
| --- | --- | --- | --- |
| `1.0.0` | <https://public.fyers.in/tbtproto/1.0.0/msg.proto> | <https://public.fyers.in/tbtproto/1.0.0/protogencode.zip> | 20-02-2025 |

#### Response structures

| Type | Data Format | Field Explanation |
| --- | --- | --- |
| `SocketMessage` | * `type`: value will always be `MessageType.depth` * `feeds`: string (key) will be the symbol ticker and value will be the [`MarketFeed`](#mfeed) datastructure. This value will have the actual 50 depth values. * `snapshot`: true if it's a snapshot and false if it's a diff packet. * `msg`: will mostly contain error msgs when error = true. * `error`: true if it is an error, else false. In case of true, feeds will be nil/empty. | ``` message SocketMessage {   MessageType type = 1;   map<string, MarketFeed> feeds = 2;   bool snapshot = 3;   string msg = 4;   bool error = 5; } ``` |
| `MarketFeed` | * `depth`: [`Depth`](#depth) datastructure. This field will have the actual market depth value. * `feed_time`: time of packet in unix epoch. * `send_time`: time of packet at the time of sending from server. * `token`: fytoken for symbol. * `snapshot`: true if snapshot, false if diff packet. * `ticker`: symbol ticker. * **Note:** other fields can be ignored | ``` message MarketFeed {   Quote quote = 1;   ExtendedQuote eq = 2;   DailyQuote dq = 3;   OHLCV ohlcv = 4;   Depth depth = 5;   google.protobuf.UInt64Value feed_time = 6;   google.protobuf.UInt64Value send_time = 7;   string token = 8;   uint64 sequence_no = 9;   bool snapshot = 10;   string ticker = 11;   SymDetail symdetail = 12; } ``` |
| `Depth` | * `tbq`: total bid qty * `tsq`: total sell qty * `asks`: array of asks of type [`MarketLevel`](#mlevel) datastructure * `bids`: array of bids of type [`MarketLevel`](#mlevel) datastructure | ``` message Depth {   google.protobuf.UInt64Value tbq = 1;   google.protobuf.UInt64Value tsq = 2;   repeated MarketLevel asks = 3;   repeated MarketLevel bids = 4; } ``` |
| `MarketLevel` | * `price`: price * `qty`: qty in the market depth for the price * `nord`: number of orders in market depth for the price * `num`: depth number, for 50 depth will be between 0 and 49 [0 based array indexing] | ``` message MarketLevel {   google.protobuf.Int64Value price = 1;   google.protobuf.UInt32Value qty = 2;   google.protobuf.UInt32Value nord = 3;   google.protobuf.UInt32Value num = 4; } ``` |

### Rate limits

Following ratelimits apply for TBT Websocket. The symbol limit is per user, across all connections: Standard allows 1 symbol and Prime allows 15 symbols, which is up to 3 connections with 5 symbols each. See [Plans & rate limits](https://fyers.in/api-docs/v3/getting-started/plans-and-limits/).

| Description | Standard plan | Prime plan |
| --- | --- | --- |
| Symbols per user, across all connections [Market Depth] | 1 | 15 |
| Active Connections Per App Per User | 1 | 3 |
| Symbols per connection [Market Depth] | 1 | 5 |
| Channels per connection | 50 (1-50) | 50 (1-50) |
