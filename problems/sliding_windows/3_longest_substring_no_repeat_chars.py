"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        seen = set()
        longest = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right]) # add the original conflict to the set so we can keep going
                left += 1
        
        return longest

if __name__ == "__main__":
    solution = Solution()
    
    # s1 = "abcabcbb"
    # result1 = solution.lengthOfLongestSubstring(s1)
    # print(f"Input: {s1}, Output: {result1}, Expected: 3")
    
    # s2 = "bbbbb"
    # result2 = solution.lengthOfLongestSubstring(s2)
    # print(f"Input: {s2}, Output: {result2}, Expected: 1")
    
    # s3 = "pwwkew"
    # result3 = solution.lengthOfLongestSubstring(s3)
    # print(f"Input: {s3}, Output: {result3}, Expected: 3")

    s4 = "tmmzuxt"
    result4 = solution.lengthOfLongestSubstring(s4)
    print(f"Input: {s4}, Output: {result4}, Expected: 5")
