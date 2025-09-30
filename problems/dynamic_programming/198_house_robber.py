"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        result = [0]  * (len(nums))
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            result[i] = max(result[i - 2] + nums[i], result[i - 1])
        return result[-1]


def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        # {
        #     'nums': [1, 2, 3, 1],
        #     'expected': 4
        # },
        # {
        #     'nums': [2, 7, 9, 3, 1],
        #     'expected': 12
        # },
        {
            'nums': [2, 1, 1, 2],
            'expected': 4
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.rob(test['nums'])
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: nums={test['nums']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()