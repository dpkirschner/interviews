"""
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
- -2^31 <= x <= 2^31 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
    ]

    for i, (input_val, expected) in enumerate(test_cases, 1):
        result = solution.reverse(input_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: Input: {input_val}, Output: {result}, Expected: {expected}")
