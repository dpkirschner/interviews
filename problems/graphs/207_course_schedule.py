"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        requirements = [[] for _ in range(numCourses)] # courses that need to be finished before this one
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            requirements[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        while queue:
            current = queue.popleft()
            for requirement in requirements[current]:
                in_degree[requirement] -= 1
                if in_degree[requirement] == 0:
                    queue.append(requirement)
        
        return not any([i for i in range(numCourses) if in_degree[i] > 0])




def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_207():
    solution = Solution()

    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[1,0]]
    expected1 = True
    actual1 = solution.canFinish(numCourses1, prerequisites1)
    run_test("Test 1", "numCourses = 2, prerequisites = [[1,0]]", expected1, actual1)

    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[1,0],[0,1]]
    expected2 = False
    actual2 = solution.canFinish(numCourses2, prerequisites2)
    run_test("Test 2", "numCourses = 2, prerequisites = [[1,0],[0,1]]", expected2, actual2)


if __name__ == "__main__":
    test_207()