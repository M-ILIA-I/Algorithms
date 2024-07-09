from typing import Deque

class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         lst = [x for x in range(1,n+1)]
#         i = 0
#         cnt = 1
#         while n != 1:
#             if i >= n:
#                 i = 0
#             if cnt >= k:
#                 lst.pop(i)
#                 n-=1
#                 cnt = 1
#             else:
#                 i+=1
#                 cnt+=1
#         return lst.pop()
    

    def findTheWinner(self, n: int, k: int) -> int:
        deq = Deque([x for x in range(1,n+1)])
        
        while len(deq) > 1:
            for i in range(k):
                deq.append(deq.popleft())
            deq.pop()
        return deq.pop()

if __name__ == "__main__":
    c = Solution()
    print(c.findTheWinner(6,5))