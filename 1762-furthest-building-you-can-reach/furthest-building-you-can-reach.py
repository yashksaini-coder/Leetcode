import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        n = len(heights)
        heap = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                if ladders > 0:
                    heapq.heappush(heap, diff)
                    ladders -= 1
                elif heap and diff > heap[0]:
                    bricks -= heapq.heappop(heap)
                    heapq.heappush(heap, diff)
                else:
                    bricks -= diff

                if bricks < 0:
                    return i

        return n - 1

# Example usage:
sol = Solution()
heights1, bricks1, ladders1 = [4, 2, 7, 6, 9, 14, 12], 5, 1
heights2, bricks2, ladders2 = [4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2
heights3, bricks3, ladders3 = [14, 3, 19, 3], 17, 0

print(sol.furthestBuilding(heights1, bricks1, ladders1))  # Output: 4
print(sol.furthestBuilding(heights2, bricks2, ladders2))  # Output: 7
print(sol.furthestBuilding(heights3, bricks3, ladders3))  # Output: 3
