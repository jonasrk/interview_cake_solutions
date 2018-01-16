import sys

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def contains_cycle(first_node):
    max = -sys.maxsize
    current_node = first_node

    while True:
        if not current_node.next:
            return False
        elif current_node.next.value == max:
            return True
        else:
            if current_node.next.value > max:
                max = current_node.next.value
            current_node = current_node.next


a = LinkedListNode(1)
b = LinkedListNode(3)

a.next = b
# b.next = a

print(contains_cycle(a))

# complexity: O(n) space / O(n) space
