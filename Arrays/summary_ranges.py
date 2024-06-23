class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Problem description:

        You are given a sorted unique integer array nums.

        A range [a,b] is the set of all integers from a to b (inclusive).

        Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

        Each range [a,b] in the list should be output as:

        "a->b" if a != b
        "a" if a == b
        """
        res = []
        first = 0
        second = 0
        i = 0
        n = len(nums)
        while i < n:
            first = i
            while i < n-1 and nums[i] == nums[i+1]-1:
                i+=1
            
            if first == i:
                res.append(f'{nums[first]}')
            else:
                res.append(f'{nums[first]}->{nums[i]}')
            i+=1

        return res