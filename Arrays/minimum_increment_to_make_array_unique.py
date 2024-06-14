class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """Problem description: 
        You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

        Return the minimum number of moves to make every value in nums unique.

        The test cases are generated so that the answer fits in a 32-bit integer.
        """
        if not nums:
            return 0

        nums.sort()
        res = 0
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if prev >= nums[i]:
                prev += 1
                res += prev - nums[i]
            else:
                prev = nums[i]
        
        return res