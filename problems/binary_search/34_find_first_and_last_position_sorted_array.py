"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
     
        left = 0
        right = len(nums) - 1
        left_edge = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left_edge = mid
                right = mid - 1 # keep going left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1
        right_edge = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right_edge = mid
                left = mid + 1 # keep going right
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return [left_edge, right_edge] if left_edge != -1 else [-1, -1]

def test_solution():
    solution = Solution()

    nums1 = [5,7,7,8,8,10]
    target1 = 8
    result1 = solution.searchRange(nums1, target1)
    expected1 = [3,4]
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print()

    nums2 = [5,7,7,8,8,10]
    target2 = 6
    result2 = solution.searchRange(nums2, target2)
    expected2 = [-1,-1]
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()

    nums3 = []
    target3 = 0
    result3 = solution.searchRange(nums3, target3)
    expected3 = [-1,-1]
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")

    nums4 = [2, 2]
    target4 = 2
    result4 = solution.searchRange(nums4, target4)
    expected4 = [0, 1]
    print(f"Test 4: {'PASS' if result4 == expected4 else 'FAIL'}")
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {result4}")

if __name__ == "__main__":
    test_solution()
