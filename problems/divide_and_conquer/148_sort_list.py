"""
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):

    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        mid = self.findMid(head)
        left = head
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right #which ever one is left over
        return dummy.next # new head

    
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # naive solution: selection sort by traversing the list and building the result
    # insertion sort to build the new list
    # use an outside DS like a hash to pull them back
    # convert to a tree by inserting them, do inorder to pull back. thats 2n, right?


def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_solution():
    solution = Solution()

    head1 = array_to_list([4, 2, 1, 3])
    result1 = solution.sortList(head1)
    output1 = list_to_array(result1)
    expected1 = [1, 2, 3, 4]
    print(f"Test 1: {'PASS' if output1 == expected1 else 'FAIL'}")
    print(f"Input: [4,2,1,3]")
    print(f"Output: {output1}")
    print()

    # head2 = array_to_list([-1, 5, 3, 4, 0])
    # result2 = solution.sortList(head2)
    # output2 = list_to_array(result2)
    # expected2 = [-1, 0, 3, 4, 5]
    # print(f"Test 2: {'PASS' if output2 == expected2 else 'FAIL'}")
    # print(f"Input: [-1,5,3,4,0]")
    # print(f"Output: {output2}")
    # print()

    # head3 = array_to_list([])
    # result3 = solution.sortList(head3)
    # output3 = list_to_array(result3)
    # expected3 = []
    # print(f"Test 3: {'PASS' if output3 == expected3 else 'FAIL'}")
    # print(f"Input: []")
    # print(f"Output: {output3}")
    # print()

    # head4 = array_to_list([4,19,14,5,-3,1,8,5,11,15])
    # result4 = solution.sortList(head4)
    # output4 = list_to_array(result4)
    # expected4 = [-3,1,4,5,5,8,11,14,15,19]
    # print(f"Test 4: {'PASS' if output4 == expected4 else 'FAIL'}")
    # print(f"Input: [4,19,14,5,-3,1,8,5,11,15]")
    # print(f"Output: {output4}")

if __name__ == "__main__":
    test_solution()