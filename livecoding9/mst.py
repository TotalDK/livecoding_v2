import networkx as nx
from uf import WeightedQuickUnionWithPathCompressionUF as UF
#from algs4_uf import WeightedQuickUnionUF as UF 

G = nx.read_weighted_edgelist('edge_list.txt')


def Kruskal(Graph):
    edges=sorted(Graph.edges(data=True), key=lambda t: t[2]['weight'])
    maximum = max(list(map(lambda f: int(f),Graph.nodes())))+1
    unions = UF(maximum)
    
    mst = []
    for edge in edges:
        u = int(edge[0])
        v = int(edge[1])
        if not unions.connected(u,v):
            mst.append(edge)
            unions.union(u,v)


    return mst



print(len(G.edges()))
print(len(Kruskal(G)))

#Networkx
mst = nx.minimum_spanning_tree(G, weight='weight')
print(len(mst.edges()))
