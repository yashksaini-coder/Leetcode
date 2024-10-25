class MyCircularDeque {
    private int[] v;
    private int front, back, size, capacity;

    public MyCircularDeque(int k) {
        v = new int[k];
        Arrays.fill(v, -1);
        front = 0;
        back = 0;
        size = 0;
        capacity = k;
    }

    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }

        if (front == 0) {
            front = capacity - 1;
        } else {
            front--;
        }

        v[front] = value;
        size++;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }

        v[back] = value;

        if (back == capacity - 1) {
            back = 0;
        } else {
            back++;
        }

        size++;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }

        v[front] = -1;

        if (front == capacity - 1) {
            front = 0;
        } else {
            front++;
        }

        size--;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }

        if (back == 0) {
            back = capacity - 1;
        } else {
            back--;
        }
        v[back] = -1;

        size--;
        return true;
    }

    public int getFront() {
        if (isEmpty()) {
            return -1;
        }
        return v[front];
    }

    public int getRear() {
        if (isEmpty()) {
            return -1;
        }
        if (back == 0) {
            return v[capacity - 1];
        } else {
            return v[back - 1];
        }
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }
}
