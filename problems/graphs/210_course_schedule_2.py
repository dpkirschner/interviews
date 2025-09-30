"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # things I'm blocking -> next items on the queue
        # how many things are blocking me -> am i ready to go on the queue?

        requirements = [[] for _ in range(numCourses)] # the things that I am blocking
        in_degree = [0] * numCourses # the number of things that I'm blocked by
        for course, prereq in prerequisites:
            requirements[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i, degree in enumerate(in_degree) if degree == 0])
        seen = set()
        results = []
        while queue:
            node = queue.popleft()
            if node in seen:
                continue
            seen.add(node)
            results.append(node)
            for neighbor in requirements[node]:
                if neighbor in seen:
                    continue
                in_degree[neighbor] -= 1
                if in_degree[neighbor] <= 0:
                    queue.append(neighbor)
        return results

    def findOrder2(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        graph = [[] for _ in prerequisites]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        WHITE, GREY, BLACK = 0, 1, 2 # unseen, in progress, finished
        colors = [WHITE] * numCourses
        results = []
        def dfs(index):
            if colors[index] == GREY:
                return False # cycle detected
            if colors[index] == BLACK:
                return True # end of path is already completed
            
            colors[index] = GREY
            for neighbor in graph[index]:
                if not dfs(neighbor):
                    return False
            colors[index] = BLACK
            results.append(index)
            return True
        
        for index, value in enumerate(graph):
            if not dfs(index):
                return []
        
        return results[::-1]
        
        

        
            

def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_210():
    solution = Solution()

    # Test case 1
    # numCourses1 = 2
    # prerequisites1 = [[1,0]]
    # expected1 = [0,1]
    # actual1 = solution.findOrder(numCourses1, prerequisites1)
    # run_test("Test 1", "numCourses = 2, prerequisites = [[1,0]]", expected1, actual1)

    # Test case 2
    numCourses2 = 4
    prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
    expected2 = [0,2,1,3]
    actual2 = solution.findOrder2(numCourses2, prerequisites2)
    run_test("Test 2", "numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]", expected2, actual2)

    # Test case 3
    numCourses3 = 1
    prerequisites3 = []
    expected3 = [0]
    actual3 = solution.findOrder2(numCourses3, prerequisites3)
    run_test("Test 3", "numCourses = 1, prerequisites = []", expected3, actual3)


if __name__ == "__main__":
    test_210()