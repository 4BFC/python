class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def add_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        break
                    else:
                        current_node = current_node.left_child
                else:
                    if current_node.right_child is None:
                        current_node.left_child = new_node
                        break
                    else:
                        current_node = current_node.right_child
