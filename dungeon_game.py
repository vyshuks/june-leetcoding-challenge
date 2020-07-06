"""
The demons had captured the princess (P) and imprisoned her
in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms
laid out in a 2D grid. Our valiant knight (K) was initially positioned in the
top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health
(negative integers) upon entering these rooms; other rooms are either
empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible,
the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health
so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must
be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

"""


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])

        sol = [[0] * cols for _ in range(rows)]
        sol[rows - 1][cols - 1] = 1 if dungeon[rows - 1][cols - 1] > 0 else (1 - dungeon[rows - 1][cols - 1])

        for i in range(rows - 2, -1, -1):
            sol[i][cols - 1] = max(sol[i + 1][cols - 1] - dungeon[i][cols - 1], 1)

        for j in range(cols - 2, -1, -1):
            sol[rows - 1][j] = max(sol[rows - 1][j + 1] - dungeon[rows - 1][j], 1)

        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                sol[i][j] = max(min(sol[i + 1][j], sol[i][j + 1]) - dungeon[i][j], 1)

        return sol[0][0]