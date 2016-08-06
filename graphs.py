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

test_dfs()
test_bfs()
test_all_paths()
test_dft()
