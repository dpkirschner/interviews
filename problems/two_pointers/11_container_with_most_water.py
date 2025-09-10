"""
ou are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)  - 1
        best = 0
        while left < right:
            pillar_size = min(height[left], height[right])
            best = max(best, pillar_size * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best

        

if __name__ == "__main__":
    solution = Solution()
    
    height1 = [1,8,6,2,5,4,8,3,7]
    result1 = solution.maxArea(height1)
    print(f"Input: {height1}, Output: {result1}, Expected: 49")
    
    height2 = [1,1]
    result2 = solution.maxArea(height2)
    print(f"Input: {height2}, Output: {result2}, Expected: 1")

    height3 = [1,2,1]
    result3 = solution.maxArea(height3)
    print(f"Input: {height3}, Output: {result3}, Expected: 2")