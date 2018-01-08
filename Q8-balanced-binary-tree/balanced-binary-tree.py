class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_superbalanced(self):
        max_depth = self.maxdepth()
        print(max_depth)
        min_depth = self.mindepth()
        print(min_depth)
        if max_depth - min_depth > 1:
            return False
        else:
            return True

    def maxdepth(self):
        if self.left and self.right:
            return 1 + max(self.left.maxdepth(), self.right.maxdepth())
        elif self.left:
            return 1 + self.left.maxdepth()
        elif self.right:
            return 1 + self.right.maxdepth()
        else:
            return 1

    def mindepth(self):
        if self.left and self.right:
            return 1 + min(self.left.mindepth(), self.right.mindepth())
        elif self.left:
            return 1 + self.left.mindepth()
        elif self.right:
            return 1 + self.right.mindepth()
        else:
            return 1


A = BinaryTreeNode(1)
A.insert_right(2)
A.insert_left(22)
A.right.insert_right(3)
A.right.right.insert_right(4)
A.left.insert_right(5)

print(A.is_superbalanced())	
