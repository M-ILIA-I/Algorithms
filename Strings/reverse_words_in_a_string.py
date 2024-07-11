class Solution:
    def reverseWords(self, s: str) -> str:

        """
        Problem description:

        Given a string s, reverse the order of characters in each word within
        
        a sentence while still preserving whitespace and initial word order.
        """
        lst = s.split()

        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
            
        res = " ".join(lst)
        return res