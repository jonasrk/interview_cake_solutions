import sys

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def contains_cycle(first_node):
    current_node_r1 = first_node
    if not current_node_r1.next:
         return False
    current_node_r2 = first_node.next

    while True:
        if current_node_r2.value == current_node_r1.value:
            return True
        elif not current_node_r2.next:
            return False

        current_node_r2 = current_node_r2.next
        
        if current_node_r2.value == current_node_r1.value:
            return True
        elif not current_node_r2.next:
            return False

        current_node_r2 = current_node_r2.next
        current_node_r1 = current_node_r1.next



a = LinkedListNode(1)
b = LinkedListNode(3)

a.next = b
b.next = a

print(contains_cycle(a))

# complexity: O(n) space / O(1) space
