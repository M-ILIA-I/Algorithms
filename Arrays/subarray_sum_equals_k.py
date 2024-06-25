class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Problem description:
        
        iven an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

        A subarray is a contiguous non-empty sequence of elements within an array.
        """
        sub_sum = 0
        sub_sum_hm = {0:1}
        res = 0

        for num in nums:
            sub_sum += num
            if sub_sum-k in sub_sum_hm:
                res += sub_sum_hm[sub_sum-k]
            if sub_sum in sub_sum_hm:
                sub_sum_hm[sub_sum] += 1
            else:
                sub_sum_hm[sub_sum] = 1
        return res