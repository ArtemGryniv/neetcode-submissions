class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        right = 1
        max_len = 0

        if len(s) <= 1:
            return len(s)
        
        st.add(s[left])
        length = 1
        while right < len(s):
            if s[right] not in st:
                st.add(s[right])
                right += 1
                length += 1
                max_len = max(length, max_len)
            else:
                while s[right] in st:
                    st.remove(s[left])
                    left += 1
                    length -= 1
                

        return max_len


        