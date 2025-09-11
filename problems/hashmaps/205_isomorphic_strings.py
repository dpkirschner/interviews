"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return
        s_seen = {}
        t_seen = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char not in s_seen and t_char not in t_seen:
                s_seen[s_char] = t_char
                t_seen[t_char] = s_char
            elif s_seen.get(s_char, '.') != t_char or t_seen.get(t_char, '.') != s_char:
                return False
        return True
                


if __name__ == "__main__":
    solution = Solution()
    
    # result1 = solution.isIsomorphic("egg", "add")
    # expected1 = True
    # print("Test 1:", "PASS" if result1 == expected1 else "FAIL")
    
    # result2 = solution.isIsomorphic("foo", "bar")
    # expected2 = False
    # print("Test 2:", "PASS" if result2 == expected2 else "FAIL")
    
    result3 = solution.isIsomorphic("baba", "badc")
    expected3 = True
    print("Test 3:", "PASS" if result3 == expected3 else "FAIL")