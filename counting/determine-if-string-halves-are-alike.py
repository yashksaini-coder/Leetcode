class Solution:
    def halvesAreAlike(self, s):
        def count_vowels(string):
            vowels = set('aeiouAEIOU')
            return sum(1 for char in string if char in vowels)

        n = len(s)
        mid = n // 2
        first_half = s[:mid]
        second_half = s[mid:]

        return count_vowels(first_half) == count_vowels(second_half)

# Example usage:
solution = Solution()
print(solution.halvesAreAlike("book"))  # Output: True
print(solution.halvesAreAlike("textbook"))  # Output: False
