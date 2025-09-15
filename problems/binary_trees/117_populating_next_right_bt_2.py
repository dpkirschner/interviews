"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = deque([root])
        
        while queue:
            level = len(queue)
            prev = None
            for i in range(level):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def serialize_with_next(root):
    """Serialize tree with next pointers showing level structure"""
    if not root:
        return []
    
    result = []
    level = [root]
    
    while level:
        next_level = []
        for i, node in enumerate(level):
            result.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        if next_level:  # Add separator between levels
            result.append('#')
        level = next_level
    
    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: root = [1,2,3,4,5,null,7] => [1,#,2,3,#,4,5,7,#]
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(7)
    
    result1 = sol.connect(root1)
    serialized1 = serialize_with_next(result1)
    expected1 = [1, '#', 2, 3, '#', 4, 5, 7]
    assert serialized1 == expected1
    
    # Test case 2: root = [] => []
    result2 = sol.connect(None)
    assert serialize_with_next(result2) == []
    
    print("All test cases passed!")