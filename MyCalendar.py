from typing import *
from functools import total_ordering

@total_ordering
class Slot:
    def __init__(self, start_time, end_time):
        # Always assume start < end
        self.start_time = start_time
        self.end_time = end_time
        self.left = None
        self.right = None
        self.height = 1

    def __eq__(self, slot_to_compare):
        return not self.__lt__(slot_to_compare) and not self.__gt__(slot_to_compare)

    def __lt__(self, slot_to_compare):
        if not isinstance(slot_to_compare, Slot):
            return NotImplemented
        return self.end_time <= slot_to_compare.start_time

    def __gt__(self, slot_to_compare):
        if not isinstance(slot_to_compare, Slot):
            return NotImplemented
        return slot_to_compare.end_time <= self.start_time

    def compare(self, slot_to_compare):
        """ -1 if slot_to_compare is before, 0 for duplicate, 1 for after """
        if slot_to_compare.end_time <= self.start_time:
            return -1
        elif self.end_time <= slot_to_compare.start_time:
            return 1
        else:
            return 0

class MyCalendar:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        return node.height

    def _get_balance(self, node):
        """returns how much left leaf is greater than right leaf"""
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _rotate_right(self, node) -> Slot:
        left_node = node.left
        t2 = left_node.right

        node.left = t2
        left_node.right = node

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        left_node.height = max(self._get_height(left_node.left), self._get_height(left_node.right)) + 1

        return left_node


    def _rotate_left(self, node) -> Slot:
        right_node = node.right
        t2 = right_node.left

        node.right = t2
        right_node.left = node

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        right_node.height = max(self._get_height(right_node.left), self._get_height(right_node.right)) + 1

        return right_node


    def _insertBookNode(self, current_node, node_to_insert) -> Tuple[bool, Optional[Slot]]:
        # Find an empty leaf, insert this new node
        if current_node == None:
            return True, node_to_insert
        
        if current_node == node_to_insert: 
            """ Has comflict """
            return False, current_node
        if node_to_insert < current_node:
            is_inserted, current_node.left = self._insertBookNode(current_node.left, node_to_insert)
        else:
            is_inserted, current_node.right = self._insertBookNode(current_node.right, node_to_insert)

        balance = self._get_balance(current_node)

        if balance > 1:
            if node_to_insert > current_node.left:
                """ 
                LR:
                       3             3         2
                   1       ->      2     ->  1   3
                     2           1
                """
                current_node.left = self._rotate_left(current_node.left)
            """
            LL:
                    3      2
                  2  ->  1   3
                1 
            """
            current_node = self._rotate_right(current_node)
        if balance < -1:
            if node_to_insert < current_node.right:
                current_node.right = self._rotate_right(current_node.right)
            current_node = self._rotate_left(current_node)

        return is_inserted, current_node

    def book(self, startTime: int, endTime: int) -> bool:
        node_to_insert = Slot(startTime, endTime)
        is_inserted, self.root = self._insertBookNode(self.root, node_to_insert)
        return is_inserted
    
# Create calendar instance
calendar = MyCalendar()
print("Booking (10, 20):", calendar.book(10, 20))
print("Booking (21, 30):", calendar.book(20, 30))
print("Booking (21, 30):", calendar.book(50, 60))
print("Booking (21, 30):", calendar.book(60, 70))
print("Booking (21, 30):", calendar.book(40, 50))
print("Booking (21, 30):", calendar.book(30, 40))
