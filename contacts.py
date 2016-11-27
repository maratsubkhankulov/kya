import fileinput
from sets import Set

class Trie:
    def __init__(self):
        self.words = Set()

    def add(self, word):
        self.words.add(word)

    def count_ocurrences(self, prefix):
        return len([word for word in self.words if word.startswith(prefix)])

operation_types = ["add", "find"]

if __name__ == "__main__":
    line_num = 0
    op_count = 0
    ops = []
    for line in fileinput.input():
        if line_num == 0:
            try:
                op_count = int(line)
            except Exception:
                print "uh oh, incorrect input"
        else:
            op = line.split(" ")
            assert(len(op) == 2)
            assert(op[0] in operation_types)
            op[1] = op[1].strip('\n')
            ops.append(op)
        line_num += 1
        if op_count == line_num - 1:
            break

    trie = Trie()
    for op in ops:
        if op[0] == "add":
            trie.add(op[1])
        elif op[0] == "find":
            print trie.count_ocurrences(op[1])
    
