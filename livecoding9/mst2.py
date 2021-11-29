import networkx as nx
from uf import WeightedQuickUnionWithPathCompressionUF as UF

def Kruskal(filename):
    edge_list = []
    with open(filename) as f:
        maximum  = 0
        for edge in f:
            e = tuple(map(int, tuple(edge.strip().split(' '))))
            maximum2 = max(e[0],e[1]) 
            if maximum2 > maximum:
                maximum = maximum2
            edge_list.append(e)
    edge_list_sorted = sorted(edge_list, key = lambda t: t[2])
    unions = UF(maximum+1)
    mst = [] 
    for edge in edge_list_sorted:
        u = edge[0]
        v = edge[1]
        if not unions.connected(u,v):
            mst.append(edge)
            unions.union(u,v)

    return mst


G = nx.read_weighted_edgelist('edge_list.txt')
print(len(G))
mst = nx.minimum_spanning_tree(G)



print(len(Kruskal('edge_list.txt')))
print(len(mst))
