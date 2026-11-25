# Overview

## Introduction

XTS API is a high-performance trading API designed to deliver seamless integration with advanced trading platforms. It enables developers, brokers, and third-party vendors to build reliable, low-latency trading and investment solutions with ease.  
  
The API offers REST-like endpoints for executing and modifying orders in real time, managing portfolios, accessing live market data, and implementing complex trading strategies. All communication is secured and handled via JSON-formatted requests and responses, with standard HTTP codes used to indicate success or failure states.  
  
Users receive a unique API key and secret during application registration, along with the option to register a redirect URL for secure authentication flows. The API is optimized for high throughput, scalable performance, and supports large concurrent user bases, ensuring stability even in volatile market conditions.  
  
**Disclaimer:** The API access and data are strictly for registered clients and vendors. Users should safeguard their trading credentials and never embed sensitive secrets directly in client applications.  
  
***Note:*** API key has to be created by client itself not anyone else. Please do not share trading id / Password with anyone.

## API Environment URLs

```http
POST https://developers.symphonyfintech.in/hostlookup
```

## Libraries and SDKs

Below is a list of pre-built client libraries and SDKs for Symphony API written in various programming languages that can be used to interact with the APIs without having to make raw HTTP calls

**Symphony Python Library**

[Python API SDK](https://github.com/symphonyfintech/xts-pythonsdk-binarymarketdata-withbroadcastmode-api-sdk)

**Symphony Node JS Library**

[NodeJs Interactive API](https://www.npmjs.com/package/xts-interactive-api)

[NodeJs MarketData API](https://github.com/symphonyfintech/xts-binary-marketdata-nodeJS-api)

**Symphony Java Library**

[Java API SDK](https://github.com/symphonyfintech/xts-javaclient-api-sdk)

## Obtain Your API Credentials

**to Get Access to XTS Trimmed Interactive API Services**

#### To access Trimmed Interactive API services, you need a public key. Follow these steps:

- **Register on the Broker’s API Dashboard**
  - Visit your broker’s API dashboard page.
  - Register yourself as an API user.
- **Verify Your Email**
  - After registration, you’ll receive a verification link via email.
  - Click the link to validate your email ID.
  - You will be redirected to the login page.
- **Subscribe to the API Service**
  - Log in to the API dashboard: This is sample url [https://developers.symphonyfintech.in/dashboard](https://developers.symphonyfintech.in/dashboard)
  - Select **Trimmed Interactive API subscription** and provide the required details.
  - Wait for an approval email from the broker’s support team.
- **Receive Your API Keys**
  - Once approved, you’ll get an email containing your **appKey** and **secretKey**.
  - Keep these keys safe for future use.
- **Important Notes**
  - Only **One session** is allowed per **appKey–secretKey** combination.
  - Do **not share** your keys with others.
  - If you suspect your keys are compromised, log in to the API dashboard and **regenerate** new keys then update them in your source code or configuration.

### How To Access XTS Trimmed Interactive API Services

Register![](https://symphonyfintech.com/api-document/asset/img/right_arrow_blue.svg) Verify Email ![](https://symphonyfintech.com/api-document/asset/img/right_arrow_blue.svg) Subscrive ![](https://symphonyfintech.com/api-document/asset/img/right_arrow_blue.svg) Approval ![](https://symphonyfintech.com/api-document/asset/img/right_arrow_blue.svg) Get Key

## Authentication Token Requirement

For all API requests **the login API**, an **authentication token** must be included in the request header.

- The token is generated only after a **successful user login**.
- It remains valid for **24 hours** from the time of generation..
- After the validity period, the token will **expire** and must be refreshed by logging in again.

```http
Headers:
Content-Type: application/json
authorization: eyJ1c2VySUQiOiJSVVBFU0giLCJpYXQiOjE1NTIxMjIwOTEsImV4cCI6MTU1MjIwODQ5MX0

```

**Note:** Default values are examples provided in response.

## Request & Response Structure

All GET and DELETE request parameters go as query parameters, and POST and PUT parameters as form-encoded. The user has to input an authorization in the header for every request. All request parameters as application/json parameters.  
Responses from the API will be in JSON

### Successful request:

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "type": "success",
  "code": "status code",
  "description": "description message",
  "result":
}
```

All responses from the API server are JSON with the content-type application/json unless explicitly stated otherwise. A successful 200 OK response always has a JSON response body with a status key with the value success. The result key contains the full response payload.

### Failed request:

```http
HTTP/1.1 400 Server error
Content-Type: application/json
```

```json
{
  "type": "error",
  "code": "error code",
  "description": "error message",
}
```

## Error Handling

**Common HTTP error codes**

| Code | Error Description |
| --- | --- |
| 400 | Missing or bad request parameters or values |
| 404 | Request resource was not found |
| 429 | Too many requests to the API (rate limiting) |
| 500 | Something unexpected went wrong |

## Rate Limit

Here is the rate limit for Interactive API calls

### Why Throttling is Important

#### Throttling ensures that API requests are distributed evenly over time to:

- Prevent server overload and downtime during peak hours
- Maintain fair access to resources for all clients
- Protect the stability and performance of the trading system during volatile market conditions
- Avoid accidental denial-of-service caused by excessive automated requests

### Rate Limits Table

| API Name | Endpoint | Method | Limit (API Request/Sec) |
| --- | --- | --- | --- |
| Unified Order API Throttle Limit | Unified Order API Throttle Limit | Note | 10 |
| Balance | /user/balance | GET | 1 |
| Profile | /user/profile | GET | 1 |
| Brokerage Calculator | /user/calculatebrokerage | POST | 10 |
| Cancel All | /orders/cancelall | POST | 1 |
| Orderbook / Order History | /orders | GET | 1 |
| Tradebook | /orders/trades | GET | 1 |
| Spread Orderbook | /orders/spread | GET | 1 |
| Place GTT Order | /orders/gttorder | POST | 1 |
| Modify GTT Order | /orders/gttorder | PUT | 1 |
| Cancel GTT Order | /orders/gttorder | DELETE | 1 |
| GTT Orderbook | /orders/gttorderbook | GET | 1 |
| Holding | /portfolio/holdings | GET | 1 |
| Position | /portfolio/positions | GET | 1 |
| Position Convert | /portfolio/positions/convert | PUT | 10 |
| Regular Order Margin | /orders/margindetails | POST | 10 |
| Regular Order Modify Margin | /orders/modifyordermargindetails | POST | 10 |
| Cover Order Margin | /orders/comargindetails | POST | 10 |
| Cover Order Modify Margin | /orders/comodifymargindetails | POST | 10 |
| Bracket Order Margin | /orders/bomargindetails | POST | 10 |
| Exchange Status | /status/exchange | GET | 1 |
| Exchange Message | /messages/exchange | GET | 1 |

***Note:*Unified Order Throttle Limit:**  
  
This is a combined rate limit applied across all order-related APIs listed below.  
The standard limit is 10 requests per second, shared cumulatively among these APIs  
(Place Order,Modify Order,Cancel Order,Place BO (Bracket Order),Modify BO,Cancel BO,Place CO (Cover Order),Exit Cover,Place Spread Order,Modify Spread Order,Cancel Spread Order).
