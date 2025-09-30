"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        results = [0] * (n + 1)
        results[1] = 1
        results[2] = 2

        for i in range(3, n + 1):
            results[i] = results[i - 1] + results[i - 2]
        return results[n]

def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        {
            'n': 2,
            'expected': 2
        },
        {
            'n': 3,
            'expected': 3
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.climbStairs(test['n'])
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: n={test['n']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()