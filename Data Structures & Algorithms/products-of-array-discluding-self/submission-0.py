class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []
        left_product = 1
        for i in range(len(nums)):
            out.append(left_product)
            left_product *= nums[i]

        right_product = 1
        i = len(nums) - 1
        while i >= 0:
            out[i] *= right_product
            right_product *= nums[i]
            i -= 1

        return out
