# Socket Streaming

## Introduction

**order to get streaming interactive events, you need to use the socket.io library.  
For more information, you can visit: [https://socket.io/.](https://socket.io/)**

### Real-Time Streaming Flow

Once the connection is established, real-time streaming can be achieved by listening to the socket for relevant interactive events. You can receive the corresponding streaming data on these events.

Follow the steps below to enable real-time streaming of interactive events:

- **Establish the socket connection.**
- **Register interactive events on the socket connection.**
- **Listen for real-time interactive events to receive live updates.**

## Establishment of socket connection

```python
import socketio

url = "https://developers.symphonyfintech.in" 	 # base url
userID = "SYMP" 	#userID received from login api
token = "xxxxxx" 	 #Token generated from login api
apiType = "INTERACTIVE"
socketio_path = "/1interactive/socket.io"  	#note:- /1interactive is endpoint you have recieved from hostlookup load balance step
logger = False  # or "True"

sio = socketio.Client()

if __name__ == "__main__":
    try:
        connectionString = f"{url}?token={token}&userID={userID}&apiType={apiType}"
        sio.connect(url=connectionString, socketio_path=socketio_path, transports=["websocket"])
        sio.wait()

    except KeyboardInterrupt:
        print("Stopping client...")
        sio.disconnect()

    except Exception as e:
        print("Connection failed:", e)

```

**Note:**

XTS uses **Socket.io** protocol for the Interactive order related data.

Users must note that some programming languages does not support socket.io protocol directly, so they need to find compatible websocket libraries.

## Connect

This event triggers when socket connection is successfull.

```python
@sio.on("connect")
def connect():
  print("Connection Established")

```

## Joined

If a successful connection is established with the server, this event will be raised to indicate that the user has been connected.

```python
@sio.on("joined")
def on_joined(data):
    print("Socket Joined", data)

```

## Error

In case of any error with the server, this event will be raised along with the cause of the error. For example, if you send an incorrect token while connecting, the server will raise this event and disconnect your socket connection.

```python
@sio.on("error")
def on_error(data):
    print("Error", data)

```

## Disconnect

In case a socket disconnection occurs with the server, this event will be raised to indicate the disconnection.

```python
@sio.on("disconnect")
def on_disconnect():
    print("Disconnected")

```

## Orders

To listen for order state change events such as New, Filled, Partially Filled, etc., register for this event.

```python
@sio.on("ordert")
def on_order(data):
    print("Order Received:- ",data)

```

Below is order object you will receive when any of your order state changes

```json
{
  "LoginID": "SYMP1",
  "ClientID": "SYMP1",
  "AppOrderID": 648468730,
  "OrderReferenceID": "",
  "GeneratedBy": "WSAPI",
  "ExchangeOrderID": "1005239196374108",
  "OrderCategoryType": "NORMAL",
  "ExchangeSegment": "NSECM",
  "ExchangeInstrumentID": 16921,
  "OrderSide": "BUY",
  "OrderType": "LIMIT",
  "ProductType": "NRML",
  "TimeInForce": "DAY",
  "OrderPrice": 0,
  "OrderQuantity": 1,
  "OrderStatus": "New",
  "OrderAverageTradedPrice": 2615.8,
  "LeavesQuantity": 1,
  "CumulativeQuantity": 0,
  "OrderDisclosedQuantity": 0,
  "OrderGeneratedDateTime": "14-05-2021 11:17:29",
  "ExchangeTransactTime": "14-05-2021 11:17:30",
  "LastUpdateDateTime": "14-05-2021 11:17:29",
  "OrderExpiryDate": "01-01-1980 00:00:00",
  "CancelRejectReason": "",
  "OrderUniqueIdentifier": "454845",
  "OrderLegStatus": "SingleOrderLeg",
  "IsSpread": false,
  "BoLegDetails": "",
  "MessageCode": 4,
  "MessageVersion": 4,
  "ApplicationType": 0,
  "SequenceNumber": 0
}

```

## Trade

When any order gets executed (fully or partially filled), a new trade event will be generated. The server will raise trade events, and you can listen to these events by registering for them.

```python
@sio.on("trade")
def on_trade(data):
    print("Trade Recieved:- ", data)

```

Below is trade object you will receive when any trade happens on your account.

```json
{
  "LoginID": "YMS",
  "ClientID": "YMSCLI",
  "AppOrderID": 648468731,
  "OrderReferenceID": "",
  "GeneratedBy": "TWSAPI",
  "ExchangeOrderID": "1005239196374109",
  "OrderCategoryType": "NORMAL",
  "ExchangeSegment": "NSECM",
  "ExchangeInstrumentID": 16921,
  "OrderSide": "BUY",
  "OrderType": "Limit",
  "ProductType": "NRML",
  "TimeInForce": "DAY",
  "OrderPrice": 0,
  "OrderQuantity": 1,
  "OrderStatus": "Filled",
  "OrderAverageTradedPrice": 44.00,
  "LeavesQuantity": 0,
  "CumulativeQuantity": 1,
  "OrderDisclosedQuantity": 0,
  "OrderGeneratedDateTime": "14-05-2021 11:17:29",
  "ExchangeTransactTime": "14-05-2021 11:17:30",
  "LastUpdateDateTime": "14-05-2021 11:17:29",
  "OrderUniqueIdentifier": "454845",
  "OrderLegStatus": "SingleOrderLeg",
  "LastTradedPrice": 44,
  "LastTradedQuantity": 1,
  "LastExecutionTransactTime": "14-05-2021 11:17:29",
  "ExecutionID": "1320599196383056",
  "ExecutionReportIndex": 3,
  "IsSpread": false,
  "MessageCode": 9005,
  "MessageVersion": 4,
  "TokenID": 0,
  "ApplicationType": 0,
  "SequenceNumber": 0
}

```

## Position

If any position change occurs in your account, the server will raise this event to indicate the updated position. By registering for this event, you can track position changes.

```python
@sio.on("position")
def on_position(data):
    print("Position Recieved:- ", data)

```

Below is Position object that you will receive when any position change happens on your account.

```json
{
  "LoginID": "SYMP1",
  "AccountID": "SYMP1",
  "TradingSymbol": "ACC",
  "ExchangeSegment": "NSECM",
  "ExchangeInstrumentID": "22",
  "ProductType": "CNC",
  "Multiplier": 1,
  "Marketlot": 1,
  "BuyAveragePrice": 41.78,
  "SellAveragePrice": 41.63,
  "LongPosition": 5,
  "ShortPosition": 0,
  "NetPosition": 5,
  "BuyValue": 1671.00,
  "SellValue": 2498.00,
  "NetValue": 827.00,
  "UnrealizedMTM": 0,
  "RealizedMTM": 0,
  "MTM": 0,
  "BEP": 0,
  "SumOfTradedQuantityAndPriceBuy": 1671.00,
  "SumOfTradedQuantityAndPriceSell": 2498.00,
  "StatisticsLevel": "ParentLevel",
  "IsInterOpPosition": false,
  "childPositions": [{}],
  "MessageCode": 9002,
  "MessageVersion": 1,
  "TokenID": 0,
  "ApplicationType": 0,
  "SequenceNumber": 0
}

```

## Trade conversion

If any trade conversion occurs in your account, the server will raise this event to indicate the trade conversion status. By registering for this event, you can track the trade conversion status.

```python
@sio.on("tradeConversion")
def on_tradeconversion(data):
    print("TradeConversion Recieved:- ", data)

```

Below is Position object that you will receive when any position change happens on your account.

```json
{
  "LoginID": "SYMP1",
  "ClientID": "SYMP1",
  "Success": true,
  "ErrorMessage": "",
  "OriginalProduct": "MIS",
  "TargetProduct": "NRML",
  "OriginalQty": 10,
  "TargetQty": 10,
  "EntityType": "Client",
  "ExchangeSegment": "NSECM",
  "ExchangeInstrumentId": 0,
  "TargetEntityId": "SYMP1",
  "NetValue": -2587.5,
  "Status": "PositionConverted",
  "RejectionReason": "",
  "RejectedBy": "",
  "Price": -2587.5,
  "NOWTimeStamp": "2021-10-29T17:22:25.945707",
  "OrderSide": "Buy",
  "IsProOrder": false,
  "MessageCode": 9007,
  "MessageVersion": 4,
  "TokenID": 0,
  "ApplicationType": 0,
  "SequenceNumber": 0
}

```

## GTT Order

When any GTT order gets executed, a new trade event will be generated. The server will raise trade events & you can listen to this event by registering it.

```python
@sio.on("gttOrder")
def on_gttOrder(data):
    print("GTT Order Recieved:- ", data)

```

Below is the gttOrder object that you will receive when any gttOrder change happens on your account.

```json
{
  "LoginID": "SYMP",
  "ClientID": "SYMP1",
  "AppOrderID": "1311100040",
  "OrderReferenceID": "",
  "GeneratedBy": "Web",
  "ExchangeOrderID": "",
  "OrderCategoryType": "NORMAL",
  "ExchangeSegment": "NSECM",
  "ExchangeInstrumentID": 1333,
  "OrderSide": "BUY",
  "OrderType": "Limit",
  "ProductType": "CNC",
  "TimeInForce": "None",
  "OrderPrice": 1500,
  "TradingSymbol": "HDFCBANK",
  "OrderQuantity": 1,
  "OrderStopPrice": 1500,
  "OrderStatus": "New",
  "OrderAverageTradedPrice": "",
  "LeavesQuantity": 1,
  "CumulativeQuantity": 0,
  "OrderDisclosedQuantity": 0,
  "OrderGeneratedDateTime": "21-04-2026 16:51:27",
  "ExchangeTransactTime": "21-04-2026 16:51:27",
  "LastUpdateDateTime": "21-04-2026 16:51:27",
  "OrderExpiryDate": "21-04-2026 16:51:27",
  "CancelRejectReason": "",
  "OrderUniqueIdentifier": "",
  "OrderLegStatus": "SingleOrderLeg",
  "BoLegDetails": 0,
  "IsSpread": false,
  "SecurityType": "",
  "MessageCode": 9004,
  "MessageVersion": 4,
  "TokenID": 0,
  "ApplicationType": 0,
  "SequenceNumber": 0
}

```

## GTT Order Rejection

When any GTT order gets rejected, a new trade event will be generated. The server will raise trade events & you can listen to this event by registering it.

```python
@sio.on("gttOrderRejection")
def on_gttOrderRejection(data):
    print("GTT Order Rejection Recieved:- ", data)

```

Below is gttOrderRejection object that you will receive when any gttOrder rejection change happens on your account.

```json
{
  "Type": 783,
  "Data": "",
  "ErrorString": "Gateway:Freeze Quantity: Required Limit[1000000] Freeze Quantity Limit[6]",
  "ClientID": "SYMP",
  "UserID": "SYMP1"
}

```

## Market Status Update

marketStatusUpdate

```python
@sio.on("marketStatusUpdate")
def on_marketStatusUpdate(data):
    print("marketStatusUpdate Recieved:- ", data)

```

Below is marketStatusUpdate.

```json
{
  "timeStamp": "9-16-2025 1:30:00 PM",
  "exchangeSegment": "BSECM",
  "marketSession": "NormalStart"
}

```

## Exchange Adapter State

exchangeAdapterState

```python
@sio.on("exchangeAdapterState")
def on_exchangeAdapterState(data):
    print("exchangeAdapterState Recieved:- ", data)

```

Below is exchangeAdapterState.

```json

```

## Logout

When your session is logged out by the server, it will raise this event. By registering for this event, you can track your session state.

```python
@sio.on("logout")
def on_logout(data):
    print("Logout Recieved:- ", data)

```

**Note:** Here you will not get any data object from the server. This event itself notifies that the session has been closed by the server.
