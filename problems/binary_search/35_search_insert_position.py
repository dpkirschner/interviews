"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

def test_solution():
    solution = Solution()

    # nums1 = [1,3,5,6]
    # target1 = 5
    # result1 = solution.searchInsert(nums1, target1)
    # expected1 = 2
    # print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    # print(f"Input: nums = {nums1}, target = {target1}")
    # print(f"Output: {result1}")
    # print()

    nums2 = [1,3,5,6]
    target2 = 2
    result2 = solution.searchInsert(nums2, target2)
    expected2 = 1
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()

    nums3 = [1,3,5,6]
    target3 = 7
    result3 = solution.searchInsert(nums3, target3)
    expected3 = 4
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")

if __name__ == "__main__":
    test_solution()