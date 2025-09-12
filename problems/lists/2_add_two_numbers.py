"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.addTwoNumbersHelper(l1, l2, None, None, 0)

    def addTwoNumbersHelper(self, l1, l2, node, head, carry):
        # base case:
        if l1 is None and l2 is None:
            if carry != 0:
                node.next = ListNode(carry)
            return head

        if l1 is not None:
            l1_val = l1.val
        else:
            l1_val = 0

        if l2 is not None:
            l2_val = l2.val
        else:
            l2_val = 0

        sub = l1_val + l2_val + carry
        carry = 0
        if sub >= 10:
            sub -= 10
            carry = 1
        listNode = ListNode(sub)
        if node is not None:
            node.next = listNode
        else:
            head = listNode
        return self.addTwoNumbersHelper(l1.next if l1 else None, l2.next if l2 else None, listNode, head, carry)
        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # # Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    # l1 = list_to_linked_list([2,4,3])
    # l2 = list_to_linked_list([5,6,4])
    # result = sol.addTwoNumbers(l1, l2)
    # assert linked_list_to_list(result) == [7,0,8]
    
    # Test case 2: [0] + [0] = [0]
    # l1 = list_to_linked_list([0])
    # l2 = list_to_linked_list([0])
    # result = sol.addTwoNumbers(l1, l2)
    # assert linked_list_to_list(result) == [0]
    
    # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1 = list_to_linked_list([9,9,9,9,9,9,9])
    l2 = list_to_linked_list([9,9,9,9])
    result = sol.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [8,9,9,9,0,0,0,1]
    
    print("All test cases passed!")