# Reduced Quotes Streamer

```csharp
#Callback Method sample

public void SubscriberCallbackQuotes(string msg)
{
System.Console.WriteLine(msg);
}

APIConnect apiconnect = new APIConnect (apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiconnect.initQuotesStreaming().SubscribeReducedQuotesFeed(symbolList, SubscriberCallbackQuotes);
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
const quotesStreamer = apiConnect.initQuotesStreaming();
quotesStreamer.subscribeReducedQuotesFeed(symbols, callBack);
quotesStreamer.unsubscribeReducedQuotesFeed();
})
.catch(console.log("Init Failed"));
```

```python
  
#Callback Method Sample

def callBack(response)
print(response)

from APIConnect.APIConnect import APIConnect
from feed.reduced_quotes_feed import ReducedQuotesFeed

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

quotes_streamer = api_connect.initReducedQuotesStreaming()
quotes_streamer.subscribeReducedQuotesFeed(symbols,  callBack)
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
IQuotesFeed quotesFeed = connect.initQuotesStreaming();
quotesFeed.subscribeReducedQuotesFeed(symbols,callback);
```

### Parameters

| Parameter | Description |
| --- | --- |
| symbols | Symbol list for subscription : Symbol_exchange (exchangetoken) to be obtained from Contract File |
| callBack | Callback method to receive the Feed in |

### Unsubscribe

This method will unsubscribe the symbols from the streamer. After successful invocation of this, will stop the streamer packets of these symbols.

```csharp
apiconnect.initQuotesStreaming().UnsubscribeReducedQuotesFeed();        
```

```python
quotes_streamer.unsubscribeReducedQuotesFeed()
```

```java
quotesFeed.unsubscribeReducedQuotesFeed();
```

Reduced Quotes Streamer End

### Reduced Quotes Responses

```
{
   "response":{
      "data":{
         "aPr":"2527.00",
         "aSz":"1277",
         "altt":"21 Jul 2023, 12:44:55 PM",
         "avgPrc":"2560.72",
         "bPr":"2526.15",
         "bSz":"252",
         "c":"2637.95",
         "chg":"-28.95",
         "chgp":"-1.10",
         "futPrc":"0.00",
         "h":"0.00",
         "hCL":"2881.80",
         "l":"0.00",
         "lCL":"2357.90",
         "ltp":"2609.00",
         "ltq":"3",
         "ltt":"21 Jul 2023, 12:44:55 PM",
         "lut":"21 Jul 2023, 12:44:55 PM",
         "mO":"0",
         "ntTrdVal":"219959.91",
         "o":"2609.00",
         "oI":"58056750",
         "oiChg":"--",
         "oiChgp":"--",
         "refLP":"0.00",
         "spotPrc":"0.00",
         "sym":"2885_NSE",
         "tBQ":"297310",
         "tSQ":"571992",
         "ttlImbalance":"0",
         "vol":"8589768",
         "yHgh":"2856.15",
         "yLw":"2180.00",
      },
      "streaming_type":"quote"
   }
}
```

| Symbol | Value |
| --- | --- |
| o | OPEN |
| h | HIGH |
| l | LOW |
| c | CLOSE |
| hCL | HIGH CIRCUIT LIMIT |
| lCL | LOW CIRCUIT LIMIT |
| ltp | LAST TRADED PRICE |
| vol | TOTAL VOLUME |
| yHgh | YEAR HIGH |
| yLw | YEAR LOW |
| avgPrc | AVERAGE PRICE |
| chg | CHANGE |
| chgp | CHANGE % |
| oiChg | OI CHANGE |
| oiChgp | OI CHANGE % |
| mO | MARKET STATUS (IF OPEN(1) OR CLOSE(2)) |
| tBQ | TOTAL BUY QTY |
| tSQ | TOTAL SELL QTY |
| ltq | LAST TRADED QUANTITY |
| oI | OPEN INTEREST |
| spotPrc | SPOT PRICE |
| futPrc | FUTURE PRICE |
| ltt | LAST TRADED TIME |
| lut | LAST UPDATED TIME |
| aPr | ASK PRICE |
| bPr | BID PRICE |
| aSz | ASK SIZE |
| bSz | BID SIZE |
| sym | SYMBOL |
| altt | ACTUAL LAST TRADED TIME |
| ntTrdVal | NET TRADED VALUE |

MiniQuotes Streamer Starts
