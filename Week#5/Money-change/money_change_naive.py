def recursCahge(money, coins):
    if money == 0:
        return 0
    minNumCoins = money + 1
    for coin in coins:
        if coin <= money:
            numCoins = recursCahge(money - coin, coins)
            if numCoins + 1 < minNumCoins:
                minNumCoins = numCoins + 1
    return minNumCoins


money = int(input())
coins = 1, 3, 4
print(recursCahge(money, coins))