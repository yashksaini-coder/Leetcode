import collections
import heapq
from typing import List

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

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    result1 = solution.findItinerary(tickets1)
    print(result1)  # Output: ["JFK","MUC","LHR","SFO","SJC"]

    # Test case 2
    tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    result2 = solution.findItinerary(tickets2)
    print(result2)  # Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
