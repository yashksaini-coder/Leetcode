class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n, cntN, cntY = len(customers), 0, 0
        prefixN, suffixY = [0], [0]
        
        for c in customers:
            cntN += (c == 'N')
            prefixN.append(cntN)
        
        for c in reversed(customers):
            cntY += (c == 'Y')
            suffixY.append(cntY)
        
        suffixY.reverse()
        
        best_hour, _ = min(enumerate(a + b for a, b in zip(prefixN, suffixY)), key=lambda x: x[1])
        
        return best_hour