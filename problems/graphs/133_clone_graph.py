"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
""""""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = deque([root])
        seen = set()
        next = {}
        while queue:
            current = queue.popleft()
            if current in seen:
                continue
            seen.add(current)
            if not current.val in next:
                next[current.val] = Node(current.val)
            for neighbor in current.neighbors:
                if neighbor not in seen:
                    queue.append(neighbor)
        
        for node in seen:
            for neighbor in node.neighbors:
                next[node.val].neighbors.append(next[neighbor.val])
        return next.get(root.val)


def create_graph_from_adjlist(adjList):
    """Helper function to create graph from adjacency list"""
    if not adjList:
        return None

    nodes = {}
    for i in range(len(adjList)):
        nodes[i + 1] = Node(i + 1)

    for i, neighbors in enumerate(adjList):
        for neighbor_val in neighbors:
            nodes[i + 1].neighbors.append(nodes[neighbor_val])

    return nodes[1] if nodes else None


def graph_to_adjlist(node):
    """Helper function to convert graph back to adjacency list"""
    if not node:
        return []

    visited = set()
    adjList = {}

    def dfs(curr):
        if curr.val in visited:
            return
        visited.add(curr.val)
        adjList[curr.val] = [neighbor.val for neighbor in curr.neighbors]
        for neighbor in curr.neighbors:
            dfs(neighbor)

    dfs(node)

    # Convert to list format
    if not adjList:
        return []

    max_val = max(adjList.keys())
    result = [[] for _ in range(max_val)]
    for val, neighbors in adjList.items():
        result[val - 1] = sorted(neighbors)

    return result


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_133():
    solution = Solution()

    # Test case 1
    adjList1 = [[2,4],[1,3],[2,4],[1,3]]
    expected1 = [[2,4],[1,3],[2,4],[1,3]]
    graph1 = create_graph_from_adjlist(adjList1)
    cloned1 = solution.cloneGraph(graph1)
    actual1 = graph_to_adjlist(cloned1)
    run_test("Test 1", "adjList = [[2,4],[1,3],[2,4],[1,3]]", expected1, actual1)

    # Test case 2
    adjList2 = [[]]
    expected2 = [[]]
    graph2 = create_graph_from_adjlist(adjList2)
    cloned2 = solution.cloneGraph(graph2)
    actual2 = graph_to_adjlist(cloned2)
    run_test("Test 2", "adjList = [[]]", expected2, actual2)

    # Test case 3
    adjList3 = []
    expected3 = []
    graph3 = create_graph_from_adjlist(adjList3)
    cloned3 = solution.cloneGraph(graph3)
    actual3 = graph_to_adjlist(cloned3)
    run_test("Test 3", "adjList = []", expected3, actual3)


if __name__ == "__main__":
    test_133()