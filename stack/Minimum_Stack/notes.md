### Time Complexity
- O(1) for `push`, `pop`, `top`, and `getMin` operations.

### Space Complexity
- O(n), where n is the number of elements in the stack.

### Pattern
- Stack (Augmented Data Structure)

#### Notes
- The key is to store extra information with each element to make `getMin` efficient.
- The stack stores tuples of `(value, current_minimum)`.
- When a new element is pushed, we calculate the new minimum by comparing the new value with the current minimum (`min(new_val, current_min)`).
- This ensures that retrieving the minimum value is always a constant-time O(1) operation, as it's stored with the top element.
