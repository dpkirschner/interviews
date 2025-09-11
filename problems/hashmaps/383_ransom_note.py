"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        
        for char in ransom_counter:
            if char not in magazine_counter or magazine_counter[char] < ransom_counter[char]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    
    result1 = solution.canConstruct("a", "b")
    expected1 = False
    print("Test 1:", "PASS" if result1 == expected1 else "FAIL")
    
    result2 = solution.canConstruct("aa", "ab")
    expected2 = False
    print("Test 2:", "PASS" if result2 == expected2 else "FAIL")
    
    result3 = solution.canConstruct("aa", "aab")
    expected3 = True
    print("Test 3:", "PASS" if result3 == expected3 else "FAIL")