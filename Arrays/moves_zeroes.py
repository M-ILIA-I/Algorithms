class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Problem description:

        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.
        """
        n = len(nums)
        cnt_zero, i = 0, 0

        while i < n:
            if nums[i] == 0:
                while i < n and nums[i] == 0:
                    cnt_zero += 1
                    i+=1
                j = i
                while j < n and i-j < cnt_zero and nums[j] != 0:
                    nums[j-cnt_zero], nums[j] = nums[j], nums[j-cnt_zero]
                    j+=1
                i=j
            else:
                i+=1

        