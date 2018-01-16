class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(b):
	b.value = b.next.value
	b.next = b.next.next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)

print(a.next.value)
