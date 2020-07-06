"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * m for _ in range(n)]

        for c in range(m):
            paths[n - 1][c] = 1

        for r in range(n):
            paths[r][m - 1] = 1

        for r in range(n - 2, -1, -1):
            for c in range(m - 2, -1, -1):
                paths[r][c] = paths[r][c + 1] + paths[r + 1][c]

        return paths[0][0]