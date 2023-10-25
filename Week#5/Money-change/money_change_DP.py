def PDCahge(money, coins):
    # minNumCoins = []
    # minNumCoins.append(0)
    minNumCoins = [money + 1] * (money + 1)
    minNumCoins[0] = 0
    for m in range(1, money + 1):
        # minNumCoins.append(money + 1)
        for coin in coins:
            if coin <= m:
                # minNumCoins[m] = min(minNumCoins[m], minNumCoins[m - coin] + 1)
                if minNumCoins[m - coin] + 1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m - coin] + 1
    return minNumCoins[money]


money = int(input())
coins = 1, 3, 4
print(PDCahge(money, coins))
