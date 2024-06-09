class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Problem description:

        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and uses only constant extra space.
        """
        hs = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hs:
                return nums[i]
            else:
                hs[nums[i]] = 1


