# Takeaways: BST, TreeMap, and AVL

## 1. Binary Search Tree (BST)

### Key Characteristics
- **Structure**: A binary tree where each node has up to two children.
- **Ordering Invariant**: For any node:
  - Keys in the left subtree are **less** than the node's key.
  - Keys in the right subtree are **greater** than the node's key.
- **Operations Complexity**: 
  - Average case for search, insert, and delete: **O(log n)**.
  - Worst case (a skewed tree): **O(n)**.

### Common Operations
- **Insert**: Traverse down the tree to find the correct leaf position for the new key.
- **Search**: Recursively move left or right depending on whether the search key is smaller or greater than the node’s key.
- **Delete**: 
  - If the node has no children: remove it directly.
  - If the node has one child: replace it with its child.
  - If the node has two children: replace it with its inorder successor or predecessor, then remove that successor/predecessor’s original node.

### Example (Placeholder for code)
```python
def insert(node, key):
    if node is None:
        return TreeNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
```

---

## 2. TreeMap

### Concept
- A **Map** data structure (key-value pairs) that always keeps the keys in **sorted order**.
- Typically backed by a self-balancing BST (like a Red-Black Tree) to ensure efficient lookups, insertions, and deletions.

### Key Features
- **Sorted Keys**: Keys are maintained in ascending order.
- **Efficient Lookups**: Operations like `get`, `put`, and `remove` run in O(log n) on average for balanced trees.
- **Range Queries**: Easy to perform operations like `subMap`, `headMap`, and `tailMap` if the implementation provides them.

### Example (Placeholder for code)
```python
from sortedcontainers import SortedDict
tree_map = SortedDict()
tree_map[10] = "Ten"
tree_map[5] = "Five"
print(tree_map)  # {5: 'Five', 10: 'Ten'}
```

---

## 3. AVL Tree

### What is an AVL Tree?
- A self-balancing Binary Search Tree.
- **Balance Condition**: For every node, the heights of the left and right subtrees differ by at most 1.
- Ensures that operations remain **O(log n)** in the worst case.

### How It Works
- After every insertion or deletion, the tree checks the **balance factor** of affected nodes.
- If the tree is unbalanced, it performs **rotations** to restore balance.
- **Rotations**:
  - **Right Rotation (RR)**: Fixes left-heavy trees.
  - **Left Rotation (LL)**: Fixes right-heavy trees.
  - **Left-Right (LR)** and **Right-Left (RL)** Rotations: Fix scenarios where a subtree is heavy in the opposite direction.

### Balance Factor
- Defined as `height(left_subtree) - height(right_subtree)`.
- Must be **-1, 0, or 1** in a balanced AVL tree.

### Example of Insertion with Balancing
```python
def insert(node, key):
    # Normal BST insert
    if not node:
        return AVLNode(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        # Duplicate keys not allowed or update value if needed
        return node

    # Update height
    node.height = 1 + max(height(node.left), height(node.right))

    # Check balance and rotate if needed
    balance = get_balance(node)
    if balance > 1 and key < node.left.key:  # LL Case
        return rotate_right(node)
    if balance < -1 and key > node.right.key: # RR Case
        return rotate_left(node)
    if balance > 1 and key > node.left.key: # LR Case
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and key < node.right.key: # RL Case
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node
```

---

## Use Cases and Trade-offs

- **BST**:
  - Simple to implement.
  - Performance degrades if the tree becomes skewed (like a linked list).

- **TreeMap**:
  - Provides sorted key-value pairs.
  - Backed by a balanced tree (e.g., Red-Black Tree), it ensures good performance for large datasets.
  - Ideal for scenarios requiring sorted maps and range queries.

- **AVL Tree**:
  - More strictly balanced than Red-Black Trees.
  - Guarantees O(log n) complexity even in the worst case.
  - Slightly more complex insertions/deletions due to rotations.

---

## Summary

- **BST**: A fundamental data structure for maintaining keys in a tree with efficient average operations.
- **TreeMap**: A sorted map typically backed by a self-balancing BST for consistent O(log n) access and ordered key retrieval.
- **AVL**: A type of self-balancing BST that ensures strict height balance for guaranteed performance.

All these structures rely on tree-based logic and ordering invariants to provide efficient data operations. The key difference lies in how well the tree remains balanced, which affects worst-case performance. AVL trees and Red-Black Trees power the efficiency behind TreeMap implementations.