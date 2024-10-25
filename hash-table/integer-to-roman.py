class Solution(object):
    def intToRoman(self, num):
        roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        result = ''
        # Sort the keys in reverse order (largest to smallest)
        sorted_keys = sorted(roman_numerals.keys(), reverse=True)
        
        for key in sorted_keys:
            while num >= key:
                result += roman_numerals[key]
                num -= key
        
        return result
