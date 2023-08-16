def maxProduct(n, prices, clicks):
    if n == 0:
        return 0
    max_prices = max(prices)
    max_clicks = max(clicks)
    product = max_prices * max_clicks
    prices.remove(max_prices)
    clicks.remove(max_clicks)
    n -= 1
    return product + maxProduct(n, prices, clicks)


n = int(input())
prices = list(map(int, input().split()[:n]))
clicks = list(map(int, input().split()[:n]))
print(maxProduct(n, prices, clicks))