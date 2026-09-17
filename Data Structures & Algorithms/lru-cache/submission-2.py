class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node, delete_key: bool = False):

        # node = self.cache[key]
        print(f"Removing Node with val: {node.val} and next: {node.next} and prev: {node.prev.val}")
        prev, next = node.prev, node.next
        # Remove the node
        prev.next, next.prev = next, prev

        if delete_key:
            self.cache.pop(node.key)

    def insert(self, node, prev = None, next= None):
        '''
        Inserts the new node at the tail end
        '''
        last = self.tail.prev
        if not (prev and next):
            node.prev, node.next = last, self.tail
        last.next = node
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        val = node.val
        # Move the node to last to mark it most recently used
        print(f"from Get funcion, Removing node for key: {key} and value: {val}")
        self.remove(node=node)
        self.insert(node=node)
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the existing node's value and insert it to the last
            node = self.cache[key]
            print(f"from put funcion, Removing node for key: {key} and value: {node.val}")
            self.remove(node=node)
            node.val = value # Update the node's value to the new value
        else:    
            node = Node(key=key, val=value, prev=self.tail.prev, next=self.tail)
            while len(self.cache) >= self.capacity:
                print(f"from put funcion, Removing node for key: not knowsn and value: {self.head.next.val}")
                key_to_rm_cache = self.remove(self.head.next, delete_key=True) # Remove the first node since it will be the LRU
                # key_to_rm_cache = self.remove(self.head.next, return_key = True) # Remove the first node since it will be the LRU
                # TO DO: Remvoe the key value pair also from the cache dicitonary
                # self.cache.pop(key_to_rm_cache)

        # Insert the new node at the end
        self.insert(node=node)
        
        # Update the LRUcache dicitonary
        self.cache[key] = node
        
        
