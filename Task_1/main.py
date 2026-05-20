coins = [50, 25, 10, 5, 2, 1]

#Функція жадібного алгоритму
def find_coins_greedy(sum: int, coins: list) -> dict:
    count_coins = {}
    for coin in coins:
        count = sum // coin
        if count > 0:
            count_coins[coin] = count
        sum -= count * coin
    return count_coins

if __name__ == "__main__":
    sum = int(input("Введіть суму: "))
    result = find_coins_greedy(sum, coins)
    print("Результат жадібного алгоритму:")
    for coin, count in result.items():
        print(f"{coin} копійок: {count} шт.")