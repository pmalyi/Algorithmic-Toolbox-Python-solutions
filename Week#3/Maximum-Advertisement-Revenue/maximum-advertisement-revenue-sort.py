def dotProduct(n, prices, clicks):
    prices.sort()
    clicks.sort()
    dot_product = 0
    for i in range(n):
        prod = prices[i] * clicks[i]
        dot_product += prod
    return dot_product


n = int(input())
prices = list(map(int, input().split()[:n]))
clicks = list(map(int, input().split()[:n]))
print(dotProduct(n, prices, clicks))
