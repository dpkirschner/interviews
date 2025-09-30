"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique."""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        results = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if len(word) <= i + 1 and s[i + 1 - len(word):i + 1] == word:
                    if (i + 1 - len(word) == 0) or results[i - len(word)]:
                        results[i] = True
        return results[len(s) - 1]



def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        {
            's': "leetcode",
            'wordDict': ["leet", "code"],
            'expected': True
        },
        {
            's': "applepenapple",
            'wordDict': ["apple", "pen"],
            'expected': True
        },
        {
            's': "catsandog",
            'wordDict': ["cats", "dog", "sand", "and", "cat"],
            'expected': False
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.wordBreak(test['s'], test['wordDict'])
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: s=\"{test['s']}\", wordDict={test['wordDict']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()