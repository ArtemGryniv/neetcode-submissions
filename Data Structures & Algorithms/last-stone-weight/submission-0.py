import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [stone * -1 for stone in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            x = heapq.heappop(nums) * -1
            y = heapq.heappop(nums) * -1

            diff = abs(x - y)
            if diff > 0:
                heapq.heappush(nums, diff * -1)

        if nums:
            return nums[0] * -1

        return 0