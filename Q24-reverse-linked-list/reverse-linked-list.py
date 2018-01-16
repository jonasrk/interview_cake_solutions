class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head):
    previous = head
    current = head.next
    next = current.next

    previous.next = None

    needs_swapping = True

    while needs_swapping:
        # swap directions

        current.next = previous
        previous = current
        current = next
        next = current.next

        if not next.next:

            current.next = previous
            previous = current
            current = next
            return_node = next
            return_node.next = previous
            next = current.next

            needs_swapping = False

    return return_node


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')

a.next = b
b.next = c
c.next = d

a = reverse(a)

current = a
print(current.value)
while current.next:
    print(current.next.value)
    current = current.next
