class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        l_max = height[0]
        r_max = height[-1]

        while left < right:
            if height[left] < height[right]:
                l_max = max(l_max, height[left])
                total += l_max - height[left]
                left += 1
            else:
                r_max = max(r_max, height[right])
                total += r_max - height[right]
                right -= 1

        return total
            