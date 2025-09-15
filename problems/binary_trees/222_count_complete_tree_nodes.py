"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
"""

from utils import TreeNode, run_test


class Solution:
    def countNodes(self, root):
        pass


def test_222():
    solution = Solution()

    # Test case 1: [1,2,3,4,5,6]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)

    result1 = solution.countNodes(root1)
    expected1 = 6
    run_test("Test 1", "[1,2,3,4,5,6]", expected1, result1)

    # Test case 2: []
    result2 = solution.countNodes(None)
    expected2 = 0
    run_test("Test 2", "[]", expected2, result2)

    # Test case 3: [1]
    root3 = TreeNode(1)
    result3 = solution.countNodes(root3)
    expected3 = 1
    run_test("Test 3", "[1]", expected3, result3)


if __name__ == "__main__":
    test_222()