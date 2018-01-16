class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')

a.next = b
b.next = c
c.next = d

def kth_last(head, k):
    first_runner = head
    second_runner = head

    for i in range(0, k):
        first_runner = first_runner.next

    while first_runner.next:
        first_runner = first_runner.next
        second_runner = second_runner.next

    return second_runner.value

print(kth_last(a, 1))
