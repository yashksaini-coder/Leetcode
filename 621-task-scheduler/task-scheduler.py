import heapq
from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        
        task_counts = Counter(tasks)
        max_heap = [(-count, task) for task, count in task_counts.items()]
        heapq.heapify(max_heap)
        
        cycles = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    count, task = heapq.heappop(max_heap)
                    if count + 1 < 0:
                        temp.append((count + 1, task))
                cycles += 1
                if not max_heap and not temp:
                    break
            for item in temp:
                heapq.heappush(max_heap, item)
        
        return cycles
