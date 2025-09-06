"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        candidate = nums[0]
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1
        return candidate
                


if __name__ == "__main__":
    test_cases = [
        # ([3,2,3], 3),
        # ([2,2,1,1,1,2,2], 2),
        ([8,9,8,9,8], 8),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        nums_copy = nums[:]  # Make a copy since the function modifies the array
        print(f"Test {i+1}: Input={nums}, Expected={expected}")
        result = Solution().majorityElement(nums_copy)
        print(f"  Result={result}, {'PASS' if result == expected else 'FAIL'}")
        print()