"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
class Solution(object):
    def maxProfit(self, prices):
        left = [0] * len(prices)
        right = [0] * len(prices)

        max_profit = 0
        min_seen = prices[0]
        for i in range(len(prices)):
            left[i] = max(max_profit, prices[i] - min_seen)
            min_seen = min(min_seen, prices[i])

        max_profit = 0
        max_seen = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            right[i] = max(max_profit, max_seen - prices[i])
            max_seen = max(max_seen, prices[i])
            max_profit = max(max_profit, right[i])

        max_profit = 0
        for i in range(len(prices)):
            if i < len(right) - 1:
                max_profit = max(max_profit, left[i] + right[i+1])
            else:
                max_profit = max(max_profit, left[i])
        return max_profit

    def greedy_max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_seen = prices[0]
        results = [0] * len(prices)
        for index, value in enumerate(prices):
            profit = value - min_seen
            results[index] = max(results[index], profit)
            # This is the core issue with greedy choices. 
            # I need to pick at this point, do i reset the profit counter? or do i continue going?
            # profit under 0 doesn't help me make this decision. I need to actually do the calculations to know.
            # this is why DP works, because DP doesn't require this decision
            if profit < 0:
                min_seen = value
        
        max_profits = [0]
        for i in range(len(results)):
            max_profits[-1] = max(max_profits[-1], results[i])
            if results[i] == 0 and max_profits[-1] != 0:
                max_profits.append(0)

        sorted_max_profits = sorted(max_profits)
        if len(sorted_max_profits) == 0:
            return 0
        if len(sorted_max_profits) == 1:
            return sorted_max_profits[0]
        else:
            return sorted_max_profits[-1] + sorted_max_profits[-2]


def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        # {
        #     'prices': [3, 3, 5, 0, 0, 3, 1, 4],
        #     'expected': 6
        # },
        {
            'prices': [1, 2, 3, 4, 5],
            'expected': 4
        },
        # {
        #     'prices': [7, 6, 4, 3, 1],
        #     'expected': 0
        # },
        # {
        #     'prices': [6,1,3,2,4,7],
        #     'expected': 7
        # }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.maxProfit(test['prices'])
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: prices={test['prices']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()