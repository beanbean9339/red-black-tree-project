import time
import matplotlib.pyplot as plt
from src.red_black_tree import RedBlackTree
from src.bst import BinarySearchTree
from src.avl import AVLTree

# Function to measure insertion time for each tree type
def measure_insertion_time(tree, keys):
    start_time = time.time()
    for key in keys:
        tree.insert(key)
    end_time = time.time()
    return end_time - start_time

# Function to measure search time for each tree type
def measure_search_time(tree, keys):
    start_time = time.time()
    for key in keys:
        tree.search(key)
    end_time = time.time()
    return end_time - start_time

# Function to measure deletion time for each tree type
def measure_deletion_time(tree, keys):
    start_time = time.time()
    for key in keys:
        tree.delete(key)
    end_time = time.time()
    return end_time - start_time

# Main performance test
def performance_test():
    input_sizes = [100, 1000, 10000, 100000]
    rbt_insertion_times = []
    bst_insertion_times = []
    avl_insertion_times = []
    rbt_search_times = []
    bst_search_times = []
    avl_search_times = []
    rbt_deletion_times = []
    bst_deletion_times = []
    avl_deletion_times = []

    for size in input_sizes:
        keys = list(range(size))  # Sorted input for testing

        # Create tree instances
        rbt = RedBlackTree()
        bst = BinarySearchTree()
        avl = AVLTree()

        # Measure times for insertion
        rbt_insertion_time = measure_insertion_time(rbt, keys)
        bst_insertion_time = measure_insertion_time(bst, keys)
        avl_insertion_time = measure_insertion_time(avl, keys)

        # Measure times for search
        rbt_search_time = measure_search_time(rbt, keys)
        bst_search_time = measure_search_time(bst, keys)
        avl_search_time = measure_search_time(avl, keys)

        # Measure times for deletion
        rbt_deletion_time = measure_deletion_time(rbt, keys)
        bst_deletion_time = measure_deletion_time(bst, keys)
        avl_deletion_time = measure_deletion_time(avl, keys)

        # Store results for plotting
        rbt_insertion_times.append(rbt_insertion_time)
        bst_insertion_times.append(bst_insertion_time)
        avl_insertion_times.append(avl_insertion_time)

        rbt_search_times.append(rbt_search_time)
        bst_search_times.append(bst_search_time)
        avl_search_times.append(avl_search_time)

        rbt_deletion_times.append(rbt_deletion_time)
        bst_deletion_times.append(bst_deletion_time)
        avl_deletion_times.append(avl_deletion_time)

        print(f"Input Size: {size}")
        print(f"RBT Insertion Time: {rbt_insertion_time:.6f} seconds")
        print(f"BST Insertion Time: {bst_insertion_time:.6f} seconds")
        print(f"AVL Insertion Time: {avl_insertion_time:.6f} seconds")
        print()

    # Plotting results for insertion time comparison
    plt.plot(input_sizes, rbt_insertion_times, label='Red-Black Tree (Insertion)')
    plt.plot(input_sizes, bst_insertion_times, label='Binary Search Tree (Insertion)')
    plt.plot(input_sizes, avl_insertion_times, label='AVL Tree (Insertion)')
    plt.xlabel('Input Size')
    plt.ylabel('Insertion Time (seconds)')
    plt.legend()
    plt.title('Insertion Performance of Different Trees')
    plt.show()

if __name__ == "__main__":
    performance_test()
