"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import heapq
class MedianFinder(object):

    def __init__(self):
        self.larger_side = []
        self.smaller_side = []
        self.size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.size == 0:
            heapq.heappush(self.smaller_side, -num)
        elif self.size == 1:
            if len(self.smaller_side) == 1:
                if num < -self.smaller_side[0]:
                    heapq.heappush(self.larger_side, -heapq.heappop(self.smaller_side))
                    heapq.heappush(self.smaller_side, -num)
                else:
                    heapq.heappush(self.larger_side, num)
            else:
                if num > self.larger_side[0]:
                    heapq.heappush(self.smaller_side, -heapq.heappop(self.larger_side))
                    heapq.heappush(self.smaller_side, -num)
                else:
                    heapq.heappush(self.larger_side, num)
        else:
            if len(self.smaller_side) == 0 or num <= -self.smaller_side[0]:
                heapq.heappush(self.smaller_side, -num)
            else:
                heapq.heappush(self.larger_side, num)
        
        if abs(len(self.larger_side) - len(self.smaller_side)) >= 2:
            if len(self.larger_side) > len(self.smaller_side):
                heapq.heappush(self.smaller_side, -heapq.heappop(self.larger_side))
            else:
                heapq.heappush(self.larger_side, -heapq.heappop(self.smaller_side))
    
        self.size += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.size == 1:
            if len(self.smaller_side) == 1:
                return -self.smaller_side[0]
            else:
                return self.larger_side[0]
        if self.size % 2 == 0:
            return (-self.smaller_side[0] + self.larger_side[0]) / 2
        return -self.smaller_side[0] if len(self.smaller_side) > len(self.larger_side) else self.larger_side[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def test_solution():
    # Test cases from problem examples
    test_cases = [
        {
            'operations': ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            'values': [[], [1], [2], [], [3], []],
            'expected': [None, None, None, 1.5, None, 2.0]
        }
    ]

    for i, test in enumerate(test_cases, 1):
        operations = test['operations']
        values = test['values']
        expected = test['expected']

        medianFinder = None
        results = []

        for j, (op, val) in enumerate(zip(operations, values)):
            if op == "MedianFinder":
                medianFinder = MedianFinder()
                results.append(None)
            elif op == "addNum":
                medianFinder.addNum(val[0])
                results.append(None)
            elif op == "findMedian":
                result = medianFinder.findMedian()
                results.append(result)

        status = 'PASS' if results == expected else 'FAIL'
        print(f"Test {i}: {status}")
        print(f"Operations: {operations}")
        print(f"Values: {values}")
        print(f"Output: {results}")
        print(f"Expected: {expected}")
        print()

if __name__ == "__main__":
    test_solution()