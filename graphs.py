# Structures

# 0 - unvisited
# 1 - in progress
# 2 - visited

class Node:
    def __init__(self, data, edges, status):
        self.data = data
        self.edges = edges
        self.status = status
        self.search_parent = None

class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices

class MatrixNode:
    def __init__(self, data, status):
        self.data = data
        self.status = status

class MatrixGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.matrix = []
        for node_index in range(len(nodes)):
            row = []
            for node_index in range(len(nodes)):
                row.append(0)
            self.matrix.append(row)

    def find_node(self, node_name):
        for node in self.nodes:
            if (node.data == node_name):
                return node

    def _reset_nodes(self):
        for node in self.nodes:
            node.status = 0

    def _find_node_index(self, node_name):
        for index in range(len(self.nodes)):
            if (self.nodes[index].data == node_name):
                return index
        print("Node not found for name: %s", node_name)
        return None

    def put_edge(self, node_name_a, node_name_b, weight):

        index_a = self._find_node_index(node_name_a)
        index_b = self._find_node_index(node_name_b)

        self.matrix[index_a][index_b] = weight
    
    def dfs_path(self, source_name, target_name):
        source_node = self.find_node(source_name)
        path = []
        is_found = self._dfs_path(source_node, target_name, path)
        self._reset_nodes()
        return path

    def _dfs_path(self, current_node, target_name, path):
        is_found = False
        path.append(current_node.data)
        if current_node.data == target_name:
            return True
        else:
            current_node.status = 1
            for node in self.get_neighbours(current_node.data):
                if node.status != 2:
                    is_found = self._dfs_path(node, target_name, path)
                    if is_found:
                        break
                    else:
                        path.pop()
            current_node.status = 2
        return is_found

    def get_neighbours(self, name):
        node_index = self._find_node_index(name)
        neighbours = []
        for index in range(len(self.nodes)):
            if node_index == index:
                continue
            if (self.matrix[node_index][index] > 0):
                neighbours.append(self.nodes[index])
        return neighbours

# Algorithms

def dfs_path(current_node, goal_node_name):
    path = []
    result = dfs(current_node, goal_node_name, path)
    if result == None:
        path.pop()
    return path

def dfs(current_node, goal_node_name, path):
    result = None
    path.append(current_node.data)
    if current_node.data == goal_node_name:
        return current_node 
    else:
        current_node.status = 1
        for edge in current_node.edges:
            neighbour = edge.to
            if neighbour.status == 0:
                result = dfs(neighbour, goal_node_name, path)
                if result:
                    break
                else:
                    path.pop()
            current_node.status = 2
    return result

def bfs(start, goal_name):
    queue = []
    queue.append(start)
    while len(queue) > 0:
        node = queue.pop(0)
        if node.status != 2:
            node.status = 2
            if node.data == goal_name:
                return node
            for edge in node.edges:
                if edge.to.status != 2:
                    edge.to.search_parent = node
                queue.append(edge.to)

def bfs_path(start, goal_name):
    result = bfs(start, goal_name)
    return bfs_construct_path(result)

def bfs_construct_path(node):
    path = []
    while node != None:
        path.insert(0, node.data)
        if node.search_parent != None:
            node = node.search_parent
        else:
            break
    return path

# Return all paths from source to target_name
def all_paths(source, target_name):
    all_paths = []
    all_paths_helper(source, target_name, all_paths, [])
    return all_paths

# Input:
# - source node target node name, a list of all paths and the
# intermediate path
# Output:
# - return true if a path has successfully been added
# - update all_paths with every successful path

def all_paths_helper(current_node, target_name, all_paths, path):
    path.append(current_node.data)
    if current_node.data == target_name:
        all_paths.append(path)
        return True
    else:
        current_node.status = 1
        for edge in current_node.edges:
            neighbour = edge.to
            if neighbour.status == 0:
                # create a copy of the path until this point for every
                # diverging path
                new_path = list(path)
                all_paths_helper(neighbour, target_name, all_paths, new_path)
        current_node.status = 2
    return False

