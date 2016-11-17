# A Hashmap implementation

class HashMap:
    n_buckets = 100

    def __init__(self):
        self.buckets = HashMap.n_buckets*[[]]
        self.size = 0

    @staticmethod
    def hash_function(key):
        if type(key) is str:
            sum = 0
            for char in key:
                sum += ord(char)
            return (len(key) + sum) % HashMap.n_buckets
        elif type(key) is int:
            return key % HashMap.n_buckets

    def put(self, key, value):
        bi = self._get_bucket_index(key)
        if self.contains_key(key):
            kv_index = [i for i,kv in enumerate(self.buckets[bi]) if kv[0] == key][0]
            self.buckets[bi][kv_index] = (key,value)
        else:
            self.buckets[bi].append((key,value))
            self.size += 1

    def remove(self, key):
        bi = self._get_bucket_index(key)
        if len(self.buckets[bi]) > 0:
            kv_indices = [i for i,kv in enumerate(self.buckets[bi]) if kv[0] == key]
            if len(kv_indices) == 1:
                self.buckets[bi].pop(kv_indices[0])
                self.size -= 1


    def contains_key(self, key):
        bi = self._get_bucket_index(key)
        if len(self.buckets[bi]) == 0:
            return False
        elif len(self.buckets[bi]) > 0:
            keys = [kv[0] for kv in self.buckets[bi] if kv[0] == key]
            return len(keys) > 0

    def get(self, key):
        bi = self._get_bucket_index(key)
        if len(self.buckets[bi]) == 0:
            return None
        elif len(self.buckets[bi]) > 0:
            values = [kv[1] for kv in self.buckets[bi] if kv[0] == key]
            return values[0]

    def _get_bucket_index(self, key):
        return HashMap.hash_function(key)

    def __len__(self):
        return self.size

def test():
    print "HashMap test"
    my_map = HashMap()

    my_map.put("a", "apple")
    my_map.put("a", "apple")
    my_map.put("o", "orange")
    my_map.put("p", "pear")
    my_map.put(1, "one")
    my_map.put(21, "twentyone")
    my_map.put(1001, "onethousandone")

    print "Test contains_key()"
    print my_map.contains_key("a")
    print my_map.contains_key("o")
    print my_map.contains_key("p")
    print my_map.contains_key(1)
    print my_map.contains_key(21)
    print my_map.contains_key(1001)
    print not my_map.contains_key("x")

    print "Test get()"
    print my_map.get("a") == "apple"
    print my_map.get("o") == "orange"
    print my_map.get("p") == "pear"
    print my_map.get(1) == "one"
    print my_map.get(21) == "twentyone"
    print my_map.get(1001) == "onethousandone"

    print "Test remove()"
    print len(my_map) == 6
    my_map.remove("a")
    my_map.remove("o")
    my_map.remove("o")
    my_map.remove("p")
    print len(my_map) == 3
    my_map.remove(1)
    my_map.remove(21)
    my_map.remove(1001)
    print len(my_map) == 0


if __name__ == "__main__":
    test()
