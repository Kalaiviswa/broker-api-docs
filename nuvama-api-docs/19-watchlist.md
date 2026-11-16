# Watchlist

Api's related to Watchlist

## Get Watchlist Groups

These are groups that user creates his/her favourite stocks and monitors the performance of stock

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.GetWatchlistGroup();
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const watchlistGroups = apiConnect
      .getWatchlistGroups()
      .then(function (result) {})
      .catch((err) => {
        console.log("Error watchlistGroups", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));        
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.getWatchlistGroups()        
```

`GET /accounts/groups`

> Example responses

> 200 Response

```
{"resp":
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "defGr": [
    {
      "grID": "string",
      "grName": "string",
      "grValue": "string",
      "edit": "string",
      "updatedOn": 0
    }
  ],
  "usrGr": [
    {
      "grID": "string",
      "grName": "string",
      "grValue": "string",
      "edit": "string",
      "updatedOn": 0
    }
  ],
  "idxGr": [
    {
      "grID": "string",
      "grName": "string",
      "grValue": "string",
      "edit": "string",
      "updatedOn": 0
    }
  ],
  "usrTbs": [
    {
      "tab": "string",
      "tabtype": "string"
    }
  ]
  }  
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Get Watchlist Groups ends here
Get Watchlist scrips starts here

## Get Watchlist Scrips

Scrips/stocks that user created under the watchlist

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.getWatchlistScrips(string grpNm);        
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const watchlistScrips = apiConnect
      .getWatchlistScrips(groupName)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error watchlistScrips", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));               
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.getWatchlistScrips(GroupName = "MyGroup")          
```

`GET /accounts/groups/symbols`

### Parameters

| Parameter | Description |
| --- | --- |
| Group_Name | Watchlist group |

> Example responses

> 200 Response

```
{"resp":
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "syLst": [
      {
        "trdSym": "string",
        "sym": "string",
        "asTyp": "string",
        "yrLw": "string",
        "yrLwDt": "string",
        "yrH": "string",
        "yrHDt": "string",
        "o": "string",
        "h": "string",
        "l": "string",
        "c": "string",
        "ltp": "string",
        "ltt": "string",
        "altt": "string",
        "lut": "string",
        "atp": "string",
        "bidPr": "string",
        "askPr": "string",
        "vol": "string",
        "loCt": "string",
        "hiCt": "string",
        "chg": "string",
        "chgP": "string",
        "ltSz": "string",
        "tkSz": "string",
        "dpNm": "string",
        "stkPrc": "string",
        "opTyp": "string",
        "exp": "string",
        "desc": "string",
        "exc": "string",
        "brdLotQty": "string",
        "qtyUnits": "string",
        "prcUnits": "string",
        "prcQtn": "string",
        "dpInsTyp": "string",
        "bdSz": "string",
        "akSz": "string",
        "dpExpDt": "string",
        "expFlg": true,
        "opInt": "string",
        "opIntChg": "string",
        "opIntChgP": "string",
        "spotSym": "string",
        "spot": "string",
        "spotChg": "string",
        "spotChgP": "string",
        "rlOvrP": "string",
        "rlCAbs": "string",
        "ltTQty": "string",
        "tdrStDt": "string",
        "tdrEndDt": "string",
        "srpStDt": "string",
        "mxLtSz": "string",
        "trdInfoId": [
          "string"
        ],
        "ntByQty": "string",
        "ntSlQty": "string",
        "onewkhi": "string",
        "onewklo": "string",
        "onemnhi": "string",
        "onemnlo": "string",
        "thrmnhi": "string",
        "thrmnlo": "string",
        "alltmhi": "string",
        "alltmhidt": "string",
        "alltmlo": "string",
        "alltmlodt": "string",
        "askivfut": "string",
        "askivspt": "string",
        "bidivfut": "string",
        "bidivspt": "string",
        "ltpivfut": "string",
        "ltpivspt": "string",
        "ntTrdVal": "string",
        "mns": "string",
        "isMTFEnabled": true,
        "rchFlg": "string",
        "nwsFlg": "string",
        "rlOvrCst": "string",
        "rlOvrCstPrc": "string",
        "rlOvrPrc": "string",
        "bta": "string",
        "pe": "string",
        "mktCap": "string",
        "delta": "string",
        "gamma": "string",
        "theta": "string",
        "vega": "string",
        "idxFutTrdSym": "string",
        "dpVal": "string",
        "pcr": "string",
        "pdVal": "string",
        "bas": "string",
        "isin": "string",
        "asSym": "string",
        "asExc": "string"
      }
    ]  
  }  
 }
} 
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Get Watchlist scrips ends here
Get Watchlist scrips starts here

## Create Watchlist Group

