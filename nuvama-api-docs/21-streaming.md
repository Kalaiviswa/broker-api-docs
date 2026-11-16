# Streaming

To subscribe to a streamer, fetch the instance of that streamer and call subscibe method from the instance providing callback method. After successful subscription, callback method will be called whenever packet is available at the streamer.

Code samples

```csharp
const feed = new Feed(accid, userid, iniFilePath);
feed.subscribe(symbols, callback, subscribe_order = true, subscribe_quote = true, accType);
```

```javascript
const feed = new Feed(accid,userid);
feed.subscribe(symbols,callBack,subscribe_order = true, subscribe_quote = true)
```

```python
        
from APIConnect.APIConnect.feed import Feed
feed = Feed(accid, userid, conf):
feed.subscribe(symbols, callBack, subscribe_order, subscribe_quote)
      
```

```java
const feed = new Feed(conf);
feed.subscribe(callBack, symbols, subscribe_order = True, subscribe_quote = True)
```

### Parameters

| Parameter | Description |
| --- | --- |
| symbols | Symbol list for subscription : Symbol_exchange (exchangetoken) to be obtained from Contract File |
| accid | Customer Account ID (Trading A/C No. available in My Profile section of Edelweiss.in OR get it from eqAccID of [Get Login Info](#get-login-info)) |
| userid | Your user name for Edelweiss.in |
| callback | Callback method to receive the Feed in |
| subscribe_order | Subscribe to order True/False |
| subscribe_quote | Subscribe to order True/False |

> Example responses

> 200 Response

Reduced Quotes Streamer Starts
