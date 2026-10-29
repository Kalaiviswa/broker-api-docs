> Source: https://docs.sahi.com/api/v1/reference/authentication/ (via llms-full.txt), fetched 2026-10-29.

# Authentication

Every Sahi API request carries a Bearer access token, and you mint your own.
There is no OAuth redirect to build and no secret we hold on your behalf: you
create an **API key** in your Sahi account, exchange it for a short-lived token,
and send that token on every call.

Three things have to be true before a token will work, and each has a section
below. The key must exist with the scopes you need. You must have approved it
for the current trading day. And requests that **place, modify, or cancel an
order** must reach us from a **registered static IP**. The last two are exchange
requirements rather than Sahi policy, and both are checked per request rather
than once at onboarding.

Paths on this page are relative to two base URLs: the **auth** base URL, which
serves `/api/v1/apikeys/token`, and the **API** base URL, which serves
everything under `/v1`. If you do not have them, write to
[developers@sahi.com](mailto:developers@sahi.com).

## Create an API key

Keys are self-serve, from the **API keys** section of your Sahi account. You are
asked to complete two-factor verification first: creating a credential that can
place orders is not something a first-factor session can do. The same section is
where you approve a key for the day and revoke it.

Give the key a name and choose its scopes.

**Scopes are fixed for the life of the key.** A token minted from it can carry
that set or a subset of it, never more. To trade under a different set, create a
different key.

| Scope | Grants |
|---|---|
| `orders.write` | Place, modify and cancel orders |
| `orders.read` | Read the order book and trade history |
| `positions.read` | Read open positions |
| `holdings.read` | Read demat holdings |
| `funds.read` | Read available funds and margin |
| `profile.read` | Read profile details |
| `marketdata.read` | Read quotes, historical candles and instrument data |

**What you get back.** A key id, which begins `pk_`, and a secret, which begins
`sahi_sk_`. The secret is **shown exactly once**. Sahi stores only a hash of it
and cannot show it again, so put it straight into your secret store; if you lose
it, revoke the key and create another. The key id is not a secret and is safe to
log.

You may hold **at most 5 active keys** at a time. Revoked keys do not count
against that, but revocation is terminal: a revoked key can never be reactivated.

**Revoking is immediate, and it is retrospective.** Revoking a key does not
merely stop it minting new tokens; every token already minted from it stops
being accepted straight away, rather than running out its remaining life. That
is the lever to pull if a secret leaks.

## Register your static IP

Placing, modifying, or cancelling an order is permitted only from IP addresses
registered in advance. This follows SEBI's framework for retail algorithmic
trading, in force since 1 April 2026, and applies to everyone placing orders
through the API.

Registration lives with your **account, not with a key**: one registration
covers every key you hold, and adding a key does not mean registering an address
again. You register from the same part of the Sahi account UI that manages keys,
and, as with keys, it takes a two-factor session.

There are **two slots**, a primary and a secondary, each holding one address.
The second exists for connectivity redundancy: register the egress address of a
backup line or a second region, not a second trading process. Both IPv4 and IPv6
are accepted.

Four rules are worth knowing before you register rather than after:

- **One address belongs to one account.** An IP registered to another Sahi
  account cannot be registered to yours while that registration stands. Shared
  office NAT, a shared VPN exit, or a cloud NAT gateway used by more than one
  trader will collide. There is no family-sharing exception.
- **A slot is locked for 7 days after it takes an address.** Once a slot holds
  an IP, that slot will not accept a *different* one for a week. The two slots
  are tracked separately, so a locked primary does not stop you setting the
  secondary. Plan a move rather than discovering the lock during one.
- **The lock survives removal.** Emptying a slot and re-registering does not
  reset its clock, and re-adding the address that was just removed is treated
  like any other change. Removing an address is never itself blocked, though: it
  only narrows what may trade, so you can always revoke access immediately.
- **Exceptional changes go through us.** If an address has to move inside the
  7-day window, contact support rather than working around it.

**What enforcement looks like.** The check covers the three order-write
endpoints — `POST /orders`, `PUT /orders/{order_id}`, and
`DELETE /orders/{order_id}`. One of those from an unregistered address is
refused with `403` and the code `IP_NOT_ALLOWED`, whatever the token would
otherwise have permitted. Everything else — the order book, positions, funds,
holdings, profile, market data, and both WebSocket streams — is not IP-checked,
so a read-only client needs no registration. Removing your last registered
address therefore costs you the ability to trade through the API, not your
access to it.

The address that matters is the **public egress address your traffic actually
arrives from**, which is often not the address configured on the machine. Check
it from the host that will run your client before you register.

## Approve the key for the trading day

A key mints tokens only on trading days you have approved it for. Approval is a
daily act, done from the same **API keys** section, and it is an exchange
requirement rather than something Sahi can waive.

A trading day runs **06:00 IST to 06:00 IST**. Approval lapses at that boundary,
so a key approved on Tuesday morning stops minting on Wednesday at 06:00 until
it is approved again. Creating a key counts as approving it, so a key is usable
on the day it is made without a second step.

An unapproved key still exists and still lists; it simply cannot mint. Attempts
to mint from one are refused with `403`.

## Mint an access token

This is the only endpoint your code calls to authenticate, and the only public
one on the auth host. It takes the key id and secret in the body; there is no
`Authorization` header on this request.

