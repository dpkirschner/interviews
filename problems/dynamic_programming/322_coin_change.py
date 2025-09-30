"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        results = [float('inf')] * (amount + 1)
        results[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= amount and coin <= i:
                    results[i] = min(results[i], results[i - coin] + 1)
        return results[amount] if results[amount] != float('inf') else -1


def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        {
            'coins': [1, 2, 5],
            'amount': 11,
            'expected': 3
        },
        {
            'coins': [2],
            'amount': 3,
            'expected': -1
        },
        {
            'coins': [1],
            'amount': 0,
            'expected': 0
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.coinChange(test['coins'], test['amount'])
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: coins={test['coins']}, amount={test['amount']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()