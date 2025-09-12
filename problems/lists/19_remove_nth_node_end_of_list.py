"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = n
        fast = head
        while count > 0 and fast:
            fast = fast.next
            count -= 1
        
        if not fast and count == 0:
            return head.next if head.next else None

        if not fast or count > 0:
            return head
        
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        
        return head

        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,4,5], n=2 => [1,2,3,5]
    # head1 = list_to_linked_list([1,2,3,4,5])
    # result1 = sol.removeNthFromEnd(head1, 2)
    # assert linked_list_to_list(result1) == [1,2,3,5]
    
    # # Test case 2: [1], n=1 => []
    # head2 = list_to_linked_list([1])
    # result2 = sol.removeNthFromEnd(head2, 1)
    # assert linked_list_to_list(result2) == []
    
    # # Test case 3: [1,2], n=1 => [1]
    # head3 = list_to_linked_list([1,2])
    # result3 = sol.removeNthFromEnd(head3, 1)
    # assert linked_list_to_list(result3) == [1]

    head4 = list_to_linked_list([1,2])
    result4 = sol.removeNthFromEnd(head4, 2)
    assert linked_list_to_list(result4) == [2]
    
    print("All test cases passed!")

        