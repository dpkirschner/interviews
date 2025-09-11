"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
"""
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(words) != len(pattern):
            return False

        pattern_seen = {}
        s_seen = {}
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if char not in pattern_seen and word not in s_seen:
                pattern_seen[char] = word
                s_seen[word] = char
            elif pattern_seen.get(char, '.') != word or s_seen.get(word, '.') != char:
                return False
        return True
        
        
if __name__ == "__main__":
    solution = Solution()
    
    result1 = solution.wordPattern("abba", "dog cat cat dog")
    expected1 = True
    print("Test 1:", "PASS" if result1 == expected1 else "FAIL")
    
    result2 = solution.wordPattern("abba", "dog cat cat fish")
    expected2 = False
    print("Test 2:", "PASS" if result2 == expected2 else "FAIL")
    
    result3 = solution.wordPattern("aaaa", "dog cat cat dog")
    expected3 = False
    print("Test 3:", "PASS" if result3 == expected3 else "FAIL")