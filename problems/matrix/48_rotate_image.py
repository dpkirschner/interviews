"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        for layer in range(len(matrix) // 2):
            first = layer
            last = len(matrix) - 1 - layer
            
            for i in range(first, last):
                offset = i - first
                
                # Save top
                temp = matrix[first][i]
                
                # Left -> Top
                matrix[first][i] = matrix[last-offset][first]
                
                # Bottom -> Left  
                matrix[last-offset][first] = matrix[last][last-offset]
                
                # Right -> Bottom
                matrix[last][last-offset] = matrix[first+offset][last]
                
                # Top -> Right
                matrix[first+offset][last] = temp
        

if __name__ == "__main__":
    solution = Solution()
    
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix1)
    expected1 = [[7,4,1],[8,5,2],[9,6,3]]
    print("Test 1:", "PASS" if matrix1 == expected1 else "FAIL")
    
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix2)
    expected2 = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print("Test 2:", "PASS" if matrix2 == expected2 else "FAIL")
    
    # Failing test case
    matrix3 = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
    solution.rotate(matrix3)
    expected3 = [[4,33,13,32,12,2],[24,1,14,33,27,29],[1,20,32,32,9,20],[6,7,27,2,25,26],[32,21,22,28,13,16],[34,7,26,14,21,28]]
    print("Test 3:", "PASS" if matrix3 == expected3 else "FAIL")
    if matrix3 != expected3:
        print("Actual:")
        for row in matrix3:
            print(row)
        print("Expected:")
        for row in expected3:
            print(row)