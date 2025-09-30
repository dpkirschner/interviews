"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        results = []
        visited = set()
        path = [0]
        self.dfs(0, graph, visited, path, results)
        return results
    
    def dfs(self, index, graph, visited, path, results):
        if index == len(graph) - 1:
            results.append(path[:])
            return
        
        if index in visited:
            return
        visited.add(index)

        for neighbor in graph[index]:
            if neighbor in visited:
                continue
            path.append(neighbor)
            self.dfs(neighbor, graph, visited, path, results)
            path.pop()
        visited.remove(index)





def test_all_paths_source_target():
    solution = Solution()

    test_cases = [
        {
            'input': [[1,2],[3],[3],[]],
            'expected': [[0,1,3],[0,2,3]]
        },
        {
            'input': [[4,3,1],[3,2,4],[3],[4],[]],
            'expected': [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        }
    ]

    for i, test_case in enumerate(test_cases):
        result = solution.allPathsSourceTarget(test_case['input'])

        # Sort both result and expected for comparison since order doesn't matter
        result_sorted = sorted([sorted(path) for path in result])
        expected_sorted = sorted([sorted(path) for path in test_case['expected']])

        if result_sorted == expected_sorted:
            print(f"PASS - Input: {test_case['input']}, Output: {result}")
        else:
            print(f"FAIL - Input: {test_case['input']}, Expected: {test_case['expected']}, Got: {result}")

if __name__ == "__main__":
    test_all_paths_source_target()

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
