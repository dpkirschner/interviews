"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # first pass: dupe each node and place it in the 'next' spot of its original connect dupe next to original next
        # second pass: attach random pointer, strip, re-attach original next

        current = head
        while current.next:
            further = current.next
            dupe = Node(current.val)
            dupe.next = further
            current.next = dupe
            current = dupe.next
        current.next = Node(current.val)
        
        current = head
        while current:            
            dupe = current.next
            if current.random:
                dupe.random = current.random.next
            current = dupe.next
        
        current = head
        dupe = current.next
        dupe_head = dupe

        while current and dupe:
            current.next = dupe.next
            if dupe.next and dupe.next.next:
                dupe.next = dupe.next.next
                dupe = dupe.next 
            current = current.next
        return dupe_head
        

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def build_list_from_array(arr):
    if not arr:
        return None
    
    nodes = [Node(val) for val, _ in arr]
    
    for i in range(len(arr)):
        if i < len(arr) - 1:
            nodes[i].next = nodes[i + 1]
        
        random_idx = arr[i][1]
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
    
    return nodes[0]

def list_to_array(head):
    if not head:
        return []
    
    # First pass: collect all nodes and build index mapping
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    
    # Second pass: build result array
    result = []
    for i, node in enumerate(nodes):
        random_idx = None
        if node.random:
            for j, n in enumerate(nodes):
                if n is node.random:
                    random_idx = j
                    break
        result.append([node.val, random_idx])
    
    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    head1 = build_list_from_array([[7,None],[13,0],[11,4],[10,2],[1,0]])
    result1 = sol.copyRandomList(head1)
    assert list_to_array(result1) == [[7,None],[13,0],[11,4],[10,2],[1,0]]
    
    # Test case 2: [[1,1],[2,1]]
    head2 = build_list_from_array([[1,1],[2,1]])
    result2 = sol.copyRandomList(head2)
    assert list_to_array(result2) == [[1,1],[2,1]]
    
    # Test case 3: [[3,null],[3,0],[3,null]]
    head3 = build_list_from_array([[3,None],[3,0],[3,None]])
    result3 = sol.copyRandomList(head3)
    assert list_to_array(result3) == [[3,None],[3,0],[3,None]]
    
    print("All test cases passed!")