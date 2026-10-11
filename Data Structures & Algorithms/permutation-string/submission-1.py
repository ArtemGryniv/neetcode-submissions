class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts_s1 = {}
        for char in s1:
            counts_s1[char] = counts_s1.get(char, 0) + 1
        
        left = 0
        right = len(s1) - 1
        counts_s2 = {}
        for char in s2[:right + 1]:
            counts_s2[char] = counts_s2.get(char, 0) + 1

        while right < len(s2):
            if counts_s1 == counts_s2:
                return True

            if s2[left] not in counts_s2 or counts_s2[s2[left]] <= 1:
                counts_s2.pop(s2[left])
            else:
                counts_s2[s2[left]] -= 1

            left += 1
            right += 1

            if right < len(s2):
                counts_s2[s2[right]] = counts_s2.get(s2[right], 0) + 1
            
        
        return False