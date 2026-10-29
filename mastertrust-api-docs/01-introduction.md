# Introduction

Master Trust's trading API (built on the Tradelab platform) is a set of REST endpoints for profile, order, portfolio, funds, and instrument data. All responses are JSON.

## Base URL

The upstream docs write the base URL as `<base_url>`. Every example request on the portal uses:

```
https://masterswift-beta.mastertrust.co.in
```

All endpoint paths in these docs (e.g. `/api/v1/orders`) are relative to it.

## Endpoints at a Glance

| Endpoint | Method | Path | Doc |
| --- | --- | --- | --- |
| Profile | GET | `/api/v1/user/profile?client_id=<clientID>` | [User](03-user.md) |
| Trading Info | GET | `/api/v1/user/trading_info` | [User](03-user.md) |
| Place Normal Order | POST | `/api/v1/orders` | [Orders](04-orders.md) |
| Modify Order | PUT | `/api/v1/orders` | [Orders](04-orders.md) |
| Cancel Normal Order | DELETE | `/api/v1/orders/<omsOrderNum>?client_id=<clientID>` | [Orders](04-orders.md) |
| Place Cover Order | POST | `/api/v1/orders` | [Orders](04-orders.md) |
| Place Bracket Order | POST | `/api/v1/orders/bracket` | [Orders](04-orders.md) |
| Exit Bracket Order | DELETE | `/api/v1/orders/bracket` | [Orders](04-orders.md) |
| Exit Cover Order | DELETE | `/api/v1/orders/cover` | [Orders](04-orders.md) |
| Order Book — Pending | GET | `/api/v1/orders?type=pending&client_id=<clientID>` | [Order & Trade Book](05-order-and-trade-book.md) |
| Order Book — Completed | GET | `/api/v1/orders?type=completed&client_id=<clientID>` | [Order & Trade Book](05-order-and-trade-book.md) |
| Trade Book | GET | `/api/v1/trades?client_id=<clientID>` | [Order & Trade Book](05-order-and-trade-book.md) |
| Order History | GET | `/api/v1/order/<omsOrderNum>/history?client_id=<clientID>` | [Order & Trade Book](05-order-and-trade-book.md) |
| Position Book — Daywise | GET | `/api/v1/positions?type=live&client_id=<clientID>` | [Portfolio](06-portfolio.md) |
| Position Book — Netwise | GET | `/api/v1/positions?type=historical&client_id=<clientID>` | [Portfolio](06-portfolio.md) |
| Demat Holdings | GET | `/api/v1/holdings?client_id=<clientID>` | [Portfolio](06-portfolio.md) |
| Cash Positions | GET | `/api/v1/funds/view?client_id=<clientID>&type=all` | [Funds](07-funds.md) |
| Scrip Info | GET | `/api/v1/contract/<exchange>?info=scrip&token=<instrumentToken>` | [Instruments](08-instruments.md) |
| Search Scrip | GET | `/api/v1/search?key=<keyword>` | [Instruments](08-instruments.md) |
| Contract Master Download | GET | `/api/v1/contract/Compact?info=download` | [Instruments](08-instruments.md) |

## Conventions

- All responses are in JSON format.
- All request parameters are mandatory unless explicitly marked as `[optional]`.
- See [Glossary](09-glossary.md) for HTTP status codes.
