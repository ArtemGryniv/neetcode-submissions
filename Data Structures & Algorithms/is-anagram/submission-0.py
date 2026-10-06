class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        counts_t = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        for char in t:
            if char in counts_t:
                counts_t[char] += 1
            else:
                counts_t[char] = 1

        return counts == counts_t