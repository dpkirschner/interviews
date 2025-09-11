"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = defaultdict(list)
        for s in strs:
            alpha = ''.join(sorted(s))
            seen[alpha].append(s)

        return list(seen.values())
        
        
if __name__ == "__main__":
    solution = Solution()
    
    result1 = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]
    print("Test 1:", "PASS" if sorted(sorted(group) for group in result1) == sorted(sorted(group) for group in expected1) else "FAIL")
    
    result2 = solution.groupAnagrams([""])
    expected2 = [[""]]
    print("Test 2:", "PASS" if result2 == expected2 else "FAIL")
    
    result3 = solution.groupAnagrams(["a"])
    expected3 = [["a"]]
    print("Test 3:", "PASS" if result3 == expected3 else "FAIL")