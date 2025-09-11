"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for val in nums:
            seen.add(val)
        
        current_total = 0
        total = 0
        for val in nums:
            # count up from here
            current_val = val
            while current_val in seen:
                current_total += 1
                current_val += 1
            
            current_val = val - 1
            while current_val in seen:
                current_total += 1
                current_val -= 1
            # count down from here
            total = max(total, current_total)
            current_total = 0
        return total
        

if __name__ == "__main__":
    sol = Solution()
    
    assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
    assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert sol.longestConsecutive([1,0,1,2]) == 3
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([1]) == 1
    
    print("All test cases passed!")