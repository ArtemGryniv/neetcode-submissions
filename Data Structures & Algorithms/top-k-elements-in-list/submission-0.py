class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        arr = [ [] for _ in range(len(nums))]
        for key, value in counts.items():
            arr[value - 1].append(key)

        i = len(arr) - 1
        out = []
        while k > 0:
            if len(arr[i]) <= k:
                out += arr[i]
            else:
                out += arr[i][:k]

            k -= len(arr[i])
            i -= 1
        
        return out
            
