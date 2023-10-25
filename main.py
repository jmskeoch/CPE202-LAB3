from dataclasses import dataclass
import unittest

@dataclass
class TreeNode:
    value: int
    left_child: 'TreeNode' = None
    right_child: 'TreeNode' = None

@dataclass
class BinaryTree:
    root: TreeNode = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is not None:
                self._insert_recursive(current_node.left_child, value)
            else:
                current_node.left_child = TreeNode(value)
        elif value > current_node.value:
            if current_node.right_child is not None:
                self._insert_recursive(current_node.right_child, value)
            else:
                current_node.right_child = TreeNode(value)
        else:
            # Value already exists in the tree, handle as per your requirement.
            pass

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if not current_node:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left_child, value)
        else:
            return self._search_recursive(current_node.right_child, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node  # If the tree is empty or the node is not found, return None.
            # Recursive calls for ancestors of the node to be deleted
        if value < current_node.value:
            # Recur down the left subtree if the value is smaller.
            current_node.left_child = self._delete_recursive(current_node.left_child, value)
        elif value > current_node.value:
            # Recur down the left subtree if the value is greater
            current_node.right_child = self._delete_recursive(current_node.right_child, value)
        else:
            # Node with only one child or no child
            if current_node.left_child is None:
                temp_node = current_node.right_child
                del current_node
                return temp_node
            elif current_node.right_child is None:
                temp_node = current_node.left_child
                del current_node
                return temp_node

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            current_node.value = self._find_min_value(current_node.right_child)

            # Delete the inorder successor
            current_node.right_child = self._delete_recursive(current_node.right_child, current_node.value)

        return current_node

    def _find_min_value(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current.value

    # TODO
    def isBST(self):
        pass

    # TODO
    def convert_to_sorted_array(self):
        pass

    # TODO
    def lowest_common_ancestor(self, val1: int, val2: int, root: TreeNode):
        if root is None:
            return None

        current = root  # Start at root
        while current is not None:  # If we can traverse...
            if val1 < current.value and val2 < current.value:  # Both values less than current, traverse left
                if current.left_child.value == val1 or current.left_child.value == val2:  # Check Inline
                    return current.value
                current = current.left_child  # Traverse left_child
            elif val1 > current.value and val2 > current.value:  # Both values greater than current, traverse right
                if current.right_child.value == val1 or current.right_child.value == val2:  # Check Inline
                    return current.value
                current = current.right_child  # Traver right_child
            else:
                return current.value  # One node must be greater than current while the other is less, so return current

        return None

    def delete_tree(self):
        self.root = None


binary_tree = BinaryTree()
elements = [44, 17, 88, 8, 32, 65, 97, 54, 82, 93, 78, 80]
"""
                  44
                 /  \
                17   88
             /    \ /   \
            8    32 65    97
                    /\    /\
                   54 82 93
                      /
                     78
                      \
                      80
"""

for element in elements:
    binary_tree.insert(element)

class TestCases(unittest.TestCase):
    def test_lca_root(self):
        lca = binary_tree.lowest_common_ancestor(17, 88, binary_tree.root)
        self.assertEqual(lca, 44)

    def test_lca_leafs(self):
        lca = binary_tree.lowest_common_ancestor(54, 97, binary_tree.root)
        self.assertEqual(lca, 88)

    def test_lca_inline(self):
        lca = binary_tree.lowest_common_ancestor(54, 65, binary_tree.root)
        self.assertEqual(lca, 88)

        #hellpo


