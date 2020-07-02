"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border
of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not
connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        R = len(board)
        if R <= 2:
            return
        C = len(board[0])
        if C <= 2:
            return
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O' and (i == 0 or i == R - 1 or j == 0 or j == C - 1):
                    self.dfs(i, j)

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == 'A':
                    self.board[i][j] = 'O'

    def dfs(self, i, j):
        if i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board[0]) and self.board[i][j] == 'O':
            self.board[i][j] = 'A'
            self.dfs(i + 1, j)
            self.dfs(i, j + 1)
            self.dfs(i - 1, j)
            self.dfs(i, j - 1)
