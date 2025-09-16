"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
class Solution(object):
    letters = {
        "1": [],
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
        "0": [],
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        results = []
        self.helper(digits, "", results)
        return results
    
    def helper(self, digits, path, results):
        if not digits:
            results.append(path)
            return

        num = digits[0]
        for char in self.letters[num]:
            self.helper(digits[1:], path + char, results)

def test_solution():
    solution = Solution()

    # Test case 1
    input1 = "23"
    output1 = solution.letterCombinations(input1)
    expected1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(f"Test 1: {'PASS' if sorted(output1) == sorted(expected1) else 'FAIL'}")
    print(f"Input: {input1}")
    print(f"Output: {output1}")
    print()

    # Test case 2
    input2 = ""
    output2 = solution.letterCombinations(input2)
    expected2 = []
    print(f"Test 2: {'PASS' if output2 == expected2 else 'FAIL'}")
    print(f"Input: {input2}")
    print(f"Output: {output2}")
    print()

    # Test case 3
    input3 = "2"
    output3 = solution.letterCombinations(input3)
    expected3 = ["a","b","c"]
    print(f"Test 3: {'PASS' if sorted(output3) == sorted(expected3) else 'FAIL'}")
    print(f"Input: {input3}")
    print(f"Output: {output3}")
    print()

if __name__ == "__main__":
    test_solution()        