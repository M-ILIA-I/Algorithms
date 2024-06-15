class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Problem description:

        Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

        You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

        Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

        Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

        The answer is guaranteed to fit in a 32-bit signed integer.
        """
        n = len(capital)
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        max_heap = []
        
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i+=1

            if not max_heap:
                break

            w -= heapq.heappop(max_heap)

        return w