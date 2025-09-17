"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = nums[mid]
            if mid == 0:
                if nums[mid + 1] < value:
                    return mid
                else:
                    left = mid + 1
            elif mid == len(nums) - 1:
                if nums[mid - 1] < value:
                    return mid  
                else:
                    right = mid - 1
            elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            else:
                if nums[mid - 1] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            
            


def test_solution():
    solution = Solution()

    nums1 = [1,2,3,1]
    result1 = solution.findPeakElement(nums1)
    expected1 = 2
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print()

    nums2 = [1,2,1,3,5,6,4]
    result2 = solution.findPeakElement(nums2)
    expected2a = 1
    expected2b = 5
    print(f"Test 2: {'PASS' if result2 == expected2a or result2 == expected2b else 'FAIL'}")
    print(f"Input: {nums2}")
    print(f"Output: {result2}")

if __name__ == "__main__":
    test_solution()