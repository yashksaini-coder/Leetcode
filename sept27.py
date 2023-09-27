class Solution:
    def decodeAtIndex(self, inputString: str, k: int) -> str:
        decoded_length = 0  # Total length of the decoded string

        for char in inputString:
            if char.isdigit():
                # If the character is a digit, update the decoded length accordingly
                decoded_length *= int(char)
            else:
                # If the character is a letter, increment the decoded length
                decoded_length += 1

        # Traverse the input string in reverse to decode and find the kth character
        for i in range(len(inputString) - 1, -1, -1):
            current_char = inputString[i]

            if current_char.isdigit():
                # If the character is a digit, adjust the length and k accordingly
                decoded_length //= int(current_char)
                k %= decoded_length
            else:
                # If the character is a letter, check if it's the kth character
                if k == 0 or decoded_length == k:
                    return current_char  # Return the kth character as a string

                decoded_length -= 1

        return ""  # Return an empty string if no character is found


solution = Solution()

# Test case 1
# The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".
print(solution.decodeAtIndex("leet2code3", 10))  # Output: "o"

# Test case 2
# The decoded string is "hahahaha".
# The 5th letter is "h".
print(solution.decodeAtIndex("ha22", 5))  # Output: "h"

# Test case 3
# The decoded string is "a" repeated 8301530446056247680 times.
# The 1st letter is "a".
print(solution.decodeAtIndex("a2345678999999999999999", 1))  # Output: "a"

# Test case 4
# The decoded string is "abcde".
# The 8th letter is "e".
print(solution.decodeAtIndex("abcde", 8))  # Output: "e"

# Test case 5
# The decoded string is "abacabadabacabaeabacabadabacabaf".
# The 24th letter is "e".
print(solution.decodeAtIndex("abacabadabacabaeabacabadabacabaf", 24))  # Output: "e"
