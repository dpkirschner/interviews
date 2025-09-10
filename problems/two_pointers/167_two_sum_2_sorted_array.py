"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            value = numbers[left] + numbers[right]
            if value == target:
                return [left + 1, right + 1]
            if value < target:
                left += 1
            if value > target:
                right -= 1
        return []

if __name__ == "__main__":
    solution = Solution()
    
    numbers1, target1 = [2,7,11,15], 9
    result1 = solution.twoSum(numbers1, target1)
    print(f"Input: numbers={numbers1}, target={target1}, Output: {result1}, Expected: [1,2]")
    
    numbers2, target2 = [2,3,4], 6
    result2 = solution.twoSum(numbers2, target2)
    print(f"Input: numbers={numbers2}, target={target2}, Output: {result2}, Expected: [1,3]")
    
    numbers3, target3 = [-1,0], -1
    result3 = solution.twoSum(numbers3, target3)
    print(f"Input: numbers={numbers3}, target={target3}, Output: {result3}, Expected: [1,2]")