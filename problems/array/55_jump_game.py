"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        must_reach = len(nums) - 1
        current = len(nums) - 1
        while current >= 0:
            if nums[current] >= must_reach - current:
                must_reach = current
            current -= 1
        return must_reach == 0


if __name__ == "__main__":
    test_cases = [
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"Test {i+1}: Input={nums}, Expected={expected}")
        result = Solution().canJump(nums)
        print(f"  Result={result}, {'PASS' if result == expected else 'FAIL'}")
        print()
