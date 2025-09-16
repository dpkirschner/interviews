"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.helper(nums, [], results)
        return results
    
    def helper(self, nums, path, results):
        # naive idea: pull an index out of the list. pass list[:index] + list[index + 1:] 
        # better idea: queue of 10 numbers. every level gets another queue
        if not nums:
            results.append(path[:])
            return
        
        for i in range(len(nums)):
            next_set = nums[:i] + nums[i + 1:]
            path.append(nums[i])
            self.helper(next_set, path, results)
            path.pop()

if __name__ == "__main__":
    solution = Solution()

    # Test 1
    input1 = [1,2,3]
    expected1 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    result1 = solution.permute(input1)
    result1.sort()
    expected1.sort()
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: {input1}")
    print(f"Output: {result1}")

    # Test 2
    input2 = [0,1]
    expected2 = [[0,1],[1,0]]
    result2 = solution.permute(input2)
    result2.sort()
    expected2.sort()
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: {input2}")
    print(f"Output: {result2}")

    # Test 3
    input3 = [1]
    expected3 = [[1]]
    result3 = solution.permute(input3)
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: {input3}")
    print(f"Output: {result3}")