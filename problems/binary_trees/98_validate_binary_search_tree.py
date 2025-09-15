"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, node, left, right):
        if not node:
            return True
        if node.val <= left or node.val >= right:
            return False

        return self.helper(node.left, left, node.val) and self.helper(node.right, node.val, right)


from utils import TreeNode, run_test


def test_98():
    solution = Solution()

    # Test case 1: [2,1,3]
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)

    result1 = solution.isValidBST(root1)
    expected1 = True
    run_test("Test 1", "[2,1,3]", expected1, result1)

    # Test case 2: [5,1,4,null,null,3,6]
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)

    result2 = solution.isValidBST(root2)
    expected2 = False
    run_test("Test 2", "[5,1,4,null,null,3,6]", expected2, result2)


if __name__ == "__main__":
    test_98()