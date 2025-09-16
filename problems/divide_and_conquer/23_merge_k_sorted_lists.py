"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-999)
        node = dummy
        while True:
            minIndex = None
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minIndex == None or lists[i].val < lists[minIndex].val:
                    minIndex = i
            if minIndex == None:
                break
            next_node = ListNode(lists[minIndex].val)
            lists[minIndex] = lists[minIndex].next
            node.next = next_node
            node = next_node

        return dummy.next            



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

    lists1 = [array_to_list([1,4,5]), array_to_list([1,3,4]), array_to_list([2,6])]
    result1 = solution.mergeKLists(lists1)
    output1 = list_to_array(result1)
    expected1 = [1,1,2,3,4,4,5,6]
    print(f"Test 1: {'PASS' if output1 == expected1 else 'FAIL'}")
    print(f"Input: [[1,4,5],[1,3,4],[2,6]]")
    print(f"Output: {output1}")
    print()

    lists2 = []
    result2 = solution.mergeKLists(lists2)
    output2 = list_to_array(result2)
    expected2 = []
    print(f"Test 2: {'PASS' if output2 == expected2 else 'FAIL'}")
    print(f"Input: []")
    print(f"Output: {output2}")
    print()

    lists3 = [array_to_list([])]
    result3 = solution.mergeKLists(lists3)
    output3 = list_to_array(result3)
    expected3 = []
    print(f"Test 3: {'PASS' if output3 == expected3 else 'FAIL'}")
    print(f"Input: [[]]")
    print(f"Output: {output3}")

if __name__ == "__main__":
    test_solution()