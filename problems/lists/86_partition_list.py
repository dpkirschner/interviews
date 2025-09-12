"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head

        lowHead = None
        lowTail = None
        highHead = None
        highTail = None

        current = head
        while current:
            if current.val < x:
                if not lowHead:
                    lowHead = current
                    lowTail = current
                else:
                    lowTail.next = current
                    lowTail = current
            else:
                if not highHead:
                    highHead = current
                    highTail = current
                else:
                    highTail.next = current
                    highTail = current
            
            current = current.next

        if not lowTail:
            highTail.next = None
            return highHead
        if not highTail:
            lowTail.next = None
            return lowHead

        lowTail.next = highHead
        highTail.next = None
        return lowHead


        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,4,3,2,5,2], x=3 => [1,2,2,4,3,5]
    head1 = list_to_linked_list([1,4,3,2,5,2])
    result1 = sol.partition(head1, 3)
    assert linked_list_to_list(result1) == [1,2,2,4,3,5]
    
    # Test case 2: [2,1], x=2 => [1,2]
    head2 = list_to_linked_list([2,1])
    result2 = sol.partition(head2, 2)
    assert linked_list_to_list(result2) == [1,2]
    
    print("All test cases passed!")