"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = ""
        # LCP will be this length (or shorter) by definition
        for i in range(len(strs[0])):
            potential_prefix = strs[0][i]
            for j in range (1, len(strs)):
                if len(strs[j]) <= i:
                    return prefix
                if strs[j][i] != potential_prefix:
                    return prefix
            prefix += potential_prefix
        return prefix

if __name__ == "__main__":
    solution = Solution()
    
    strs1 = ["flower","flow","flight"]
    result1 = solution.longestCommonPrefix(strs1)
    print(f"Input: {strs1}, Output: {result1}, Expected: fl")
    
    strs2 = ["dog","racecar","car"]
    result2 = solution.longestCommonPrefix(strs2)
    print(f"Input: {strs2}, Output: {result2}, Expected: ")