T = dict()


def recursCahge(money, coins):
    if money not in T:
        if money == 0:
            T[money] = 0
        else:
            minNumCoins = money + 1
            for coin in coins:
                if coin <= money:
                    numCoins = recursCahge(money - coin, coins)
                    if numCoins + 1 < minNumCoins:
                        minNumCoins = numCoins + 1
            T[money] = minNumCoins
    return T[money]


money = int(input())
coins = 1, 3, 4
print(recursCahge(money, coins))
