class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Problem description:

        You are given an integer array bloomDay, an integer m and an integer k.

        You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

        The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

        Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
        """
        if m*k > len(bloomDay):
            return -1
        def is_valid(num_day):
            cur_bloom = 0
            cur_bouqets = 0
            for i in bloomDay:
                if num_day < i:
                    cur_bloom = 0
                else:
                    cur_bloom += 1
                    if cur_bloom == k:
                        cur_bouqets += 1
                        cur_bloom = 0
                        if cur_bouqets == m:
                            return True
            return False

        timers = sorted(set(bloomDay))

        left, right = 0, len(timers)-1
        optimal_day = 0

        while left <= right:
            mid = left + (right - left) // 2
            if is_valid(timers[mid]):
                optimal_day = mid
                right = mid-1
            else:
                left = mid + 1
        return timers[optimal_day]