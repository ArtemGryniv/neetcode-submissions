class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def find_counts(word):
            counts = {}
            for letter in word:
                counts[letter] = counts.get(letter, 0) + 1

            return tuple(sorted(counts.items()))

        mp = {} # dict -> []
        for word in strs:
            counts = find_counts(word)
            if counts in mp:
                mp[counts].append(word)
            else:
                mp[counts] = [word]

        out = []
        for arr in mp.values():
            out.append(arr)

        return out
    
    
