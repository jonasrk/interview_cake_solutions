class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(b):
	deleted = False
	current_node = a
	while not deleted:
		if not current_node.next:
			raise ValueError('node not in list')
		elif current_node.next == b:
			current_node.next = b.next
			deleted = True
		else:
			current_node = current_node.next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)

print(a.next.value)
