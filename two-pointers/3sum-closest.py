class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the array in ascending order
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum

solution = Solution()
