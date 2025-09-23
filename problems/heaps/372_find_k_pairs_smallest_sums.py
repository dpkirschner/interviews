"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length
"""
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        pairs_heap = []
        seen = set()
        heapq.heappush(pairs_heap, ((nums1[0] + nums2[0]), (0, 0)))
        seen.add((0, 0))
        while len(results) < k and pairs_heap:
            sum, indices = heapq.heappop(pairs_heap)
            left, right = indices[0], indices[1]
            results.append([nums1[left], nums2[right]])
            if left + 1 < len(nums1) and (left+1, right) not in seen:
                heapq.heappush(pairs_heap, ((nums1[left + 1] + nums2[right]), (left + 1, right)))
                seen.add((left + 1, right))
            if right + 1 < len(nums2) and (left, right + 1) not in seen:
                heapq.heappush(pairs_heap, ((nums1[left] + nums2[right + 1]), (left, right + 1)))
                seen.add((left, right + 1))
        
        return results



def test_solution():
    solution = Solution()

    # Test cases from problem examples
    test_cases = [
        {
            'nums1': [1, 7, 11],
            'nums2': [2, 4, 6],
            'k': 3,
            'expected': [[1, 2], [1, 4], [1, 6]]
        },
        {
            'nums1': [1, 1, 2],
            'nums2': [1, 2, 3],
            'k': 2,
            'expected': [[1, 1], [1, 1]]
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.kSmallestPairs(
            test['nums1'],
            test['nums2'],
            test['k']
        )
        status = 'PASS' if result == test['expected'] else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Input: nums1={test['nums1']}, nums2={test['nums2']}, k={test['k']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print()

if __name__ == "__main__":
    test_solution()