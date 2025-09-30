"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        results = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    results[i] = max(results[i], results[j] + 1)
        return max(results)


def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        {
            'nums': [10, 9, 2, 5, 3, 7, 101, 18],
            'expected': 4
        },
        {
            'nums': [0, 1, 0, 3, 2, 3],
            'expected': 4
        },
        {
            'nums': [7, 7, 7, 7, 7, 7, 7],
            'expected': 1
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.lengthOfLIS(test['nums'])
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: nums={test['nums']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()