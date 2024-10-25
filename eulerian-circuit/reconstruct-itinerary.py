import collections
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        graph = collections.defaultdict(list)

        for a, b in tickets:
            graph[a].append(b)

        for u in graph:
            heapq.heapify(graph[u])

        def dfs(u: str) -> None:
            while u in graph and graph[u]:
                dfs(heapq.heappop(graph[u]))
            ans.append(u)

        dfs('JFK')
        return ans[::-1]