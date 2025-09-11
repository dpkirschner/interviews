"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        push_values = ['(', '[', '{']
        pop_values = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        seen = []
        for char in s:
            if char in push_values:
                seen.append(char)
            else:
                if not bool(seen) or seen[-1] != pop_values[char]:
                    return False
                else:
                    seen.pop()

        return not bool(seen)
        

if __name__ == "__main__":
    sol = Solution()
    
    assert sol.isValid("()") == True
    assert sol.isValid("()[]{}")== True
    assert sol.isValid("(]") == False
    assert sol.isValid("([])") == True
    assert sol.isValid("([)]") == False
    
    print("All test cases passed!")