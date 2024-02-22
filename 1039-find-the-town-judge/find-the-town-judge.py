class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Create an array to keep track of incoming and outgoing trusts
        trust_count = [0] * (n + 1)
        
        # Iterate through the trust relationships
        for a, b in trust:
            trust_count[a] -= 1  # a trusts someone
            trust_count[b] += 1  # b is trusted by someone
            
        # Check for the town judge
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        
        return -1
