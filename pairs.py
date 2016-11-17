# Find all pairs of numbers which sum to zero
# e.g.
# input: [1,2,5,-1,-5]
# output: [(1,-1),(5,-5)]

from hashmap import HashMap

def find_pairs(array):
    if len(array) < 2:
        return []
    else:
        output = []
        zero_count = 0
        for item in array:
            if item == 0:
                zero_count += 1
        if zero_count > 1:
            output.append((0,0))
        mymap = HashMap()
        for item in array:
            mymap.put(-item, item)

        for item in array:
            if mymap.contains_key(item):
                if item != 0:
                    output.append((item, -item))
                    mymap.remove(item)
                    mymap.remove(-item)
        return output
            

def test():
    print find_pairs([1,2,5,-1,-5])
    print find_pairs([0])
    print find_pairs([1,-1,1,0])
    print find_pairs([1,-1,1,0,0])
    print find_pairs([0,0])

if __name__ == "__main__":
    test()
