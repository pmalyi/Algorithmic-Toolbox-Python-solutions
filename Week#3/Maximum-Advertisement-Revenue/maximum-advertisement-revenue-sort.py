def maxProduct(n, prices, clicks):
    prices.sort()
    clicks.sort()
    max_product = 0
    for i in range(n):
        prod = prices[i] * clicks[i]
        max_product += prod
    return max_product


n = int(input())
prices = list(map(int, input().split()[:n]))
clicks = list(map(int, input().split()[:n]))
print(maxProduct(n, prices, clicks))
