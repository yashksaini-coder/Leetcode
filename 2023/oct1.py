class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()  # Split the sentence into words
        reversed_words = [word[::-1] for word in words]  # Reverse each word
        return ' '.join(reversed_words)  # Join the reversed words with whitespace

# Test cases
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))  # Output: "s'teL ekat edoCteeL tsetnoc"
print(solution.reverseWords("God Ding"))  # Output: "doG gniD"
