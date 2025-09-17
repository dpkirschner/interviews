"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # if I'm not in the sorted side, I must be in the random rotation side
            # we don't know whats happening over there because we don't know how large the endpoint is
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                    

def test_solution():
    solution = Solution()

    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    result1 = solution.search(nums1, target1)
    expected1 = 4
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print()

    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    result2 = solution.search(nums2, target2)
    expected2 = -1
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()

    nums3 = [1]
    target3 = 0
    result3 = solution.search(nums3, target3)
    expected3 = -1
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")

if __name__ == "__main__":
    test_solution()