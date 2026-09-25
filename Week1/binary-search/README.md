## Problem
an array of numbers sorted in ascending order and a target number, and find the index of that target number in the array. If the number is not in the array, the program must return `-1`.

## Approach
1. Set two pointers: `left` to the beginning of the array (index 0) and `right` to the end of the array (index `len(nums) - 1`).
2. Start a `while left <= right` loop.
3. Find the index of the middle: `mid = left + (right - left) // 2`.
4. Compare the number in the middle, `nums[mid]`, with our `target`.
5. If they are equal, return `mid`.
6. If `nums[mid] < target`, then the number we’re looking for is to the right. Shift the left boundary: `left = mid + 1`.
7. If `nums[mid] > target`, the number is to the left. Shift the right boundary: `right = mid - 1`.
8. If the loop has ended and the number hasn’t been found, return `-1`.
   
## Time Complexity
**Time Complexity:** O(log n)
*Explanation:* On each iteration of the loop, the algorithm discards half of the remaining elements. Thus, the number of checks grows logarithmically with respect to the array size `n`, which makes the search incredibly fast.

## Space Complexity
**Space Complexity:** O(1)
*Explanation:* The algorithm uses only three additional integer variables (`left`, `right`, `mid`) to store indices. Regardless of the size of the input array, the amount of additional memory does not increase.

## Reflection / Improvement
This solution is already the most efficient one for the search. Initially, the problem could have been solved using a simple brute-force approach (a `for` loop), but then the complexity would have been O(n). Using binary search (O(log n)) is a necessary improvement for this problem.
