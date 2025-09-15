"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

from utils import TreeNode, run_test


def test_530():
    solution = Solution()

    # Test case 1: [4,2,6,1,3]
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)

    result1 = solution.getMinimumDifference(root1)
    expected1 = 1
    run_test("Test 1", "[4,2,6,1,3]", expected1, result1)

    # Test case 2: [1,0,48,null,null,12,49]
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(48)
    root2.right.left = TreeNode(12)
    root2.right.right = TreeNode(49)

    result2 = solution.getMinimumDifference(root2)
    expected2 = 1
    run_test("Test 2", "[1,0,48,null,null,12,49]", expected2, result2)


if __name__ == "__main__":
    test_530()