"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""
class Solution(object):
    directions = [(-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (-1, 1), (1, -1)]

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        mine = [[0] * len(board[0]) for _ in range(len(board))] 
        for row in range(len(board)):
            for column in range(len(board[0])):
                neighbors = self.neighborCount(board, row, column)
                if board[row][column] == 1:
                    if neighbors < 2 or neighbors > 3:
                        mine[row][column] = 0
                    else:
                        mine[row][column] = 1
                if board[row][column] == 0 and neighbors == 3:
                    mine[row][column] = 1
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                board[row][column] = mine[row][column]

    def neighborCount(self, board, row, column):
        count = 0
        for dx, dy in self.directions:
            nx = dx + row
            ny = dy + column
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:
                count += 1
        return count
        
        
if __name__ == "__main__":
    solution = Solution()
    
    board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution.gameOfLife(board1)
    expected1 = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    print("Test 1:", "PASS" if board1 == expected1 else "FAIL")
    
    # board2 = [[1,1],[1,0]]
    # solution.gameOfLife(board2)
    # expected2 = [[1,1],[1,1]]
    # print("Test 2:", "PASS" if board2 == expected2 else "FAIL")