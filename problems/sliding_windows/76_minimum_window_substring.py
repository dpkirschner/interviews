"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        

if __name__ == "__main__":
    solution = Solution()
    
    s1, t1 = "ADOBECODEBANC", "ABC"
    result1 = solution.minWindow(s1, t1)
    print(f"Input: s={s1}, t={t1}, Output: {result1}, Expected: BANC")
    
    s2, t2 = "a", "a"
    result2 = solution.minWindow(s2, t2)
    print(f"Input: s={s2}, t={t2}, Output: {result2}, Expected: a")
    
    s3, t3 = "a", "aa"
    result3 = solution.minWindow(s3, t3)
    print(f"Input: s={s3}, t={t3}, Output: {result3}, Expected: ")