from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left_child: 'Node' = None
    right_child: 'Node' = None

@dataclass
class BinaryTree:
    root: Node = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is not None:
                self._insert_recursive(current_node.left_child, value)
            else:
                current_node.left_child = Node(value)
        elif value > current_node.value:
            if current_node.right_child is not None:
                self._insert_recursive(current_node.right_child, value)
            else:
                current_node.right_child = Node(value)
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
    def lowest_common_ancestor(self):
        pass

    # TODO
    def delete_tree(self):
        pass


# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree()
    elements = [44, 17, 88, 8, 32, 65, 97,54,82,93,78,80]

    for element in elements:
        binary_tree.insert(element)

    print(binary_tree.search(65))  # Output: True
    print(binary_tree.search(9))  # Output: False
    print("Original Binary Search Tree:")
    print(binary_tree.search(65))  # Output: True

    # Deleting a node with one child
    binary_tree.delete(65)
    print("Binary Search Tree after deleting 65:")
    print(binary_tree.search(65))  # Output: False

    # Deleting a node with no children
    binary_tree.delete(8)
    print("Binary Search Tree after deleting 8:")
    print(binary_tree.search(8))   # Output: False

    # Deleting a node with two children
    binary_tree.delete(88)
    print("Binary Search Tree after deleting 88:")
    print(binary_tree.search(88))  # Output: False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#test comment from nick
# test comment for jason
