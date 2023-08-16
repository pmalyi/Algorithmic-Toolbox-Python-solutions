def maxIndex(someList):
    max_item = someList[0]
    max_index = 0
    for i in range(len(someList)):
        if someList[i] > max_item:
            max_item = someList[i]
            max_index = i
    return max_index


def dotProduct(n, prices, clicks):
    if n == 0:
        return 0
    max_index_prices = maxIndex(prices)
    max_index_clicks = maxIndex(clicks)
    product = prices[max_index_prices] * clicks[max_index_clicks]
    prices[max_index_prices] = 0
    clicks[max_index_clicks] = 0
    n -= 1
    return product + dotProduct(n, prices, clicks)


n = int(input())
prices = list(map(int, input().split()[:n]))
clicks = list(map(int, input().split()[:n]))
print(dotProduct(n, prices, clicks))
