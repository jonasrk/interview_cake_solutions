import sys

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
	max = -sys.maxsize
	for element in self.items:
		if element > max:
			max = element
	return max

s = Stack()
s.push(4)
s.push(8)
s.push(15)
s.push(1337)
s.push(16)
s.push(23)
s.push(42)

print(s.get_max())
