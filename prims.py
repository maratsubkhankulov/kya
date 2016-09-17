import heaps
import graphs

# Prim's algorithm finds the minimum spanning tree in a weighted undirected graph.

# The simple version of Prim's uses an adjacency matrix and a list of weighted edges
# Run time complexity is O(|V|) where |V| is the number of vertices
def simple_prim(G):
    C = {} # Cost of getting to v
    E = {} # Edge connecting v to previous nodes
    for node in G.nodes:
        C[node] = sys.maxint # infinity
        E[node] = None # no connecting edge

    F = [] # A forest is an array of trees
    Q = g.nodes[:] # Vertices which have not been included in F
    while len(Q) > 0:
        v = min(Q, key=Q.get)
        F.append(v)
        if E(v):
            F.append(E(v))
        neighbours = G.get_neighbours(v)
        for w in neighbours:
            if w in Q and G.get_cost(v, w) < C[w]:
                C[w] = G.get_cost(v, w)
                E[w] = G.get_edge(v, w)

    return F

# Heap prim uses adjancency matrix and heap of edges sorted by weight
# Run time complexity is O(|E|log|E|) where |E| is the number of edges
def heap_prim(G):
    return

def test():
    # Initialize a graph
    G = graphs.create_matrix_graph()
    G.print_graph()

    # Find minimum spanning tree using Prim's algorithm

if __name__ == "__main__":
    test()
