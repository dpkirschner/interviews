"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

P I N
A L S I G
Y A H R
P I

Input: s = "A", numRows = 1
Output: "A"
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        row = 0
        isDown = True
        for char in s:
            rows[row].append(char)

            if isDown:
                row += 1
            else:
                row -= 1

            if row == numRows - 1:
                isDown = False
            elif row == 0:
                isDown = True
            
        result = ""
        for row in rows:
            result += "".join(row)
        return result
            
        

if __name__ == "__main__":
    solution = Solution()
    
    s1, numRows1 = "PAYPALISHIRING", 3
    result1 = solution.convert(s1, numRows1)
    print(f"Input: s={s1}, numRows={numRows1}, Output: {result1}, Expected: PAHNAPLSIIGYIR")
    
    s2, numRows2 = "PAYPALISHIRING", 4
    result2 = solution.convert(s2, numRows2)
    print(f"Input: s={s2}, numRows={numRows2}, Output: {result2}, Expected: PINALSIGYAHRPI")
    
    s3, numRows3 = "A", 1
    result3 = solution.convert(s3, numRows3)
    print(f"Input: s={s3}, numRows={numRows3}, Output: {result3}, Expected: A")