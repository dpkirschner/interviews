"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = [0] * len(height)
        for i in range(1, len(height)):
            result[i] = max(height[i - 1], result[i - 1])
        
        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            right_max = max(height[i], right_max)
            water_level = min(result[i], right_max)
            result[i] = max(0, water_level - height[i])

        return sum(result)


if __name__ == "__main__":
    solution = Solution()
    
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    result1 = solution.trap(height1)
    print(f"Input: {height1}, Output: {result1}, Expected: 6")
    
    height2 = [4,2,0,3,2,5]
    result2 = solution.trap(height2)
    print(f"Input: {height2}, Output: {result2}, Expected: 9")
        