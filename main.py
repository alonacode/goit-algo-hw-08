from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, List
import heapq


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


# Helper for building a BST (for demo/tests)
def bst_insert(root: Optional[Node], x: int) -> Node:
    if root is None:
        return Node(x)
    cur = root
    while True:
        if x < cur.value:
            if cur.left is None:
                cur.left = Node(x)
                break
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = Node(x)
                break
            cur = cur.right
    return root


def build_bst(values: Iterable[int]) -> Optional[Node]:
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root


# =====================================
# Task 1
# =====================================
def bst_min_value(root: Optional[Node]) -> Optional[int]:
    """
    Returns the minimum value (left-most) or None for an empty tree.
    Works for both AVL and regular BST: "go as far left as possible".
    Time complexity O(h), where h is the height of the tree (O(log n) for balanced, O(n) in the worst case).
    """

    if root is None:
        return None
    cur = root
    while cur.left:
        cur = cur.left
    return cur.value


# =====================================
# Task 2
# =====================================
def bst_sum(root: Optional[Node]) -> int:
    """
    Returns the sum of values in the tree. Any traversal order works.
    Below is an iterative in-order traversal to avoid deep recursion.
    Time complexity O(n), space complexity O(h).
    """
    total = 0
    stack: List[Node] = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        total += cur.value
        cur = cur.right
    return total


# Alternative (recursive):
def bst_sum_recursive(root: Optional[Node]) -> int:
    if root is None:
        return 0
    return root.value + bst_sum_recursive(root.left) + bst_sum_recursive(root.right)

# ============================================================
# Task 3
# ============================================================
def min_total_merge_cost(lengths: Iterable[int]) -> int:
    """
    Always merge the two shortest lengths (min-heap).
    Time complexity O(n log n), space complexity O(n).
    Returns the minimal possible total cost.
    """

    heap = list(lengths)
    if not heap:
        return 0
    heapq.heapify(heap)

    total_cost = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        heapq.heappush(heap, cost)
    return total_cost


# -----------------------------
# Test
# -----------------------------
if __name__ == "__main__":
    # Tree for tasks 1–2
    vals = [7, 3, 10, 1, 5, 9, 12, 0, 2, 4, 6]
    tree = build_bst(vals)

    print("Min value:", bst_min_value(tree))
    print("Sum (iter):", bst_sum(tree))
    print("Sum (recur):", bst_sum_recursive(tree))

    # Cables for task 3
    cables = [8, 4, 6, 12]
    print("Min total merge cost:", min_total_merge_cost(cables))

