class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        max_length = 0
        length = 0
        left = 0 

        for right in range(len(s)):
            if s[right] not in st:
                st.add(s[right])
                length += 1
                max_length = max(max_length, length)
            else:
                while s[right] in st:
                    st.remove(s[left])
                    length -= 1
                    left += 1

                st.add(s[right])
                length += 1
                max_length = max(max_length, length)


        return max_length



        