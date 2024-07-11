class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        """
        Problem description:
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)

        of the characters without disturbing the relative positions of the remaining characters.
        
        (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        """
        lst = list(s)
        n = 0
        for i in t:
            if n < len(lst) and i == lst[n]:
                n+=1
        return True if n==len(lst) else False