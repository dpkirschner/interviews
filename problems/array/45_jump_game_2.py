"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the key part here is to find the range of possibilities from any specific index
        # in my case that range is current_reach -> furthest_reach.
        current_reach = 0
        furthest_reach = 0
        steps = 0
        # look at every indx
        for i in range(len(nums) - 1):
            # figure out the furthest we can reach from any index we see
            furthest_reach = max(furthest_reach, i + nums[i])
            # the level goes from current_reach -> furthest_reach
            # if we hit this, the current level is done
            if i == current_reach:
                # every new level is a step
                steps += 1
                # new range starts at the end of the last one
                current_reach = furthest_reach
                if furthest_reach >= len(nums) - 1:
                    # if we made it? we're done. yay!
                    break
                
        return steps

    def jump_bfs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        queue = deque()
        secondary = deque()
        queue.append(0)
        steps = 1
        seen = set(())
        while queue:
            current_index = queue.popleft()
            value = nums[current_index]
            if current_index + value >= len(nums) - 1:
                break
            
            seen.add(current_index)
            for i in range(1, value + 1):
                if current_index + i in seen:
                    continue
                secondary.append(current_index + i)
            if not queue:
                queue = secondary
                secondary = deque()
                steps += 1
        return steps
            



if __name__ == "__main__":
    test_cases = [
        ([2,3,1,1,4], 2),
        ([1,2,1,1,1,4,4,1,5,2,3,4,1,4,2,5,2,6,4,4,2,2,5,6,2,3,4,5,4,4,2,3,1,4,1,6,2,3,5,3,6,6,1,2,5,3,3,4,6,1,1,5,3,3,4,5,1,4,2,6,6,4,1,4,1,2,1,4,4,2,1,2,2,5,6,5,4,4,3,6,5,2,5,6,1,4,3,4,3,3,1,2,6,5,3,6,1,2,6,4,2,3,3,4,6,3,5,3,2,3,3,1,3,2,4,1,3,5,1,1,5,2,4,2,2,5,3,4,2,1,3,3,1,2,4,5,4,6,2,5,6,4,6,5,2,2,1,4,6,4,2,4,1,6,3,3,6,1,4,5,4,5,1,2,3,6,1,4,3,2,5,1,5,2,5,1,2,3,3,6,6,3,5,2,6,1,6,4,3,4,1,2,5,1,5,6,5,3,1,5,6,3,6,3,5,6,2,2,6,3,4,1,4,1,1,3,4,1,5,6,5,4,2,5,3,6,4,1,2,3,5,6,5,2,3,6,1,3,4,6,3,2,5,5,1,6,6,6,2,3,5,5,4,5,2,1,6,6,2,5,1,3,2,5,1,2,3,4,1,1,5,1,4,1,2,2,6,1,4,3,2,1,6,5,1,6,2,3,5,3,6,6,5,2,1,4,4,5,3,5,5,1,3,2,6,1,6,6,4,6,5,3,3,1,6,2,6,4,2,4,1,2,2,2,2,1,5,4,3,6,3,2,5,5,4,6,4,1,5,2,4,6,2,4,5,5,3,4,6,6,1,6,6,5,3,1,4,6,5,3,5,3,5,2,3,4,6,2,5,6,6,2,5,6,1,1,5,4,5,6,6,5,5,3,3,4,4,5,2,6,5,1,3,2,3,1,3,1,2,3,5,2,5,3,2,2,3,4,4,2,6,5,1,3,4,6,1,6,4,4,2,4,5,2,5,6,6,1,3,1,1,4,6,5,6,4,1,3,1,1,6,2,6,4,5,5,3,5,3,6,6,2,1,3,2,5,5,3,5,3,3,5,3,2,1,2,2,6,1,6,4,2,2,2,6,2,4,2,5,5,2,3,1,1,5,6,6,3,4,6,2,1,2,1,4,2,5,6,5,5,3,2,1,5,1,3,2,2,5,1,6,1,6,5,6,2,6,3,6,5,1,4,6,3,3,6,6,4,1,4,6,3,4,1,4,2,5,5,5,4,2,5,6,6,3,1,5,4,2,3,6,1,6,4,1,5,5,6,4,5,4,4,6,5,2,5,1,4,3,2,6,1,5,2,6,2,6,1,2,3,5,5,4,4,5,4,2,1,4,1,4,6,1,1,2,6,2,3,6,4,4,5,6,6,4,1,6,3,2,4,1,4,5,5,2,6,6,4,2,5,4,6,6,5,2,4,1,1,4,1,1,4,6,1,5,2,4,6,5,1,6,6,6,2,1,6,1,5,5,4,5,2,3,2,2,2,6,4,6,2,4,6,4,5,1,3,2,4,2,6,6,4,3,3,1,1,4,4,5,5,4,1,6,5,1,3,3,6,5,5,3,6,3,5,2,4,3,4,6,5,2,6,6,1,2,3,4,6,1,5,6,4,6,6,1,1,2,4,6,4,1,1,6,6,2,1,1,2,3,6,5,3,1,6,1,3,6,2,4,5,3,2,5,3,5,5,2,1,3,4,4,6,2,4,3,3,1,5,3,3,1,2,5,2,5,2,2,4,2,2,4,6,3,1,4,2,3,4,2,2,6,3,2,6,3,3,5,5,5,2,3,1,6,5,4,5,2,6,5,2,1,2,2,2,2,2,3,2,6,3,1,5,6,1,4,6,5,3,3,5,5,6,5,1,4,3,5,5,3,4,6,4,6,3,2,1,1,6,2,2,5,5,3,1,3,5,6,3,6,2,5,6,2,1,4,4,2,2,6,2,1,5,6,1,1,3,3,5,5,3,2,5,2,1,3,2,4,3,5,2,5,5,4,1,1,3,4,3,1,3,5,5,4,5,5,1,3,5,4,6,5,4,2,1,2,6,6,4,4,5,6,6,6,3,4,3,5,2,5,6,5,2,1,4,5,3,1,6,4,1,5,4,5,2,5,1,4,2,6,3,3,5,1,3,4,3,3,6,6,5,5,5,4,5,3,6,6,6,4,2,4,4,1,2,2,2,3,2,2,5,6,5,6,3,3,1,1,4,1,6,6,5,3,2,6,5,2,1,6,1,4,6,4,1,2,1,2,5,1,1,6,3,2,5,4,5,2,6,5,6,2,2,1,5,5,1,6,2,1,3,4,5,4,3,1,5,6,5,4,1,2,3,4,2,2,6,2,4,3,2,5,3,2,2,5,6,3,3,2,1,4,5,2,3,2,5,3,1,3,6,3,6,4,2,5,3,6,1,6,5,2,1,5,2,1,1,4,3,3,1,1,2,2,1,1,4,1,6,5,5,6,4,6,6,2,2,2,6,1,1,1,1,5,2,2,1,6,5,6,1,3,1,6,4,1,2,1,5,1,1,3,6,4,5,4,2,3,4,1,5,2,2,1,6,2,3,2,3,3,1,1,4,5,5,3,5,3,6,4,5,4,4,4,2,2,1,4,6,0,0,0,0,0], 274),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"Test {i+1}: Input={nums}, Expected={expected}")
        result = Solution().jump(nums)
        print(f"  Result={result}, {'PASS' if result == expected else 'FAIL'}")
        print()