class LRU():
    def __init__(self, size):
        self.els = {}
        self.keys = {}
        self.counter = 0
        self.size = size

    def write(self, key, value):
        self.els[key] = value
        self.keys[self.counter] = key
        
        if self.counter >= self.size:
            del self.els[self.keys[self.counter - self.size]]
        
        self.counter += 1

    def read(self, key):
        if key in self.els:
            return self.els[key]
        else:
            raise ValueError('Key not in cache.')

lru = LRU(1)

lru.write('foo', 23)
print(lru.read('foo'))
lru.write('bar', 42)
print(lru.read('bar'))
print(lru.read('foo'))
