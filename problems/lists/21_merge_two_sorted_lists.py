"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1 is None and list2 is None:
            return None
        
        l1 = list1
        l2 = list2
        head = None
        current = None
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                mine = l1
                l1 = l1.next
            else:
                mine = l2
                l2 = l2.next

            if head is None:
                head = mine
            if current is not None:
                current.next = mine
            current = mine

        if l1 is not None:
            current.next = l1
        if l2 is not None:
            current.next = l2
        return head
        

from list_utils import ListNode, list_to_linked_list, linked_list_to_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,4] + [1,3,4] = [1,1,2,3,4,4]
    # list1 = list_to_linked_list([1,2,4])
    # list2 = list_to_linked_list([1,3,4])
    # result = sol.mergeTwoLists(list1, list2)
    # assert linked_list_to_list(result) == [1,1,2,3,4,4]

    list1 = list_to_linked_list([-9, 3])
    list2 = list_to_linked_list([5, 7])
    result = sol.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [-9, 3, 5, 7]
    
    # Test case 2: [] + [] = []
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    result = sol.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == []
    
    # Test case 3: [] + [0] = [0]
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([0])
    result = sol.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [0]
    
    print("All test cases passed!")