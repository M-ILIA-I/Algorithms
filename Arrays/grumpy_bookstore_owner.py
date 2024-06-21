from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        res = customers[0] if grumpy[0] == 0 else 0
        max_res = 0
        sum_arr = [0]*(len(customers)+1)
        sum_arr[1] = customers[0] if grumpy[0] == 1 else sum_arr[1]
        
        for i in range(1, len(sum_arr)):
            if grumpy[i-1] == 1:
                sum_arr[i] = (sum_arr[i-1]+customers[i-1])
                
            else:
                res += customers[i-1]
                sum_arr[i] = sum_arr[i-1] + sum_arr[i]

        for i in range(len(sum_arr)-minutes):
            max_res=max(max_res, sum_arr[i+minutes] - sum_arr[i])

        return res + max_res
    

if __name__ == "__main__":
    c = Solution()

    print(c.maxSatisfied([8,8], [1,0], 2))
