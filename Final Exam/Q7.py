# Hsuan-You Lin Final Exam Question 7
import numpy as np

# weight capacity of the cart
W = 20

def shopping_cart(items):
    dp = [0 for _ in range(W+1)]
    for i in range(1, W+1):
        for(prices, weight) in items:
            if weight <= i:
                dp[i] = max(dp[i], dp[i - weight] + prices)

    return dp[i]
    
if __name__ == "__main__" :
    # list of items in the store, each item is a tuple with the price and weight
    items = [(160, 7), (90, 3), (15, 2)]
    ans = shopping_cart(items)
    print("The Max profit = $", ans)