class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def max_value(self):
        if self.right and self.left:
            return max(self.value, self.right.max_value(), self.left.max_value())
        elif self.right:
            return max(self.value, self.right.max_value())

        elif self.left:
            return max(self.value, self.left.max_value())
        else:
            return self.value

    def is_bst(self):
        maxleft = None
        maxright = None
        if self.left:
            maxleft = self.left.max_value()
        if self.right:
            maxright = self.right.max_value()

        if self.right and self.left:
            if maxright > maxleft:
                return self.right.is_bst() and self.left.is_bst()
            else:
                return False

        if self.right:
            if maxright > self.value:
                return self.right.is_bst()
            else:
                return False

        if self.left:
            if maxleft < self.value:
                return self.left.is_bst()
            else:
                return False


        else:
            return True


A = BinaryTreeNode(10)
A.insert_right(15)
A.insert_left(5)
A.right.insert_right(20)
A.right.right.insert_right(25)
A.left.insert_right(8)

print(A.is_bst())
