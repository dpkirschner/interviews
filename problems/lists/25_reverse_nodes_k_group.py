"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,4,5], k=2 => [2,1,4,3,5]
    head1 = list_to_linked_list([1,2,3,4,5])
    result1 = sol.reverseKGroup(head1, 2)
    assert linked_list_to_list(result1) == [2,1,4,3,5]
    
    # Test case 2: [1,2,3,4,5], k=3 => [3,2,1,4,5]
    head2 = list_to_linked_list([1,2,3,4,5])
    result2 = sol.reverseKGroup(head2, 3)
    assert linked_list_to_list(result2) == [3,2,1,4,5]
    
    print("All test cases passed!")