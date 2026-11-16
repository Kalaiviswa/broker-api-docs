# API Usage Threshold

| Parameter | Limit | If breached? |
| --- | --- | --- |
| Number of API orders allowed per day | **2000** | App is blocked (see below) |
| Total API requests allowed per day | **86400** | App is blocked (see below) |
| Order:Trade ratio (A → Number of API hits for Order Placed / Modify / Cancel; B → total Trades; OTR = A/B, rounded to the nearest integer) | **49:1** | App is blocked (see below) |
| Allowed orders placed per second | **10** | Reject the orders. |
| Continuous API requests | **3000 / 5 min / IP** | API requests will be get blocked for 1 min during which any further API requests will get rejected |

**Blocking for the first three limits** (one merged cell in the source table): the app will get blocked for a specified time period communicated over email; repetitive breaches may lead to permanent blocking.

- 15 mins for the first breach
- 30 mins for 2nd breach
- 1 hr for 3rd breach
- 2 hrs for 4th breach
- full day for 5th breach
