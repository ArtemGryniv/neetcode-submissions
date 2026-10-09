class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        if len(prices) <= 1:
            return max_profit

        while right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)

            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1

        return max_profit