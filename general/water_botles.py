class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Problem description:

        There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

        The operation of drinking a full water bottle turns it into an empty bottle.

        Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
        """
        res = numBottles
        empty = numBottles
        remaining = 0
        while empty >= numExchange:
            res += empty // numExchange
            remaining = empty % numExchange            
            empty = remaining + (empty // numExchange)
            

        return res
    

if __name__ == "__main__":
    c = Solution()
    numBottles = 9
    numExchange = 3
    a = c.numWaterBottles(numBottles, numExchange)
    print(a)