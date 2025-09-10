"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not t:
            return False
        left = 0
        right = 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
                if left == len(s):
                    return True
            right += 1
        return left == len(s)

if __name__ == "__main__":
    solution = Solution()
    
    s1, t1 = "abc", "ahbgdc"
    result1 = solution.isSubsequence(s1, t1)
    print(f"Input: s={s1}, t={t1}, Output: {result1}, Expected: True")
    
    s2, t2 = "axc", "ahbgdc"
    result2 = solution.isSubsequence(s2, t2)
    print(f"Input: s={s2}, t={t2}, Output: {result2}, Expected: False")