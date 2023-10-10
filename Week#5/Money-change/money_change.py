def PDCahge(money, coins):
    minNumCoins = []
    minNumCoins.append(0)
    for m in range(1, money + 1):
        minNumCoins.append(money)
        for coin in coins:
            if coin <= m:
                minNumCoins[m] = min(minNumCoins[m], minNumCoins[m - coin] + 1)
    return minNumCoins[money]


money = int(input())
coins = 1, 3, 4
print(PDCahge(money, coins))
