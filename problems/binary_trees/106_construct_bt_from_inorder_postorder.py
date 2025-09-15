"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.helper(inorder, postorder, 0, len(inorder) - 1, len(inorder) - 1)

    def search(self, nums, value, left, right):
        for i in range(left, right + 1):
            if nums[i] == value:
                return i
        return -1
    
    def helper(self, inorder, postorder, left, right, postIndex):
        if left > right:
            return None

        root = TreeNode(postorder[postIndex])
        index = self.search(inorder, root.val, left, right)

        right_subtree_size = right - index
        root.right = self.helper(inorder, postorder, index + 1, right, postIndex - 1)
        root.left = self.helper(inorder, postorder, left, index - 1, postIndex - 1 - right_subtree_size)

        return root
        

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root):
    """Convert tree to list for comparison (level order with nulls)"""
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
    
    # Test case 1: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3] => [3,9,20,null,null,15,7]
    result1 = sol.buildTree([9,3,15,20,7], [9,15,7,20,3])
    assert tree_to_list(result1) == [3,9,20,None,None,15,7]
    
    # Test case 2: inorder = [-1], postorder = [-1] => [-1]
    result2 = sol.buildTree([-1], [-1])
    assert tree_to_list(result2) == [-1]
    
    print("All test cases passed!")