import java.util.*;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        final String start = "0000";
        
        if (deadSet.contains(start) || deadSet.contains(target)) {
            return -1;
        }
        
        queue.offer(start);
        visited.add(start);
        int turns = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            for (int i = 0; i < size; i++) {
                String current = queue.poll();
                
                if (current.equals(target)) {
                    return turns;
                }
                
                List<String> neighbors = getNeighbors(current);
                for (String neighbor : neighbors) {
                    if (!visited.contains(neighbor) && !deadSet.contains(neighbor)) {
                        queue.offer(neighbor);
                        visited.add(neighbor);
                    }
                }
            }
            
            turns++;
        }
        
        return -1; // Target not reachable
    }
    
    private List<String> getNeighbors(String code) {
        List<String> neighbors = new ArrayList<>();
        char[] digits = code.toCharArray();
        
        for (int i = 0; i < digits.length; i++) {
            char original = digits[i];
            
            // Increment digit
            digits[i] = (char) ((digits[i] - '0' + 1) % 10 + '0');
            neighbors.add(new String(digits));
            
            // Decrement digit
            digits[i] = original == '0' ? '9' : (char) (original - 1);
            neighbors.add(new String(digits));
            
            // Restore original digit
            digits[i] = original;
        }
        
        return neighbors;
    }
}
