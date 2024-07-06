class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums)
        n = len(nums)
        start = -1
        end = -1

        for i in range(n):
            if nums[i]!=temp[i] and start==-1:
                start = i
            if nums[n-i-1] != temp[n-i-1] and end ==-1:
                end = n-i-1

        return end-start+1 if start!=-1 else 0
