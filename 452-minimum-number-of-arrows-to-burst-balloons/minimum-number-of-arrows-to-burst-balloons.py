class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Sort balloons based on end points
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        # Iterate through balloons and count arrows needed
        for start, x_end in points:
            if start > end:
                arrows += 1
                end = x_end
        
        return arrows
