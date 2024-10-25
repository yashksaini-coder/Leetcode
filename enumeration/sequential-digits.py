class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    result.append(num)
        return sorted(result)
