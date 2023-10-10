def PDCahge(money, coins):
    #minNumCoins = [money + 1] * (money + 1) можна проініціалізувати весь масив (масиви) дефолтними значеннями
    #minNumCoins[0] = 0
    #prev = [-1] * (money + 1)
    min_coin = min(coins)
    #TakeCoins = [min_coin] * (money + 1)
    minNumCoins = [0,] # ініціалізуємо тільки перші елементи масиву (масивів)
    TakeCoins = [-1,]
    prev = [-1,]
    for m in range(1, money + 1):
        minNumCoins.append(money + 1) # ініціалізуємо масиви поелементно, додаючи в кінець масиву дефолтні значення
        prev.append(0)
        TakeCoins.append(min_coin)
        for coin in coins:
            if coin <= m:
                if minNumCoins[m - coin] + 1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m - coin] + 1
                    prev[m] = m - coin
                    TakeCoins[m] = coin
    tracing = []
    current = money
    while current > 0:
        tracing.append(TakeCoins[current])
        current = prev[current]
    return minNumCoins[money], tracing


#money = int(input())
coins = 1, 3, 4
# coins = 1, 2, 3, 5, 10, 15, 20, 50 - радянські номінали монет
for money in range(1, 101):
    r1, r2 = PDCahge(money, coins)
    print(f'Cents - {money}')
    print(f'Minimum number coins - {r1}')
    print(f'List of coins needed to change {money} cents - {", ".join(map(str, r2))}')
