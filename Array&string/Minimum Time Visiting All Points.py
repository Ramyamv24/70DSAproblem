from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0

        for i in range(1, len(points)):
            res += max(
                abs(points[i][0] - points[i - 1][0]),
                abs(points[i][1] - points[i - 1][1])
            )

        return res


# Main part
if __name__ == "__main__":
    points = [[1, 1], [3, 4], [-1, 0]]

    obj = Solution()
    result = obj.minTimeToVisitAllPoints(points)

    print(result)