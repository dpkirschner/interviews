"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        result = []

        queue = deque([root])
        
        while queue:
            level = len(queue)
            node = None
            for i in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(node.val)
        return result



from utils import TreeNode, run_test


def test_199():
    solution = Solution()

    # Test case 1: [1,2,3,null,5,null,4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)

    result1 = solution.rightSideView(root1)
    expected1 = [1, 3, 4]
    run_test("Test 1", "[1,2,3,null,5,null,4]", expected1, result1)

    # Test case 2: [1,2,3,4,null,null,null,5]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.left.left = TreeNode(5)

    result2 = solution.rightSideView(root2)
    expected2 = [1, 3, 4, 5]
    run_test("Test 2", "[1,2,3,4,null,null,null,5]", expected2, result2)

    # Test case 3: [1,null,3]
    root3 = TreeNode(1)
    root3.right = TreeNode(3)

    result3 = solution.rightSideView(root3)
    expected3 = [1, 3]
    run_test("Test 3", "[1,null,3]", expected3, result3)

    # Test case 4: []
    result4 = solution.rightSideView(None)
    expected4 = []
    run_test("Test 4", "[]", expected4, result4)


if __name__ == "__main__":
    test_199()