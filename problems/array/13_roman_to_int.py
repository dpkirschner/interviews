"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
class Solution(object):
    denominations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # IV = 4 IX = 10
    # XL = 40 XC = 90
    # CD = 400 CM = 9000
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        index = 0
        while index < len(s):
            value = s[index]
            if index < len(s) - 1 and self.denominations[value] < self.denominations[s[index + 1]]:
                total -= self.denominations[value]
            else:
                total += self.denominations[value]
            index += 1
        return total
            
        

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "III"
    result1 = solution.romanToInt(s1)
    print(f"Input: {s1}, Output: {result1}, Expected: 3")
    
    s2 = "LVIII"
    result2 = solution.romanToInt(s2)
    print(f"Input: {s2}, Output: {result2}, Expected: 58")
    
    s3 = "MCMXCIV"
    result3 = solution.romanToInt(s3)
    print(f"Input: {s3}, Output: {result3}, Expected: 1994")