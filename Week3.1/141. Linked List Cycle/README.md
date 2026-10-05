1. Problem: Determine whether a singly-linked list contains a cycle (a node that can be reached again by following the next pointers).
2. Approach: Use Floyd’s Cycle-Finding Algorithm (Two Pointers). Advance slow by one node and fast by two nodes per step. If slow == fast, a cycle exists. If fast or fast.next becomes None, then there is no cycle.
Written tracing (head = 3 → 2 → 0 → -4 → back to 2):
Init: slow = 3, fast = 3
Step 1: slow → 2, fast → 0 (slow ≠ fast)
Step 2: slow → 0, fast → 2 (slow ≠ fast)
Step 3: slow → -4, fast → -4 (slow = fast → cycle detected!)
3. Time Complexity
Time complexity is O(N). If there is no cycle, the fast pointer reaches the end in N/2 steps. If a cycle exists, fast catches up to slow in $O(N)$ steps.
Space complexity: $O(1)$
Only two pointer variables are used, regardless of the list size.
Reflection/improvement: Is there a more efficient approach? No. $O(N)$ time and $O(1)$ space are optimal.
What would you need to change? A hash set could store visited nodes instead.
What complexity could the improved solution achieve? A hash set keeps O(N) time but increases space complexity to O(N).
