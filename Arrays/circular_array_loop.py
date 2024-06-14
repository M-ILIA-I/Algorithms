class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        Problem description:

        You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

        If nums[i] is positive, move nums[i] steps forward, and
        If nums[i] is negative, move nums[i] steps backward.
        Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

        A cycle in the array consists of a sequence of indices seq of length k where:

        Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
        Every nums[seq[j]] is either all positive or all negative.
        k > 1
        Return true if there is a cycle in nums, or false otherwise.
        """
        slow = 0
        fast = 0
        n = len(nums)

        if n <= 2:
            return False 
        
        while True:
            slow = (slow + nums[slow]) % n
            fast = (fast + slow + nums[slow]) % n

            if (slow + nums[slow])%n == slow:
                return False

            if slow == fast:
                if nums[slow] + nums[(slow + nums[slow])%n] == 0:
                    return False    


        
        return True

        