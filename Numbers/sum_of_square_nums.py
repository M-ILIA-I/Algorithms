class Solution:
    def is_sqrt(self, n):
        low = 0
        high = n+1

        while True:
            if low == high-1:
                return False
            mid = (low+high) // 2
            if n < mid**2:
                high = mid
            elif n > mid**2:
                low = mid
            else:
                return True
        

    def judgeSquareSum(self, c: int) -> bool:
        """
        Problem description:

        Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
        """
        if c == 0:
            return True        

        print(self.is_sqrt(26))
        for i in range( int(c**1/2)+1):
            tmp = c - i**2
            if tmp < i ** 2:
                return False

            if self.is_sqrt(tmp):
                return True

        return False
            