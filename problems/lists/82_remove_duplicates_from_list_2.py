"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not node or not node.next:
            return node

        if node.next.val != node.val:
            node.next = self.helper(node.next)
            return node

        
        current = node
        while current and current.val == node.val:
            current = current.next
        return self.helper(current)
        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,3,4,4,5] => [1,2,5]
    head1 = list_to_linked_list([1,2,3,3,4,4,5])
    result1 = sol.deleteDuplicates(head1)
    assert linked_list_to_list(result1) == [1,2,5]
    
    # Test case 2: [1,1,1,2,3] => [2,3]
    head2 = list_to_linked_list([1,1,1,2,3])
    result2 = sol.deleteDuplicates(head2)
    assert linked_list_to_list(result2) == [2,3]
    
    print("All test cases passed!")