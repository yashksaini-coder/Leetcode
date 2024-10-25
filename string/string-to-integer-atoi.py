class Solution(object):
    def myAtoi(self, s):
        # Remove leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0
        
        sign = 1  # Initialize the sign to positive
        
        if s[0] in ('+', '-'):
            # If the first character is a sign, update it and remove it from the string
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        # Initialize the result and iterate through the characters
        result = 0
        for char in s:
            if char.isdigit():
                # If the character is a digit, update the result
                result = result * 10 + int(char)
            else:
                # If the character is not a digit, break the loop
                break
        
        # Apply sign and clamp to the 32-bit integer range
        result = sign * result
        result = max(min(result, 2**31 - 1), -2**31)
        
        return result
