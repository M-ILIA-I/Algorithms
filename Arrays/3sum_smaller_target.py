from typing import (
    List,
)

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        result = 0

        for i in range(n):
            l = i
            r = n-1

            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm > target:
                    r -= 1
                elif sm < target:
                    result+=1
                    l += 1
                r -= 1
                
        return result
    

if __name__ == "__main__":
    c = Solution()

    print(c.three_sum_smaller(nums = [-2,0,-1,3], target=2))