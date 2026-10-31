class MyHashMap:
    def _hash(self, key): return key % 1000
    
    def __init__(self):
        self.buckets = [[] for _ in range(1000)]
        
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = [key, value]
                return
        bucket.append([key, value])
    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                break
        

# Your MyHashMap object will be instantiated and called a/s such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)