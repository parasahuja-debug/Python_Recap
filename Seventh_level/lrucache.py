class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


lRUCache = LRUCache(2)
lRUCache.put(1, 1); 
#// cache is {1=1}
lRUCache.put(2, 2); 
#// cache is {1=1, 2=2}
lRUCache.get(1);    
#// return 1
lRUCache.put(3, 3); 
#// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    
#// returns -1 (not found)
lRUCache.put(4, 4); 
#// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    
#// return -1 (not found)
lRUCache.get(3);    
#// return 3
lRUCache.get(4);    
#// return 4