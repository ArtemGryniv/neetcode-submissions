class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.mp = {}
        self.head = None
        self.tail = None

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def insert(self, node):
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        node = self.mp[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.value = value

            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.mp[key] = node
            self.insert(node)
            self.length += 1

            if self.length > self.capacity:
                lru = self.tail
                self.remove(lru)
                del self.mp[lru.key]
                self.length -= 1