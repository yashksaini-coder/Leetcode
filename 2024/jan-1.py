class Solution:
    def findContentChildren(self, g, s):
        # Sort the greed factors and cookie sizes in ascending order
        g.sort()
        s.sort()

        content_children = 0
        i, j = 0, 0

        while i < len(g) and j < len(s):
            # If the current cookie size is sufficient for the current child's greed factor
            if s[j] >= g[i]:
                content_children += 1
                i += 1  # Move to the next child
            j += 1  # Move to the next cookie

        return content_children

# Example usage:
solution = Solution()
print(solution.findContentChildren([1, 2, 3], [1, 1]))  # Output: 1
print(solution.findContentChildren([1, 2], [1, 2, 3]))    # Output: 2
