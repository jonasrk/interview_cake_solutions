class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def contains_cycle(first_node):
    s = set()
    current_node = first_node

    while True:
        if not current_node.next:
            return False
        elif current_node.next.value in s:
            return True
        else:
            s.add(current_node.next.value)
            current_node = current_node.next


a = LinkedListNode('A')
b = LinkedListNode('B')

a.next = b
# b.next = a

print(contains_cycle(a))
