import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="red", parent=None, left=None, right=None):
        self.key = key
        self.color = color  # "red" or "black"
        self.parent = parent
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color="black")  # Sentinel NIL node (black)
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key=key, color="red", left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def traverse(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node != self.NIL:
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self._inorder_helper(node.right, result)

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node == self.NIL or key == node.key:
            return node if node != self.NIL else None

        if key < node.key:
            return self.search(key, node.left)
        else:
            return self.search(key, node.right)

    def delete(self, key):
        node = self.search(key)
        if node is None:
            print(f"Key {key} not found in the tree. No deletion performed.")
            return

        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == "black":
            self.fix_delete(x)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.right.color == "black" and sibling.left.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def visualize(self):
        G = nx.DiGraph()

        def add_edges(node):
            if node != self.NIL:
                # Add the current node with its color attribute
                G.add_node(node.key, color=node.color)
                
                if node.left != self.NIL:
                    G.add_edge(node.key, node.left.key, color=node.left.color)
                    add_edges(node.left)
                if node.right != self.NIL:
                    G.add_edge(node.key, node.right.key, color=node.right.color)
                    add_edges(node.right)

        add_edges(self.root)

        # Now, extract the color from the node attribute
        node_colors = ["red" if G.nodes[node]["color"] == "red" else "lightgray" for node in G.nodes]
        edge_colors = [G[u][v]["color"] for u, v in G.edges]

        # Positions for nodes in a 2D plane
        pos = nx.spring_layout(G)
        
        # Drawing the graph
        nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, edge_color=edge_colors, font_weight="bold", font_size=10)

        plt.title("Red-Black Tree Visualization")
        plt.show()

# Example usage:
if __name__ == "__main__":
    rbt = RedBlackTree()
    keys = [20, 15, 25, 10, 5, 1]
    for key in keys:
        rbt.insert(key)

    # Visualize the tree
    rbt.visualize()
