"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runningTotal = 0
        currentMax = float('-inf')
        for i in range(len(nums)):
            runningTotal = max(runningTotal + nums[i], nums[i])
            currentMax = max(currentMax, runningTotal)
        return currentMax

def test_solution():
    solution = Solution()

    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    result1 = solution.maxSubArray(nums1)
    expected1 = 6
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print()

    nums2 = [1]
    result2 = solution.maxSubArray(nums2)
    expected2 = 1
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print()

    nums3 = [5,4,-1,7,8]
    result3 = solution.maxSubArray(nums3)
    expected3 = 23
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: {nums3}")
    print(f"Output: {result3}")

if __name__ == "__main__":
    test_solution()