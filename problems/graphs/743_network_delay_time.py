"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all n nodes to receive the signal. If it is impossible for all nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation: We start at node 2, and from node 2 we can reach node 1 (time 1) and node 3 (time 1). From node 3, we can reach node 4 (time 1). So it takes 2 time units for all nodes to receive the signal.

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Explanation: We start at node 1 and can reach node 2 in 1 time unit.

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: We start at node 2, but node 1 is unreachable.

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)



build a graph of nodes -> connections
keep a stack of (total cost, current node)
for each neighbor, if its better use it. if not dump it.

if any value isn't solid, return -1, or the max value
"""
import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = []
            graph[time[0]].append((time[2], time[1]))
        best = [float('inf')] * (n + 1)

        visited = set()
        best[k] = 0
        heap = [(0, k)]
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_node in visited:
                continue
            visited.add(current_node)
            if current_node not in graph: # no outgoing edges
                continue
            for distance, neighbor in graph[current_node]:
                best[neighbor] = min(best[neighbor], current_distance + distance)
                if neighbor not in visited:
                    heapq.heappush(heap, (best[neighbor], neighbor))


        if any([i for i in range(1, len(best)) if best[i] == float('inf')]):
            return -1

        return max(best[1:])




def test_network_delay_time():
    solution = Solution()

    test_cases = [
        {
            'times': [[2,1,1],[2,3,1],[3,4,1]],
            'n': 4,
            'k': 2,
            'expected': 2
        },
        {
            'times': [[1,2,1]],
            'n': 2,
            'k': 1,
            'expected': 1
        },
        {
            'times': [[1,2,1]],
            'n': 2,
            'k': 2,
            'expected': -1
        }
    ]

    for i, test_case in enumerate(test_cases):
        result = solution.networkDelayTime(test_case['times'], test_case['n'], test_case['k'])

        if result == test_case['expected']:
            print(f"PASS - Times: {test_case['times']}, N: {test_case['n']}, K: {test_case['k']}, Output: {result}")
        else:
            print(f"FAIL - Times: {test_case['times']}, N: {test_case['n']}, K: {test_case['k']}, Expected: {test_case['expected']}, Got: {result}")

if __name__ == "__main__":
    test_network_delay_time()

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
