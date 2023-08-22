import time
import argparse

#Naive Soluttion
def max_profit(prices):
    days = len(prices)
    profits = []
    max_selling_price = prices[0]
    for index, price in enumerate(prices):
        if price != max_selling_price:
            profit = max_selling_price - price
        else:
            max_selling_price = max(prices[index+1:days], default=price)
            profit = max_selling_price - price

        if profit >= 0:
            profits.append(profit)
    max_profit = max(profits)
    print(max_profit)

#Optimized Solution
def max_profit_optimized(prices):
    max_profit = 0
    min_price = prices[0]
    for i in prices:
        min_price = i if i < min_price else min_price
        max_profit = i - min_price if i - min_price > max_profit else max_profit

    return max_profit


test = [7,1,5,3,6,4]
test1 = [3,2,6,5,0,3]

if __name__ == "__main__":
    max_profit_optimized(test1)
