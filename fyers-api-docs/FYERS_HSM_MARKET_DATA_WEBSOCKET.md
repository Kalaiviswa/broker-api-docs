# FYERS HSM Market-Data WebSocket — Wire Protocol Reference

**Status:** verified against the live Fyers endpoint on **2026-08-31** and cross-checked
against the official `fyers-apiv3` **3.1.16** SDK (`FyersWebsocket/data_ws.py`).

## Why this file exists

`FYERS_API_v3.md` documents the market-data socket **only through the Python/Node SDK
wrapper** (`FyersDataSocket.subscribe(...)`). It contains no endpoint URL, no handshake
byte layout and no frame-type table — the string "HSM" does not appear in it at all.
OpenAlgo talks to this socket directly (`openalgo/broker/fyers/streaming/fyers_hsm_websocket.py`),
so the wire protocol is recorded here.

The other two Fyers sockets *are* covered in `FYERS_API_v3.md`: the order socket
(~line 6010) and the TBT/50-depth socket (~line 6237). They authenticate completely
differently — see the comparison table below.

---

## ⚠️ Do NOT send an `Authorization` header on the HSM handshake

This is the single most important fact in this document, and the cause of a live
outage on 2026-08-31 (`Failed to authenticate with Fyers HSM WebSocket (timeout)`).

The HSM feed authenticates **in-band only**, via the binary request-type-1 frame.
Fyers' gateway **silently drops** any handshake that carries an `Authorization`
header. The failure mode is deliberately quiet and easy to misdiagnose:

- The WebSocket upgrade **succeeds** (HTTP 101, `on_open` fires normally).
- The auth frame is accepted at the TCP level and **never answered**.
- No error frame, no close frame, no close code — the socket simply sits mute
  until the client's own timeout fires.

Measured against `wss://socket.fyers.in/hsm/v1-5/prod` with a valid token:

| Handshake headers | Auth response |
| --- | --- |
| *(none)* | ✅ type-1 frame, status `K` |
| `User-Agent: OpenAlgo-HSM/1.0` | ✅ type-1 frame, status `K` |
| `X-Custom: test` | ✅ type-1 frame, status `K` |
| `Authorization: <bare JWT>` | ❌ silence |
| `Authorization: <appId>:<JWT>` | ❌ silence |
| `Authorization: x` | ❌ silence |

The header's *value* is irrelevant — its mere presence is disqualifying. Any other
header is harmless. The official SDK passes no headers at all here
(`data_ws.py:1653`, `__init_connection`).

**This applies to the HSM socket only.** The order socket and the TBT socket both
*require* `Authorization: <appId>:<accessToken>` — do not remove it there.

---

## Endpoint

```
wss://socket.fyers.in/hsm/v1-5/prod
```

Still current as of 2026-08-31. Confirmed in `fyers-apiv3` 3.1.16 (PyPI, 2026-08-06)
and `fyers-web-sdk-v3` 2.0.0 (npm, 2026-08-02) — the JS SDK kept the same URL across
its major-version bump. Probing adjacent versions (`v1-4`, `v1-6` … `v2-0`) returns
**HTTP 404** from Cloudflare, so `v1-5` is the only live version; a 404 at handshake
means the URL is wrong, not that the version has moved on.

## Credential: the `hsm_key` JWT claim

The HSM socket does **not** use the raw access token. It uses the `hsm_key` claim
embedded in the access token's JWT payload (a 56-character string):

```python
payload_b64 = access_token.split(".")[1]
payload_b64 += "=" * (-len(payload_b64) % 4)          # restore base64 padding
payload = json.loads(base64.urlsafe_b64decode(payload_b64))
hsm_key = payload["hsm_key"]
```

Pass the **bare JWT**, not the `appId:token` form — the SDK splits on `.` and an
`appId:` prefix mangles the payload segment. Check `payload["exp"]` against the
current epoch before connecting; an expired token cannot be distinguished from a
network fault once the socket is open.

Representative payload claims: `aud`, `at_hash`, `display_name`, `oms`, **`hsm_key`**,
`isDdpiEnabled`, `isMtfEnabled`, `fy_id`, `appType`, `exp`, `iat`, `iss`, `nbf`, `sub`.

## Framing

Every frame is a **binary** WebSocket message (`ABNF.OPCODE_BINARY`), big-endian:

```
[u16 length][u8 request_type][u8 field_count]  then field_count × [u8 field_id][u16 field_length][value]
```

`length` is the total frame size **minus 2** (it does not count itself).

### Request type 1 — authenticate

Sent immediately on `on_open`. Four fields:

| # | Field | Length | Value |
| --- | --- | --- | --- |
| 1 | AuthToken | `len(hsm_key)` | the `hsm_key` string |
| 2 | Mode | 1 | `"P"` (production) |
| 3 | Flag | 1 | `0x01` |
| 4 | Source | `len(source)` | client identifier string |

Total size is `18 + len(hsm_key) + len(source)`.

