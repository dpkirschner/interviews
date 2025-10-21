"""
Binary Tree Level Order Traversal - LeetCode #102 (Medium)

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

Topics: Tree, Breadth-First Search, Binary Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            node = queue.pop(0)
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            result.append(level)

        return result


# Test cases
def build_tree(values):
    """Helper function to build a binary tree from a list"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def test_level_order():
    solution = Solution()

    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ]

    for tree_values, expected in test_cases:
        root = build_tree(tree_values)
        result = solution.levelOrder(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | Input: {tree_values} | Output: {result} | Expected: {expected}")


if __name__ == "__main__":
    test_level_order()
