# MY SOLUTION 
class Solution:
    """
    Descrition problem:

    You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

    There is at least one empty seat, and at least one person sitting.

    Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

    Return that maximum distance to the closest person.
    """
    def maxDistToClosest(self, seats: list[int]) -> int:
        distance = 1
        result = 1

        n = len(seats)
        i = 0

        while i != n-1:
            if seats[i] == 0:
                while  i != n-1 and seats[i] != 1:
                    i += 1
                    distance += 1 
                if i - distance == -1:
                    if result < distance and seats[i] == 1:
                        result = distance-1
                if i == n-1 and seats[i] == 0:
                    if result < distance:
                        result = distance
                if result <= distance // 2:
                    result = distance // 2
            else:
                distance = 1
                i += 1
                

        return result 