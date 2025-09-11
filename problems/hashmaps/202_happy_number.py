"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        val = n
        while val != 1:
            val = self.convert(val)
            if val in seen:
                return False
            seen.add(val)
        return val == 1
    
    def convert(self, num):
        total = 0
        for char in str(num):
            total += int(char) * int(char)
        return total

        

if __name__ == "__main__":
    sol = Solution()
    
    assert sol.isHappy(19) == True
    assert sol.isHappy(2) == False
    assert sol.isHappy(1) == True
    assert sol.isHappy(7) == True
    
    print("All test cases passed!")