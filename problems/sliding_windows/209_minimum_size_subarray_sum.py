"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left = 0
        total = 0
        minimum = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minimum = min(minimum, right - left + 1)
                total -= nums[left]
                left += 1

        return minimum if minimum != float('inf') else 0

        

if __name__ == "__main__":
    solution = Solution()
    
    target1, nums1 = 7, [2,3,1,2,4,3]
    result1 = solution.minSubArrayLen(target1, nums1)
    print(f"Input: target={target1}, nums={nums1}, Output: {result1}, Expected: 2")
    
    target2, nums2 = 4, [1,4,4]
    result2 = solution.minSubArrayLen(target2, nums2)
    print(f"Input: target={target2}, nums={nums2}, Output: {result2}, Expected: 1")
    
    target3, nums3 = 11, [1,1,1,1,1,1,1,1]
    result3 = solution.minSubArrayLen(target3, nums3)
    print(f"Input: target={target3}, nums={nums3}, Output: {result3}, Expected: 0")