# NodeJS library for Accessing the Services Provided by Nuvama

The Library API Connect is a set of REST-like APIs that expose many capabilities required to build
a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live
market data, and more, with the simple HTTP API collection This module provides an easy to use abstraction
over the HTTP APIs. The HTTP calls have been converted to methods and their JSON responses are returned.

NodeJS SDK :

- API version: v1

## NodeJS supported

- Node v14.17.6 or later

## NodeJS Dependencies

- [ini](https://www.npmjs.com/package/ini)
- [fs](https://www.npmjs.com/package/fs)
- [readline](https://www.npmjs.com/package/readline)
- [net](https://www.npmjs.com/package/net)
- [jszip](https://www.npmjs.com/package/jszip)
- [log4js](https://www.npmjs.com/package/log4js)

We recommend using [npm](https://www.npmjs.com/) to install the latest
version of the packages:

```javascript
npm install ini
npm install fs
npm install readline
npm install net
npm install jszip
npm install log4js
```

## Installation

Run the following command to install node packages

```javascript
npm install api_connect_nodejs
```

## Configuration from external INI file

When using APIConnect wrapper ,various parameters are read from the [Settings.ini](https://www.nuvamawealth.com/library-documentation/source/assets/settings-nodejs.zip) file.These
parameters are configurable. Description for these parameters is given below. This ini file has to be present
inside of **conf** directory.

| Parameters | Description | Remarks |
| --- | --- | --- |
| [GLOBAL] | Contains global configuration |  |
| LogLevel | Contains logging related configuration | All |
| hostName | Host address of streaming socket. | ncst.nuvamawealth.com |
| port | Port of streaming socket. | 9443 |

# APIConnect documentation

- [User Login Flow](https://www.nuvamawealth.com/library-documentation/docs/UserLoginFlow.md.html)

## Getting Started

```javascript
#!node
const { APIConnect } = require("api_connect_nodejs");
# Redirect the user to the login url - <https://www.nuvamawealth.com/api-connect/login?api_key=xxx>
# after the login flow, You will get requestId.
# Generate a session with this request id
# as follows.
apiConnect = new APIConnect("apiKey", "api_secret_password", "requestId", 'true');
# Place an order
apiConnect.Init().then(()=>{
    response = apiConnect.PlaceTrade('symbol',
                          'exchange',
                          'buy-sell',
                          validity',
                          'orderType',
                          'quantity',
                          'exchangeCode',
                          'limitPrice',
                          'productCode');
                          # Fetch all orders
apiConnect.OrderBook();
#Fetch all trades
apiConnect.TradeBook();
}).catch((err) => console.log("Init Failed"+err))
```
