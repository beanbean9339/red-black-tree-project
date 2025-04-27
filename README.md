# Red-Black Tree Implementation in Python

## Overview

This project implements a Red-Black Tree (RBT) in Python, a type of self-balancing binary search tree.  
Red-Black Trees maintain approximate balance using color properties and rotation rules, ensuring O(log n) time complexity for key operations.

Implemented functionalities:
- `insert(value)` - Insert a value into the tree
- `delete(value)` - Remove a value from the tree
- `search(value)` - Search for a value in the tree
- `traverse()` - In-order tree traversal

---

## Files

- `rbtree.py` — Contains the Red-Black Tree class and methods.
- `performance.py` — Scripts for measuring and comparing performance with other trees (optional).

---

## Performance Analysis

| Operation  | Time Complexity |
|------------|-----------------|
| Insertion  | O(log n)         |
| Deletion   | O(log n)         |
| Searching  | O(log n)         |

Compared With:
- **AVL Trees**: Slightly faster lookups, but more rotations.
- **Unbalanced Binary Search Trees (BST)**: May degrade to O(n) on sorted input.

### Observations:
- Red-Black Trees require fewer rotations than AVL trees during insertions and deletions.
- They maintain balance efficiently without the overhead of AVL strictness.

### Hypothetical Performance Table:

| Input Size | RBT Insert Time | RBT Search Time | AVL Insert Time | AVL Search Time | BST Insert Time | BST Search Time |
|------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| 1,000      | ~0.003s          | ~0.002s          | ~0.004s          | ~0.002s          | ~0.002s          | ~0.01s           |
| 10,000     | ~0.03s           | ~0.02s           | ~0.04s           | ~0.02s           | ~0.02s           | ~0.12s           |
| 100,000    | ~0.3s            | ~0.2s            | ~0.4s            | ~0.2s            | ~0.2s            | ~1.2s            |

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/red_black_tree.git
cd red_black_tree
