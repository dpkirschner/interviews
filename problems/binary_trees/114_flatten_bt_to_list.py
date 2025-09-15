"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        queue = deque()
        
        self.helper(root, queue)

        prev = None
        while queue:
            node = queue.popleft()
            if prev:
                prev.right = node
            prev = node
            node.left = None
        return root
    
    def helper(self, node, queue):
        if not node:
            return
        
        queue.append(node)
        self.helper(node.left, queue)
        self.helper(node.right, queue)
        

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_flattened_list(root):
    """Convert flattened tree to list representation"""
    if not root:
        return []
    
    result = []
    current = root
    while current:
        result.append(current.val)
        if current.left:  # Should be None in flattened tree
            result.append("ERROR: left child exists")
        current = current.right
    
    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: root = [1,2,5,3,4,null,6] => [1,2,3,4,5,6] (flattened preorder)
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)
    
    sol.flatten(root1)
    assert tree_to_flattened_list(root1) == [1,2,3,4,5,6]
    
    # Test case 2: root = [] => []
    sol.flatten(None)  # Should not crash
    
    # Test case 3: root = [0] => [0]
    root3 = TreeNode(0)
    sol.flatten(root3)
    assert tree_to_flattened_list(root3) == [0]
    
    print("All test cases passed!")