# for문 중첩시 n^2만큼 걸린다. 더 적은 복잡도로 해결 가능하다.

def max_profit(prices):
    n = len(prices)
    maxprofit = 0
    min_price = prices[0]

    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > maxprofit:
            maxprofit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return maxprofit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

print(max_profit(stock))