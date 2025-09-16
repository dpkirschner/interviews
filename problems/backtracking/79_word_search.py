"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
class Solution(object):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not word:
            return False
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    seen = set()
                    seen.add((row, column))
                    result = self.helper(board, row, column, word[1:], seen)
                    if result:
                        return result
        return False
    
    def helper(self, board, row, column, word, seen):      
        if not word:
            return True
        
        for direction in self.directions:
            dx = row + direction[0]
            dy = column + direction[1]
            if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and word[0] == board[dx][dy]:
                if (dx, dy) in seen:
                    continue
                seen.add((dx, dy))
                result = self.helper(board, dx, dy, word[1:], seen)
                if result:
                    return result
                seen.remove((dx, dy))
        return False

        


if __name__ == "__main__":
    solution = Solution()

    # # Test 1
    # input1_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # input1_word = "ABCCED"
    # expected1 = True
    # result1 = solution.exist(input1_board, input1_word)
    # print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    # print(f"Input: board = {input1_board}, word = \"{input1_word}\"")
    # print(f"Output: {result1}")

    # # Test 2
    # input2_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # input2_word = "SEE"
    # expected2 = True
    # result2 = solution.exist(input2_board, input2_word)
    # print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    # print(f"Input: board = {input2_board}, word = \"{input2_word}\"")
    # print(f"Output: {result2}")

    # # Test 3
    # input3_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # input3_word = "ABCB"
    # expected3 = False
    # result3 = solution.exist(input3_board, input3_word)
    # print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    # print(f"Input: board = {input3_board}, word = \"{input3_word}\"")
    # print(f"Output: {result3}")

    # Test 4
    input4_board = [["a","a"]]
    input4_word = "aaa"
    expected4 = False
    result4 = solution.exist(input4_board, input4_word)
    print(f"Test 4: {'PASS' if result4 == expected4 else 'FAIL'}")
    print(f"Input: board = {input4_board}, word = \"{input4_word}\"")
    print(f"Output: {result4}")