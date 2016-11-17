# A Hashmap implementation

class HashMap:
    store_size = 1000

    def __init__(self):
        self.array = HashMap.store_size*[None]

    @staticmethod
    def hash_function(string):
        sum = 0
        for char in string:
            sum += ord(char)
        return (len(string) + sum) % HashMap.store_size

    def put(self, key, value):
        self.array[HashMap.hash_function(key)] = value

    def contains_key(self, key):
        return self.get(key) != None

    def get(self, key):
        return self.array[HashMap.hash_function(key)]

def test():
    print "HashMap test"
    my_map = HashMap()

    my_map.put("a", "apple")
    my_map.put("o", "orange")
    my_map.put("p", "pear")

    print my_map.contains_key("a")
    print my_map.contains_key("o")
    print my_map.contains_key("p")
    print not my_map.contains_key("x")

    print my_map.get("a") == "apple"
    print my_map.get("o") == "orange"
    print my_map.get("p") == "pear"

if __name__ == "__main__":
    test()
