# Master Trust Trade API Documentation

> **Unofficial Markdown conversion** of the Master Trust trading API documentation, sourced from the official documentation portal:
> <https://tradeapi.mastertrust.co.in/>

Master Trust's API runs on the Tradelab platform: OAuth2 (authorization code) login, then plain REST/JSON endpoints under `/api/v1` with an `Authorization: Bearer {access_token}` header.

## Base URLs

| Purpose | Base URL |
| --- | --- |
| REST API (as used in all upstream examples) | `https://masterswift-beta.mastertrust.co.in` |
| OAuth2 authorize | `<base_url>/oauth2/auth` |
| OAuth2 token | `<base_url>/oauth2/token` |
| Contract master download | `https://masterswift-beta.mastertrust.co.in/api/v1/contract/Compact?info=download` |

## Table of Contents

| # | Document | Description |
| --- | --- | --- |
| 01 | [Introduction](01-introduction.md) | Base URL, endpoint summary, conventions |
| 02 | [Authentication](02-authentication.md) | OAuth2 configuration, login flow, bearer token, TOTP setup |
| 03 | [User](03-user.md) | Profile and trading info |
| 04 | [Orders](04-orders.md) | Place/modify/cancel normal orders, Cover and Bracket orders and their exits |
| 05 | [Order Book, Trade Book & Order History](05-order-and-trade-book.md) | Pending/completed orders, trades, per-order history |
| 06 | [Portfolio](06-portfolio.md) | Daywise and netwise positions, demat holdings |
| 07 | [Funds](07-funds.md) | Cash positions / margin view |
| 08 | [Instruments](08-instruments.md) | Contract master download, scrip info, scrip search |
| 09 | [Glossary](09-glossary.md) | Conventions and HTTP status codes |

## Notes

- `client_id` is the trading account code; most GET endpoints take it as a query parameter.
- Each endpoint has a cURL and a Python example. The portal also has JavaScript, Go and Java tabs, but every upstream snippet (Python included) pastes the JSON body in unescaped, so none compile or run as written. The cURL and Python examples here are rewritten from the same method, URL and body so they work. The JS/Go/Java tabs are not reproduced.
- Long sample responses (search results, completed orders, holdings) are shortened to the entries that show each distinct exchange / order type / status / product, so NSE, BSE, NFO, BFO and MCX shapes and every order-history status (`put order req received`, `validation pending`, `open pending`, `open`, `modify pending`, `modify validation pending`, `modified`, `complete`) are kept.
- Upstream samples contain a real account holder's name, PAN, phone, bank, DP, and address details plus a bearer token. These are replaced with placeholders (`CLIENT123`, `JOHN DOE`, `ABCDE1234F`, `{access_token}`, ...). The upstream TOTP screenshots are not vendored — one shows a TOTP enrollment QR code.