def dft(current_node):
    print(current_node.data)
    current_node.status = 1
    for edge in current_node.edges:
        if edge.to.status == 0:
            dft(edge.to)
    current_node.status = 2       

def test_search(algo, G, starting_node, target_name):
    result = algo(starting_node, target_name)
    print("Path %s -> %s: %s" % (starting_node.data, target_name, result))
    # Reset node status
    for node in G.vertices:
        node.status = 0

# Tests

def create_graph():
    s = Node("s",[], 0)
    a = Node("a",[], 0)
    b = Node("b",[], 0)
    c = Node("c",[], 0)
    d = Node("d",[], 0)

    G = Graph([a,b,c,d,s])

    s.edges = [Edge(a, 8), Edge(b, 7)]
    a.edges = [Edge(b, 10)]
    b.edges = [Edge(c, 5)]
    d.edges = [Edge(c, 2)]
    c.edges = [Edge(d, 3)]

    return G

def create_dag():
    a = Node("a",[], 0)
    b = Node("b",[], 0)
    c = Node("c",[], 0)
    d = Node("d",[], 0)
    e = Node("e",[], 0)
    f = Node("f",[], 0)

    G = Graph([a,b,c,d,e,f])

    a.edges = [Edge(b, 1), Edge(c, 1)]
    b.edges = [Edge(c, 1), Edge(d, 1), Edge(f, 1)]
    d.edges = [Edge(e, 1)]
    e.edges = [Edge(c, 1)]

    return G

def create_matrix_graph():
    a = MatrixNode("a", 0)
    b = MatrixNode("b", 0)
    c = MatrixNode("c", 0)
    d = MatrixNode("d", 0)
    e = MatrixNode("e", 0)
    f = MatrixNode("f", 0)

    G = MatrixGraph([a,b,c,d,e,f])

    G.put_edge("a","b",1)
    G.put_edge("a","c",2)
    G.put_edge("b","c",3)
    G.put_edge("b","d",4)
    G.put_edge("b","f",5)
    G.put_edge("d","e",6)
    G.put_edge("e","c",7)

    return G

def test_dfs():
    print("Test DFS")

    G = create_graph()
    test_search(dfs_path, G, G.vertices[0], "c")
    test_search(dfs_path, G, G.vertices[0], "e")
    test_search(dfs_path, G, G.vertices[1], "s")
    test_search(bfs_path, G, G.vertices[4], "d")

def test_bfs():
    print("Test BFS")
    G = create_graph()
    test_search(bfs_path, G, G.vertices[0], "c")
    test_search(bfs_path, G, G.vertices[0], "e")
    test_search(bfs_path, G, G.vertices[1], "s")
    test_search(bfs_path, G, G.vertices[4], "d")

def test_all_paths():
    print("Test BFS")
    def test(source, target_name):
        paths = all_paths(source, target_name)   
        print("All paths %s -> %s:" % (source.data, target_name))
        for path in paths:
            print(path)
        for node in G.vertices:
            node.status = 0
    G = create_dag()
    test(G.vertices[0], "c")
    test(G.vertices[0], "e")
    test(G.vertices[1], "s")
    test(G.vertices[1], "d")
    test(G.vertices[0], "f")

def test_dft():
    print("Test DFT")

    G = create_dag()
    dft(G.vertices[0])

def test_matrix_graph():
    print("Test MatrixGraph")   

    G = create_matrix_graph()
    for name in ["a","b","c","d","e","f","g"]:
        print("Lookup node %s: %s" % (name, G.find_node(name)))

    print("MatrixGraph.bfs")
    def test(source_name, target_name):
        print("Path %s -> %s: %s" % (source_name, target_name, G.dfs_path(source_name, target_name)))

    test("a", "c")
    test("a", "f")
    test("d", "e")
    test("b", "c")

test_dfs()
test_bfs()
test_all_paths()
test_dft()
test_matrix_graph()
