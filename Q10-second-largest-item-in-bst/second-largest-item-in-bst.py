class BinaryTreeNode:

    def __init__(self, value, parent):
        self.value = value
        self.left  = None
        self.right = None
        self.parent = parent

    def insert_left(self, value, parent):
        self.left = BinaryTreeNode(value, parent)
        return self.left

    def insert_right(self, value, parent):
        self.right = BinaryTreeNode(value, parent)
        return self.right

    def get_second_largest(self):
        current_node = self
        at_largest = False
        while not at_largest:
            if current_node.right:
                current_node = current_node.right
            elif current_node.parent:
                at_largest = True
                current_node = current_node.parent
            elif current_node.left:
                return current_node.left.get_first_largest()
            else:
                raise ValueError("Only one element")

        if current_node.left:
            return current_node.left.get_first_largest()
        else:
            return current_node.value

    def get_first_largest(self):
        current_node = self
        at_largest = False
        while not at_largest:
            if current_node.right:
                current_node = current_node.right
            else:
                return current_node.value

A = BinaryTreeNode(10, None)
A.insert_left(5, A)
A.left.insert_right(8, A.left)

A.insert_right(15, A)
A.right.insert_right(20, A.right)
A.right.right.insert_right(25, A.right.right)

print(A.get_second_largest())