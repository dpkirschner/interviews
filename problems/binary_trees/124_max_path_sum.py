"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = [-float('inf')]
        self.helper(root, result)
        return result[0]

    def helper(self, node, result):
        if not node:
            return 0 
        
        left = self.helper(node.left, result)
        right = self.helper(node.right, result)

        not_root = max(node.val + left, node.val + right, node.val)
        incl_root = max(not_root, left + node.val + right)

        result[0] = max(result[0], not_root, incl_root)

        return not_root

from utils import TreeNode, run_test


def test_124():
    solution = Solution()

    # Test case 1: [-1, 2]
    # root1 = TreeNode(2)
    # root1.left = TreeNode(-1)

    # result1 = solution.maxPathSum(root1)
    # expected1 = 2
    # print(f"Test 1: Input=[2,-1], Expected={expected1}, Got={result1}, {'PASS' if result1 == expected1 else 'FAIL'}")

    # Test case 2: [-1,-2,10,-6,null,-3,-6]
    root2 = TreeNode(-1)
    root2.left = TreeNode(-2)
    root2.right = TreeNode(10)
    root2.left.left = TreeNode(-6)
    root2.right.left = TreeNode(-3)
    root2.right.right = TreeNode(-6)

    result2 = solution.maxPathSum(root2)
    expected2 = 10
    run_test("Test 2", "[-1,-2,10,-6,null,-3,-6]", expected2, result2)


if __name__ == "__main__":
    test_124()