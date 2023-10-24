def largestCoin(money,denominations):
    maxCoin = 0
    for i in range(0, len(denominations)):
        if maxCoin < denominations[i] <= money:
            maxCoin = denominations[i]
    return maxCoin


def change(money, denominations):
    if money == 0:
        return 0
    maxCoin = largestCoin(money, denominations)
    print(maxCoin, end=' ')
    return 1 + change(money - maxCoin, denominations)

denominations = [10, 5, 1]
money = int(input())
numCoints = change(money, denominations)
print()
print(numCoints)