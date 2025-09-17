"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged = []
        left = right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                merged.append(nums1[left])
                left += 1
            else:
                merged.append(nums2[right])
                right += 1
        
        merged.extend(nums1[left:])
        merged.extend(nums2[right:])

        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0


def test_solution():
    solution = Solution()

    nums1 = [1,3]
    nums2 = [2]
    result1 = solution.findMedianSortedArrays(nums1, nums2)
    expected1 = 2.00000
    print(f"Test 1: {'PASS' if abs(result1 - expected1) < 0.00001 else 'FAIL'}")
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result1}")
    print()

    nums1 = [1,2]
    nums2 = [3,4]
    result2 = solution.findMedianSortedArrays(nums1, nums2)
    expected2 = 2.50000
    print(f"Test 2: {'PASS' if abs(result2 - expected2) < 0.00001 else 'FAIL'}")
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result2}")

if __name__ == "__main__":
    test_solution()