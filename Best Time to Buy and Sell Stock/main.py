## Incomplete another solution needs to be added

prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
max_profit = 0

for i in range(len(prices)):
    curr = prices[i]
    if curr < min_price:
        min_price = prices[i]

    curr_profit = curr - min_price
    if max_profit < curr - min_price:
        max_profit = curr - min_price


print(max_profit)
