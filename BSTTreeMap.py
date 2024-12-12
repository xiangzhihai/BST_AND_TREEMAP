"""
In this file I will be writing a BST tree map without balancing.

The BSTTreeMap will support insertion, deletion, (in-order) traversal, and search.
"""

from typing import *


class TreeNode:
    def __init__(self, key: int, value) -> None:
        self.key = key
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BSTTreeMap:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node: TreeNode, key: int, value):
        # Update value if key is already in the map
        if node.key == key:
            node.value = value
        elif key < node.key:
            if node.left:
                self._insert(node.left, key, value)
            else:
                node.left = TreeNode(key, value)
        else:
            if node.right:
                self._insert(node.right, key, value)
            else:
                node.right = TreeNode(key, value)

    def _search(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None

        if node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def get(self, key: int) -> Optional[any]:
        return (
            None
            if not (node_found := self._search(self.root, key))
            else node_found.value
        )

    def _find_largest_node(self, node: TreeNode) -> TreeNode:
        if node.right:
            return self._find_largest_node(node.right)
        return node

    def _delete(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Function will delete the key under the node and its children and will
        return this node after the deletion.
        """
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # This is node to be deleted
            if not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                # Replace this node with the largest key that is smaller than it
                node_to_replace = self._find_largest_node(node.left)
                node.key, node.value = node_to_replace.key, node_to_replace.value
                node.left = self._delete(node.left, node_to_replace.key)
        return node

    def delete(self, key: int):
        self.root = self._delete(self.root, key)

    def _in_order_traversal(
        self, node: Optional[TreeNode], result_list: List[Tuple[int, any]]
    ):
        if node:
            self._in_order_traversal(node.left, result_list)
            result_list.append((node.key, node.value))
            self._in_order_traversal(node.right, result_list)

    def items(self) -> List[Tuple[int, any]]:
        result = []
        self._in_order_traversal(self.root, result)
        return result
