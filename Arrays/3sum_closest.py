class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Problrm description:

        Given an integer array nums of length n and an integer target,
         
        find three integers in nums such that the sum is closest to target.

        Return the sum of the three integers.

        You may assume that each input would have exactly one solution.
        """
        n=len(nums)
        nums.sort()
        diff=20001
        val=0
        for i in range(n):
            a=i+1
            b=n-1
            while(a<b):
                cc=nums[i]+nums[a]+nums[b]
                kk=abs(cc-target)
                if(kk<diff):
                    diff=kk
                    val=cc
                if(cc==target):
                    return target
                elif(cc<target):
                    a+=1
                else:
                    b-=1
            
        return val