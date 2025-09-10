"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        sorted_nums = sorted(nums)
        for hold in range(len(sorted_nums)):
            if hold > 0 and sorted_nums[hold] == sorted_nums[hold-1]:
                continue

            target = 0 - sorted_nums[hold]
            left = hold + 1
            right = len(sorted_nums) - 1

            while left < right:
                value = sorted_nums[left] + sorted_nums[right]
                if value == target:
                    results.append(sorted([sorted_nums[hold], sorted_nums[left], sorted_nums[right]]))
                    left += 1
                elif value > target:
                    right -= 1
                else:
                    left += 1
        
        unique_tuples = set()
        for result in results:
            unique_tuples.add(tuple(sorted(result)))
        return [list(t) for t in unique_tuples]


if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [-1,0,1,2,-1,-4]
    result1 = solution.threeSum(nums1)
    expected1 = [[-1,-1,2],[-1,0,1]]
    print(f"Input: {nums1}, Output: {result1}, Expected: {expected1}")
    
    nums2 = [0,1,1]
    result2 = solution.threeSum(nums2)
    expected2 = []
    print(f"Input: {nums2}, Output: {result2}, Expected: {expected2}")
    
    nums3 = [0,0,0]
    result3 = solution.threeSum(nums3)
    expected3 = [[0,0,0]]
    print(f"Input: {nums3}, Output: {result3}, Expected: {expected3}")