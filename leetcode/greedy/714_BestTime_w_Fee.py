"""
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.

"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        profit = 0
        eff_buy = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - eff_buy - fee)
            eff_buy = min(eff_buy, prices[i] - profit)
        return profit

# [1, 3, 2, 8, 4, 9]