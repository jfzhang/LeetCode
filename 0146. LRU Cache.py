"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
    * LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    * int get(int key) Return the value of the key if the key exists, otherwise return -1.
    * void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
    cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.hash_map[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                remove_node = self.remove_tail()
                del self.hash_map[remove_node.key]
                self.size -= 1

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next
        node.pre, node.next = None, None

    def add_to_head(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def remove_tail(self):
        node = self.tail.pre
        self.remove_node(node)
        return node


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))  # -1
