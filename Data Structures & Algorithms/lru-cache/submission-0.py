class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def pop_tail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
    def insertAtFront(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        # Move to front
        self.removeNode(node)
        self.insertAtFront(node)
        
        return node.value 
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap: 
            ##remove or moved 
            node = self.hashmap[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
            ##insert lines
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
        else :
            newNode = Node(key,value)
            self.hashmap[key] = newNode
            ##insertion lines 
            newNode.prev = self.head
            newNode.next = self.head.next
            self.head.next.prev = newNode
            self.head.next = newNode
            if len(self.hashmap) > self.capacity :
                removed = self.pop_tail()  # hold the reved node
                del self.hashmap[removed.key]  


        
