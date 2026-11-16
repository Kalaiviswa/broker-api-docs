# Trade

Api's related to Trade

## Place Trade / Order Slicing

• Order placement refers to the function by which you as a user can place an order to respective exchanges. Order
placement allows you to set various parameters like the symbol, action (buy, sell, stop loss buy, stop loss
sell), product type, validity period and few other custom parameters and then finally place the order. Any order
placed will first go through a risk validation in our internal systems and will then be sent to exchange.
Usually any order successfully placed will have OrderID and ExchangeOrderID fields populated. If ExchangeOrderID
is blank it usually means that the order has not been sent and accepted at respective exchange.

• Place trade API can be used for Order slicing also. Order Slicing is a feature that helps break down
a large order into smaller slices. This feature is allowed on Equity derivative segment only.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.PlaceTrade(tradingSymbol,exchange, action, duration, orderType, quantity, streamingSymbol, limitPrice, disclosedQuantity, triggerPrice , productCode);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const PlaceTrade = apiConnect.PlaceTrade(Trading_Symbol,
		Exchange,
		Action,
		Duration,
		Order_Type,
		Quantity,
		Streaming_Symbol,
		Limit_Price,
		Disclosed_Quantity = "0",
		TriggerPrice = "0",
		ProductCode = "CNC").then(function(result) {

  }).catch((err) => {console.log("Error PlaceTrade",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect 
        
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum
from constants.duration import DurationEnum
from constants.action import ActionEnum

response = api_connect.PlaceTrade(Trading_Symbol = "INE090A01021", Exchange = ExchangeEnum.NSE, Action = ActionEnum.BUY, Duration = DurationEnum.DAY, Order_Type = OrderTypeEnum.MARKET, Quantity = 1, Streaming_Symbol = "4963_NSE", Limit_Price = "400", Disclosed_Quantity="0", TriggerPrice="0", ProductCode = ProductCodeENum.CNC)
      
      
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String placeTradeResponse = connect.placeTrade(Trading_Symbol, Exchange, Action, Duration, Order_Type, Quantity, Streaming_Symbol, Limit_Price, Disclosed_Quantity='0', TriggerPrice='0', ProductCode='CNC');
```

`POST /eq/trade/placetrade/v1/{userID}`

> Body parameter

```json
{
  "trdSym": "INE843F01014",
  "exc": "BSE",
  "action": "BUY",
  "dur": "DAY",
  "flQty": 0,
  "ordTyp": "MARKET",
  "qty": 1,
  "dscQty": 0,
  "sym": "TRICOMFRU",
  "mktPro": null,
  "lmPrc": 0,
  "trgPrc": 0,
  "prdCode": "MIS",
  "posSqr": "N",
  "minQty": 0,
  "ordSrc": "API",
  "vnCode": null,
  "rmk": null,
  "dtDays": null
}
```

### Parameters

| Parameter | Description |
| --- | --- |
| Trading_Symbol | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| Exchange | Name of the exchange, BSE/NSE/CDS/MCX/NCDEX/NFO/BFO |
| Action | BUY/SELL |
| Duration | Order validity, DAY/IOC/EOS(for BSE) |
| Order_Type | Order type, LIMIT/MARKET/STOP_LIMIT/STOP_MARKET |
| Quantity | Quantity of the scrip to transact |
| Streaming_Symbol | exchangetoken to be obtained from Contract file downloaded |
| Limit_Price | Limit price of scrip |
| Disclosed_Quantity | Quantity to be disclosed publicly while order placement (default 0) |
| TriggerPrice | Trigger Price applicable for SL/SL-M Orders (default 0) |
| ProductCode | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF (default CNC) |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| body | body | [EQPlaceTradeRequestDao](27-schemas.md#eqplacetraderequestdao) | true | none |

> Example responses

> 200 Response

```json
//Order after slice 
{"resp":
 {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "failedShrs": "string",
    "ord": [
      {
        "lsz": "string",
        "oid": "string"
      }
    ]
  }
 }
}

//Order not sliced
{"resp":
 {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string",
  }
 }
 }
```

> 401 Response

```json
{
  "config": {},
  "error": {
    "actCd": "52",
    "errCd": "EGN0011",
    "errMsg": "Session Expired"
  },
  "msgID": "22eb607d-bf65-4a9f-9b59-7f60d0370857",
  "srvTm": 1623912675844
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PlaceTradeDao](27-schemas.md#placetradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Modify a Trade for a client

Modify orders allows a user to change certain aspects of the order once it is placed. Depending on the
execution state of the order (i.e. either completely open, partially open) there are various levels of
modification allowed. As a user you can edit the product type, order quantity, order validity and certain other
parameters. Please note that any modifications made to an order will be sent back to the risk system for
validation before being submitted and there are chances that an already placed order may get rejected in case of
a modification.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.ModifyTrade( tradingSymbol, exchange, action, duration, orderType, quantity, streamingSymbol, limitPrice, orderID, disclosedQuantity , triggerPrice ,productCode, currentQuantity );
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const ModifyTrade = apiConnect.ModifyTrade(Trading_Symbol,
		Exchange,
		Action,
		Duration,
		Order_Type,
		Quantity,
		Streaming_Symbol,
		Limit_Price,
		Order_ID,
		Disclosed_Quantity = "0",
		TriggerPrice = "0",
		ProductCode = "CNC",
    CurrentQuantity = "0").then(function(result) {

  }).catch((err) => {console.log("Error ModifyTrade",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect 
        
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
        
from constants.exchange import ExchangeEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum
from constants.duration import DurationEnum
from constants.action import ActionEnum
        
response = api_connect.ModifyTrade(Trading_Symbol="INE090A01021", Exchange=ExchangeEnum.NSE, Action=ActionEnum.BUY, Duration=DurationEnum.DAY, Order_Type=OrderTypeEnum.LIMIT, Quantity=1, CurrentQuantity=1, Streaming_Symbol="4963_NSE", Limit_Price="620.00", Order_ID=211101000000001, Disclosed_Quantity="0", TriggerPrice="0", ProductCode=ProductCodeENum.CNC)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String modifyTradeResp = connect.modifyTrade(Trading_Symbol, Exchange, Action, Duration, Order_Type, Quantity, Streaming_Symbol, Limit_Price, Order_ID, Disclosed_Quantity='0', TriggerPrice='0', ProductCode='CNC',CurrentQuantity);
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/modifytrade/v1/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`PUT /eq/trade/modifytrade/v1/{userID}`

> Body parameter

```json
 {
  "trdSym": "INE409B01013",
  "exc": "NSE",
  "action": "SELL",
  "dur": "DAY",
  "flQty": "0",
  "ordTyp": "LIMIT",
  "qty": "1",
  "curQty": "1",
  "dscQty": "0",
  "sym": "11909_NSE",
  "mktPro": "",
  "lmPrc": "200.0",
  "trgPrc": "",
  "prdCode": "CNC",
  "dtDays": "",
  "nstOID": "76578587"
    }
```

### Parameters

| Parameter | Description |
| --- | --- |
| Trading_Symbol | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| Exchange | Name of the exchange, BSE/NSE/CDS/MCX/NCDEX/NFO/BFO |
| Action | BUY/SELL |
| Duration | Order validity, DAY/IOC/EOS(for BSE) |
| Order_Type | Order type, LIMIT/MARKET/STOP_LIMIT/STOP_MARKET |
| Quantity | Quantity of the scrip to transact |
| Current Quantity | Current Quantity of the scrip to transact |
| Streaming_Symbol | exchangetoken to be obtained from Contract file downloaded |
| Limit_Price | Limit price of scrip |
| Order_ID | Parent order Id |
| Disclosed_Quantity | Quantity to be disclosed publicly while order placement (default 0) |
| TriggerPrice | Trigger Price applicable for SL/SL-M Orders (default 0) |
| ProductCode | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF (default CNC) |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | USER ID of the client |
| body | body | [EQModifyTradeRequestDao](27-schemas.md#eqmodifytraderequestdao) | false | none |

> Example responses

> 200 Response

```json
//Order after slice 
{"resp":
      {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "failedShrs": "string",
    "ord": [
      {
        "lsz": "string",
        "oid": "string"
      }
    ]
  }
 }
}

//Order not sliced
{"resp":
  {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string",
  }
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [ModifyTradeDao](27-schemas.md#modifytradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Cancel trade for a client.

An order can be cancelled, as long as on order is open or pending in the system

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.CancelTrade(orderId, exchange, orderType, productCode, Trading_Symbol, Action, streaming_symbol, CurrentQuantity);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const CancelTrade = apiConnect.CancelTrade(OrderId, Exchange, Order_Type, ProductCode, Trading_Symbol, Action, streaming_symbol, CurrentQuantity).then(function(result) {

  }).catch((err) => {console.log("Error CancelTrade",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
        
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum

response = api_connect.CancelTrade(Order_ID=211101000000001, Exchange=ExchangeEnum.NSE, Order_Type=OrderTypeEnum.LIMIT, Product_Code=ProductCodeENum.CNC, Trading_Symbol= "INE793A01012", Action= ActionEnum.BUY, streaming_symbol= "7053_NSE", CurrentQuantity= "1")
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String cancelTradeResp = connect.cancelTrade(OrderId, Exchange, Order_Type, Product_Code, Trading_Symbol, Action, streaming_symbol, CurrentQuantity);
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/canceltrade/v1/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`PUT /eq/trade/canceltrade/v1/{userID}`

> Body parameter

```json
{
  "nstOID": "12433232313",
  "exc": "NSE",
  "prdCode": "CNC",
  "ordTyp": "LIMIT",
  "action": "BUY",
  "trdSym": "INE793A01012",
  "sym": "7053_NSE",
  "curQty": "1"
}
```

### Parameters

| Parameter | Description |
| --- | --- |
| OrderId | Parent order Id |
| Exchange | Name of the exchange, BSE/NSE/CDS/MCX/NCDEX/NFO/BFO |
| Order_Type | Order type, LIMIT/MARKET/STOP_LIMIT/STOP_MARKET |
| ProductCode | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF (default CNC) |
| Action | BUY/SELL |
| Streaming_Symbol | exchangetoken to be obtained from Contract file downloaded |
| Trading_Symbol | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| Current Quantity | Current Quantity of the scrip to transact |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | USER ID of the client |
| body | body | [EQCancelTradeReq](27-schemas.md#eqcanceltradereq) | true | nstOID, exc, ordTyp, prdCode are mandatory |

> Example responses

> 200 Response

```json
{"resp":
        {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string"
  }
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [CancelTradeDao](27-schemas.md#canceltradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Get AMO Flag

Before placing AMO order, you can check if AMO orders can be placed at this time

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.GetAMOFlag();
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const GetAMOStatus = apiConnect.GetAMOStatus().then(function(result) {

  }).catch((err) => {console.log("Error GetAMOStatus",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect
api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')
api_connect.GetAMOStatus()
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.GetAMOStatus();
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/amostatus/{exchange}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /eq/trade/amostatus/{exchange}`

> Example responses

> 200 Response

```json
{"resp":
        {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "sts": "string"
  }
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [CommAMODao](27-schemas.md#commamodao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Position squareOff API For Equity and Commodity

Square off is a term used in intraday and simply means closing all open positions by the end of the trading
day.

OrderList : List of orders to be Squared Off.

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.PositionSquareOff(orderlist);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
	   var orderlist = new Array(new Order( {values} ));
	   orderlist.push(order);
       const PositionSquareOff = apiConnect.PositionSquareOff(orderlist).then(function(result) {

  }).catch((err) => {console.log("Error PositionSquareOff",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum
from constants.action import ActionEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum
from constants.duration import DurationEnum
from APIConnect.order import Order

orderlist = [
 Order(
  Exchange=ExchangeEnum.NSE,
  TradingSymbol="TATCHE",
  StreamingSymbol="3405_NSE",
  Action=ActionEnum.BUY,
  ProductCode=ProductCodeENum.CNC,
  Duration=DurationEnum.DAY,
  Price="307",
  TriggerPrice="307",
  OrderType=OrderTypeEnum.LIMIT,          	
  Quantity=2,
  DisclosedQuantity="1",
  GTDDate="NA",
  Remark="UserRemarksTesting"             	
  ),             	      	
  Order(
  Exchange=ExchangeEnum.NSE,
  TradingSymbol="TATCHE",
  StreamingSymbol="TATACHEM",
  Action=ActionEnum.BUY,
  ProductCode=ProductCodeENum.CNC,
  OrderType=OrderTypeEnum.LIMIT,
  Duration=DurationEnum.DAY,
  Price="306",
  TriggerPrice="306",
  Quantity=2,
  DisclosedQuantity="1",
  GTDDate="NA",
  Remark="UserRemarksTesting"
  )          	
]

response = api_connect.PositionSquareOff(orderlist=orderlist)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.positionSquareOff(OrderList);
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/position/sqroff/v1/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`POST /eq/trade/position/sqroff/v1/{userID}`

> Body parameter

```json
{
  "sqrLst": [
    {
      "trdSym": "INE438A01022",
      "exc": "NSE",
      "action": "SELL",
      "dur": "DAY",
      "flQty": "0",
      "ordTyp": "MARKET",
      "qty": "1",
      "dscQty": "0",
      "sym": "163_NSE",
      "mktPro": "",
      "lmPrc": "0",
      "trgPrc": "0",
      "prdCode": "CO",
      "dtDays": null,
      "posSqr": "",
      "minQty": "0",
      "ordSrc": "TX3",
      "vnCode": "",
      "rmk": ""
    }
  ]
}
```

### Parameters

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| body | body | [PositionSquareOffRequestDto](27-schemas.md#positionsquareoffrequestdto) | true | Position square off Request Fields |

> Example responses

> 200 Response

```json
{"resp":
 {"resp":
    {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "posSqrOffs": [
      {
        "errMsg": "string",
        "errCd": "string",
        "actCd": "string",
        "msg": "string",
        "oid": "string"
      }
    ]
   }
  }
  }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [PositionSquareOffResponseDto](27-schemas.md#positionsquareoffresponsedto) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| 403 | Forbidden | Invalid AppID Key | [ErrorResponseDao](27-schemas.md#errorresponsedao) |
| 500 | Internal Server Error | Something went wrong, please try again later | [ErrorResponseDao](27-schemas.md#errorresponsedao) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Convert a position for a clients

Convert Position : converts your holding position from MIS to CNC and vice-versa

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.ConvertPosition(orderId, fill Id, newProductCode, oldProductCode, exchange, orderType);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const ConvertPosition = apiConnect.ConvertPosition(Order_Id, Fill Id, New_Product_Code, Old_Product_Code, Exchange, orderType).then(function(result) {

  }).catch((err) => {console.log("Error ConvertPosition",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum

response = api_connect.ConvertPosition(Order_ID=211101000000001, Fill_Id= "30414", New_Product_Code= ProductCodeENum.MIS, Old_Product_Code= ProductCodeENum.CNC, Exchange= ExchangeEnum.NSE, Order_Type= OrderTypeEnum.MARKET)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.convertPosition(Order_Id, Fill Id, New_Product_Code, Old_Product_Code, Exchange, orderType);
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/convertposition/v1/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`PUT /eq/trade/convertposition/v1/{userID}`

> Body parameter

```json
{
  "prdCodeCh": "CNC",
  "prdCode": "NRML",
  "nstOID": "210621000000351",
  "flID": "30414",
  "exc": "BSE",
  "ordTyp": "LIMIT"
}
```

### Parameters

| Parameter | Description |
| --- | --- |
| OrderId | Parent order Id |
| Fill_Id | Fill Id of the trade obtained from TradeBook API |
| New_Product_Code | New Product code of the trade |
| Old_Product_Code | Existing Product Code of the trade |
| Exchange | Name of the exchange, BSE/NSE/CDS/MCX/NCDEX/NFO/BFO etc |
| orderType | Order type, LIMIT/MARKET/STOP_LIMIT/STOP_MARKET |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | USER ID of the client |
| body | body | [EQConvertPositionReq](27-schemas.md#eqconvertpositionreq) | false | none |

> Example responses

> 200 Response

```json
{"resp":        
        {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string"
    }
  } 
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [EqConvertPositionDao](27-schemas.md#eqconvertpositiondao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Place AMO trade for a client in equity and commodity

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.PlaceAMOTrade(tradingSymbol, exchange, action, duration, orderType, quantity, streamingSymbol, limitPrice, disclosedQuantity , triggerPrice , productCode);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const PlaceAMOTrade = apiConnect.PlaceAMOTrade(Trading_Symbol,
		Exchange,
		Action,
		Duration,
		Order_Type,
		Quantity,
		Streaming_Symbol,
		Limit_Price,
		Disclosed_Quantity = "0",
		TriggerPrice = "0",
		ProductCode = "CNC").then(function(result) {

  }).catch((err) => {console.log("Error PlaceAMOTrade",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum
from constants.action import ActionEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum
from constants.duration import DurationEnum

response = api_connect.PlaceAMOTrade(Trading_Symbol= "INE793A01012", Exchange= ExchangeEnum.NSE, Action= ActionEnum.BUY, Duration= DurationEnum.DAY, Order_Type= OrderTypeEnum.MARKET, Quantity=1, Streaming_Symbol= "7053_NSE", Limit_Price= "1220.50", Disclosed_Quantity="0", TriggerPrice="0", ProductCode=ProductCodeENum.CNC)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.placeAMOTrade(Trading_Symbol, Exchange, Action, Duration, Order_Type, Quantity, Streaming_Symbol, Limit_Price, Disclosed_Quantity='0', TriggerPrice='0', ProductCode='CNC');
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/amo/placetrade/v1/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`POST /eq/trade/amo/placetrade/v1/{userID}`

> Body parameter

```json
{
  "vnCode": "118",
  "dur": "DAY",
  "sym": "8696_NSE",
  "trgPrc": "",
  "action": "BUY",
  "ordTyp": "LIMIT",
  "prdCode": "CNC",
  "posSqr": "NO",
  "amoFlg": "YES",
  "minQty": "",
  "lmPrc": "167.70",
  "mktPro": "",
  "trdSym": "INE366I01010",
  "dtDays": "",
  "dscQty": "",
  "exc": "NSE",
  "rmk": "AMO remarks",
  "qty": "1"
}
```

### Parameters

| Parameter | Description |
| --- | --- |
| Trading_Symbol | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| Exchange | Name of the exchange, BSE/NSE/CDS/MCX/NCDEX/NFO/BFO |
| Action | BUY/SELL |
| Duration | Order validity, DAY/IOC/EOS(for BSE) |
| Order_Type | Order type, LIMIT/MARKET/STOP_LIMIT/STOP_MARKET |
| Quantity | Quantity of the scrip to transact |
| Streaming_Symbol | exchangetoken to be obtained from Contract file downloaded |
| Limit_Price | Limit price of scrip |
| Disclosed_Quantity | Quantity to be disclosed publicly while order placement (default 0) |
| TriggerPrice | Trigger Price applicable for SL/SL-M Orders (default 0) |
| ProductCode | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF (default CNC) |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | UserId of the client |
| body | body | [EQPlaceTradeRequestDao](27-schemas.md#eqplacetraderequestdao) | false | none |

> Example responses

> 200 Response

```json
//Order after slice 
{"resp":
      {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "failedShrs": "string",
    "ord": [
      {
        "lsz": "string",
        "oid": "string"
      }
    ]
  }
 }
}

//Order not sliced
{"resp":
 {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string",
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

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Modify amo Trade for a client

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.ModifyAMOTrade(tradingSymbol,exchange, action, duration, orderType, quantity, streamingSymbol,limitPrice,orderID, disclosedQuantity,triggerPrice, productCode, currentQuantity);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const ModifyAMOTrade = apiConnect.ModifyAMOTrade(Trading_Symbol,
		Exchange,
		Action,
		Duration,
		Order_Type,
		Quantity,
		Streaming_Symbol,
		Limit_Price,
		Order_ID,
		Disclosed_Quantity = "0",
		TriggerPrice = "0",
		ProductCode = "CNC",
    CurrentQuantity = "0").then(function(result) {

  }).catch((err) => {console.log("Error ModifyAMOTrade",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum
from constants.action import ActionEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum
from constants.duration import DurationEnum

response = api_connect.ModifyAMOTrade(Trading_Symbol="INE094I01018", Exchange=ExchangeEnum.NSE, Action=ActionEnum.SELL, Duration=DurationEnum.DAY, Order_Type=OrderTypeEnum.MARKET, Quantity=1, CurrentQuantity =1, Streaming_Symbol="15124_NSE", Limit_Price="0", Order_ID=211101000000001, Disclosed_Quantity="0", TriggerPrice="0", ProductCode=ProductCodeENum.CNC)
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.modifyAMOTrade(Trading_Symbol, Exchange, Action, Duration, Order_Type, Quantity, Streaming_Symbol, Limit_Price, Order_ID, Disclosed_Quantity='0', TriggerPrice='0', ProductCode='CNC',CurrentQuantity='0');
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/amo/modifytrade/v1/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`PUT /eq/trade/amo/modifytrade/v1/{userID}`

> Body parameter

```json
{
  "dur": "DAY",
  "sym": "15124_NSE",
  "trgPrc": "",
  "nstOID": "210622000285636",
  "action": "SELL",
  "ordTyp": "MARKET",
  "prdCode": "CNC",
  "lmPrc": "",
  "mktPro": "",
  "trdSym": "INE094I01018",
  "dtDays": "",
  "dscQty": "0",
  "exc": "NSE",
  "flQty": "0",
  "qty": "3",
  "curQty": "3",
  "nstReqID": "2"
}
```

### Parameters

| Parameter | Description |
| --- | --- |
| Trading_Symbol | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| Exchange | Name of the exchange, BSE/NSE/CDS/MCX/NCDEX/NFO/BFO |
| Action | BUY/SELL |
| Duration | Order validity, DAY/IOC/EOS(for BSE) |
| Order_Type | Order type, LIMIT/MARKET/STOP_LIMIT/STOP_MARKET |
| Quantity | Quantity of the scrip to transact |
| Current Quantity | Current Quantity of the scrip to transact |
| Streaming_Symbol | exchangetoken to be obtained from Contract file downloaded |
| Limit_Price | Limit price of scrip |
| Order_ID | Parent order Id |
| Disclosed_Quantity | Quantity to be disclosed publicly while order placement (default 0) |
| TriggerPrice | Trigger Price applicable for SL/SL-M Orders (default 0) |
| ProductCode | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF (default CNC) |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | USER ID of the client |
| body | body | [EQModifyTradeRequestDao](27-schemas.md#eqmodifytraderequestdao) | false | none |

> Example responses

> 200 Response

```json
//Order after slice 
{"resp":
      {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "failedShrs": "string",
    "ord": [
      {
        "lsz": "string",
        "oid": "string"
      }
    ]
  }
 } 
}

//Order not sliced
{"resp":
 {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string",
  }
 } 
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [ModifyTradeDao](27-schemas.md#modifytradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization

## Cancel AMO trade for a client in equity and commodity

> Code samples

```csharp
APIConnect apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract, iniFilePath);
apiConnect.CancelAMOTrade(orderId, exchange, orderType, productCode, Trading_Symbol, Action, streaming_symbol, CurrentQuantity);
```

```javascript
const apiConnect = new APIConnect(apiKey, api_secret_password, reqId, downloadContract)
apiConnect.Init().then(()=>{
       const CancelAMOTrade = apiConnect.CancelAMOTrade(OrderId, Exchange, Order_Type, Product_Code, Trading_Symbol, Action, streaming_symbol, CurrentQuantity).then(function(result) {

  }).catch((err) => {console.log("Error CancelAMOTrade",err);throw err});
}).catch(console.log("Init Failed"))
```

```python
from APIConnect.APIConnect import APIConnect

api_connect = APIConnect(apiKey, api_secret_password, reqId, downloadContract=True, 'settings.ini')

from constants.exchange import ExchangeEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum

response = api_connect.CancelAMOTrade(Order_ID=211101000000001, Exchange=ExchangeEnum.NSE, Order_Type=OrderTypeEnum.LIMIT, ProductCode=ProductCodeENum.CNC, Trading_Symbol= "INE793A01012", Action= ActionEnum.BUY, streaming_symbol= "7053_NSE", CurrentQuantity= "1")
```

```java
APIConnect connect = new APIConnect(apiKey, api_secret_password, reqID, downloadContract, iniFilePath);
String response = connect.cancelAMOTrade(OrderId, Exchange, Order_Type, Product_Code, Trading_Symbol, Action, streaming_symbol, CurrentQuantity);
```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "https://emtuat.edelweiss.in/edelmw-eq-uat/eq/trade/amo/canceltrade/{userID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`PUT /eq/trade/amo/canceltrade/{userID}`

> Body parameter

```json
{
  "nstOID": "210623000000155",
  "exc": "NSE",
  "prdCode": "CNC",
  "ordTyp": "MARKET",
  "action": "BUY",
  "trdSym": "INE793A01012",
  "sym": "7053_NSE",
  "curQty": "1"
}
```

### Parameters

| Parameter | Description |
| --- | --- |
| OrderId | Parent order Id |
| Exchange | Name of the exchange, BSE/NSE/CDS/MCX/NCDEX/NFO/BFO |
| Order_Type | Order type, LIMIT/MARKET/STOP_LIMIT/STOP_MARKET |
| ProductCode | Margin product to use for the order (margins are blocked based on this), CNC/MIS/NRML/MTF (default CNC) |
| Action | BUY/SELL |
| Streaming_Symbol | exchangetoken to be obtained from Contract file downloaded |
| Trading_Symbol | Trading Symbol of the Scrip, to be obtained from Contract file downloaded |
| Current Quantity | Current Quantity of the scrip to transact |

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| userID | path | string | true | USER ID of the client |
| body | body | [EQCancelTradeRequestDao](27-schemas.md#eqcanceltraderequestdao) | false | none |

> Example responses

> 200 Response

```json
{"resp":
 {
  "appID": "663051cfbac7d699a1c59b96048b50e7",
  "config": {},
  "msgID": "aeae1389-9784-4b23-9774-f0a63f3074d6",
  "srvTm": "string",
  "data": {
    "type": "string",
    "msg": "string",
    "oid": "string"
  }
 }
}
```

### Responses

| Status | Meaning | Description | Schema |
| --- | --- | --- | --- |
| 200 | OK | successful operation | [CancelTradeDao](27-schemas.md#canceltradedao) |
| 401 | Unauthorized | Session Expired | [SessionExpired](27-schemas.md#sessionexpired) |
| default | Default | unexpected error | [CommonErrorResponse](27-schemas.md#commonerrorresponse) |

To perform this operation, you must be authenticated by means of one of the following methods:
Authorization
