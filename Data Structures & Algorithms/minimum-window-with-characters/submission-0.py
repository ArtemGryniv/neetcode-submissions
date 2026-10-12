class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1
            
        left = 0
        s_counts = {}
        required = len(t_counts)
        formed = 0
        min_length = float("inf")
        start = 0
    
        for right in range(len(s)):
            s_counts[s[right]] = s_counts.get(s[right], 0) + 1

            if s[right] in t_counts and s_counts[s[right]] == t_counts[s[right]]:
                formed += 1
            
            while formed == required:
                length = right - left + 1
                if length < min_length:
                    min_length = length
                    start = left

                s_counts[s[left]] -= 1
                if s[left] in t_counts and s_counts[s[left]] < t_counts[s[left]]:
                    formed -= 1


                left += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]
                


