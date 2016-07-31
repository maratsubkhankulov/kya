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
    a.edges = [Edge(b, 10), Edge(s, 1)]
    b.edges = [Edge(c, 5)]
    d.edges = [Edge(c, 2)]
    c.edges = [Edge(d, 3)]

    return G

def dfs(current_node, goal_node_name):
    result = None
    if current_node.data == goal_node_name:
        return current_node 
    else:
        current_node.status = 1
        for edge in current_node.edges:
            neighbour = edge.to
            if neighbour.status == 0:
                result = dfs(neighbour, goal_node_name)
                if result:
                    break
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

def bfs_construct_path(node):
    path = []
    while True:
        path.insert(0, node.data)
        if node.search_parent != None:
            node = node.search_parent
        else:
            break
    return path

def test_search(algo, starting_node, target_name):
    result = algo(starting_node, target_name)
    print("Path %s -> %s: %s" % (starting_node.data, target_name, result != None))

def test_dfs():
    print("Test DFS")

    G = create_graph()
    test_search(dfs, G.vertices[0], "c")
    G = create_graph()
    test_search(dfs, G.vertices[0], "e")
    G = create_graph()
    test_search(dfs, G.vertices[1], "s")

def test_bfs():
    print("Test BFS")
    G = create_graph()
    test_search(dfs, G.vertices[0], "c")
    test_search(dfs, G.vertices[0], "c")
    test_search(dfs, G.vertices[0], "c")

test_dfs()
test_bfs()
