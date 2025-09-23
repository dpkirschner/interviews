"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.backing = []
        self.size = 0
    
    def push(self, val):
        # everything is in k'th largest
        if self.size < self.capacity:
            self.backing.append(val)
            self.size = self.size + 1
            self.bubble_up(len(self.backing) - 1)
            return
        
        # won't be in the k'th largest values
        if val <= self.backing[0]:
            return
        
        # root is no longer in k'th largest so discard and fix heap
        self.backing[0] = val
        self.bubble_down(0)

    def pop(self):
        temp = self.backing[0]
        self.backing[0] = self.backing[self.size - 1]
        self.size -= 1
        self.bubble_down(0)

        return temp

    def peek(self):
        return self.backing[0] if self.size > 0 else None

    def isEmpty(self):
        return self.size == 0
    
    def getParent(self, index):
        if index == 0:
            return None
        return (index - 1) // 2
    
    def getChildren(self, index):
        if index < 0:
            return None
        
        left = (2 * index) + 1
        right = (2 * index) + 2

        return (left, right)
    
    def bubble_up(self, index):
        if index < 0 or index >= self.size:
            return None
        parent = self.getParent(index)
        if parent is None:
            return
        
        if self.backing[parent] > self.backing[index]:
            self.swap(index, parent)
            self.bubble_up(parent)

    def bubble_down(self, index):
        if index < 0 or index >= self.size:
            return None
        
        left, right = self.getChildren(index)

        left_val = self.backing[left] if left < self.size else float('inf')
        right_val = self.backing[right] if right < self.size else float('inf')
        smallest = min(self.backing[index], left_val, right_val)
        if smallest != self.backing[index]:
            if smallest == left_val:
                self.swap(index, left)
                self.bubble_down(left)
            elif smallest == right_val:
                self.swap(index, right)
                self.bubble_down(right)

    def swap(self, a, b):
        temp = self.backing[a]
        self.backing[a] = self.backing[b]
        self.backing[b] = temp
            


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = MinHeap(k)
        for num in nums:
            minHeap.push(num)
        
        print(minHeap.size)
        return minHeap.peek()


def test_solution():
    solution = Solution()

    # nums1 = [3,2,1,5,6,4]
    # k1 = 2
    # result1 = solution.findKthLargest(nums1, k1)
    # expected1 = 5
    # print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    # print(f"Input: nums = {nums1}, k = {k1}")
    # print(f"Output: {result1}")
    # print()

    # nums2 = [3,2,3,1,2,4,5,5,6]
    # k2 = 4
    # result2 = solution.findKthLargest(nums2, k2)
    # expected2 = 4
    # print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    # print(f"Input: nums = {nums2}, k = {k2}")
    # print(f"Output: {result2}")

    nums3 = [2, 1]
    k3 = 2
    result3 = solution.findKthLargest(nums3, k3)
    expected3 = 1
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")

if __name__ == "__main__":
    test_solution()
