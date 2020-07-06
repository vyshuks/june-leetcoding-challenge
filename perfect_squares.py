"""
Given a positive integer n, find the least number of
perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        isSquare = lambda n: int(n ** 0.5) ** 2 == n

        if isSquare(n):
            return 1
        dp = [0] * (n + 1)

        for x in range(1, n + 1):
            min_val = x
            sq = 1
            y = 1

            while sq <= x:
                min_val = min(min_val, 1 + dp[x - sq])
                y += 1
                sq = y * y

            dp[x] = min_val

        return dp[n]