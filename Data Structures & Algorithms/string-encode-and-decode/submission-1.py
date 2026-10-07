class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            l = len(string)
            s += f'{l}#{string}'
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
                
            lst.append(s[i + 1: int(length) + i + 1])
            i += int(length) + 1

        return lst