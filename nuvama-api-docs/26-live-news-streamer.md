# Live News Streamer

### Properties

| Parameter | Description |
| --- | --- |
| callBack | Callback method to receive the Feed in |

```csharp
#Callback Method sample

public void SubscriberCallbackOrder(string msg)
{
    System.Console.WriteLine(msg);
}

APIConnect apiconnect = new APIConnect (apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiconnect.initLiveNewsStreaming().SubscribeLiveNewsFeed(SubscriberCallbackLiveNews);
  
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
const newsStreamer = apiConnect.initLiveNewsStreaming();
newsStreamer.subscribeLiveNewsFeed(callBack);
newsStreamer.unsubscribeLiveNewsFeed();
})
.catch(console.log("Init Failed"));
  
```

```python
      
 #Callback Method Sample

def callBack(response)
    print(response)  

from APIConnect.APIConnect import APIConnect

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

news_streamer = api_connect.initLiveNewsStreaming()
news_streamer.subscribeLiveNewsFeed(callBack)
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
ILiveNewsFeed liveNewsFeed = connect.initLiveNewsStreaming();
liveNewsFeed.subscribeLiveNewsFeed(callback);
  
```

### Unsubscribe

This method will unsubscribe the symbols from the streamer. After successful invocation of this, will stop the streamer packets.

```csharp
apiconnect.initLiveNewsStreaming().UnsubscribeLiveNewsFeed();
```

```python
  news_streamer.unsubscribeLiveNewsFeed()
```

```java
liveNewsFeed.unsubscribeLiveNewsFeed();
```

```
Succesful Response

{
  "response": {
    "data": {
      "category": "Default",
      "custom_elements": [
        {
          "dpName": "abc",
          "hghlTxt": "ABC",
          "sym": "13844_NSE"
        }     
      ],
        "date": "2022-01-01T00:00:00",
        "description": "xyz",
        "guid": "5b04ff38f4cd392339e7126f",
        "title": "XYZ" 
      },
      "streaming_type": "news"
  }
}
```

Live News Streamer End
