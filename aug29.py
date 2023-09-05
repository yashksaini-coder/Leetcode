class Solution:
    def minimumCustomers(self, customers: str) -> int:
        n = len(customers)
        
        def calculate_penalty(closing_hour):
            penalty = 0
            for i in range(n):
                if (i < closing_hour and customers[i] == 'N') or (i >= closing_hour and customers[i] == 'Y'):
                    penalty += 1
            return penalty
        
        left, right = 0, n  # Initialize the search space
        
        while left < right:
            mid = (left + right) // 2
            penalty_mid = calculate_penalty(mid)
            penalty_mid_plus_one = calculate_penalty(mid + 1)
            
            if penalty_mid > penalty_mid_plus_one:
                left = mid + 1
            else:
                right = mid
        
        return left

# Example usage:
solution = Solution()
customers = "YYNY"
print(solution.minimumCustomers(customers))  # Output: 2
