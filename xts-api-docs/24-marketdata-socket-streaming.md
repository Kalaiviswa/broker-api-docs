# Market Data API: Socket Streaming

## Introduction

To receive streaming Market Data events, you must use the Socket.IO library. For more information, visit: [https://socket.io/.](https://socket.io/)

### Real-Time Streaming Flow

Once the connection is established, real-time streaming data can be obtained by listening to the socket on the relevant market data ports. The streaming data will be received on these ports, and upon receiving the data, you are free to process it as required.  
  
Below are the steps to follow to correctly implement the real-time streaming flow:

1. Establish the socket connection
2. Listen to real-time streaming events

## Establishment of Socket Connection

You can connect to the server by sending the userID, token, source, and broadcastMode as query parameters. The token is available only after a successful RESTful login request, as described in the RESTful section of the documentation.

```python
import socketio

# Base URL of the ApiMarketdata API server
url = "https://developers.symphonyfintech.in"

# Required credentials
userID = ""
token = ""

broadcastMode = "Full" # "Partial"
publishFormat = "JSON"
socketio_path = "/apibinarymarketdata/socketio"
logger = False # True

# Create Socket.IO client
sio = socketio.Client()

connectionString = f"{url}?token={token}&userID={userID}&publishFormat={publishFormat}&broadcastMode={broadcastMode}"

@sio.on("connect")
def connect():
    print("Connection Established")

@sio.on("disconnect")
def disconnect():
    print("Disconnected")

@sio.on("joined")
def joined(data):
    print("Socket Joined", data)

@sio.on("error")
def error(data):
    print("Error", data)
```

#### Listening to Real-Time Streaming

Once the socket connection is successfully established, you can listen to real-time streaming data by subscribing to the attached market data ports. The complete market data will be received as a string.

## Connect

**The user needs to connect to the server via a socket (i.e., WebSocket). It is important to set the path parameter value as /socket.io during the connection. The token will only be available after a successful login, so make sure you log in first before connecting to the server via socket.  
  
Here, the URL is the REST API address used to connect to the interactive server (e.g., www.test.example.com). Once connected to the server, you can listen to the following events: SocketEvents.An example of a connect event is given below**

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

## Binary Marketdata Event

### BinaryData

Binary data event

```python
@sio.on("xts-binary-packet")
def on_binary_full(data):
    print("Binary data Full:", data)

```

### Note

- If the packet is compressed, decompress it using **zlib,** and then deserialize the final packet.
- If the packet is not compressed, you can directly deserialize the packet.
- The **isGzipCompressed** flag is present in the parent header of the received packet. The final packet must be iterated accordingly.
- Further deserialization should be performed based on the **message code.**

### Touchline event (1501)

| Field Name | Data Type | Description |
| --- | --- | --- |
| Header |  |  |
| isGzipCompressed | int8 | Indicates whether the packet payload is gzip compressed (1 = compressed, 0 = not compressed). |
| messageCode | uint16 | Header-level message code. |
| exchangeSegment | int16 | Exchange segment identifier. |
| exchangeInstrumentID | int32 | Unique identifier of the instrument within the exchange. |
| bookType | int16 | Order book type. |
| marketType | int16 | Market type identifier. |
| uncompressedPacketSize | uint16 | Size of the packet after decompression. |
| compressedPacketSize | uint16 | Size of the compressed packet. |
| **If isGzipCompressed is 1 then it is a compressed packet, need to deserialize using zlib, if isGzipCompressed is 0 then it is non compressed packet.** |  |  |
| messageCode | uint16 | Actual message code inside the decompressed payload. |
| **Touchline event (1501)** |  |  |
| messageVersion | uint16 | Version of the message format. |
| applicationType | uint16 | Application type identifier. |
| tokenID | uint64 | Unique token identifier for the instrument. |
| sequenceNumber<br>(if messageVersion >= 4) | uint64 | Incremental sequence number used for ordering messages. |
| SkipBytes (if messageVersion >= 4) | int32 | Number of bytes to skip for forward compatibility. |
| exchangeSegment | int16 | Exchange segment identifier. |
| exchangeInstrumentId | int32 | Unique instrument identifier within the exchange. |
| exchangeTimestamp | uint64 | Timestamp generated by the exchange for this update. |
| **Marketdepth Row (Bid & Ask)** |  |  |
| size (Bid) | long | Bid quantity available at the best price level. |
| rowprice (Bid) | double | Best bid price. |
| totalOrders (Bid) | uint32 | Total number of buy orders at the best bid. |
| backmarketmakerflag (Bid) | int16 | Indicates market maker presence on the bid side. |
| size (Ask) | long | Ask quantity available at the best price level. |
| rowprice (Ask) | double | Best ask price. |
| totalOrders (Ask) | uint32 | Total number of sell orders at the best ask. |
| backmarketmakerflag (Ask) | int16 | Indicates market maker presence on the ask side. |
|  |  |  |
| LastUpdateTime | uint64 | Timestamp of the latest market data update. |
| LastTradedPrice | double | Price at which the last trade occurred. |
| LastTradedQuantity | long | Quantity traded in the last transaction. |
| TotalBuyQuantity | long | Total buy quantity available in the order book. |
| TotalSellQuantity | long | Total sell quantity available in the order book. |
| TotalTradedQuantity | long | Total quantity traded for the trading session. |
| AverageTradedPrice | double | Weighted average traded price. |
| LastTradedTime | int64 | Timestamp of the last trade. |
| percentChange | double | Percentage change compared to the previous close. |
| Open | double | Opening price of the trading session. |
| High | double | Highest traded price of the session. |
| Low | double | Lowest traded price of the session. |
| Close | double | Closing price of the previous trading session. |
| TotalValueTraded | double | Total traded value for the session. |
| bbtotalbuy | int16 | Total buy quantity from buyback orders. |
| bbtotalsell | int16 | Total sell quantity from buyback orders. |
| Booktype | int16 | Order book type. |
| MarketType | int16 | Market type identifier. |

### Marketdepth Event (1502)

| Field Name | Data Type | Description |
| --- | --- | --- |
| Header |  |  |
| isGzipCompressed | int8 | Indicates whether the packet payload is gzip compressed (1 = compressed, 0 = not compressed). |
| messageCode | uint16 | Header-level message code. |
| exchangeSegment | int16 | Exchange segment identifier. |
| exchangeInstrumentID | int32 | Unique identifier of the instrument within the exchange. |
| bookType | int16 | Order book type. |
| marketType | int16 | Market type identifier. |
| uncompressedPacketSize | uint16 | Size of the packet after decompression. |
| compressedPacketSize | uint16 | Size of the compressed packet. |
| **If isGzipCompressed is 1 then it is a compressed packet, need to deserialize using zlib, if isGzipCompressed is 0 then it is non compressed packet.** |  |  |
| messageCode | uint16 | Actual message code inside the decompressed payload. |
| **Marketdepth event (1502)** |  |  |
| messageVersion | uint16 | Version of the message structure. |
| applicationType | uint16 | Identifies the application type generating the message. |
| tokenID | uint64 | Unique token identifier for the instrument. |
| sequenceNumber<br>(if messageVersion >= 4) | uint64 | Sequential number used to maintain message ordering. |
| SkipBytes (if messageVersion >= 4) | int32 | Reserved bytes to skip for forward compatibility. |
| exchangeSegment | int16 | Exchange segment identifier. |
| exchangeInstrumentId | int32 | Unique instrument identifier within the exchange. |
| exchangeTimestamp | uint64 | Timestamp generated by the exchange for this update. |
| bidCount | int32 | Total number of bid levels present in the message. |
|  |  |  |
| **Marketdepth Row (Bid)** |  |  |
| size (Bid) | long | Bid quantity available at the current price level. |
| rowprice (Bid) | double | Bid price at this level. |
| totalOrders (Bid) | uint32 | Total number of buy orders at this bid level. |
| backmarketmakerflag (Bid) | int16 | Indicates market maker participation on the bid side. |
|  |  |  |
| askCount | int32 | Total number of ask levels present in the message. |
|  |  |  |
| **Marketdepth Row (Ask)** |  |  |
| size (Ask) | long | Ask quantity available at the current price level. |
| rowprice (Ask) | double | Ask price at this level. |
| totalOrders (Ask) | uint32 | Total number of sell orders at this ask level. |
| backmarketmakerflag (Ask) | int16 | Indicates market maker participation on the ask side. |
|  |  |  |
| LastUpdateTime | uint64 | Timestamp of the latest market data update. |
| LastTradedPrice | double | Price at which the most recent trade occurred. |
| LastTradedQuantity | long | Quantity traded in the last transaction. |
| TotalBuyQuantity | long | Total buy quantity available in the order book. |
| TotalSellQuantity | long | Total sell quantity available in the order book. |
| TotalTradedQuantity | long | Total quantity traded during the trading session. |
| AverageTradedPrice | double | Weighted average price of all executed trades. |
| LastTradedTime | int64 | Timestamp of the last executed trade. |
| percentChange | double | Percentage change compared to the previous close price. |
| Open | double | Opening price of the trading session. |
| High | double | Highest traded price during the session. |
| Low | double | Lowest traded price during the session. |
| Close | double | Closing price of the previous trading session. |
| TotalValueTraded | double | Total traded value for the trading session. |
| bbtotalbuy | int16 | Total buy quantity from buyback orders. |
| bbtotalsell | int16 | Total sell quantity from buyback orders. |
| Booktype | int16 | Order book type identifier. |
| MarketType | int16 | Market type identifier. |

### OpenInterest Event (1510)

| Field Name | Data Type | Description |
| --- | --- | --- |
| Header |  |  |
| isGzipCompressed | int8 | Indicates whether the packet payload is gzip compressed (1 = compressed, 0 = not compressed). |
| messageCode | uint16 | Header-level message code. |
| exchangeSegment | int16 | Exchange segment identifier. |
| exchangeInstrumentID | int32 | Unique identifier of the instrument within the exchange. |
| bookType | int16 | Order book type. |
| marketType | int16 | Market type identifier. |
| uncompressedPacketSize | uint16 | Size of the packet after decompression. |
| compressedPacketSize | uint16 | Size of the compressed packet. |
| **If isGzipCompressed is 1 then it is a compressed packet, need to deserialize using zlib, if isGzipCompressed is 0 then it is non compressed packet.** |  |  |
| messageCode | uint16 | Actual message code inside the decompressed payload. |
| **OpenInterest event (1510)** |  |  |
| messageVersion | uint16 | Version of the message format. |
| applicationType | uint16 | Identifies the application type generating the message. |
| tokenID | uint64 | Unique token identifier for the instrument. |
| sequenceNumber<br>(if messageVersion >= 4) | uint64 | Sequential number used to maintain message ordering. |
| SkipBytes (if messageVersion >= 4) | int32 | Reserved bytes to skip for forward compatibility. |
| exchangeSegment | int16 | Exchange segment identifier. |
| exchangeInstrumentId | int32 | Unique instrument identifier within the exchange. |
| exchangeTimestamp | uint64 | Timestamp generated by the exchange. |
| MarketType | int16 | Market type identifier. |
| openInterest | long | Total open interest for the instrument. |
| underlyingExchangeSegment | int16 | Exchange segment of the underlying instrument. |
| underlyingInstrumentID | uint64 | Unique identifier of the underlying instrument. |
| isStringExits | int8 | Indicates whether underlying index name string is present (1 = yes, 0 = no). |
| stringLength (if isStringExits = 1) | int8 | Length of the underlying index name string. |
| UnderlyingIndexName<br>(if isStringExits = 1) | string | Name of the underlying index. |
| underlyingTotalOpenInterest | uint64 | Total open interest of the underlying instrument. |

## Candle Data Event

Candle Data Event message for JSON Full Packet

```python
@sio.on("1505-json-full")
def on_1505_json_full(data):
    print("CandleData data Full:", data)

```

Candle Data Event message for JSON Full Packet

```json
{
  "MessageCode": 1505,
  "MessageVersion": 1,
  "ApplicationType": 142,
  "TokenID": 0,
  "ExchangeSegment": 1,
  "ExchangeInstrumentID": 2885,
  "BarTime": 1737731759,
  "BarVolume": 13161312,
  "High": 1246.05,
  "Low": 1245.5,
  "Open": 1246,
  "Close": 1245.95,
  "OpenInterest": 0,
  "SumOfQtyInToPrice": 0
}

```

Candle Data Event message for JSON Partial Packet

```python
@sio.on("1505-json-partial")
def on_1505_json_partial(data):
    print("CandleData Partial:", data)

```

Response to 1505-json-partial

```
t:1_2885,o:1246,h:1246.05,l:1245.5,c:1245.95,bt:1737731759,bv:13161312,pv:0

```

| Symbol | Explanation |
| --- | --- |
| t | ExchangeSegment_InstrumentID (exchange segment enum with underscore along with instrumentID of the particular subscribed instrument) |
| o | Open |
| h | High |
| l | Low |
| c | Close |
| bt | Bar Time |
| bv | Bar Volume |
| pv | Sum of Quantity In Price |
