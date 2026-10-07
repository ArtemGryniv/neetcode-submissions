class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in st:
                
                length = 0
                while num in st:
                    length += 1
                    num += 1

                if length > longest:
                    longest = length

        return longest
