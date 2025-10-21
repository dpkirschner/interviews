"""
Common utilities for leetcode problems.
"""

from typing import List, Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        # definitely a useful comment here
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Convert a list to a linked list."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert a linked list to a list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
