"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""
from collections import deque
class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        return self.bfs(beginWord, endWord, set(wordList))
        # return self.backtrack(beginWord, endWord, set(wordList), set(), 0)

    # returns fastest (earliest, closest) match due to level by level
    def bfs(self, start, end, wordList):
        if end not in wordList:
            return 0 # can't get there
        
        queue = deque([(start, 1)]) # word, steps
        seen = set()
        while queue:
            word, steps = queue.popleft()
            if word == end:
                return steps
            
            if word in seen:
                continue

            for index in range(len(start)):
                for choice in 'abcdefghijklmnopqrstuvwxyz':
                    if word[index] == choice:
                        continue
                    nextWord = word[:index] + choice + word[index+1:]
                    if nextWord in wordList and nextWord not in seen:
                        queue.append((nextWord, steps + 1))
        return 0



    # returns first match found, not optimal match
    def backtrack(self, start, end, wordList, seen, steps):
        if start == end:
            return steps

        for index, char in enumerate(start):    
            for choice in 'abcdefghijklmnopqrstuvwxyz':
                if start[index] == choice:
                    continue
                nextWord = start[:index] + choice + start[index+1:]
                if nextWord not in wordList:
                    continue
                if nextWord in seen:
                    continue
                seen.add(nextWord)
                result = self.backtrack(nextWord, end, wordList, seen, steps + 1)
                if result:
                    return result
        return 0


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_127():
    solution = Solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    actual1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    run_test("Test 1", "beginWord = 'hit', endWord = 'cog', wordList = ['hot','dot','dog','lot','log','cog']", expected1, actual1)

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    actual2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    run_test("Test 2", "beginWord = 'hit', endWord = 'cog', wordList = ['hot','dot','dog','lot','log']", expected2, actual2)

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    actual3 = solution.ladderLength(beginWord3, endWord3, wordList3)
    run_test("Test 3", "beginWord = 'a', endWord = 'c', wordList = ['a','b','c']", expected3, actual3)


if __name__ == "__main__":
    test_127()