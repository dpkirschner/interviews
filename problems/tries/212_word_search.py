"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""
class TrieNode(object):
    def __init__(self, key, terminal=False):
        self.terminal = False
        self.key = key
        self.backing = {}

    def __contains__(self, key):
          return key in self.backing

    def get(self, key):
        return self.backing[key]

    def put(self, key, node):
        self.backing[key] = node

    def hasWords(self):
        return len(self.backing) > 0

class Trie(object):

    def __init__(self):
        self.root = TrieNode('#')

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not word or len(word) == 0:
            return None

        node = self.root
        for index in range(len(word)):
            if word[index] not in node:
                node.put(word[index], TrieNode(word[index]))
            node = node.get(word[index])
        node.terminal = True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if not prefix or len(prefix) == 0:
            return # searching for nothing

        node = self.root
        for index in range(len(word)):
            if word[index] not in node:
                node.put(word[index], TrieNode(word[index]))
            node = node.get(word[index])

        return node.hasWords() or node.terminal

class Solution(object):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        results = []
        for row in range(len(board)):
            for column in range(len(board[0])):
                seen = set()
                seen.add((row, column))
                if board[row][column] in trie.root:
                    self.findWordFrom(board, row, column, trie.root.get(board[row][column]), board[row][column], results, seen)

        return list(set(results)) # drop duplicates if any
    
    def findWordFrom(self, board, row, column, trie_node, path, results, seen):
        if trie_node.terminal:
            results.append(path)
            trie_node.terminal = False # reset this so we don't add the same word multiple times

        if not trie_node.hasWords():
            return # no point in checking other spots since this chain is dead

        for direction in self.directions:
            dx, dy = direction[0] + row, direction[1] + column
            if (dx, dy) in seen or not (0 <= dx < len(board) and 0 <= dy < len(board[0])):
                continue
            
            next_char = board[dx][dy]
            if next_char in trie_node:
                seen.add((dx, dy))
                self.findWordFrom(board, dx, dy, trie_node.get(next_char), path + next_char, results, seen)
                seen.remove((dx, dy))


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if sorted(actual) == sorted(expected) else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={sorted(expected)}, Got={sorted(actual)}, {status}")
    return sorted(actual) == sorted(expected)


def test_212():
    solution = Solution()

    # Test case 1
    board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words1 = ["oath","pea","eat","rain"]
    expected1 = ["eat","oath"]
    actual1 = solution.findWords(board1, words1)
    run_test("Test 1", "4x4 board with words=['oath','pea','eat','rain']", expected1, actual1)

    # Test case 2
    board2 = [["a","b"],["c","d"]]
    words2 = ["abcb"]
    expected2 = []
    actual2 = solution.findWords(board2, words2)
    run_test("Test 2", "2x2 board with words=['abcb']", expected2, actual2)


if __name__ == "__main__":
    test_212()