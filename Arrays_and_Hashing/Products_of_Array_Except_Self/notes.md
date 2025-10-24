# Product of Array Except Self

## Algorithm Explanation

The problem asks us to compute an array `answer` where `answer[i]` is the product of all elements in the input array `nums` except `nums[i]`. The key constraint is to do this in O(n) time and without using the division operator.

The most efficient way to solve this is with a **two-pass approach**. The core idea is that the product except self for an element at index `i` is the product of all elements to its *left* multiplied by the product of all elements to its *right*.

`answer[i] = (product of elements left of i) * (product of elements right of i)`

We can calculate this in two separate loops or "passes" over the array.

### Pass 1: Prefix Products

1. Initialize an answer array `res` of the same size as `nums`, with all its values set to `1`.
2. Create a variable `prefix_product`, initialized to `1`.
3. Iterate through the `nums` array from left to right (from index `0` to `n-1`).
4. In each iteration `i`, first set `res[i]` to the current `prefix_product`. This stores the product of all elements to the left of `i`.
5. Then, update `prefix_product` by multiplying it with `nums[i]` to prepare for the next iteration.

After this pass, `res[i]` will correctly hold the product of all elements to the left of `i`.

### Pass 2: Suffix Products

1. Create a variable `suffix_product`, initialized to `1`.
2. Iterate through the `nums` array from right to left (from index `n-1` down to `0`).
3. In each iteration `i`, multiply the existing `res[i]` (which already contains the prefix product) by the current `suffix_product`. This completes the calculation for `res[i]`.
4. Then, update `suffix_product` by multiplying it with `nums[i]` to prepare for the next iteration.

After the second pass, the `res` array will contain the final desired products.

## Complexity Analysis

*   **Time Complexity: O(n)**. We iterate through the input array twice—once from left to right and once from right to left. Since each pass takes O(n) time, the total time complexity is O(n) + O(n) = O(2n), which simplifies to O(n).
*   **Space Complexity: O(1)** (excluding the output array). The problem statement often specifies that the space used by the output array does not count towards the space complexity. Besides the `res` array, we only use a few constant-space variables (`prefix_product`, `suffix_product`, `n`, `i`), so the auxiliary space complexity is O(1). If the output array were counted, it would be O(n).
