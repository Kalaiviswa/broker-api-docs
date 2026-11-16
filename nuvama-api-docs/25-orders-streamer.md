# Orders Streamer

```csharp
#Callback Method sample

 public void SubscriberCallbackOrder(string msg)
 {
     System.Console.WriteLine(msg);
 }

APIConnect apiconnect = new APIConnect (apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiconnect.initOrdersStreaming().SubscribeOrderFeed(e.Stremer_AccId, e.Stremer_UserId, SubscriberCallbackOrder);
```

```javascript
  #Callback Method Sample

  const callBack = (error, data, socketClose) => {
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
const ordersStreamer = apiConnect.initOrdersStreaming(accId, userId);
ordersStreamer.subscribeOrdersFeed(callBack);
ordersStreamer.unsubscribeOrdersFeed();
})
.catch(console.log("Init Failed"));
```

```python
      
#Callback Method Sample

def callBack(response)
    print(response)

from APIConnect.APIConnect import APIConnect

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

orders_streamer = api_connect. initOrdersStreaming(acc_id, user_id)
orders_streamer.subscribeOrdersFeed(callBack)
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
  
import com.apiconnect.lib.APIConnect;
APIConnect connect = new APIConnect(apiKey,password,reqId,true,iniFilePath);
IOrdersFeed ordersFeed = connect.initOrdersStreaming(accId,userId);
ordersFeed.subscribeOrdersFeed(callback);
```

### Parameters

| Parameter | Description |
| --- | --- |
| acc_id | Customer Account ID (Trading A/C No. available in My Profile section of Nuvamawealth.com OR get it from eqAccID of Get Login Info) |
| user_id | Your User ID for Nuvamawealth.com |
| callBack | Callback method to receive the Feed in |

### Unsubscribe

This method will unsubscribe the symbols from the streamer. After successful invocation of this, will stop the streamer packets.

```csharp
apiconnect.initOrdersStreaming().UnsubscribeOrderFeed();
```

```python
    orders_streamer.unsubscribeOrdersFeed()
```

```java
ordersFeed.unsubscribeOrdersFeed(callback);
```

Live News Streamer Start
