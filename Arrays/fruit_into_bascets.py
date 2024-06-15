class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Problem description:

        You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

        You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

        You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
        Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
        Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
        Given the integer array fruits, return the maximum number of fruits you can pick
        """
        n = len(fruits)
        if n <= 2:
            return n

        fst_bascet = fruits[0]
        snd_bascet = -1
        res = 1
        tmp_res = 1
        
        for i in range(1,n):
            if fruits[i] == fst_bascet or fruits[i] == snd_bascet:
                tmp_res += 1
            else:
                if snd_bascet == -1:
                    snd_bascet = fruits[i]
                    tmp_res += 1
                    continue
                res = max(res, tmp_res)
                tmp_res = 1
                fst_bascet = fruits[i-1]
                j = i-1
                while fruits[j] == fst_bascet and j >= 0:
                    tmp_res += 1
                    j -= 1
                snd_bascet = fruits[i]

        return max(res, tmp_res)


if __name__ == "__main__":
    c = Solution()

    fruits = [0,1,6,6,4,4,6]
    print(c.totalFruit(fruits=fruits))