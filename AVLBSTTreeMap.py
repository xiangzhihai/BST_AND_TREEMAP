class AVLNode:
    """Node class for AVL Tree"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVLTreeMap:
    """TreeMap implementation using an AVL Tree"""
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        """Get the height of a node"""
        return node.height if node else 0

    def _get_balance(self, node):
        """Get the balance factor of a node"""
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_right(self, y):
        """Perform a right rotation"""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1

        return x

    def _rotate_left(self, x):
        """Perform a left rotation"""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        return y

    def _insert(self, node, key, value):
        """Helper method to insert a key-value pair into the AVL tree"""
        if not node:
            return AVLNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # Update value if key already exists
            return node

        # Update the height of this ancestor node
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

        # Get the balance factor to check if rebalancing is needed
        balance = self._get_balance(node)

        # Perform rotations if the tree is unbalanced
        # Left Heavy (LL Case)
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Right Heavy (RR Case)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Left-Right Heavy (LR Case)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Left Heavy (RL Case)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, key, value):
        """Insert a key-value pair into the AVL TreeMap"""
        self.root = self._insert(self.root, key, value)

    def _in_order(self, node, result):
        """Helper method for in-order traversal"""
        if node:
            self._in_order(node.left, result)
            result.append((node.key, node.value))
            self._in_order(node.right, result)

    def items(self):
        """Return all key-value pairs in sorted order"""
        result = []
        self._in_order(self.root, result)
        return result

    def __str__(self):
        """String representation of the AVL TreeMap"""
        return str(self.items())


# Example Usage
avl_tree_map = AVLTreeMap()
avl_tree_map.insert(10, "Ten")
avl_tree_map.insert(20, "Twenty")
avl_tree_map.insert(5, "Five")
avl_tree_map.insert(15, "Fifteen")

print("AVL Tree Map:", avl_tree_map)