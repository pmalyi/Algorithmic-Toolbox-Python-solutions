def dotProduct(n, prices, clicks):
    dot_product = 0
    for i in range(n):
        max_prices = max(prices)
        max_clicks = max(clicks)
        product = max_prices * max_clicks
        prices.remove(max_prices)
        clicks.remove(max_clicks)
        dot_product += product
    return dot_product


n = int(input())
prices = list(map(int, input().split()[:n]))
clicks = list(map(int, input().split()[:n]))
print(dotProduct(n, prices, clicks))