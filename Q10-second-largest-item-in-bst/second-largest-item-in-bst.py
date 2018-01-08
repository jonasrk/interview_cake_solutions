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
        if self.right:
            return self.right.get_second_largest()
        if self.left:
            return self.left.get_first_largest()
        elif self.parent:
            return self.parent.value
        else:
            raise ValueError("Only one element")

    def get_first_largest(self):
        if self.right:
            return self.right.get_first_largest()
        else:
            return self.value

A = BinaryTreeNode(10, None)
A.insert_left(5, A)
A.left.insert_right(8, A.left)

print(A.get_second_largest())