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
        requirements = [[] for _ in range(numCourses)] # the things that I am blocking
        in_degree = [0] * numCourses # the number of things that I'm blocked by
        for course, prereq in prerequisites:
            requirements[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i, val in enumerate(in_degree) if val == 0])
        result = []
        while queue:
            current = queue.popleft() # someone who isn't blocked by anyone
            result.append(current)

            for i in requirements[current]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

        if any([i for i, val in enumerate(in_degree) if val > 0]):
            return []

        return result


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
    actual2 = solution.findOrder(numCourses2, prerequisites2)
    run_test("Test 2", "numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]", expected2, actual2)

    # Test case 3
    numCourses3 = 1
    prerequisites3 = []
    expected3 = [0]
    actual3 = solution.findOrder(numCourses3, prerequisites3)
    run_test("Test 3", "numCourses = 1, prerequisites = []", expected3, actual3)


if __name__ == "__main__":
    test_210()