import networkx as nx # used for useful functions for graphs in code(check connectivity, isomorphism)

"""
input: graph G, motif_list - list of motifs(each motif is a list with tuples represent edges)
output: return true if found a motif in motif_list which is isomorphic to G, else false
"""
def check_if_isomorphism_not_exists(G, motif_list):
    temp_G = nx.DiGraph() # we create a graph that stores edges of each motif, it is useful when we want to check if G isomorphic to motif
    temp_G.add_nodes_from(list(range(1, len(G.nodes)+1)))
    isom_flag = True # we use this flag to indicate if we have not found a motif in list which is isomorphic to G
    for i in motif_list:
        temp_G.add_edges_from(i)
        if(nx.is_isomorphic(G, temp_G)): # we check if G isomorphic to motif
            isom_flag = False # found a motif isomorphic to graph, and flag set to false
        temp_G.remove_edges_from(i)
    return isom_flag

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
input: positive integer n
output: generates all different connected sub-graphs of size n 
"""
def print_motifs(n):
    edges = []
    for i in range(1, n+1): # loop that add all the possible edges except of self-edges
        for j in range(1, n+1):
            if(i != j):   
                edges.append((i, j))
    allcomb = list(powerset(edges)) # gets a list of all possible sub-graphs
    for i in allcomb:
        if(len(i) < n-1): # if subgraph contains less than (n-1) edges, we can say that it is not connected
            allcomb.remove(i)

    motif_list = []
    count = 0
    G = nx.DiGraph()
    G.add_nodes_from(list(range(1, n+1)))
    
    for i in allcomb: # iterate through all subgrahps in list
        G.add_edges_from(i)
        is_connected = nx.is_weakly_connected(G) # check if subgraph is weakly connected( it means that if we relate its edges as not-direct, it is connectd graph)
        if(is_connected and check_if_isomorphism_not_exists(G, motif_list) and i != []): # we check if subgraph is weakly connected and not isomorphic to graphs we have already added to motif_list
            motif_list.append(list(G.edges)) # if true, we add subgraph edges list to motif_list
            count = count + 1 # we found one more motif, so we increment count
        G.remove_edges_from(i)


    print("n = " + str(n)) # print input paramater n       
    print("count = " + str(count)) # print number of different subgraphs/number of motifs
    counter = 1
    for i in motif_list: # iterate through motif_list, print each motif edges list
        print("#" + str(counter))
        counter = counter + 1
        for k in i: # print edges of motif
            print(str(k[0]) + " " + str(k[1]))
            
            
for n in range(1, 5): # call function print_motifs for n=1 to n=4 
    print_motifs(n)
