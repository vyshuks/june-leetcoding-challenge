"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        T = [0] * (n + 1)
        T[0] = 1
        T[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                T[i] += T[j] * T[i - j - 1]

        return T[n]
