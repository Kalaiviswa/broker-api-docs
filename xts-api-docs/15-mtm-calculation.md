# MTM Calculation

MTM represents the realized and unrealized profit or loss calculated using the user’s current position and the instrument’s Last Traded Price (LTP). MTM values are not provided in Interactive API responses; users must compute MTM on their end using current position that can be fetched by GET Position api or Position data recieved on Interactive websocket, LastTradedPrice for particular instrument can be fetched using marketdata apis & websocket. **referring** the sample logic provided below.

```python
openBuyQty = int(position["OpenBuyQuantity"])
openSellQty = int(position["OpenSellQuantity"])

# Realized MTM
def safe_div(numerator, denominator):
    return float(numerator) / float(denominator) if denominator else 0.0

if openBuyQty == 0 or openSellQty == 0:
    realizedMTM = 0.0
else:
    totalSquaredOffQuantity = min(openBuyQty, openSellQty)

    sellWeightedAvgPrice = safe_div(position["SumOfTradedQuantityAndPriceSell"], openSellQty)
    buyWeightedAvgPrice = safe_div(position["SumOfTradedQuantityAndPriceBuy"], openBuyQty)

    realizedMTM = (
        totalSquaredOffQuantity
        * (sellWeightedAvgPrice - buyWeightedAvgPrice)
        * (float(position["Multiplier"]) * PriceNumerator / PriceDenominator)
    )

# Unrealized MTM
if int(position["Quantity"]) > 0:
    lastPrice = lastPrice if lastPrice and lastPrice != 0 else closePrice
    squareOfPrice = lastPrice
    if squareOfPrice == 0.0:
        unRealizedMTM = 0.0
    else:
        buyWeightedAvgPrice = float(position["SumOfTradedQuantityAndPriceBuy"]) / float(position["OpenBuyQuantity"])
        unRealizedMTM = abs(int(position["Quantity"])) * (squareOfPrice - buyWeightedAvgPrice) * (float(position["Multiplier"]) * PriceNumerator / PriceDenominator)
else:
    lastPrice = lastPrice if lastPrice and lastPrice != 0 else closePrice
    squareOfPrice = lastPrice
    if squareOfPrice == 0.0:
        unRealizedMTM = 0.0
    else:
        sellWeightedAvgPrice = float(position["SumOfTradedQuantityAndPriceSell"]) / float(position["OpenSellQuantity"])
        if not sellWeightedAvgPrice or sellWeightedAvgPrice != sellWeightedAvgPrice:
            sellWeightedAvgPrice = 0.0

    unRealizedMTM = ( abs(int(position["Quantity"])) * (sellWeightedAvgPrice - squareOfPrice) * (float(position["Multiplier"]) * PriceNumerator / PriceDenominator) )

totalMTM = realizedMTM + unRealizedMTM

```
