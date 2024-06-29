class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Problem description:

        Given an array of intervals where intervals[i] = [starti, endi],
        merge all overlapping intervals, and return an array of the non-overlapping intervals
        that cover all the intervals in the input.
        """
        n = len(intervals)
        if n <= 1:
            return intervals
    
        res = []
        intervals.sort(key=lambda x: x[0])
    
        i = 0

        while i < n:
            start_i = intervals[i][0]
            end_i = intervals[i][1]
            while i < n and end_i >= intervals[i][0]:
                end_i = max(end_i, intervals[i][0], intervals[i][1])
                i+=1
            
            res.append([start_i, end_i])
            

        return res