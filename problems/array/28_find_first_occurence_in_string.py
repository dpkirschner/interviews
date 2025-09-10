"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
          return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    solution = Solution()
    
    haystack1, needle1 = "sadbutsad", "sad"
    result1 = solution.strStr(haystack1, needle1)
    print(f"Input: haystack={haystack1}, needle={needle1}, Output: {result1}, Expected: 0")
    
    haystack2, needle2 = "leetcode", "leeto"
    result2 = solution.strStr(haystack2, needle2)
    print(f"Input: haystack={haystack2}, needle={needle2}, Output: {result2}, Expected: -1")
