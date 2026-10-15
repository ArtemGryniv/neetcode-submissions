class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
    
        while left < right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += (pile + rate - 1) // rate

            if hours <= h:
                right = rate
            else:
                left = rate + 1

        return left




