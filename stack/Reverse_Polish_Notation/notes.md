### Time Complexity
- O(n), where n is the number of tokens in the list. The algorithm iterates through the list once.

### Space Complexity
- O(n). In the worst-case scenario (an input with many numbers before operators), the stack could hold a number of elements proportional to the input size.

### Pattern
- Stack

#### Notes
- The algorithm uses a stack to evaluate the expression. Numbers are pushed onto the stack.
- When an operator is encountered, the top two numbers are popped, the operation is performed, and the result is pushed back onto the stack.
- The order of operations is crucial, especially for subtraction and division (e.g., `left - right`).
- Python's `int()` function truncates floats towards zero, which is the behavior required for division in this problem (e.g., `int(13 / 5)` is `2`, and `int(-13 / 5)` is `-2`).
