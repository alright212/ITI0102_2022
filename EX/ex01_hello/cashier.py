"""Cha-ching."""
cents = int(input("Enter a sum: "))
coins = [50, 20, 10, 5, 1]
result = []

for coin in coins:
    while cents >= coin:
        cents -= coin
        result.append(coin)

print("Amount of coins needed:", len(result))
