class Solution:
    def isHappy(self, n: int) -> bool:

        str_n = n
        hs = {}

        while True:
            num = 0
            for j in str(str_n):
                num += int(j)**2
            print(num)
            if num == 1:
                return True
            if num in hs:
                return False
            else:
                hs[num] = 1

            str_n = num

if __name__ == "__main__":
    c = Solution()

    print(c.isHappy(2))