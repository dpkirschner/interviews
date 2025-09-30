"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return triangle
        if len(triangle) == 1:
            return triangle[0][0]
        
        for row in range(len(triangle) - 2, -1, -1):
            for column in range(len(triangle[row])):
                triangle[row][column] = triangle[row][column] + min(triangle[row + 1][column], triangle[row + 1][column + 1])
        return triangle[0][0]

def test_minimum_total():
    solution = Solution()

    test_cases = [
        ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
        ([[-10]], -10),
    ]

    for i, (triangle_input, expected) in enumerate(test_cases):
        result = solution.minimumTotal(triangle_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: {status}")
        print(f"  Input: {triangle_input}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


if __name__ == "__main__":
    test_minimum_total()
    