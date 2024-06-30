class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Problem description:

        Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
        
        """
        hm, res, s_len, p_len = defaultdict(int), [], len(s), len(p)

        if p_len > s_len:
            return []

        for i in range(p_len):
            hm[p[i]] += 1

        for i in range(p_len-1):
            if s[i] in hm:
                hm[s[i]] -= 1

        for i in range(-1, s_len - p_len + 1):
            if i > - 1 and s[i] in hm:
                hm[s[i]] += 1
            
            if i+p_len < s_len and s[i+p_len] in hm:
                hm[s[i+p_len]] -= 1

            if all(v == 0 for v in hm.values()):
                res.append(i+1)
        
        return res