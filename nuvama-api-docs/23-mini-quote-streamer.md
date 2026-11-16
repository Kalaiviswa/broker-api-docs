# Mini Quote Streamer

```csharp
#Callback Method sample

public void SubscriberCallbackMiniQuotes(string msg)
{
System.Console.WriteLine(msg);
}

APIConnect apiconnect = new APIConnect (apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiconnect.initMiniQuoteStreaming().subscribeMiniQuoteFeed(symbolList, SubscriberCallbackMiniQuotes);
```

```javascript
#Callback Method Sample

const callBackMethod = (error, data, socketClose) => {
if (error) {
console.log('error is ',error)
}

if (data) {
console.log('data is ',data)
}

if (socketClose) {
console.log('socket closed ')
}
}

const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract);
apiConnect.Init().then(() => {
const miniquotesStreamer = apiConnect.initMiniQuoteStreaming();
miniquotesStreamer.subscribeMiniQuoteFeed(symbols, callBack);
miniquotesStreamer.unsubscribeMiniQuoteFeed();
})
.catch(console.log("Init Failed"));
```

```python
  
#Callback Method Sample

def callBack(response)
print(response)

from APIConnect.APIConnect import APIConnect
from feed.miniQuote_feed import MiniQuoteFeed

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

mini_quotes_streamer = api_connect.initMiniQuoteStreaming()
mini_quotes_streamer.subscribeMiniQuoteFeed(symbols,  callBack)
```

```java
#Callback Method Sample

import com.apiconnect.lib.interfaces.CallBack;
private class SubscriberCallback implements CallBack {
      @Override
      public void subscribeStreaming(String response) throws IOException {
          try{
              System.out.println("Streaming response is " + response);
          }catch (Exception ex){
              out.println("Error inside SubscriberCallback subscribeStreaming method" + ex.getMessage());
          }
      }
  }

import com.apiconnect.lib.APIConnect;
APIConnect connect = new APIConnect(apiKey,password,reqId,true,iniFilePath);
IMiniQuoteFeed miniquotesFeed = connect.initMiniQuoteStreaming();
miniquotesFeed.subscribeMiniQuoteFeed(symbols,callback);
```

### Parameters

| Parameter | Description |
| --- | --- |
| symbols | Symbol list for subscription : Symbol_exchange (exchangetoken) to be obtained from Contract File |
| callBack | Callback method to receive the Feed in |

### Unsubscribe

This method will unsubscribe the symbols from the streamer. After successful invocation of this, will stop the streamer packets of these symbols.

```csharp
apiconnect.initMiniQuoteStreaming().unsubscribeMiniQuoteFeed();        
```

```python
mini_quotes_streamer.unsubscribeMiniQuoteFeed()
```

```java
miniquotesFeed.unsubscribeMiniQuoteFeed();
```

Reduced Quotes Streamer End

### Mini Quotes Responses

```
{
   "response":{
      "data":{
        
         "c":"2637.95",
         "chg":"-28.95",
         "chgp":"-1.10",
         "h":"0.00",
         "l":"0.00",
         "ltp":"2609.00",
         "lut":"21 Jul 2023, 12:44:55 PM",
         "o":"2609.00",
         "oI":"58056750",
         "oiChg":"--",
         "oiChgp":"--",
         "refLP":"0.00",
         "sym":"2885_NSE",
         "ttlImbalance":"0",
         "vol":"8589768",
      },
      "streaming_type":"miniquote"
   }
}
```

| Symbol | Value |
| --- | --- |
| o | OPEN |
| h | HIGH |
| l | LOW |
| c | CLOSE |
| ltp | LAST TRADED PRICE |
| vol | TOTAL VOLUME |
| chg | CHANGE |
| chgp | CHANGE % |
| oiChg | OI CHANGE |
| oiChgp | OI CHANGE % |
| oI | OPEN INTEREST |
| lut | LAST UPDATED TIME |
| sym | SYMBOL |

Market Depth Streamer Starts
