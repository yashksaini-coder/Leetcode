class CustomStack {
    private int n;
    private Stack<Integer> stack;
    private List<Integer> inc;

    public CustomStack(int n) {
        this.n = n;
        this.stack = new Stack<>();
        this.inc = new ArrayList<>();
    }

    public void push(int x) {
        if (stack.size() < n) {
            stack.push(x);
            inc.add(0);
        }
    }

    public int pop() {
        if (stack.isEmpty()) return -1;
        if (inc.size() > 1) inc.set(inc.size() - 2, inc.get(inc.size() - 2) + inc.get(inc.size() - 1));
        return stack.pop() + inc.remove(inc.size() - 1);
    }

    public void increment(int k, int val) {
        if (!stack.isEmpty()) {
            int index = Math.min(k, inc.size()) - 1;
            inc.set(index, inc.get(index) + val);
        }
    }
}