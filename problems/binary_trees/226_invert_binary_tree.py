"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.helper(root)
        return root

    def helper(self, node):
        if not node:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.helper(node.left)
        self.helper(node.right)
        

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root):
    """Convert tree to list for easy comparison"""
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
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [4,2,7,1,3,6,9] => [4,7,2,9,6,3,1]
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    result1 = sol.invertTree(root1)
    assert tree_to_list(result1) == [4,7,2,9,6,3,1]
    
    # Test case 2: [2,1,3] => [2,3,1]
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    result2 = sol.invertTree(root2)
    assert tree_to_list(result2) == [2,3,1]
    
    # Test case 3: [] => []
    result3 = sol.invertTree(None)
    assert tree_to_list(result3) == []
    
    print("All test cases passed!")