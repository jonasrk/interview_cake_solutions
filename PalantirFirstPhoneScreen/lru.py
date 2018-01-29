class LinkedListNode():
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previos

class LRU():
    def __init__(self, size):
        self.last_el = None
        self.oldest_el = None
        self.keys = {}
        self.counter = 0
        self.size = size

    def write(self, key, value):
        self.keys[key] = LinkedListNode(value, None, None)
        
        if self.counter == 0:
            self.last_el = self.keys[key]
            self.oldest_el = self.last_el
        else:
            self.last_el.next = self.keys[key]
            self.keys[key].previous = self.last_el
            self.last_el = self.keys[key].previous
        
        if self.counter >= self.size:
            del self.keys[self.oldest_el.value]
            self.oldest_el = self.oldest_el.next
        
        self.counter += 1


    def read(self, key):
        if key in self.els:
            el = self.els[key]
            el.previous.next = el.next
            self.latest_el.next = el
            self.latest_el = el
            return el
        else:
            raise ValueError('Key not in cache.')

lru = LRU(2)

lru.write('foo', 23)
print(lru.read('foo'))
lru.write('bar', 42)
print(lru.read('bar'))
print(lru.read('foo'))
lru.write('fub', 45)
print(lru.read('foo'))
print(lru.read('bar'))
