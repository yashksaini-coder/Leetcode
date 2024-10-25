class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Set<Integer> childrenSet = new HashSet<>();
        Map<Integer, int[]> childrenHashmap = new HashMap<>();

        for (int[] desc : descriptions) {
            int parent = desc[0];
            int child = desc[1];
            boolean isLeft = desc[2] == 1;

            childrenHashmap.putIfAbsent(parent, new int[]{-1, -1});
            childrenSet.add(child);

            if (isLeft) {
                childrenHashmap.get(parent)[0] = child;
            } else {
                childrenHashmap.get(parent)[1] = child;
            }
        }

        int headNodeVal = 0;
        for (int parent : childrenHashmap.keySet()) {
            if (!childrenSet.contains(parent)) {
                headNodeVal = parent;
                break;
            }
        }

        return constructTree(headNodeVal, childrenHashmap);
    }

    private TreeNode constructTree(int curNodeVal, Map<Integer, int[]> childrenHashmap) {
        TreeNode newNode = new TreeNode(curNodeVal);
        if (childrenHashmap.containsKey(curNodeVal)) {
            int[] children = childrenHashmap.get(curNodeVal);
            if (children[0] != -1) {
                newNode.left = constructTree(children[0], childrenHashmap);
            }
            if (children[1] != -1) {
                newNode.right = constructTree(children[1], childrenHashmap);
            }
        }
        return newNode;
    }
}