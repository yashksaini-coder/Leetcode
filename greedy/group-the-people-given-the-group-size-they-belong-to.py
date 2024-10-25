class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups = {}  # Dictionary to store groups
        result = []  # List to store the final result

        # Iterate through the groupSizes array
        for i, size in enumerate(groupSizes):
            if size in groups:
                # Add the person to an existing group of the same size
                groups[size].append(i)
            else:
                # Create a new group for this size
                groups[size] = [i]

            # If the current group is full, add it to the result and reset it
            if len(groups[size]) == size:
                result.append(groups[size])
                del groups[size]

        return result
