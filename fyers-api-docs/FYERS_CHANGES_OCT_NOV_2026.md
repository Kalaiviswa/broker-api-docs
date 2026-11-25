# FYERS API v3: changes from 29 Sep to 25 Nov 2026

`FYERS_API_v3.md` was last generated on 2026-09-29 from the OpenAPI YAML behind
`myapi.fyers.in/docsv3`. On 16 Oct 2026 Fyers moved the docs to
<https://fyers.in/api-docs/v3/> and `myapi.fyers.in/docsv3` now redirects there.
The file is now generated from the new site (186 pages). This note lists what
changed in that window, from the site's change log
(<https://fyers.in/api-docs/v3/changelog/>) and the pages themselves, with what
each change means for OpenAlgo's `broker/fyers`.

## Change log entries

| Date | Change |
| --- | --- |
| 01 Oct 2026 | Get Expired F&O Data takes `include_greeks`. Quotes adds the Closing Auction Session fields `imbalance`, `mkt_imbalance`, `reference_price` and `indicative_price`. |
| 16 Oct 2026 | FYERS Prime plan and the Plans & Limits page. New docs site. `POST /data/quotes` takes up to 1,000 symbols for Prime users (50 for Standard). |
| 30 Oct 2026 | Screeners APIs under `/api/v3/screeners` (Config, Standard, Candlestick, Technical). SDKs: Python 3.2.1, Node 2.4.1, Web JS 2.2.1, Java 2.1.1, C# 1.6.0, Go 1.7.0, C 1.5.0. |
| 18 Nov 2026 | GTT Single and GTT OCO legs take `type` (`1` Limit, the default; `2` Market). Modify GTT accepts `type` per leg (missing means Limit). GTT Order Book returns `ord_type` and `ord_type2`. Market GTT is refused for BFO symbols (code `-50`). |

## FYERS Prime: plans and limits

Source: <https://fyers.in/api-docs/v3/getting-started/plans-and-limits/>
(last updated 2026-10-14). Standard is free; Prime is a paid subscription taken
from FYERS Web or App, Profile, FYERS Prime.

| API category | Standard | Prime |
| --- | --- | --- |
| Data APIs (quotes, depth, history, option chain) | 5/s, 50/min, 5,000/day | 10/s, 500/min, 5,00,000/day |
| Transaction + User Info APIs | 10/s, 200/min, 1,00,000/day | 10/s, 500/min, 5,00,000/day |

| Feature | Standard | Prime |
| --- | --- | --- |
| Quotes symbols per request | 50 | 1,000 (POST only) |
| History, daily | last 5 years | 25+ years |
| History, intraday | last 1 year | 5+ years |
| Seconds data | not available | last 30 days |
| Expired F&O daily | last 2 years | 7+ years |
| Expired F&O intraday | 10 requests/day | Prime rate limits |
| Screeners | 50 requests/day | Prime rate limits |
| Data Socket symbols (per user, all connections) | 100 | 5,000 |
| TBT Socket symbols | 1 | 15 (3 connections x 5) |

- A rate limit breach returns `-429`. A Standard user over a limit gets `-360`
  ("Upgrade to Prime for higher API limits").
- Going over the per-minute limit more than 3 times in a day blocks the user for
  the rest of the day.
- A Data Socket subscription that would go over the symbol limit is refused: the
  connection is not established.

Before this, the docs listed one limit for every API: 10/s, 200/min, 1,00,000/day.
For a Standard user the data limits are now much lower (50 a minute, 5,000 a day).

## What this means for OpenAlgo `broker/fyers`

- **Rate limiter.** `api/rate_limiter.py` paced every call in one lane at about
  8 a second with no minute or day count. That is over Standard's 50 data
  requests a minute, and three such minutes block the account for the day. The
  limiter needs per-category budgets (data, transaction, user info) with
  per-second, per-minute and per-day windows, for the plan the trader has. OpenAlgo
  Desktop already does this (`src-tauri/src/brokers/fyers/ratelimit.rs`, plan
  chosen on Broker Configuration).
- **GTT.** OpenAlgo turns a MARKET GTT into a LIMIT with Market Price Protection
  because the old docs had no order type on a leg. Fyers now takes `type: 2`
  natively, except for BFO symbols.
- **History horizon.** Standard: 5 years daily, 1 year intraday, no seconds data.
  Prime: 25+ years daily, 5+ years intraday, 30 days of seconds data. A clamp
  for the Standard horizon is wrong for Prime users.
- **Quotes.** `GET /data/quotes` stays at 50 symbols. Prime users could batch
  1,000 through `POST /data/quotes`. The CAS fields are extra and do not change
  OpenAlgo's quote format.
- **WebSocket.** A Standard user can stream 100 symbols in all. Past that,
  the subscription is refused.
