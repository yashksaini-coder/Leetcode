class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def is_palindrome(word):
            return word == word[::-1]

        for word in words:
            if is_palindrome(word):
                return word

        return ""
