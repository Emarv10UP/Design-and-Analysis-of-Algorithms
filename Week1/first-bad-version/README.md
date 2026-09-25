# First Bad Version

## Problem
There are $n$ versions of a product (from 1 to $n$). Starting with a certain version, all subsequent versions are defective. Find the number of the first defective version using the minimum number of calls to the API `isBadVersion(version)`.

## Approach
We use binary search with correctly adjusted boundaries:
1. Set `left = 1` and `right = n`.
2. In a `while left < right` loop, find `mid = left + (right - left) // 2`.
3. If `isBadVersion(mid)` returns `True`, set `right = mid` (the first error is at `mid` or to the left).
4. If `False`, set `left = mid + 1` (the error is strictly to the right).
5. Upon completing the loop, return `left`.

## Time Complexity
**Time Complexity:** $O(\log n)$
The search range is halved at each step, requiring no more than $\log_2 n$ checks.

## Space Complexity
**Space Complexity:** $O(1)$
A fixed amount of memory is used to store three variables (`left`, `right`, `mid`).

## Reflection / Improvement
To avoid an infinite loop (hang), the condition `while left <= right` is replaced with the stricter `while left < right`, and the boundaries are shifted using `left = mid + 1` and `right = mid`. This guarantees exact convergence to the answer.
