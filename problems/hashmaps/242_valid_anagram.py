"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = Counter(s)
        t_count = Counter(t)
        if len(s_count) != len(t_count):
            return False
        for key in s_count:
            if s_count[key] != t_count[key]:
                return False
        return True
        
        
if __name__ == "__main__":
    solution = Solution()
    
    result1 = solution.isAnagram("anagram", "nagaram")
    expected1 = True
    print("Test 1:", "PASS" if result1 == expected1 else "FAIL")
    
    result2 = solution.isAnagram("rat", "car")
    expected2 = False
    print("Test 2:", "PASS" if result2 == expected2 else "FAIL")