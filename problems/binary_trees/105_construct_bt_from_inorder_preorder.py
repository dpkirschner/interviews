"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        preIndex = [0]
        return self.helper(preorder, inorder, preIndex, 0, len(preorder) - 1)
        
    def search(self, inorder, value, left, right):
        for i in range(left, right + 1):
            if inorder[i] == value:
                return i
        return -1

    def helper(self, preorder, inorder, preIndex, left, right):
        if left > right:
            return None
        rootVal = preorder[preIndex[0]]
        preIndex[0] += 1
        root = TreeNode(rootVal)

        index = self.search(inorder, rootVal, left, right)
        root.left = self.helper(preorder, inorder, preIndex, left, index - 1)
        root.right = self.helper(preorder, inorder, preIndex, index + 1, right)

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
    
    # Test case 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] => [3,9,20,null,null,15,7]
    result1 = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
    assert tree_to_list(result1) == [3,9,20,None,None,15,7]
    
    # Test case 2: preorder = [-1], inorder = [-1] => [-1]
    result2 = sol.buildTree([-1], [-1])
    assert tree_to_list(result2) == [-1]
    
    print("All test cases passed!")