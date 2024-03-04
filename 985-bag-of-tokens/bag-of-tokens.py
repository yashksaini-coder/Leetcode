class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()  # Sort the tokens in ascending order
        left, right = 0, len(tokens) - 1
        score = 0
        max_score = 0
        
        while left <= right:
            # Try to play face-up
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            # Try to play face-down
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        
        return max_score
