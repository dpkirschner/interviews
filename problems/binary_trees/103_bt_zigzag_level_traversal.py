"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """


from utils import TreeNode, run_test


def test_103():
    solution = Solution()

    # Test case 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    result1 = solution.zigzagLevelOrder(root1)
    expected1 = [[3], [20, 9], [15, 7]]
    run_test("Test 1", "[3,9,20,null,null,15,7]", expected1, result1)

    # Test case 2: [1]
    root2 = TreeNode(1)

    result2 = solution.zigzagLevelOrder(root2)
    expected2 = [[1]]
    run_test("Test 2", "[1]", expected2, result2)

    # Test case 3: []
    result3 = solution.zigzagLevelOrder(None)
    expected3 = []
    run_test("Test 3", "[]", expected3, result3)


if __name__ == "__main__":
    test_103()