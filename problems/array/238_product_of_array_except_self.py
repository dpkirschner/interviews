"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [1]
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        carry = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            result[i] = carry * result[i]
            carry = carry * nums[i]
        
        return result

def test_product_except_self():
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    result1 = solution.productExceptSelf(nums1)
    assert result1 == expected1, f"Example 1 failed: expected {expected1}, got {result1}"
    
    # Example 2
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    result2 = solution.productExceptSelf(nums2)
    assert result2 == expected2, f"Example 2 failed: expected {expected2}, got {result2}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_product_except_self()