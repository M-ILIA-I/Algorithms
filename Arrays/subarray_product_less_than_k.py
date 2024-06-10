class Solution:

    def subarry_product_less_than_k(self, nums: list[int], k: int):
        """
        Problem description:

        Given an array of integers nums and an integer k,
        
        return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
        """

        if k <= 1:
            return 0
        
        product, left, res = 1, 0, 0

        for right, num in enumerate(nums):
            product*=num

            while product >= k:
                product /= nums[left]
                left += 1

            res += right - left + 1
        
        return res
    