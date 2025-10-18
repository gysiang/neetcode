### Time Complexity
- O(log m*n)

### Pattern
- Binary Search

#### Notes
- Low = 0, = high (no of rows * no of elements in each row)
- use the mid index to get the value in the matrix, matrix[mid // items in each row][mid % items in each row]
- then use the standard binary search pattern