This will help you create watchlist groups and can have stocks under the group

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.createWatchlistGroup(string grpNm, List symbolList);               
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const createWatchlistGroup = apiConnect
      .createWatchlistGroup(groupName, symLst)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error createWatchlistGroup", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));                       
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.createWatchlistGroup(GroupName = "MyGroup", Symbols = ["3045_NSE","3456_NSE"])                 
```

`POST /accounts/groups/{groupName}`

### Parameters

| Parameter | Description |
| --- | --- |
| Group_Name | Watchlist group |
| Symbols | Each Symbol is unique and represents the stock identity. This is the exchange token to be obtained from the contract file downloaded |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "sts": "string",
      "msg": "string",
      "rearrangeTab": true,
      "updatedOn": 0    
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Create Watchlist Group ends here
Delete watchlist groups starts here

## Delete Watchlist Groups

This will help delete the active watchlist groups

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.deleteWatchlistGroups(string delGrp);                
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const deleteWatchlistGroups = apiConnect
      .deleteWatchlistGroups(groups)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error deleteWatchlistGroups", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));                    
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.deleteWatchlistGroups(GroupNames = ["MyGroup"])                  
```

`DELETE /accounts/groups`

### Parameters

| Parameter | Description |
| --- | --- |
| Group_Names | Watchlist groups that are already created earlier |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "sts": "string",
      "msg": "string",
      "rearrangeTab": true,
      "updatedOn": 0    
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Delete watchlist ends here
Rename watchlist group starts here

## Renname Watchlist Group

This will help rename the already created watchlist groups

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.renameWatchlistGroup(string grpNm, string newGrpNm);               
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const renameWatchlistGroup = apiConnect
      .renameWatchlistGroup(groupName, newGroupName)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error renameWatchlistGroup", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));                      
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.renameWatchlistGroup(GroupName = "MyGroup", NewGroupName = "MyNewGroup")                  
```

`PUT /accounts/groups/{groupName}`

### Parameters

| Parameter | Description |
| --- | --- |
| Group_Name | Watchlist group that was already created earlier |
| New_Group_Name | New Watchlist name |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "sts": "string",
      "msg": "string",
      "rearrangeTab": true,
      "updatedOn": 0    
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Rename watchlist group ends here
Add symbol to watchlist group starts here

## Add Symboles to watchlist group

Each Symbol is unique and represents the stock identity. This is the exchange token to be obtained from the
contract file downloaded and add it to the watchlist groups

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.addSymbolsWatchlist(string grpNm, List symbolList);              
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const addSymbolWatchlist = apiConnect
      .addSymbolWatchlist(groupName, symLst)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error addSymbolWatchlist", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));                   
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.addSymbolsWatchlist(GroupName = "MyGroup", Symbols = ["3495_NSE","-29"])                
```

`PUT /accounts/groups/{groupName}`

### Parameters

| Parameter | Description |
| --- | --- |
| Group_Name | Watchlist group that was already created earlier |
| Symbols | Each Symbol is unique and represents the stock identity. This is the exchange token to be obtained from the contract file downloaded |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "sts": "string",
      "msg": "string",
      "rearrangeTab": true,
      "updatedOn": 0    
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Add symbol to watchlist group ends here
Delete symbols from watchlist group starts here

## Delete Symbols from watchlist group

Will help delete the already added symbols to the groups

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.deleteSymbolsWatchlist(string grpNm, List symbolList);               
```

```javascript
const { APIConnect } = require("api_connect_nodejs");
const apiConnect = new APIConnect(
  apiKey,
  password,
  reqId,
  downloadContract
);
apiConnect
  .Init()
  .then(() => {
    const deleteSymbolWatchlist = apiConnect
      .deleteSymbolWatchlist(groupName, symLst)
      .then(function (result) {})
      .catch((err) => {
        console.log("Error deleteSymbolWatchlist", err);
        throw err;
      });
  })
  .catch((err) => console.log("Init Failed", err));                      
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
response = api_connect.deleteSymbolsWatchlist(GroupName = "MyGroup", Symbols = ["3495_NSE","-29"])                
```

`PUT /accounts/groups/{groupName}`

### Parameters

| Parameter | Description |
| --- | --- |
| Group_Name | Watchlist group that was already created earlier |
| Symbols | Each Symbol is unique and represents the stock identity. This is the exchange token to be obtained from the contract file downloaded |

> Example responses

> 200 Response

```
  {
    "msgID": "6f5da42b-668f-4e76-a129-aa85b770cacd",
    "srvTm": 1660900624895,
    "data": {
      "sts": "string",
      "msg": "string",
      "rearrangeTab": true,
      "updatedOn": 0
  }  
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

Get Watchlist Groups ends here
