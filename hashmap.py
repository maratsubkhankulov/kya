# A Hashmap implementation

class HashMap:
    n_buckets = 1000

    def __init__(self):
        self.buckets = HashMap.n_buckets*[None]

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
        self.buckets[HashMap.hash_function(key)] = (key,value)

    def remove(self, key):
        self.buckets[HashMap.hash_function(key)] = None

    def contains_key(self, key):
        return self._get_bucket(key) != None

    def get(self, key):
        bucket = self._get_bucket(key)
        if bucket != None:
            return bucket[1]
        else:
            return None

    def _get_bucket(self, key):
        return self.buckets[HashMap.hash_function(key)]

def test():
    print "HashMap test"
    my_map = HashMap()

    my_map.put("a", "apple")
    my_map.put("o", "orange")
    my_map.put("p", "pear")
    my_map.put(1, "one")
    my_map.put(21, "twentyone")
    my_map.put(1001, "onethousandone")

    print my_map.contains_key("a")
    print my_map.contains_key("o")
    print my_map.contains_key("p")
    print not my_map.contains_key("x")

    print my_map.get("a") == "apple"
    print my_map.get("o") == "orange"
    print my_map.get("p") == "pear"
    print my_map.get(1) == "one"
    print my_map.get(21) == "twentyone"
    print my_map.get(1001) == "onethousandone"

if __name__ == "__main__":
    test()
