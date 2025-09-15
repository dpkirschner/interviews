"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        result = []
        self.helper(root, k, result)
        return result[k - 1]
        
    def helper(self, node, k, result):
        if not node:
            return
        
        self.helper(node.left, k, result)
        result.append(node.val)
        self.helper(node.right, k, result)


from utils import TreeNode, run_test


def test_230():
    solution = Solution()

    # Test case 1: [3,1,4,null,2], k = 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)

    result1 = solution.kthSmallest(root1, 1)
    expected1 = 1
    run_test("Test 1", "[3,1,4,null,2], k=1", expected1, result1)

    # Test case 2: [5,3,6,2,4,null,null,1], k = 3
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)

    result2 = solution.kthSmallest(root2, 3)
    expected2 = 3
    run_test("Test 2", "[5,3,6,2,4,null,null,1], k=3", expected2, result2)


if __name__ == "__main__":
    test_230()