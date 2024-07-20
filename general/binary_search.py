class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        
        while left < right:
            mid = (right+left) // 2
            print(left, right)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1

        return -1
    

if __name__ == "__main__":
    c = Solution()
    target = 2
    nums = [-1,0,3,5,9,12]
    print(c.search(nums=nums, target=target))