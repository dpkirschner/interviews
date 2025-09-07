"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        if nums_length <= 1:
            return
        partition = k % nums_length
        if partition == 0: return
        self.reverse(nums, 0, nums_length - 1)
        self.reverse(nums, 0, partition - 1)
        self.reverse(nums, partition, nums_length - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

if __name__ == "__main__":
    test_cases = [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        # ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ]
    
    for i, (nums, k, expected) in enumerate(test_cases):
        nums_copy = nums[:]  # Make a copy since the function modifies the array
        print(f"Test {i+1}: Input={nums}, k={k}, Expected={expected}")
        Solution().rotate(nums_copy, k)
        print(f"  Result={nums_copy}, {'PASS' if nums_copy == expected else 'FAIL'}")
        print()