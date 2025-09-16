"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # naive idea: sort the candidates. create an array of candidate size with the smallest value. rotate each position through each candidate and recur
        # faster idea: if we are already bigger than the target, we can trim the rest
        results = []
        sorted_candidates = sorted(candidates)
        self.helper(sorted_candidates, target, [], results)
        return [list(t) for t in set(tuple(sorted(inner_list)) for inner_list in results)]
    
    def helper(self, sorted_candidates, target, path, results):
        if target == 0:
            results.append(path[:])
        
        if target <= 0:
            return True
        
        tooLarge = False
        for candidate in sorted_candidates:
            if tooLarge:
                continue
            path.append(candidate)
            tooLarge = self.helper(sorted_candidates, target - candidate, path, results)
            path.pop()
        
        return False


if __name__ == "__main__":
    solution = Solution()

    # Test 1
    input1_candidates = [2,3,6,7]
    input1_target = 7
    expected1 = [[2,2,3],[7]]
    result1 = solution.combinationSum(input1_candidates, input1_target)
    result1.sort()
    expected1.sort()
    print(f"Test 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Input: candidates = {input1_candidates}, target = {input1_target}")
    print(f"Output: {result1}")

    # Test 2
    input2_candidates = [2,3,5]
    input2_target = 8
    expected2 = [[2,2,2,2],[2,3,3],[3,5]]
    result2 = solution.combinationSum(input2_candidates, input2_target)
    result2.sort()
    expected2.sort()
    print(f"Test 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Input: candidates = {input2_candidates}, target = {input2_target}")
    print(f"Output: {result2}")

    # Test 3
    input3_candidates = [2]
    input3_target = 1
    expected3 = []
    result3 = solution.combinationSum(input3_candidates, input3_target)
    print(f"Test 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Input: candidates = {input3_candidates}, target = {input3_target}")
    print(f"Output: {result3}")