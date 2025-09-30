"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        #dp[0][0] = 0 becauase there is nothing to change
        #dp[0][j] = j because you can only add here
        #dp[i][0] = i because you can only add here
        #dp[i][j] = if word1[i] == word2[j]:
        #   dp[i-1][j-1] 
        #  else
        #   insertion: deletion: replace: min(dp[i-1][j], dp[i][j-1]) + 1
        for j in range(len(word2) + 1):
            for i in range(len(word1) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word2[j - 1] == word1[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[len(word1)][len(word2)]
                    


def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        {
            'word1': "horse",
            'word2': "ros",
            'expected': 3
        },
        {
            'word1': "intention",
            'word2': "execution",
            'expected': 5
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.minDistance(test['word1'], test['word2'])
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: word1=\"{test['word1']}\", word2=\"{test['word2']}\"")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()