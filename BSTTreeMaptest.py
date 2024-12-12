import unittest

from BSTTreeMap import * 

class BSTTreeMapTest(unittest.TestCase):
    def setUp(self):
        # This method runs before each test
        # Initialize any objects or variables you need for testing
        self.tree_map = BSTTreeMap()

    def test_insert_1(self):
        self.tree_map.insert(4, 4)
        self.tree_map.insert(2, 2)
        self.tree_map.insert(6, 6)
        self.tree_map.insert(1, 1)
        self.tree_map.insert(3, 3)
        self.tree_map.insert(2.5, 2.5)
        self.tree_map.insert(5, 5)
        self.tree_map.insert(7, 7)
        assert self.tree_map.root != None

    def test_get(self):
        self.test_insert_1()
        assert self.tree_map.get(2.5) == 2.5

    def test_find_largest_node(self):
        self.test_insert_1()
        assert self.tree_map._find_largest_node(self.tree_map.root).value == 7
        assert self.tree_map._find_largest_node(self.tree_map.root.left).value == 3

    def test_delete_leaf_without_children(self):
        self.test_insert_1()
        self.tree_map.delete(1)
        assert self.tree_map.get(1) == None

    def test_delete_leaf_with_single_children(self):
        self.test_insert_1()
        self.tree_map.delete(3)
        assert self.tree_map.get(3) == None
        assert self.tree_map.root.left.right.value == 2.5

    def test_delete_with_single_replacement(self):
        self.test_insert_1()
        self.tree_map.delete(2)
        assert self.tree_map.get(2) == None
        assert self.tree_map.root.left.value == 1

    def test_delete_with_recursive_replacement(self):
        self.test_insert_1()
        self.tree_map.delete(4)
        assert self.tree_map.get(4) == None
        assert self.tree_map.root.value == 3
        assert self.tree_map.root.left.right.value == 2.5

    def test_get_items(self):
        self.test_insert_1()
        items = self.tree_map.items()
        assert len(items) == 8
        assert items == sorted(items)