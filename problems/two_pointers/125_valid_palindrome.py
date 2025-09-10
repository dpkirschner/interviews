"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].isalpha() and not s[left].isnumeric():
                left += 1
                continue
            if not s[right].isalpha() and not s[right].isnumeric():
                right -= 1
                continue
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True
        

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "A man, a plan, a canal: Panama"
    result1 = solution.isPalindrome(s1)
    print(f"Input: {s1}, Output: {result1}, Expected: True")
    
    s2 = "race a car"
    result2 = solution.isPalindrome(s2)
    print(f"Input: {s2}, Output: {result2}, Expected: False")
    
    s3 = " "
    result3 = solution.isPalindrome(s3)
    print(f"Input: {s3}, Output: {result3}, Expected: True")

    s4 = "0P"
    result4 = solution.isPalindrome(s4)
    print(f"Input: {s4}, Output: {result4}, Expected: False")