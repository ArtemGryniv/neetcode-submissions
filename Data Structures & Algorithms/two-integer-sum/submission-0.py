class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in comps:
                return [comps[complement], i]
            else:
                comps[nums[i]] = i
        
