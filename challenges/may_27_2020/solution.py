from typing import List
import collections


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if dislikes == []:
            return True
        graph = collections.defaultdict(set)
        for pairs in dislikes:
            graph[pairs[0]].add(pairs[1])
            graph[pairs[1]].add(pairs[0])
        stack = collections.deque()
        colored = collections.defaultdict(lambda: False)
        visited = collections.defaultdict(lambda: False)
        colored[dislikes[0][0]] = True
        for n in graph:
            stack.append(n)
            while len(stack):
                node = stack.pop()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        colored[neighbor] = not colored[node]
                    else:
                        if colored[neighbor] == colored[node]:
                            return False
                if not visited[node]:
                    visited[node] = True
        return True


s = Solution()
print(s.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
print(s.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]))
print(s.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
