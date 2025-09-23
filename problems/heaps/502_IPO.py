"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
"""
import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        results = sorted(zip(profits, capital), key = lambda x: x[1])
        profit_heap = []
        index = 0
        cash = w
        max_size = k
        while max_size > 0:
            while index < len(results) and results[index][1] <= cash:
                heapq.heappush(profit_heap, (-results[index][0], results[index][1]))
                index += 1
            if len(profit_heap) < 0:
                break
            cash += -heapq.heappop(profit_heap)[0]
            max_size -= 1
 
        return cash



def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        {
            'k': 2,
            'w': 0,
            'profits': [1, 2, 3],
            'capital': [0, 1, 1],
            'expected': 4
        },
        {
            'k': 3,
            'w': 0,
            'profits': [1, 2, 3],
            'capital': [0, 1, 2],
            'expected': 6
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.findMaximizedCapital(
            test['k'],
            test['w'],
            test['profits'],
            test['capital']
        )
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: k={test['k']}, w={test['w']}, profits={test['profits']}, capital={test['capital']}")
        print(f"Output: {result}, Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()
