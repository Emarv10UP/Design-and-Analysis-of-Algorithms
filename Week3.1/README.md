1. Problem: Merge two sorted singly-linked lists into a single sorted list in-place and return its head.
2. Approach: Use a dummy node and a tail pointer. Compare the head values of both lists and attach the smaller node to tail.next. Then, advance that list's pointer and tail. Once one list becomes empty, attach the remaining nodes of the other list directly.
Written tracing:
list1 = [1, 2, 4]
list2 = [1, 3, 4]
Init: dummy -> None, tail -> dummy
Step 1: 1 ≤ 1 → attach list1 (1), advance list1 to 2.
List: [1]
Step 2: $2 > 1$: Attach list2 (1); advance list2 to 3.
List: [1, 1]
Step 3: $2 ≤ 3 → attach list1 (2), advance list1 to 4. List: [1, 1, 2]
Step 4: $4 > 3$: Attach list2 (3), and advance list2 to 4. List: [1, 1, 2, 3]
Step 5: $4 ≤ 4 → attach list1 (4), advance list1 to None. List: [1, 1, 2, 3, 4]
Post-loop: List1 is None. Attach the rest of List2 (4). Result: [1, 1, 2, 3, 4, 4]
3. Time complexity: O(n + m). Each step advances at least one list pointer. We visit a total of at most n + m nodes.
4. Space complexity: O(1).
Operates in place by updating pointer references without allocating new nodes.
5. Reflection/improvement: Is there a more efficient approach? No. Every node must be inspected at least once. ($O(n+m)$ time and $O(1)$ space are optimal.)
What would you need to change? A recursive solution could be used to shorten the code.
What complexity could the improved solution achieve? Recursion keeps $O(n+m)$ time complexity, but it increases the space complexity to $O(n+m)$ due to the call stack.
