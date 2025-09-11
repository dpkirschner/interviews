"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = defaultdict(list)
        for i in range(len(nums)):
            seen[nums[i]].append(i)
        
        for val in seen:
            dupes = seen[val]
            if len(dupes) >= 2:
                for i in range(len(dupes)):
                    for j in range(i + 1, len(dupes)):
                        if abs(dupes[i] - dupes[j]) <= k:
                            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    
    assert sol.containsNearbyDuplicate([1,2,3,1], 3) == True
    assert sol.containsNearbyDuplicate([1,0,1,1], 1) == True
    assert sol.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
    assert sol.containsNearbyDuplicate([1,0,1,1], 1) == True
    
    print("All test cases passed!")