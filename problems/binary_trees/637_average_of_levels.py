"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """


from utils import TreeNode, run_test


def test_637():
    solution = Solution()

    # Test case 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    result1 = solution.averageOfLevels(root1)
    expected1 = [3.0, 14.5, 11.0]
    run_test("Test 1", "[3,9,20,null,null,15,7]", expected1, result1)

    # Test case 2: [3,9,20,15,7]
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.left.left = TreeNode(15)
    root2.left.right = TreeNode(7)

    result2 = solution.averageOfLevels(root2)
    expected2 = [3.0, 14.5, 11.0]
    run_test("Test 2", "[3,9,20,15,7]", expected2, result2)


if __name__ == "__main__":
    test_637()