class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = {}
        for char in s1:
            counts[char] = counts.get(char, 0) + 1
        
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            counts_window = counts.copy()
            for i in range(left, right + 1):
                if s2[i] in counts_window:
                    counts_window[s2[i]] -= 1

            total = 0
            for val in counts_window.values():
                if val != 0:
                    total = val
            
            if total == 0:
                return True
                
            left += 1
            right += 1
        
        return False