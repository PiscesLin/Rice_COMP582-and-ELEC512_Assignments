# Hsuan-You Lin Module 13 Problem Set Question 2.
def cut_rod(prices, n):
    profit = [-1]*(n + 1)
    len = [-1]*(n + 1)
    profit[0] = 0
 
    for i in range(1, n + 1):
        q = -1
        for j in range(1, i + 1):
            temp = prices[j] + profit[i - j]
            if q < temp:
                q = temp
                len[i] = j
        profit[i] = q
 
    return profit, len
    
if __name__ == "__main__" :
    length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    prices = [None, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30];
    n = 4
    profit, len = cut_rod(prices, n)
    print('The maximum profit that can be obtained is $', profit[n])
    print('The rod needs to be cut into length(s) of ', end='')
    while n > 0:
        print(len[n], end=' ')
        n -= len[n]
        if n == 0: print("\n")
