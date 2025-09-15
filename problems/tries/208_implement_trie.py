"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
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
        self.backing = {}


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not word or len(word) == 0:
            return

        if word[0] not in self.backing:
            self.backing[word[0]] = TrieNode(word[0])
        node = self.backing[word[0]]

        for i in range(1, len(word)):
            if word[i] not in node:
                node.put(word[i], TrieNode(word[i]))
            node = node.get(word[i])
        node.terminal = True # last node gets this set

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word or len(word) == 0:
            return # searching for nothing

        if word[0] not in self.backing:
            return False
        node = self.backing[word[0]]

        for i in range(1, len(word)):
            if word[i] not in node:
                return False
            node = node.get(word[i])
        return node.terminal # only if this node is the terminal char in a word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if not prefix or len(prefix) == 0:
            return # searching for nothing

        if prefix[0] not in self.backing:
            return False
        node = self.backing[prefix[0]]

        for i in range(1, len(prefix)):
            if prefix[i] not in node:
                return False
            node = node.get(prefix[i])
        return node.hasWords() or node.terminal


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_208():
    # Test case from example
    trie = Trie()

    # Insert "apple"
    trie.insert("apple")

    # Search "apple" - should return True
    result1 = trie.search("apple")
    run_test("Test 1", "search('apple') after insert('apple')", True, result1)

    # Search "app" - should return False
    result2 = trie.search("app")
    run_test("Test 2", "search('app') after insert('apple')", False, result2)

    # StartsWith "app" - should return True
    result3 = trie.startsWith("app")
    run_test("Test 3", "startsWith('app') after insert('apple')", True, result3)

    # Insert "app"
    trie.insert("app")

    # Search "app" - should return True
    result4 = trie.search("app")
    run_test("Test 4", "search('app') after insert('app')", True, result4)


if __name__ == "__main__":
    test_208()