"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        result = [None]
        self.helper(root, p, q, result)
        return result[0]

    def helper(self, node, p, q, result):
        if not node:
            return

        isMe = node == p or node == q

        isLeft = self.helper(node.left, p, q, result)
        isRight = self.helper(node.right, p, q, result)

        if (isLeft and isRight) or (isMe and (isLeft or isRight)):
            result[0] = node

        return isLeft or isRight or isMe


from utils import TreeNode


def test_236():
    solution = Solution()

    # Test case 1: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    root1 = TreeNode(3)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    root1.left = node5
    root1.right = node1
    node5.left = TreeNode(6)
    node5.right = TreeNode(2)
    node1.left = TreeNode(0)
    node1.right = TreeNode(8)
    node5.right.left = TreeNode(7)
    node5.right.right = TreeNode(4)

    result1 = solution.lowestCommonAncestor(root1, node5, node1)
    expected1 = root1
    print(f"Test 1: p=5, q=1, Expected={expected1.val}, Got={result1.val if result1 else None}, {'PASS' if result1 == expected1 else 'FAIL'}")

    # Test case 2: same tree, p = 5, q = 4
    node4 = node5.right.right
    result2 = solution.lowestCommonAncestor(root1, node5, node4)
    expected2 = node5
    print(f"Test 2: p=5, q=4, Expected={expected2.val}, Got={result2.val if result2 else None}, {'PASS' if result2 == expected2 else 'FAIL'}")

    # Test case 3: root = [1,2], p = 1, q = 2
    root3 = TreeNode(1)
    node2 = TreeNode(2)
    root3.left = node2

    result3 = solution.lowestCommonAncestor(root3, root3, node2)
    expected3 = root3
    print(f"Test 3: p=1, q=2, Expected={expected3.val}, Got={result3.val if result3 else None}, {'PASS' if result3 == expected3 else 'FAIL'}")


if __name__ == "__main__":
    test_236()