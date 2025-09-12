"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or left == right:
            return head
        cur = head
        prev = None
        for i in range(left - 1):
            prev = cur
            cur = cur.next
        if prev is None:
            head = self.reverseList(cur, right - left) 
        else:
            prev.next = self.reverseList(cur, right - left) 
        return head

    def reverseList(self, head, distance):
        if not head or distance == 0:
            return head
        count = distance
        cur = head
        prev = None
        while cur and count >= 0:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count -= 1
        head.next = cur
        return prev
        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,4,5], left=2, right=4 => [1,4,3,2,5]
    head1 = list_to_linked_list([1,2,3,4,5])
    result1 = sol.reverseBetween(head1, 2, 4)
    assert linked_list_to_list(result1) == [1,4,3,2,5]
    
    # Test case 2: [5], left=1, right=1 => [5]
    head2 = list_to_linked_list([3, 5])
    result2 = sol.reverseBetween(head2, 1, 2)
    assert linked_list_to_list(result2) == [5, 3]
    
    print("All test cases passed!")