class LinkedListNode():
    def __init__(self, key, value, next, previous):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

class LRU():
    def __init__(self, size):
        self.last_el = None
        self.oldest_el = None
        self.keys = {}
        self.counter = 0
        self.size = size

    def write(self, key, value):
        self.keys[key] = LinkedListNode(key, value, None, None)
        
        if self.counter == 0:
            self.last_el = self.keys[key]
            self.oldest_el = self.last_el
        else:
            self.last_el.next = self.keys[key]
            self.keys[key].previous = self.last_el
            self.last_el = self.keys[key].previous
        
        if self.counter >= self.size:
            del self.keys[self.oldest_el.key]
            self.oldest_el = self.oldest_el.next
            self.counter -= 1
        
        self.counter += 1


    def read(self, key):
        if key in self.keys:
            el = self.keys[key]
            if el.previous:
                el.previous.next = el.next
            elif el == self.oldest_el and self.oldest_el.next:
                self.oldest_el = self.oldest_el.next
            self.last_el.next = el
            self.last_el = el
            return el.value
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
