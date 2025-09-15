"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import deque
class GraphNode(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else {}

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = self.buildGraph(equations, values, queries)

        results = []
        for query in queries:
            path = self.findPath(graph, query[0], query[1], [])
            if path:
                results.append(self.tracePath(graph, path))
            else:
                results.append(-1.0)
        return results

    def tracePath(self, graph, path):
        total = 1
        current = None
        for index, step in enumerate(path):
            if current == None:
                current = graph[step]
                continue
            total = total * current.neighbors[step]
            current = graph[step]
        return total
    
    def findPath(self, graph, start, end, path):
        next_path = path + [start]
        if start not in graph or end not in graph:
            return None
        if start == end:
            return path
        
        for neighbor in graph[start].neighbors:
            if neighbor not in path:
                result = self.findPath(graph, neighbor, end, next_path)
                if result:
                    return result
        path.pop()
        return None
            

    def buildGraph(self, equations, values, queries):
        graph = {}
        for index, equation in enumerate(equations):
            from_node = equation[0]
            to_node = equation[1]

            if not from_node in graph:
                graph[from_node] = GraphNode(from_node)
            if not to_node in graph:
                graph[to_node] = GraphNode(to_node)

            graph[from_node].neighbors[to_node] = values[index]
            graph[to_node].neighbors[from_node] = 1 / values[index]
        return graph


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_399():
    solution = Solution()

    # Test case 1
    equations1 = [["a","b"],["b","c"]]
    values1 = [2.0,3.0]
    queries1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    expected1 = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    actual1 = solution.calcEquation(equations1, values1, queries1)
    run_test("Test 1", "equations = [['a','b'],['b','c']], values = [2.0,3.0]", expected1, actual1)

    # Test case 2
    # equations2 = [["a","b"],["b","c"],["bc","cd"]]
    # values2 = [1.5,2.5,5.0]
    # queries2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    # expected2 = [3.75000,0.40000,5.00000,0.20000]
    # actual2 = solution.calcEquation(equations2, values2, queries2)
    # run_test("Test 2", "equations = [['a','b'],['b','c'],['bc','cd']], values = [1.5,2.5,5.0]", expected2, actual2)

    # # Test case 3
    # equations3 = [["a","b"]]
    # values3 = [0.5]
    # queries3 = [["a","b"],["b","a"],["a","c"],["x","y"]]
    # expected3 = [0.50000,2.00000,-1.00000,-1.00000]
    # actual3 = solution.calcEquation(equations3, values3, queries3)
    # run_test("Test 3", "equations = [['a','b']], values = [0.5]", expected3, actual3)


if __name__ == "__main__":
    test_399()