"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.helper(root)
        
    def helper(self, node):
        if not node:
            return 0
        
        return 1 + max(self.helper(node.left), self.helper(node.right))
    

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7] => 3
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert sol.maxDepth(root1) == 3
    
    # Test case 2: [1,null,2] => 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    assert sol.maxDepth(root2) == 2
    
    # Test case 3: [] => 0
    assert sol.maxDepth(None) == 0
    
    print("All test cases passed!")