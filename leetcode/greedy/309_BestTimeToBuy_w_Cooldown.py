"""
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

Идеи:
1) Делаем бэктрекинг (множество решений - buy/sell/cooldown)
3) Делаем переменную для хранения состояния - можем ли мы купить или нет
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # State: buy or sell
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)