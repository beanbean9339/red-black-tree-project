# Red-Black Tree Implementation in Python

## Overview

This project implements a **Red-Black Tree (RBT)** in Python, along with **AVL** and **Binary Search Tree (BST)** implementations. These are all types of self-balancing binary search trees. Red-Black Trees, in particular, use color properties and rotation rules to maintain balance and ensure logarithmic time complexity for key operations.

Implemented functionalities:
- `insert(value)` - Insert a value into the tree.
- `delete(value)` - Remove a value from the tree.
- `search(value)` - Search for a value in the tree.
- `traverse()` - In-order tree traversal.

---

## Files

- `red_black_tree.py` — Contains the Red-Black Tree class and methods.
- `avl.py` — Contains the AVL Tree class and methods.
- `bst.py` — Contains the Binary Search Tree class and methods.
- `test_red_black_tree.py` — Unit tests for the Red-Black Tree implementation.
- `performance_analysis.py` — Scripts for measuring and comparing performance with other trees.

---

## Performance Analysis

### Time Complexity
| Operation  | Time Complexity |
|------------|-----------------|
| Insertion  | O(log n)        |
| Deletion   | O(log n)        |
| Searching  | O(log n)        |

---

### **Comparison with AVL Trees and Binary Search Trees (BST)**

#### Observations:
- **Red-Black Trees (RBT)**: Generally faster for insertions and deletions compared to **AVL Trees**. They require fewer rotations due to less strict balancing rules, making them more efficient for dynamic updates.
- **AVL Trees**: Maintain a stricter balance, ensuring faster search times. However, their insertion and deletion operations tend to be slower due to the overhead of maintaining balance.
- **Binary Search Trees (BST)**: Without self-balancing, **BSTs** can degrade to O(n) in the worst case (e.g., for sorted input). Search, insert, and delete operations in **BSTs** may suffer significantly when the tree becomes unbalanced.

### **Performance Measurements**

The following table presents the measured times for **Insertion**, **Search**, and **Traversal** operations across **RBT**, **AVL**, and **BST** for various input sizes:

| Input Size | RBT Insert Time  | BST Insert Time  | AVL Insert Time  | RBT Delete Time  | BST Delete Time  | AVL Delete Time  | RBT Search Time  | BST Search Time  | AVL Search Time  | RBT Traverse Time | BST Traverse Time | AVL Traverse Time |
|------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|-------------------|-------------------|-------------------|
| 100        | 0.000000 seconds | 0.001001 seconds | 0.000000 seconds | 0.000000 seconds | 0.000000 seconds | 0.000000 seconds | 0.000000 seconds | 0.000000 seconds | 0.000999 seconds | 0.000000 seconds | 0.000999 seconds | 0.000000 seconds |
| 1,000      | 0.003999 seconds | 0.002003 seconds | 0.002996 seconds | 0.003010 seconds | 0.002999 seconds | 0.003067 seconds | 0.001997 seconds | 0.002017 seconds | 0.000998 seconds | 0.000000 seconds | 0.000998 seconds | 0.000998 seconds |
| 10,000     | 0.049369 seconds | 0.023588 seconds | 0.024994 seconds | 0.019259 seconds | 0.017037 seconds | 0.017231 seconds | 0.016584 seconds | 0.032002 seconds | 0.030053 seconds | 0.017015 seconds | 0.020014 seconds | 0.014013 seconds |

---

#### **Analysis of Results:**
- **Insertion Time**:
  - **RBT** is consistently faster than both **AVL** and **BST** due to fewer rotations during balancing.
  - **AVL** has the slowest insertion times due to its strict balancing, which requires more rotations.
  
- **Search Time**:
  - **AVL** is the fastest for searches, as it is strictly balanced and ensures logarithmic height.
  - **RBT** performs slightly worse than **AVL** but better than **BST**. Its time complexity is still logarithmic, but with slightly higher constants due to the color properties.
  - **BST** is the slowest, especially as the input size increases, due to possible unbalanced structures.

- **Traversal Time**:
  - Traversal performance across all trees is similar, as they all exhibit \( O(n) \) traversal time. **RBT** and **AVL** are slightly faster than **BST** in this case due to better internal memory structures.

#### **Conclusion**:
- **Red-Black Trees** offer a good compromise between balanced performance for insertions, deletions, and searches. They are preferable when dynamic updates (insertion/deletion) are frequent.
- **AVL Trees** are the best for search-heavy applications where tree balance is crucial, but they come at the cost of more complex insertions and deletions.
- **Binary Search Trees** (BST) are the simplest but can degrade to linear time if the tree becomes unbalanced.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/beanbean9339/red-black-tree-project.git
cd red_black_tree
```

### Install dependencies (if necessary):

```bash
pip install -r requirements.txt
```
### Run the performance analysis:

```bash
python performance_analysis.py
```
## Documentation and Optimization

### Implementation Details:
- **Red-Black Trees**: Maintain balance by using properties like node color (red/black) and rotations to ensure that the height of the tree remains logarithmic.
- **AVL Trees**: Use stricter balancing rules, requiring height balancing for each node after insertions and deletions.
- **Binary Search Trees**: Lack self-balancing mechanisms, leading to potential performance degradation in unbalanced cases.

### Optimizations:
- Reducing the number of unnecessary rotations in **RBT** operations.
- Potential future optimizations for **AVL Trees** could include caching height or improving rotation strategies.
- **BST** can be improved by adding self-balancing features like **AVL** or **RBT**.
