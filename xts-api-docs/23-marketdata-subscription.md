# Market Data API: Socket Subscription

## Subscribe to Socket

This API request is used to subscribe to market data over a WebSocket connection for specified exchange instruments and message codes provided in the request. Upon successful subscription, the user receives an acknowledgment response containing the latest quote data along with the remaining subscription count, which is AppKey-specific and configurable via the API dashboard. Once subscribed, real-time market data for the specified instrument(s) will be continuously streamed on the market data WebSocket.

### URL

```http
PUT https://developers.symphonyfintech.in/apibinarymarketdata/instruments/subscription
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **instruments** | Array | Y | Array of instrument objects |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Y | ExchangeSegment |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Y | Exchange Scrip code or Symbol Token is unique identifier |
| **MessageCode** | MessageCode (Integer, 5) | Y | It is system generated message code |

### Request Body JSON

```json
{
  "instruments": [
    {
      "exchangeSegment": 1,
      "exchangeInstrumentID": 22
    }
  ],
  "xtsMessageCode": 1502
}
```

### Response Body JSON

```json
{
  "type": "success",
  "code": "s-session-0001",
  "description": "Instrument subscribed successfully!",
  "result": {
    "mdp": 1501,
    "quotesList": [
      {
        "exchangeSegment": 1,
        "exchangeInstrumentID": 22
      }
    ],
    "listQuotes": [
      "{\"MessageCode\":1501,\"ExchangeSegment\":1,\"ExchangeInstrumentID\":\"22\",\"LastTradedPrice\":1723,\"LastTradedQunatity\":15,\"TotalBuyQuantity\":18446,\"TotalSellQuantity\":25283,\"TotalTradedQuantity\":189238,\"AverageTradedPrice\":1699.1,\"LastTradedTime\":1453476469,\"LastUpdateTime\":1453476469,\"PercentChange\":1.54,\"Open\":1696.8,\"High\":1724,\"Low\":1673.1,\"Close\":1696.8,\"TotalValueTraded\":0,\"AskInfo\":{\"Size\":1,\"Price\":1723.5,\"TotalOrders\":1,\"BuyBackMarketMaker\":0},\"BidInfo\":{\"Size\":271,\"Price\":1723,\"TotalOrders\":3,\"BuyBackMarketMaker\":0},\"XMarketType\":1,\"BookType\":1}"
    ],
    "Remaining_Subscription_Count": 48
  }
}
```

## Unsubscribe to Socket

This API request is used to unsubscribe from market data streaming for instruments that are already subscribed. Upon successful unsubscription, the server sends an acknowledgment confirming the unsubscription, stops sending market data for the specified instrument(s) on the WebSocket, and releases the corresponding subscription count, making it available for future subscriptions.

### URL

```http
PUT https://developers.symphonyfintech.in/apibinarymarketdata/instruments/subscription
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **instruments** | Array | Y | Array of instrument objects |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Y | ExchangeSegment |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Y | Exchange Scrip code or Symbol Token is unique identifier |
| **xtsMessageCode** | [xtsMessageCode](17-marketdata-enums.md#4-xts-message-code) | Y | It is system generated message code |

### Request Body JSON

```json
{
  "instruments": [
    {
      "exchangeSegment": 1,
      "exchangeInstrumentID": 22
    }
  ],
  "xtsMessageCode": 1502
}
```

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-response-0001",
    "description": "Instrument subscription deleted!",
    "result": {
      "Remaining_Subscription_Count": 4
    }
  }
]
```
