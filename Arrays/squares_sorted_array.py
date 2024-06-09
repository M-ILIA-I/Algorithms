class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Description problem:

        Given an integer array nums sorted in non-decreasing order,
        return an array of the squares of each number sorted in non-decreasing order.
        """
        n = len(nums)
        l = 0
        r = n - 1 

        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                nums.insert(r+1, nums[l]**2)
                nums.pop(l)
                r-=1
            else:
                nums[r] = nums[r]**2
                r-=1
        return nums

