class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        points = set()  # Use a set to store unique points

        for start, end in nums:
            for i in range(start, end + 1):
                points.add(i)  # Add all points between start and end to the set

        return len(points)  # Return the number of unique points
    