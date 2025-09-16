"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass

def test_solution():
    solution = Solution()

    nums1 = [1,-2,3,-2]
    result1 = solution.maxSubarraySumCircular(nums1)
    expected1 = 3
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print()

    nums2 = [5,-3,5]
    result2 = solution.maxSubarraySumCircular(nums2)
    expected2 = 10
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print()

    nums3 = [-3,-2,-3]
    result3 = solution.maxSubarraySumCircular(nums3)
    expected3 = -2
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: {nums3}")
    print(f"Output: {result3}")

if __name__ == "__main__":
    test_solution()