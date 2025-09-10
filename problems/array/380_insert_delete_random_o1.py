"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""
import random

class RandomizedSet(object):

    def __init__(self):
        self.store = {} # K: val in the cache V: the index in the backing list where the val is stored
        self.backing = [] # a list of all values store in the cache.

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.store: 
            return False
        self.backing.append(val) # add to the list at the last point
        self.store[val] = len(self.backing) - 1 # store the index for retrieval
        
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.store:
            return False
        curr_index = self.store[val] # find the index where this value is stored
        last_index = len(self.backing) - 1 # find the index of the last value

        last_value = self.backing[last_index]
        self.backing[curr_index] = last_value # move the last index to the "removed" spot
        self.backing.pop() # dump the removed data thats now in the last spot
        if self.store[last_value]: 
            self.store[last_value] = curr_index
        del self.store[val] # clean the dict
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.backing)


        


def test_randomized_set():
    randomized_set = RandomizedSet()
    
    assert randomized_set.insert(1) == True
    assert randomized_set.remove(2) == False
    assert randomized_set.insert(2) == True
    result = randomized_set.getRandom()
    assert result in [1, 2]
    assert randomized_set.remove(1) == True
    assert randomized_set.insert(2) == False
    result = randomized_set.getRandom()
    assert result == 2
    
    print("All tests passed!")


if __name__ == "__main__":
    test_randomized_set()