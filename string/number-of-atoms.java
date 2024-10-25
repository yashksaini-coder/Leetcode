class Solution {
    public String countOfAtoms(String formula) {
        int n = formula.length();
        Map<String, Integer> result_counter = new HashMap<>();
        Deque<Map<String, Integer>> parenthesis_stack = new ArrayDeque<>();
        int cur_ind = 0;

        while (cur_ind < n) {
            char cur_char = formula.charAt(cur_ind);

            if (cur_char == '(') {
                cur_ind++;
                parenthesis_stack.push(new HashMap<>());
                continue;
            }

            if (cur_char == ')') {
                StringBuilder mult_str = new StringBuilder();
                cur_ind++;

                while (cur_ind < n && Character.isDigit(formula.charAt(cur_ind))) {
                    mult_str.append(formula.charAt(cur_ind));
                    cur_ind++;
                }

                int mult = mult_str.length() == 0 ? 1 : Integer.parseInt(mult_str.toString());
                Map<String, Integer> last_counter = parenthesis_stack.pop();
                Map<String, Integer> target = parenthesis_stack.isEmpty() ? result_counter : parenthesis_stack.peek();
                
                for (Map.Entry<String, Integer> entry : last_counter.entrySet()) {
                    target.put(entry.getKey(), target.getOrDefault(entry.getKey(), 0) + entry.getValue() * mult);
                }
                continue;
            }

            StringBuilder cur_elem = new StringBuilder();
            StringBuilder cur_counter_str = new StringBuilder();
            Map<String, Integer> target = parenthesis_stack.isEmpty() ? result_counter : parenthesis_stack.peek();

            while (cur_ind < n && formula.charAt(cur_ind) != '(' && formula.charAt(cur_ind) != ')') {
                if (Character.isAlphabetic(formula.charAt(cur_ind))) {
                    if (Character.isUpperCase(formula.charAt(cur_ind)) && cur_elem.length() > 0) {
                        target.put(cur_elem.toString(), target.getOrDefault(cur_elem.toString(), 0) + (cur_counter_str.length() == 0 ? 1 : Integer.parseInt(cur_counter_str.toString())));
                        cur_elem = new StringBuilder();
                        cur_counter_str = new StringBuilder();
                    }
                    cur_elem.append(formula.charAt(cur_ind));
                } else {
                    cur_counter_str.append(formula.charAt(cur_ind));
                }
                cur_ind++;
            }

            target.put(cur_elem.toString(), target.getOrDefault(cur_elem.toString(), 0) + (cur_counter_str.length() == 0 ? 1 : Integer.parseInt(cur_counter_str.toString())));
        }

        List<String> parts = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : result_counter.entrySet()) {
            parts.add(entry.getKey() + (entry.getValue() == 1 ? "" : entry.getValue()));
        }
        Collections.sort(parts);

        StringBuilder result = new StringBuilder();
        for (String part : parts) {
            result.append(part);
        }

        return result.toString();
    }
}