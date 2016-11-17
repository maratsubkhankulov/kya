# A Hashmap implementation

class HashMap:
    store_size = 1000

    def __init__(self):
        self.keys = set()
        self.array = HashMap.store_size*[None]

    @staticmethod
    def hash_function(key):
        if type(key) is str:
            sum = 0
            for char in key:
                sum += ord(char)
            return (len(key) + sum) % HashMap.store_size
        elif type(key) is int:
            return key % HashMap.store_size

    def put(self, key, value):
        self.keys.add(key)
        self.array[HashMap.hash_function(key)] = value

    def remove(self, key):
        if self.contains_key(key):
            self.keys.remove(key)
            self.array[HashMap.hash_function(key)] = None

    def contains_key(self, key):
        return key in self.keys

    def get(self, key):
        if self.contains_key(key):
            return self.array[HashMap.hash_function(key)]
        else:
            return None

def test():
    print "HashMap test"
    my_map = HashMap()

    my_map.put("a", "apple")
    my_map.put("o", "orange")
    my_map.put("p", "pear")
    my_map.put(1, "one")
    my_map.put(21, "twentyone")

    print my_map.contains_key("a")
    print my_map.contains_key("o")
    print my_map.contains_key("p")
    print not my_map.contains_key("x")

    print my_map.get("a") == "apple"
    print my_map.get("o") == "orange"
    print my_map.get("p") == "pear"
    print my_map.get(1) == "one"
    print my_map.get(21) == "twentyone"

if __name__ == "__main__":
    test()
