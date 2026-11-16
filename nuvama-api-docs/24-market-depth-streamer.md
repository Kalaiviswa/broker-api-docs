# Market Depth Streamer

```csharp
#Callback Method sample

public void SubscriberCallbackDepth(string msg)
{
System.Console.WriteLine(msg);
}

APIConnect apiconnect = new APIConnect (apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiconnect.initDepthStreaming().subscribeDepthFeed(symbolList, SubscriberCallbackDepth);
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
const depthStreamer = apiConnect.initDepthStreaming();
depthStreamer.subscribeDepthFeed(symbols, callBack);
depthStreamer.unsubscribeDepthFeed();
})
.catch(console.log("Init Failed"));
```

```python
  
#Callback Method Sample

def callBack(response)
print(response)

from APIConnect.APIConnect import APIConnect
from feed.depth_feed import DepthFeed

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

depth_streamer = api_connect.initDepthStreaming()
depth_streamer.subscribeDepthFeed(symbols,  callBack)
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
IDepthFeed depthFeed = connect.initDepthStreaming();
depthFeed.subscribeDepthFeed(symbols,callback);
```

### Parameters

| Parameter | Description |
| --- | --- |
| symbols | Symbol list for subscription : Symbol_exchange (exchangetoken) to be obtained from Contract File |
| callBack | Callback method to receive the Feed in |

### Unsubscribe

This method will unsubscribe the symbols from the streamer. After successful invocation of this, will stop the streamer packets of these symbols.

```csharp
apiconnect.initDepthStreaming().UnsubscribeDepthFeed();        
```

```python
depth_streamer.unsubscribeDepthFeed()
```

```java
depthFeed.unsubscribeDepthFeed();
```

Market Depth Streamer End

### Depth Responses

```
{
   "response":{
      "data":{
         "askValues":[
            {
                "no":"2",
                "price":"46007.65",
                "qty":"27"
            },
            {
                "no":"20",
                "price":"46007.75",
                "qty":"27"
            },
            {
                "no":"3",
                "price":"46007.85",
                "qty":"27"
            },
            {
                "no":"5",
                "price":"46007.90",
                "qty":"27"
            },
            {
                "no":"1",
                "price":"46008.05",
                "qty":"27"
            }
         ],
         "bidValues":[
            {
                "no":"2",
                "price":"46006.80",
                "qty":"121"
            },
            {
                "no":"1",
                "price":"46006.75",
                "qty":"121"
            },
            {
                "no":"1",
                "price":"46006.70",
                "qty":"121"
            },
            {
                "no":"1",
                "price":"46006.50",
                "qty":"121"
            },
            {
                "no":"1",
                "price":"46006.20",
                "qty":"121"
            }
         ],
         "ltt":"21/07/2023 12:35:39",
         "symbol":"42692_NFO",
         "taq":"89865",
         "tbq":"67800"
      },
      "streaming_type":"quote2"
   }
}
```

| Symbol | Value |
| --- | --- |
| askValues | SELLER DATA |
| bidValues | BUYER DATA |
| no | NUMBER OF TRADES |
| price | PRICE OF THE TRADE |
| qty | QUANTITY OF TRADES |
| ltt | LAST TRADED TIME |
| symbol | SUBSCRIBED SYMBOL |
| tbq | TOTAL BUY QUANTITY |
| taq | TOTAL SELL QUANTITY |

Orders Streamer Start
