class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a dictionary to count the occurrences of each number
        num_counts = {}
        
        # Count the occurrences of each number
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        
        # Calculate the number of good pairs
        good_pairs = 0
        for count in num_counts.values():
            good_pairs += count * (count - 1) // 2
        
        return good_pairs

# Test cases
solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # Output: 4
print(solution.numIdenticalPairs([1, 1, 1, 1]))        # Output: 6
print(solution.numIdenticalPairs([1, 2, 3]))           # Output: 0
