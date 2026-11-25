# Market Data API: Overview

## Introduction

**Binary Market Data** combines **RESTful APIs** with **Socket.IO–based streaming** to deliver high-performance real-time market feeds. It offers fast, reliable data essential for building responsive stock-market and trading platforms. Designed for efficiency, it ensures **low latency, low bandwidth consumption,** and a **robust streaming experience,** enabling seamless real-time market visualization and analytics.

## API Environment URLs

```http
https://developers.symphonyfintech.in/apibinarymarketdata
```

## Libraries and SDKs

Symphony provides ready-to-use client libraries and SDKs in multiple languages. These libraries simplify authentication, request handling, and integration with Symphony APIs.

**Symphony Python Library**

[Python API SDK](https://github.com/symphonyfintech/xts-pythonsdk-binarymarketdata-api-sdk)

## Obtain Your API Credentials

**How to Get Access to XTS Binary Marketdata API Services**

#### To access XTS Binary Marketdata API services, you need a public key. Follow these steps:

- **Register on the Broker’s API Dashboard**
  - Visit your broker’s API dashboard page.
  - Register yourself as an API user.
- **Verify Your Email**
  - After registration, you’ll receive a verification link via email.
  - Click the link to validate your email ID.
  - You will be redirected to the login page.
- **Subscribe to the API Service**
  - Log in to the API dashboard: [https://developers.symphonyfintech.in/dashboard](https://developers.symphonyfintech.in/dashboard)
  - Select **Binary Marketdata API subscription** and provide the required details.
  - Wait for an approval email from the broker’s support team.
- **Receive Your API Keys**
  - Once approved, you’ll get an email containing your **appKey** and **secretKey**.
  - Keep these keys safe for future use.
- **Important Notes**
  - Only **One session** is allowed per **appKey–secretKey** combination.
  - Do **not share** your keys with others.
  - If you suspect your keys are compromised, log in to the API dashboard and **regenerate new keys** then update them in your source code or configuration.

### How To Access XTS Binary Marketdata API Services

Register![](https://symphonyfintech.com/api-document/asset/img/right_arrow_blue.svg) Verify Email ![](https://symphonyfintech.com/api-document/asset/img/right_arrow_blue.svg) Approval ![](https://symphonyfintech.com/api-document/asset/img/right_arrow_blue.svg) Get Key

## Authentication Token Requirement

For all API requests **except the login API,** an **authentication token** must be included in the request header.

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

All GET and DELETE request parameters go as query parameters, and POST and PUT parameters as form-encoded. The user has to input an authorization in the header for every request. All request parameters as application/json parameters. **Responses from the API will be in JSON**

### Successful request:

```http
HTTP/1.1 200 OK
Content-Type: application/json
{
  "type": "success",
  "code": "status code",
  "description": "description message",
  "result": {}
}
```

All responses from the API server are JSON with the content-type application/json unless explicitly stated otherwise. A successful 200 OK response always has a JSON response body with a status key with the value success. The result key contains the full response payload.

### Failed request:

```http
HTTP/1.1 400 Server Error
Content-Type: application/json

{
  "type": "error",
  "code": "error code",
  "description": "error message"
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
