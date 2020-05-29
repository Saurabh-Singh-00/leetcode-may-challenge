from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        for pair in prerequisites:
            graph[pair[0]].add(pair[1])
        in_degree = [0]*numCourses
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
        queue, count = [], 0
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            count += 1
        if count == numCourses:
            return True
        return False


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
