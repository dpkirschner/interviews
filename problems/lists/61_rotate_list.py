"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        tail = head
        count = k
        length = 0
        while count > 0:
            if not tail.next:
                length += 1 # we are at the end
                if k % length == 0: # don't rotate full circles
                    return head
                k = k % length # can we trim k maybe and save some time?
                count = k
                tail = head
            else:
                tail = tail.next
                length += 1
            count -= 1
        
        next_tail = head
        while tail.next:
            tail = tail.next
            next_tail = next_tail.next

        
        
        
        # early exit 

        next_head = next_tail.next    
        next_tail.next = None
        tail.next = head
        return next_head    

        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,4,5], k=2 => [4,5,1,2,3]
    # head1 = list_to_linked_list([1,2,3,4,5])
    # result1 = sol.rotateRight(head1, 2)
    # assert linked_list_to_list(result1) == [4,5,1,2,3]
    
    # # Test case 2: [0,1,2], k=4 => [2,0,1]
    # head2 = list_to_linked_list([0,1,2])
    # result2 = sol.rotateRight(head2, 4)
    # assert linked_list_to_list(result2) == [2,0,1]

    # head3 = list_to_linked_list([])
    # result3 = sol.rotateRight(head3, 0)
    # assert linked_list_to_list(result3) == []

    # head4 = list_to_linked_list([1])
    # result4 = sol.rotateRight(head4, 1)
    # assert linked_list_to_list(result4) == [1]

    # head5 = list_to_linked_list([1, 2])
    # result5 = sol.rotateRight(head5, 0)
    # assert linked_list_to_list(result5) == [1, 2]

    # head5 = list_to_linked_list([1, 2])
    # result5 = sol.rotateRight(head5, 1)
    # assert linked_list_to_list(result5) == [2, 1]

    head6 = list_to_linked_list([1, 2])
    result6 = sol.rotateRight(head6, 2)
    assert linked_list_to_list(result6) == [1, 2]
    
    print("All test cases passed!")