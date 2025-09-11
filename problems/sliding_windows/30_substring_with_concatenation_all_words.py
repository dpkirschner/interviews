"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

"""
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
          return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        target_count = Counter(words)  # Expected frequency
        results = []
        for i in range(len(s) - total_len + 1):
            window = s[i:i + total_len]
            window_words = [window[j:j + word_len] for j in range(0, total_len, word_len)]
            window_count = Counter(window_words)
            if window_count == target_count:
                results.append(i)

        return results

if __name__ == "__main__":
    solution = Solution()
    
    s1, words1 = "barfoothefoobarman", ["foo","bar"]
    result1 = solution.findSubstring(s1, words1)
    expected1 = [0,9]
    print(f"Input: s={s1}, words={words1}, Output: {result1}, Expected: {expected1}")
    
    s2, words2 = "wordgoodgoodgoodbestword", ["word","good","best","word"]
    result2 = solution.findSubstring(s2, words2)
    expected2 = []
    print(f"Input: s={s2}, words={words2}, Output: {result2}, Expected: {expected2}")
    
    s3, words3 = "barfoofoobarthefoobarman", ["bar","foo","the"]
    result3 = solution.findSubstring(s3, words3)
    expected3 = [6,9,12]
    print(f"Input: s={s3}, words={words3}, Output: {result3}, Expected: {expected3}")