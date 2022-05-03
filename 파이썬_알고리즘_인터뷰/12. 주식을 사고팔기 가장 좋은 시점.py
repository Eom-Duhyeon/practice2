"""
한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
Input: prices = [7,1,5,3,6,4]
Output: 5
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for i in prices:
            if i < min_price:
                min_price = i
                continue
            max_profit = max(max_profit, i - min_price)

        return max_profit
