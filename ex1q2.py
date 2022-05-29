# Ilai Ahronovitz 325167641
import networkx as nx # used for useful functions for graphs in code(check connectivity, isomorphism)

"""
input: graph G, motif_list - list of motifs(each motif is a list with tuples represent edges)
output: return true if found a motif in motif_list which is isomorphic to G, else false
"""
def check_if_isomorphism_not_exists(G, motif_list):
    temp_G = nx.DiGraph()
    temp_G.add_nodes_from(list(range(1, len(G.nodes)+1)))
    isom_flag = True
    for i in motif_list:
        temp_G.add_edges_from(i)
        if(nx.is_isomorphic(G, temp_G)):
            isom_flag = False
        temp_G.remove_edges_from(i)
    return isom_flag

"""
input: graph G_graph, motif_list - list of motifs(each motif is a list with tuples represent edges)
"""
def find_isomorphism_motif(G_graph, motif_list):
    temp_G = nx.DiGraph()
    temp_G.add_nodes_from(list(range(1, len(G.nodes)+1)))
    isom_flag = True
    counter = 0
    ind = -1
    for i in motif_list:
        temp_G.add_edges_from(i)
        if(nx.is_isomorphic(G_graph, temp_G)):
            ind = counter
            break
        temp_G.remove_edges_from(i)
        counter = counter + 1
    return ind

"""
i did not write this funtion(link: https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset)
, i use this function in order to find all combinations of subgraphs
input: list of elements(in our case it is list of all possible edges except of self-edges)
output: generator object of all sub-lists
"""
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
"""
input: input positive integer N and a graph G_graph
"""
def print_motifs_and_instances(n, G_graph):
    edges = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if(i != j):   
                edges.append((i, j))
    allcomb = list(powerset(edges))
    for i in allcomb:
        if(len(i) < n-1):
            allcomb.remove(i)
        


    allGcomb = list(powerset(list(G_graph.edges)))
    count_sub_grahps = 0
    for i in allGcomb:
        if(len(i) < n-1):
            allGcomb.remove(i)

    motif_list = []
    comb_without_motifs = []
    count = 0
    G = nx.DiGraph()
    G.add_nodes_from(list(range(1, n+1)))
    for i in allcomb:
        G.add_edges_from(i)
        is_connected = nx.is_weakly_connected(G)
        if(is_connected and check_if_isomorphism_not_exists(G, motif_list)):
            motif_list.append(list(G.edges))
            count = count + 1
        G.remove_edges_from(i)

    motif_list_counter = [0] * count
    for i in allGcomb:
        G.add_edges_from(i)
        motif = find_isomorphism_motif(G, motif_list)
        if(motif > -1):
            motif_list_counter[motif] = motif_list_counter[motif] + 1
        G.remove_edges_from(i)    
    
    print("n = " + str(n))
    print("count = " + str(count))
    print("motifs: ")
    counter = 0
    for i in motif_list:
        print("#" + str(counter + 1) + " count = " + str(motif_list_counter[counter]))
        counter = counter + 1
        for k in i:
            print(str(k[0]) + " " + str(k[1]))
            
G = nx.DiGraph()

n = int(input('Enter positive integer number n: '))
G.add_nodes_from(list(range(1, n + 1)))

edges_str = input('Enter string of edges in graph: ')
edges_lst = edges_str.split()
edges_list = []
for i in range(0,len(edges_lst), 2):
    edges_list.append((edges_lst[i],edges_lst[i+1]))
G.add_edges_from(edges_list)
#edges_list = [(2,1),(3,1),(3,2)] # list of edges, every tuple represents edge

print_motifs_and_instances(n, G) 
