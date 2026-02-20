def PDChange_with_path(money, coins):
    # minNumCoins[m] зберігає мін. кількість монет для суми m
    minNumCoins = [money + 1] * (money + 1)
    # coinUsed[m] зберігає останню монету, використану для суми m
    coinUsed = [0] * (money + 1)

    minNumCoins[0] = 0

    # 1. Заповнюємо таблицю (Динамічне програмування)
    for m in range(1, money + 1):
        for coin in coins:
            if coin <= m:
                # Якщо використання цієї монети дає меншу кількість, ніж ми вже маємо
                if minNumCoins[m - coin] + 1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m - coin] + 1
                    # Запам'ятовуємо, яку саме монету використали
                    coinUsed[m] = coin

    # 2. Відстежуємо шлях (Реконструкція списку монет)
    res_coins = []
    current_money = money

    while current_money > 0:
        # Дістаємо монету, яку ми записали для поточної суми
        last_coin = coinUsed[current_money]
        res_coins.append(last_coin)
        # Зменшуємо залишок суми
        current_money -= last_coin

    return minNumCoins[money], res_coins


if __name__ == "__main__":
    # Введення даних
    money_input = int(input("Введіть суму: "))
    available_coins = tuple(map(int, input("Введіть номінали монет: ").split()))

    count, path = PDChange_with_path(money_input, available_coins)
    print(f"Мінімальна кількість монет: {count}")
    print(f"Перелік монет: {path}")
