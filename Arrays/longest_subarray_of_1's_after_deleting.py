class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Problem description:

        Given a binary array nums, you should delete one element from it.

        Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
        """
        n = len(nums)
        if n <= 1:
            return 0

        l, res, zeros = 0, 0, 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r-l)
        return res