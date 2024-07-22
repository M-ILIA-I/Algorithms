class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Problem description

        You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

        Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

        Return a list of integers representing the size of these parts.
        """
        last_char = {}
        res = []
        start, end = 0, 0
        
        for i, char in enumerate(s):
            if i in last_char:
                last_char[char] = i
            else:
                last_char[char] = i
        
        for i,c in enumerate(s):
            end = max(end,last_char[c])
            if i==end:
                res.append(end-start+1)
                start=end+1
        return res