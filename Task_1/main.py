"""
Домашнє завдання: касова система (решта монетами).

1. find_coins_greedy — жадібний алгоритм
2. find_min_coins— динамічне програмування
"""

import time

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount, coins):
    """Жадібний алгоритм: спочатку найбільші номінали."""
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount -= count * coin
    return result


def find_min_coins(amount, coins):
    """DP: мінімальна кількість монет для заданої суми."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    if dp[amount] == float("inf"):
        return {}

    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


def print_coins(title, result):
    print(title)
    if not result:
        print("  (порожньо)")
        return
    for coin, count in sorted(result.items(), reverse=True):
        print(f"  {coin} копійок: {count} шт.")


if __name__ == "__main__":
    amount = int(input("Введіть суму: "))

    greedy_result = find_coins_greedy(amount, coins)
    dp_result = find_min_coins(amount, coins)

    print_coins("Результат жадібного алгоритму:", greedy_result)
    print_coins("Результат динамічного програмування:", dp_result)

    answer = input("\nЗапустити порівняння швидкості для великої суми? (y/n): ").strip().lower()
    if answer == "y":
        big_amount = 100_000 

        start = time.perf_counter()
        greedy_big = find_coins_greedy(big_amount, coins)
        greedy_time = time.perf_counter() - start

        start = time.perf_counter()
        dp_big = find_min_coins(big_amount, coins)
        dp_time = time.perf_counter() - start

        print(f"\n--- Порівняння для суми {big_amount:,} ---")
        print(f"Greedy: {greedy_big} | монет: {sum(greedy_big.values())}")
        print(f"DP:     {dp_big} | монет: {sum(dp_big.values())}")
        print(f"Час Greedy: {greedy_time:.6f} с")
        print(f"Час DP:     {dp_time:.6f} с")
