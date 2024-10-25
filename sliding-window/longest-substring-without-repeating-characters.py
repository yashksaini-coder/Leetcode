class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Create a dictionary to store the last index where each character appeared
        char_index = {}
        max_length = 0  # Initialize the maximum length of substring
        start = 0       # Initialize the start of the current substring

        for end, char in enumerate(s):
            # If the character is already in the dictionary and its last index is after the start of the current substring,
            # update the start of the substring to be one position after the last index of the character.
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            # Update the last index of the character in the dictionary.
            char_index[char] = end

            # Update the maximum length if the current substring is longer.
            max_length = max(max_length, end - start + 1)

        return max_length
