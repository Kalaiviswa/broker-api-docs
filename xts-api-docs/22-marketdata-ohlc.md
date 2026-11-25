# Market Data API: OHLC

## Intraday Candle OHLC

The XTS Front-end API provides intraday archived OHLC (candlestick) data from the date of access for Equity segments of NSECM and BSECM. For FO segments, OHLC data is available only for currently traded contracts, and expired contracts are not supported.  
  
The response is delivered in candle format, including timestamp (epoch time since 1970), **Open, High, Low, Close, Volume, and Open Interest (OI)**. The minimum supported interval is **60 seconds (1 minute)**, with additional supported intervals for the GET OHLC request detailed in the table below.

### Compression Value Table

| Expected Timeframe | Compression |
| --- | --- |
| 1 minute | 60 |
| 2 minutes | 120 |
| 3 minutes | 180 |
| 4 minutes | 240 |
| 5 minutes | 300 |
| 7 minutes | 420 |
| 10 minutes | 600 |
| 15 minutes | 900 |
| 30 minutes | 1800 |
| 1 hour | 3600 |
| 2 hours | 7200 |
| 3 hours | 10800 |
| 4 hours | 14400 |
| 1 day | D |
| 1 week | W |
| 1 month | M |

### URL

```http
https://developers.symphonyfintech.in/apibinarymarketdata/instruments/ohlc?exchangeSegment=1&exchangeInstrumentID=2885&startTime=Jan 27 2025 090000&endTime=Jan 28 2025 153000&compressionValue=D
```

### Request Body Parameters

| Parameter Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| **exchangeSegment** | [ExchangeSegment](17-marketdata-enums.md#1-exchangesegments) | Y | Exchange segment. |
| **exchangeInstrumentID** | ExchangeInstrumentID (Integer, 10) | Y | Exchange Scrip code or Symbol Token is unique identifier. |
| **startTime** | StartTime (Long, 13) | Y | Date and time in MMM DD YYYY HHMMSS format. Default value is Jan 27 2025 090000 |
| **endTime** | EndTime (Long, 13) | Y | Date and time in MMM DD YYYY HHMMSS format. Default value is Jan 28 2025 153000 |
| **compressionValue** | CompressionValue (Integer, 5) | Y | String value representing time interval. Default value is D. Allowed values are In1Minute (60), In2Minute (120), In3Minute (180), In5Minute (300), In10Minute (600), In15Minute (900), In30Minute (1800), In60Minute (3600) |

### Response Body JSON

```json
[
  {
    "type": "success",
    "code": "s-ohlc-0001",
    "description": "Data found",
    "result": {
      "exchangeSegment": "NSECM",
      "exchangeInstrumentID": "22",
      "dataReponse": "1737331200|1316|1316|1300.25|1305.45|14040244|0|"
    }
  }
]
```
