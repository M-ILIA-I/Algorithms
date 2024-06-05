def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Problem description:

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """
    n = len(nums)
    i = 0
    while i < n-1:
        tmp = target - nums[i]
        if tmp in nums[i+1:]:
            j = i + 1
            while j < n:
                if nums[j] == tmp:
                    return [i, j]
                j+=1
        i += 1

if __name__ == '__main__':
    print(twoSum([3,2,3], 6))


# КРАСОТА С HASHMAP
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i