```http
POST /api/v1/apikeys/token
Content-Type: application/json
```
```json
{
  "key_id": "pk_d1jqhcg55l6bd0e0oq3g",
  "secret": "sahi_sk_5Kw...Qr_9b1c2d3e",
  "scopes": ["marketdata.read"]
}
```

| Field | Type | Required | Notes |
|---|---|---|---|
| `key_id` | string | yes | The key id shown when you created the key. |
| `secret` | string | yes | The secret shown once at creation. |
| `scopes` | array | no | Narrows the token to a subset of the key's scopes. Omit it to get the key's full set. It can only narrow: asking for a scope the key does not hold is rejected. |

The response is `200 OK`:

```json
{
  "access_token": "eyJhbGciOiJFUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 65275,
  "expires_at": "2026-08-21T06:00:00+05:30",
  "scope": "marketdata.read"
}
```

| Field | Type | Notes |
|---|---|---|
| `access_token` | string | The Bearer token for every REST and WebSocket call. |
| `token_type` | string | Always `Bearer`. |
| `expires_in` | integer | Seconds until the token expires. |
| `expires_at` | string | The same moment as an RFC 3339 timestamp: the next 06:00 IST boundary. |
| `scope` | string | Space-separated scopes the token actually carries. |

Mint one token per trading day and reuse it. The endpoint is rate-limited per
caller and key, and a client that mints on every request will meet that limit;
on `429`, back off and retry in the next minute rather than immediately. That
ceiling is the auth host's own: the `/v1` endpoints carry separate per-endpoint
budgets, listed under [Rate limits](/#rate-limits).

**Narrow the scopes when you can.** A process that only reads quotes has no
business holding a token that can place orders, even if the key behind it can.
Passing `scopes` costs nothing and shrinks what a leaked token is worth.

## Call the API

Send the token on every request to the API host:

```http
GET /v1/positions
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
```

**One token covers everything it is scoped for, market data included.** There is
no separate market-data credential.

WebSocket connections authenticate the same way, with the header on the upgrade
request. See [WebSocket connections](/#websocket-connections).

## Token lifetime

- **Tokens expire at 06:00 IST, when the trading day ends.** A token lasts to
  the end of the cycle it was minted in: 06:00 the next morning for one minted
  at 09:00, 06:00 the *same* morning for one minted at 05:00. `expires_in`
  shrinks as the cycle goes on, so a token minted late in the day is short-lived
  by design.
- **There are no refresh tokens.** Mint a new one. Daily re-authorisation is the
  regulatory intent, not an omission, which is also why approval lapses on the
  same boundary.
- When a token expires, or any `/v1` call returns `401`, mint again. If the new
  mint returns `403`, the key needs approving for the new day.
- WebSocket connections close with code `4401` at expiry or revocation.
  Reconnect with a fresh token: the order stream then re-runs
  [Stream + Snapshot](/api/v1/reference/orders/#stream--snapshot), and the tick
  stream re-sends its subscriptions.

## When something goes wrong

The auth host and the API host use the same envelope, `{"code", "message"}`,
with **different code vocabularies**: the auth host uses `PascalCase`, and
everything under `/v1` uses `SCREAMING_SNAKE_CASE`. Match on the status code and
the host, not on the shape of the string.

Minting, on the auth host:

| Status | Code | Usually means |
|---|---|---|
| `400` | `InvalidRequest` | A field is missing or malformed, or the requested scopes are not a subset of the key's |
| `401` | `Unauthorized` | Unknown key id, wrong secret, or the key has been revoked. These are deliberately indistinguishable |
| `401` | `Locked` | Your account is frozen or locked |
| `403` | `Forbidden` | The key is not approved for the current trading day |
| `429` | `TooManyRequests` | Too many mint attempts. Back off to the next minute |

Calling the API, on the API host:

| Status | Code | Usually means |
|---|---|---|
| `401` | `UNAUTHORIZED` | The token is missing, malformed, expired, or was revoked with its key |
| `403` | `IP_NOT_ALLOWED` | An order write did not come from a registered static IP |
| `403` | `FORBIDDEN` | The token is valid but lacks the scope the endpoint needs |
| `429` | `RATE_LIMITED` | Over the endpoint's [rate limit](/#rate-limits). Wait out the `Retry-After` header before retrying |

A `403 IP_NOT_ALLOWED` on a call that worked yesterday almost always means your
egress address moved: a new NAT gateway, a failed-over line, a container
rescheduled into another subnet.

## Checklist

1. Create a key in your Sahi account with the scopes you need, and store the
   secret as a backend secret. It is shown once.
2. If the client places orders, register the **public egress IP** it calls from,
   checked from the host that will run it. Add a secondary only for a genuine
   backup path.
3. Approve the key each trading day.
4. Mint a token at start of day from `/api/v1/apikeys/token`, narrowing `scopes`
   to what that process needs, and reuse it until 06:00 IST.
5. Download the [scrip master](/api/v1/reference/scrip-master/) at start of day
   and map instruments to `instrument_id` for market data, or `exchange_segment`
   plus `symbol` for orders.
6. Call the REST endpoints with the Bearer token, and subscribe to the
   [order-update](/api/v1/reference/orders/#wss-v1streamorders--order-updates)
   and [tick](/api/v1/reference/market-data/#wss-v1streammarketdata--tick-stream)
   streams for live updates — applying Stream + Snapshot on every order-stream
   connect.

