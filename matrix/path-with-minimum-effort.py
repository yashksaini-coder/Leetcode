class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])
        dist=[[float('inf') for j in range(n)] for i in range(m)]
        dist[0][0]=0
        pq=[(0,0,0)]
        heapify(pq)
        while pq:
            d,i,j=heappop(pq)
            if i==m-1 and j==n-1:
                return dist[m-1][n-1]
            for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=r<m and 0<=c<n:
                    t=max(abs(heights[i][j]-heights[r][c]),d)
                    if dist[r][c]>t:
                        dist[r][c]=t
                        heappush(pq,(dist[r][c],r,c))