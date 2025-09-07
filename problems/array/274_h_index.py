"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        sorted_citations = sorted(citations)
        h_index = 0
        for i in range(len(sorted_citations)):
            if sorted_citations[i] >= len(sorted_citations) - i:
                h_index = max(h_index, len(sorted_citations) - i)
        return h_index

def test_h_index():
    solution = Solution()
    citations = [100]
    expected = 1
    result = solution.hIndex(citations)
    assert result == expected, f"Test 0 failed: expected {expected}, got {result}"
    
    # Example 1
    citations1 = [3, 0, 6, 1, 5]
    expected1 = 3
    result1 = solution.hIndex(citations1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Example 2
    citations2 = [1, 3, 1]
    expected2 = 1
    result2 = solution.hIndex(citations2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_h_index()