class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = nums[i] * -1
            left = i + 1
            right = len(nums) - 1

            while left < right:
                
                total = nums[left] + nums[right ]

                if total == target:
                    out.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

        return out