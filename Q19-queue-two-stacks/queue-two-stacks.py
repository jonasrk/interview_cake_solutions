class Queue:

    def __init__(self, stackA, stackB):
        self.stackA = stackA
        self.stackB = stackB

    def enqueue(self, element):
        for i in range(0, len(self.stackB)):
            item = self.stackB.pop()
            self.stackA.append(item)
        self.stackA.append(element)

    def dequeue(self):
        for i in range(0, len(self.stackA)):
            item = self.stackA.pop()
            self.stackB.append(item)
        return(self.stackB.pop())

q = Queue([], [])

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
