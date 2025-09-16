"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.helper(n, 0, 0, [], results)
        return results

    def helper(self, n, open_count, close_count, path, results):
        if len(path) == n * 2:
            results.append(''.join(path))
            return
    
        if open_count < n:
            path.append('(')
            self.helper(n, open_count + 1, close_count, path, results)
            path.pop()
        if close_count < open_count:
            path.append(')')
            self.helper(n, open_count, close_count + 1, path, results)
            path.pop()



if __name__ == "__main__":
    solution = Solution()

    # Test 1
    input1 = 3
    expected1 = ["((()))","(()())","(())()","()(())","()()()"]
    result1 = solution.generateParenthesis(input1)
    result1.sort()
    expected1.sort()
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: {input1}")
    print(f"Output: {result1}")

    # Test 2
    input2 = 1
    expected2 = ["()"]
    result2 = solution.generateParenthesis(input2)
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: {input2}")
    print(f"Output: {result2}")