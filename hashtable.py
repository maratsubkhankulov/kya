# A Hashmap implementation

class HashMap:

    def __init__(self):
        self.array = []

    def hash_function(string):
        return len(string) + sum_of_characters(string)

    def put(self, key, value):
        self.array[hash_function(key)] = value

    def contains_key(self, key):
        return self.array[key] != None

    def get(self, key):
        return value

def test():
    print "HashMap test"
    my_map = HashMap()

    my_map.put("a", "apple")
    my_map.put("o", "orange")
    my_map.put("p", "pear")

    print my_map.contains_key("a")
    print my_map.contains_key("o")
    print my_map.contains_key("p")

    print my_map.get("a") == "apple"
    print my_map.get("o") == "orange"
    print my_map.get("p") == "pear"
