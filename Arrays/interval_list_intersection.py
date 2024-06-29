class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Problrm description:

        You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

        Return the intersection of these two interval lists.

        A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

        The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
        """
        i, j = 0, 0
        n, m = len(firstList), len(secondList)
        res = []
        start, end, = 0, 0
        prev_max = -1
        
        while i < n and j < m:
            start_i = max(firstList[i][0], secondList[j][0])
            end_i = min(firstList[i][1], secondList[j][1])
            if min(firstList[i][0], secondList[j][0]) == prev_max:
                res.append([prev_max, prev_max])
            
            if start_i <= end_i:
                res.append([start_i, end_i])

            prev_max = max(firstList[i][1], secondList[j][1])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
            
        return res