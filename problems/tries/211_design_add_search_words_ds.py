"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""

class TrieNode(object):
    def __init__(self, key):
        self.backing = {}
        self.terminal = False
        self.key = key

    def __contains__(self, key):
        return key in self.backing
    
    def get(self, key):
        return self.backing[key]

    def put(self, key, node):
        self.backing[key] = node

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode('#')

    def addWord(self, word):
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

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word or len(word) == 0:
            return None

        return self.search_helper(word, self.root)

    def search_helper(self, word, node):
        if not word and node:
            return node.terminal
        
        if word[0] == '.':
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char in node:
                    result = self.search_helper(word[1:], node.get(char))    
                    if result:
                        return result
        elif word[0] in node:
            return self.search_helper(word[1:], node.get(word[0]))
        
        return False


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_211():
    # Test case from example
    wordDictionary = WordDictionary()

    # Add words
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")

    # Search "pad" - should return False
    result1 = wordDictionary.search("pad")
    run_test("Test 1", "search('pad') after adding bad/dad/mad", False, result1)

    # Search "bad" - should return True
    result2 = wordDictionary.search("bad")
    run_test("Test 2", "search('bad') after adding bad/dad/mad", True, result2)

    # Search ".ad" - should return True
    result3 = wordDictionary.search(".ad")
    run_test("Test 3", "search('.ad') after adding bad/dad/mad", True, result3)

    # Search "b.." - should return True
    result4 = wordDictionary.search("b..")
    run_test("Test 4", "search('b..') after adding bad/dad/mad", True, result4)


if __name__ == "__main__":
    test_211()