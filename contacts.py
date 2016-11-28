import fileinput
from sets import Set


class Contacts:
    def __init__(self):
        self.words = Set()
    def add(self, word):
        self.words.add(word)
    def count_ocurrences_(self, prefix):
        return len([word for word in self.words if word.startswith(prefix)])

class Trie:
    IS_WORD = 0
    DICT = 1
    NUM_CHILDREN = 2

    def __init__(self):
        self.root = [False,{},0]

    def add(self, word):
        node = self.root
        for char in word:
            node[Trie.NUM_CHILDREN] += 1
            if not char in node[Trie.DICT]:
                node[Trie.DICT][char] = [False,{},0]
            node = node[Trie.DICT][char]
        node[Trie.IS_WORD] = True
        node[Trie.NUM_CHILDREN] = 1

    def count_ocurrences(self, prefix):
        node = self.root
        # Find prefix node
        for char in prefix:
            if not char in node[Trie.DICT]:
                return 0
            node = node[Trie.DICT][char]

        return node[Trie.NUM_CHILDREN]

operation_types = ["add", "find"]

def contacts_test():
    line_num = 0
    op_count = 0
    trie = Trie()
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

            # Perform operation
            if op[0] == "add":
                trie.add(op[1])
            elif op[0] == "find":
                print trie.count_ocurrences(op[1])

        line_num += 1
        if op_count == line_num - 1:
            break

    #print trie.root

if __name__ == "__main__":
    contacts_test()
