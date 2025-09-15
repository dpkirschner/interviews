"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]
"""
from collections import deque
class Solution(object):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # Mark all border-connected 'O's as safe by changing them to '*'
        # Check top and bottom borders
        for col in range(cols):
            if board[0][col] == 'O':
                self.markSafe(board, 0, col)
            if board[rows-1][col] == 'O':
                self.markSafe(board, rows-1, col)

        # Check left and right borders
        for row in range(rows):
            if board[row][0] == 'O':
                self.markSafe(board, row, 0)
            if board[row][cols-1] == 'O':
                self.markSafe(board, row, cols-1)

        # Flip all remaining 'O's to 'X' and restore safe cells back to 'O'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '*':
                    board[row][col] = 'O'

    def markSafe(self, board, row, col):
        """Mark all 'O's connected to this position as safe by changing to '*'"""
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or
            board[row][col] != 'O'):
            return

        board[row][col] = '*'  # Mark as safe

        # Recursively mark all connected 'O's
        for direction in self.directions:
            self.markSafe(board, row + direction[0], col + direction[1])

        
            



def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_130():
    solution = Solution()

    # Test case 1
    board1 = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    expected1 = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]
    solution.solve(board1)
    run_test("Test 1", "4x4 board with surrounded regions", expected1, board1)

    # Test case 2
    board2 = [["X"]]
    expected2 = [["X"]]
    solution.solve(board2)
    run_test("Test 2", "1x1 board with X", expected2, board2)


if __name__ == "__main__":
    test_130()