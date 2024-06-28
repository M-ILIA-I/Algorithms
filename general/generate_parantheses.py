class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Problem description:

        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        """
        def gp(left, right, s):
            if left < n:
                gp(left+1, right, s+"(")
            if right < left:
                gp(left, right+1, s+")")
            if len(s) == 2 * n:
                res.append(s)    
        
        res = []
        gp(0,0, "")
        return res