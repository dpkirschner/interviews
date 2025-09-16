"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # naive oslution: pick the middle (or close enough) as the root. set left to root of left side. set right to root of right side
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, left, right):
        if left > right:
            return None
        
        mid = ((right - left) // 2) + left
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root

def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result

def test_solution():
    solution = Solution()

    nums1 = [-10, -3, 0, 5, 9]
    result1 = solution.sortedArrayToBST(nums1)
    output1 = tree_to_list(result1)
    expected1 = [0, -3, 9, -10, None, 5]
    print(f"Test 1: {'PASS' if output1 == expected1 or output1 == [0, -10, 5, None, -3, None, 9] else 'FAIL'}")
    print(f"Input: {nums1}")
    print(f"Output: {output1}")
    print()

    nums2 = [1, 3]
    result2 = solution.sortedArrayToBST(nums2)
    output2 = tree_to_list(result2)
    expected2a = [3, 1]
    expected2b = [1, None, 3]
    print(f"Test 2: {'PASS' if output2 == expected2a or output2 == expected2b else 'FAIL'}")
    print(f"Input: {nums2}")
    print(f"Output: {output2}")

if __name__ == "__main__":
    test_solution()
