import time
import random
import matplotlib.pyplot as plt
from src.red_black_tree import RedBlackTree
from src.bst import BinarySearchTree
from src.avl import AVLTree

# Function to measure insertion time for each tree type (non-recursive BST for better performance)
def measure_insertion_time(tree, keys):
    start_time = time.time()
    for key in keys:
        tree.insert(key)
    end_time = time.time()
    return end_time - start_time

# Function to measure deletion time for each tree type
def measure_deletion_time(tree, keys):
    # Insert all keys first
    for key in keys:
        tree.insert(key)
    start_time = time.time()
    for key in keys:
        tree.delete(key)
    end_time = time.time()
    return end_time - start_time

# Function to measure search time for each tree type
def measure_search_time(tree, keys):
    # Insert all keys first
    for key in keys:
        tree.insert(key)
    start_time = time.time()
    for key in keys:
        tree.search(key)
    end_time = time.time()
    return end_time - start_time

# Function to measure traversal time for each tree type (In-Order Traversal)
def measure_traversal_time(tree, keys):
    # Insert all keys first
    for key in keys:
        tree.insert(key)
    start_time = time.time()
    tree.traverse()  # Assuming traverse_in_order() is defined in your tree classes
    end_time = time.time()
    return end_time - start_time

# Main performance test
def performance_test():
    input_sizes = [100, 1000, 10000]  # Smaller sample sizes for faster testing
    rbt_insertion_times = []
    bst_insertion_times = []
    avl_insertion_times = []

    rbt_deletion_times = []
    bst_deletion_times = []
    avl_deletion_times = []

    rbt_search_times = []
    bst_search_times = []
    avl_search_times = []

    rbt_traversal_times = []
    bst_traversal_times = []
    avl_traversal_times = []

    for size in input_sizes:
        # Use random data for insertion, deletion, and search
        keys = random.sample(range(size * 10), size)  # Randomized keys

        # Create tree instances
        rbt = RedBlackTree()
        bst = BinarySearchTree()
        avl = AVLTree()

        # Measure times for insertion
        rbt_insertion_time = measure_insertion_time(rbt, keys)
        bst_insertion_time = measure_insertion_time(bst, keys)
        avl_insertion_time = measure_insertion_time(avl, keys)

        # Measure times for deletion
        rbt_deletion_time = measure_deletion_time(rbt, keys)
        bst_deletion_time = measure_deletion_time(bst, keys)
        avl_deletion_time = measure_deletion_time(avl, keys)

        # Measure times for search
        rbt_search_time = measure_search_time(rbt, keys)
        bst_search_time = measure_search_time(bst, keys)
        avl_search_time = measure_search_time(avl, keys)

        # Measure times for traversal
        rbt_traversal_time = measure_traversal_time(rbt, keys)
        bst_traversal_time = measure_traversal_time(bst, keys)
        avl_traversal_time = measure_traversal_time(avl, keys)

        # Store results for plotting
        rbt_insertion_times.append(rbt_insertion_time)
        bst_insertion_times.append(bst_insertion_time)
        avl_insertion_times.append(avl_insertion_time)

        rbt_deletion_times.append(rbt_deletion_time)
        bst_deletion_times.append(bst_deletion_time)
        avl_deletion_times.append(avl_deletion_time)

        rbt_search_times.append(rbt_search_time)
        bst_search_times.append(bst_search_time)
        avl_search_times.append(avl_search_time)

        rbt_traversal_times.append(rbt_traversal_time)
        bst_traversal_times.append(bst_traversal_time)
        avl_traversal_times.append(avl_traversal_time)

        print(f"Input Size: {size}")
        print(f"RBT Insertion Time: {rbt_insertion_time:.6f} seconds")
        print(f"BST Insertion Time: {bst_insertion_time:.6f} seconds")
        print(f"AVL Insertion Time: {avl_insertion_time:.6f} seconds")
        print(f"RBT Deletion Time: {rbt_deletion_time:.6f} seconds")
        print(f"BST Deletion Time: {bst_deletion_time:.6f} seconds")
        print(f"AVL Deletion Time: {avl_deletion_time:.6f} seconds")
        print(f"RBT Search Time: {rbt_search_time:.6f} seconds")
        print(f"BST Search Time: {bst_search_time:.6f} seconds")
        print(f"AVL Search Time: {avl_search_time:.6f} seconds")
        print(f"RBT Traversal Time: {rbt_traversal_time:.6f} seconds")
        print(f"BST Traversal Time: {bst_traversal_time:.6f} seconds")
        print(f"AVL Traversal Time: {avl_traversal_time:.6f} seconds")
        print()

    # Plotting results for insertion time comparison
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.plot(input_sizes, rbt_insertion_times, label='Red-Black Tree (Insertion)')
    plt.plot(input_sizes, bst_insertion_times, label='Binary Search Tree (Insertion)')
    plt.plot(input_sizes, avl_insertion_times, label='AVL Tree (Insertion)')
    plt.xlabel('Input Size')
    plt.ylabel('Insertion Time (seconds)')
    plt.legend()
    plt.title('Insertion Performance of Different Trees')

    # Plotting results for deletion time comparison
    plt.subplot(2, 2, 2)
    plt.plot(input_sizes, rbt_deletion_times, label='Red-Black Tree (Deletion)')
    plt.plot(input_sizes, bst_deletion_times, label='Binary Search Tree (Deletion)')
    plt.plot(input_sizes, avl_deletion_times, label='AVL Tree (Deletion)')
    plt.xlabel('Input Size')
    plt.ylabel('Deletion Time (seconds)')
    plt.legend()
    plt.title('Deletion Performance of Different Trees')

    # Plotting results for search time comparison
    plt.subplot(2, 2, 3)
    plt.plot(input_sizes, rbt_search_times, label='Red-Black Tree (Search)')
    plt.plot(input_sizes, bst_search_times, label='Binary Search Tree (Search)')
    plt.plot(input_sizes, avl_search_times, label='AVL Tree (Search)')
    plt.xlabel('Input Size')
    plt.ylabel('Search Time (seconds)')
    plt.legend()
    plt.title('Search Performance of Different Trees')

    # Plotting results for traversal time comparison
    plt.subplot(2, 2, 4)
    plt.plot(input_sizes, rbt_traversal_times, label='Red-Black Tree (Traversal)')
    plt.plot(input_sizes, bst_traversal_times, label='Binary Search Tree (Traversal)')
    plt.plot(input_sizes, avl_traversal_times, label='AVL Tree (Traversal)')
    plt.xlabel('Input Size')
    plt.ylabel('Traversal Time (seconds)')
    plt.legend()
    plt.title('Traversal Performance of Different Trees')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    performance_test()
