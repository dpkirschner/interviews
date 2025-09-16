"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        self.helper(n, k, 1, [], results)
        return results
    
    def helper(self, n, k, index, path, results):
        if k == 0:
            results.append(path[:])
            return

        for i in range(index, n + 1):
            path.append(i)
            self.helper(n, k - 1, i + 1, path, results)
            path.pop()
        

def test_solution():
    solution = Solution()

    # Test case 1
    n1, k1 = 4, 2
    output1 = solution.combine(n1, k1)
    expected1 = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print(f"Test 1: {'PASS' if sorted(output1) == sorted(expected1) else 'FAIL'}")
    print(f"Input: n = {n1}, k = {k1}")
    print(f"Output: {output1}")
    print()

    # Test case 2
    n2, k2 = 1, 1
    output2 = solution.combine(n2, k2)
    expected2 = [[1]]
    print(f"Test 2: {'PASS' if output2 == expected2 else 'FAIL'}")
    print(f"Input: n = {n2}, k = {k2}")
    print(f"Output: {output2}")
    print()

if __name__ == "__main__":
    test_solution()