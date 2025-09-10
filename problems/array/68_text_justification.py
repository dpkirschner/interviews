"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be       
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        pass
        

if __name__ == "__main__":
    solution = Solution()
    
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    result1 = solution.fullJustify(words1, maxWidth1)
    expected1 = ["This    is    an", "example  of text", "justification.  "]
    print(f"Input: words={words1}, maxWidth={maxWidth1}")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print()
    
    words2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16
    result2 = solution.fullJustify(words2, maxWidth2)
    expected2 = ["What   must   be", "acknowledgment  ", "shall be        "]
    print(f"Input: words={words2}, maxWidth={maxWidth2}")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print()
    
    words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth3 = 20
    result3 = solution.fullJustify(words3, maxWidth3)
    expected3 = ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "]
    print(f"Input: words={words3}, maxWidth={maxWidth3}")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")