from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        max_x = float("-inf")
        min_x = float("inf")
        pts = set()

        for i in points:
            max_x = max(max_x, i[0])
            min_x = min(min_x, i[0])
            pts.add((i[0], i[1]))

        reflect_dist = abs(max_x) + abs(min_x)

        return all((reflect_dist-x, y) in pts for x,y in pts)


if __name__ == "__main__":
    c = Solution()
    points = [(1, 1), (3, 1), (7, 1), (9, 1)]

    print(c.isReflected(points=points))