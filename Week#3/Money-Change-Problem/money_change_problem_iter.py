def largestCoin(money, denominations):
    maxCoin = 0
    for i in range(0, len(denominations)):
        if maxCoin < denominations[i] <= money:
            maxCoin = denominations[i]
    return maxCoin


def change(money, denominations):
    numCoints = 0
    while money > 0:
        maxCoin = largestCoin(money,denominations)
        money -= maxCoin
        numCoints += 1
        print(maxCoin, end=' ')
    return numCoints


denominations = [10, 5, 1]
money = int(input())
numCoints = change(money, denominations)
print()
print(numCoints)
