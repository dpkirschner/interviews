"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque
class Solution(object):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        seen = set()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if (row, column) in seen:
                    continue
                if grid[row][column] == "1":
                    self.claimIsland(grid, row, column, seen)
                    count += 1
        return count

    def claimIsland(self, grid, row, column, seen):
        searchSpace = deque([(row, column)])
        while searchSpace:
            current = searchSpace.popleft()
            if current in seen:
                continue
            seen.add((current[0], current[1]))
            for direction in self.directions:
                dx = current[0] + direction[0]
                dy = current[1] + direction[1]
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
                    if grid[dx][dy] == "1" and (dx, dy) not in seen:
                        searchSpace.append((dx, dy))


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_200():
    solution = Solution()

    # Test case 1
    # grid1 = [
    #     ["1","1","1","1","0"],
    #     ["1","1","0","1","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","0","0","0"]
    # ]
    # result1 = solution.numIslands(grid1)
    # expected1 = 1
    # run_test("Test 1", "4x5 grid with 1 island", expected1, result1)

    # # Test case 2
    # grid2 = [
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    # ]
    # result2 = solution.numIslands(grid2)
    # expected2 = 3
    # run_test("Test 2", "4x5 grid with 3 islands", expected2, result2)

    # Test case 3
    # grid3 = [
    #     ["1","1","1"],
    #     ["0","1","0"],
    #     ["1","1","1"]
    # ]
    # result3 = solution.numIslands(grid3)
    # expected3 = 1
    # run_test("Test 3", "3x3 grid with 1 connected island", expected3, result3)

    # Test case 4
    grid4 = [
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]
    ]
    result4 = solution.numIslands(grid4)
    expected4 = 1
    run_test("Test 4", "3x5 grid with 1 connected island", expected4, result4)


if __name__ == "__main__":
    test_200()