```python
size = 18 + len(hsm_key) + len(source)
b = bytearray()
b += struct.pack("!H", size - 2)
b += bytes([1, 4])                                                   # req type, field count
b += bytes([1]) + struct.pack("!H", len(hsm_key)) + hsm_key.encode()
b += bytes([2]) + struct.pack("!H", 1) + b"P"
b += bytes([3]) + struct.pack("!H", 1) + bytes([1])
b += bytes([4]) + struct.pack("!H", len(source)) + source.encode()
```

The `source` string is not validated server-side — `"OpenAlgo-HSM"` is accepted.
(The official clients send `"PythonSDK-3.0.9"` and `"JS_API"`.)

### Request type 4 — subscribe

```
[u16 length][0x04][0x02]
  [0x01][u16 blob_length][u16 symbol_count][u8 len][symbol]…   # scrip blob
  [0x02][u16 1][u8 channel]                                    # channel, default 11
```

Scrip token format — `"<prefix>|<segment>|<exchange_token>"`:

| Prefix | Feed |
| --- | --- |
| `sf` | equity / F&O quote |
| `if` | index |
| `dp` | market depth (5 levels; rejected for indices) |

Examples: `sf|nse_cm|2885` (RELIANCE), `sf|nse_cm|3045` (SBIN), `if|nse_cm|Nifty 50`.

Request type **5** is unsubscribe, with the same field layout.

## Response frame types

Dispatch on `data[2]`:

| Type | Meaning |
| --- | --- |
| 1 | Authentication response |
| 4 | Subscribe acknowledgement |
| 5 | Unsubscribe acknowledgement |
| 6 | Data feed |
| 7 / 8 | Resume / pause acknowledgement |
| 12 | Lite/full mode acknowledgement |
| 13 | Master data (large blob on connect) |

Within a data feed frame, the per-scrip data-type byte is `0x53` (`'S'`) for a
snapshot and `0x55` (`'U'`) for an incremental update.

### Reading the auth response — check for `"K"`

`data[2] == 1` means only *"this is an auth response"*. The **verdict** is a status
string carried in the first field, and it is `"K"` when the credential was accepted:

```
[0:2] u16 length   [2] request type   [3] field count   [4] field id
[5:7] u16 field length   [7 : 7+len] status string  →  "K" == accepted
```

Treating any type-1 frame as success reports a rejected token as a healthy
connection that then never delivers a tick. A real accepted response looks like:

```
663e 01 03 | 01 0001 4b | 02 0002 0002 | 03 6630 7b0a…
 len  ty fc | f1 len  'K'| f2 len  val  | f3  len  {…master data JSON…}
```

The type-1 frame is large (~26 KB) because field 3 carries the master-data JSON.

## Keepalive

The feed sends **no inbound application-level heartbeat**, so a liveness watchdog
driven purely by data arrival will misfire during quiet or closed markets. Two
options, both verified working:

- **WebSocket protocol ping/pong** — `run_forever(ping_interval=30, ping_timeout=10)`,
  feeding the liveness clock from `on_ping`/`on_pong`. This is what OpenAlgo uses.
- **Application-level ping** — the SDK's approach: send the 3-byte binary frame
  `bytes([0, 1, 11])` every 10 seconds from a dedicated thread (`data_ws.py:1644`).

## Comparison: the three Fyers sockets

| | HSM market data | Order updates | TBT 50-depth |
| --- | --- | --- | --- |
| Endpoint | `wss://socket.fyers.in/hsm/v1-5/prod` | `wss://socket.fyers.in/trade/v3` | `wss://rtsocket-api.fyers.in/versova` |
| Auth | **in-band binary frame** (`hsm_key`) | `Authorization: <appId>:<token>` header | `Authorization: <appId>:<token>` header |
| `Authorization` header | **must be absent** | required | required |
| Encoding | binary TLV | JSON text | JSON request / protobuf response |
| Docs | this file | `FYERS_API_v3.md` ~6010 | `FYERS_API_v3.md` ~6237 |

## Known SDK quirks (do not copy these)

- `FyersDataSocket` is a **singleton** — a second instantiation returns the first
  object but re-runs `__init__`, clobbering the live connection's state.
- The subscribe/unsubscribe frames compute `data_len` from the *access token* rather
  than the hsm token, so the declared length does not match the real frame. The
  server ignores it.
- The lite/full mode frame (request type 12) packs its length prefix as a literal
  zero.
- The SDK's ack-count parse in `__auth_resp` reads from a misaligned offset, so its
  request-type-3 acknowledgement effectively never fires. OpenAlgo does not implement
  acks; a 20-second run received 96 feed frames with no acks and no disconnect.

## Related regulatory context

See `FYERS_REGULATORY_CHANGES_APRIL_2026.md`. Market data is classified as a
**non-transactional** API and is explicitly exempt from the static-IP whitelisting
requirement — that gate applies to order placement only.
