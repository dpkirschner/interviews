"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""
class LRUCache(object):

    # core idea: dict for the backing storage. K -> key V -> DoubleLinkedListNode(key, value)
    # add a new key: add as the new head node
    # edit a key: dict -> node. extract node. repair other nodes. place node at front.
    # evict a key: tail node in list. remove prev pointer. del key from map

    class ListNode(object):
        def __init__(self, key=0, val=0, next=None, prev=None):
            self.val = val
            self.key = key
            self.next = next
            self.prev = prev

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.backing = {}
        self.lru_head = None
        self.lru_tail = None
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.backing:
            return -1
            
        self.touchKey(key)
        return self.backing[key].val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.backing:
            self.backing[key].val = value
        else:
            self.backing[key] = self.ListNode(key, value)

        self.touchKey(key)
        
        if len(self.backing) > self.capacity:            
            self.evictKey()

    def touchKey(self, key):
        if key not in self.backing:
            return #safety
        
        node = self.backing[key]
        if node.prev:
            node.prev.next = node.next
            if self.lru_tail == node:
                self.lru_tail = node.prev
        if node.next:
            node.next.prev = node.prev
            if self.lru_head == node:
                self.lru_head = node.next


        if not self.lru_head:
            self.lru_head = node
            self.lru_tail = node
        else :
            node.next = self.lru_head
            node.prev = None
            self.lru_head.prev = node
            self.lru_head = node
            

    def evictKey(self):
        if not self.lru_tail and not self.lru_head:
            return
        node = self.lru_tail
        self.lru_tail = self.lru_tail.prev
        self.lru_tail.next = None
        del self.backing[node.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    # Test case from example
    # lRUCache = LRUCache(2)
    # lRUCache.put(1, 1)  # cache is {1=1}
    # lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    # assert lRUCache.get(1) == 1     # return 1
    # lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # assert lRUCache.get(2) == -1    # returns -1 (not found)
    # lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # assert lRUCache.get(1) == -1    # return -1 (not found)
    # assert lRUCache.get(3) == 3     # return 3
    # assert lRUCache.get(4) == 4     # return 4
    
    # Test case that failed
    lRUCache2 = LRUCache(2)
    lRUCache2.put(2, 1)  # cache is {2=1}
    lRUCache2.put(3, 2)  # cache is {2=1, 3=2}
    assert lRUCache2.get(3) == 2     # return 2
    assert lRUCache2.get(2) == 1     # return 1
    lRUCache2.put(4, 3)  # LRU key was 3, evicts key 3, cache is {2=1, 4=3}
    assert lRUCache2.get(2) == 1     # return 1 (expected), not -1
    assert lRUCache2.get(3) == -1    # return -1 (not found)
    assert lRUCache2.get(4) == 3     # return 3
    
    print("All test cases passed!")