### Time Complexity
- O(n), where n is the number of nodes in the linked list. The algorithm iterates through the list once.

### Space Complexity
- O(1). The reversal is done in-place using a constant number of pointers.

### Pattern
- Linked List / Two Pointers

#### Notes
- This is an iterative solution that uses three pointers: `previous`, `current`, and `next_node`.
- `previous` starts as `None` because the original head's new `next` will be `None`.
- In each step of the loop:
  1. Save the next node: `next_node = current.next`.
  2. Reverse the pointer: `current.next = previous`.
  3. Move the pointers one step forward: `previous = current` and `current = next_node`.
- The new head of the reversed list is the final value of `previous`.
