def PDChange_no_extra_space(money, coins):
    # Основна таблиця динамічного програмування
    minNumCoins = [money + 1] * (money + 1)
    minNumCoins[0] = 0

    # 1. Заповнюємо таблицю як зазвичай
    for m in range(1, money + 1):
        for coin in coins:
            if coin <= m:
                if minNumCoins[m - coin] + 1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m - coin] + 1

    # 2. Відновлюємо шлях, аналізуючи значення в minNumCoins
    res_coins = []
    current_money = money

    while current_money > 0:
        for coin in coins:
            # Перевіряємо, чи ця монета могла бути частиною оптимального шляху
            if coin <= current_money and minNumCoins[current_money - coin] == minNumCoins[current_money] - 1:
                res_coins.append(coin)
                current_money -= coin
                break  # Знайшли монету, переходимо до наступного залишку

    return minNumCoins[money], res_coins



if __name__ == "__main__":
    # Введення даних
    money_input = int(input("Введіть суму: "))
    available_coins = tuple(map(int, input("Введіть номінали монет: ").split()))

    count, path = PDChange_no_extra_space(money_input, available_coins)
    print(f"Мінімальна кількість монет: {count}")
    print(f"Перелік монет: {path}")