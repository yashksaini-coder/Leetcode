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