# LS2
from operator import itemgetter
import os.path
import random
from timeit import default_timer as timer
import numpy as np
import math
import dwave_networkx as dnx

# Check if vertex cover 
# def is_vertex_cover(G, cover):
#     for edge in G.edges():
#         if edge[0] not in cover and edge[1] not in cover:
#             return False
#     return True

def approx_vertex_cover_max_degree(G):
    cover = []
    while G.edges():
        # Pick a vertex with maximum degree
        n_max_d = max(G.degree(), key=lambda x: x[1])[0]
        # Add the node to the cover
        cover.append(n_max_d)
        # remove all edges incident to the node
        incident_edges = list(G.edges(n_max_d))
        G.remove_edges_from(incident_edges)
    return cover

def greedy(graph, cutoff, randSeed, outPutName):
    trace_file = open('{}.trace'.format(outPutName), 'w')
    solution_file = open('{}.sol'.format(outPutName), 'w')
    random.seed(randSeed)

    start_time = timer()
    G = graph
    num_nodes = G.number_of_nodes()
    current = timer()

    # the initial vertex cover from the approximat
    vc = approx_vertex_cover_max_degree(G.copy())

    # print('Initial vertex cover: {}'.format(len(vc)))
    # the initial temperature is the number of nodes
    T = 1.0
    # the end temperature is 0
    Tf = 0.0000001
    # the temperature decrease ratio is 0.99
    alpha = 0.999

    # while the temperature is greater than the end temperature
    while T > Tf and (current - start_time) < cutoff:
        # randomly select one vertex
        v = np.random.choice(G.nodes())

        # if the vertex is in the cover, remove it
        if v in vc:
            vc_star = vc.copy()
            vc_star.remove(v)
            # if the vertex cover is not valid, add it back
            if dnx.is_vertex_cover(G, vc_star):
                vc = vc_star
        else:
            # if the probability is larger than a random value between 0 and 1, add the vertex to the cover
            p = np.exp(-(1+G.degree(v)) / T)
            if p > np.random.uniform(0, 1):
                vc.append(v)

        # decrease the temperature by the temperature decrease ratio
        T *= alpha

        # Writting the trace file
        current = timer()
        num_nodes_current = len(vc)
        if num_nodes_current < num_nodes:
            line = str(current - start_time) + ', ' + str(num_nodes_current) + '\n'
            trace_file.write(line)
        num_nodes = num_nodes_current

        # print(current - start)

        # Time Condition
        if current - start_time > cutoff:
            print('Cutoff was reached')
            break

    end = timer()
    # print(vc)

    # write Solution and trace
    solution_file.write(str(num_nodes) + '\n')
    for num in vc:
        solution_file.write(str(num) + ',')

    solution_file.close()
    trace_file.close()

    # print(len(vc))
    # opt = 594
    # re = (len(vc)-opt)/opt
    run_time = end - start_time
    # print(run_time)
    # print(f'Time: {run_time:.4}, VC Value: {len(vc)}, Relative Error: {re:.4}')
    print(f'{run_time:.4},{len(vc)}')

    return (end - start_time), len(vc)


# def greedy(graph, cutoff, randSeed, outPutName):
#     # Simulated Annealing
#     random.seed(randSeed)
#     start = timer()
#     trace_file = open('{}.trace'.format(outPutName), 'w')
#     solution_file = open('{}.sol'.format(outPutName), 'w')
    
#     G = graph
#     num_nodes = G.number_of_nodes()
#     vc = list(G.nodes)
#     v_list = list(G.nodes)
#     E = 0.1 #end temp
#     temperature = 1 #starting temperature 
#     alpha = 0.99 #temperature decrease ratio
#     # while(temperature>E):
#     #     v = random.choice(v_list)
#     #     if(v in vc):
#     #         vc.remove(v)
#     #         if (is_vertex_cover(G, vc)==False):   #if not valid, add node back to vertex cover
#     #             vc.append(v)
#     #         else: continue
#     #     else:
#     #         vc.append(v)
#     #         p = math.exp( - ( 1 + G.degree(v) ) / temperature)
#     #         if (p< random.uniform(0, 1)):
#     #             vc.remove(v)
#     #     current = timer()
#     #     temperature = temperature*alpha 
    
#     while(temperature>E):
#         v = random.choice(vc)
#         if(v not in vc):
#             delta = G.degree(v)
#             p = math.exp(-delta/temperature)
#             if (p>random.uniform(0, 1)):
#                 vc.append(v)
#         else:
#             vc.remove(v)
#             if (is_vertex_cover(G, vc)==False):
#                 vc.append(v)
#         temperature = temperature*alpha 

#         # Writting the trace file
#         current = timer()
#         num_nodes_current = len(vc)
#         if num_nodes_current < num_nodes:
#             line = str(current - start) + ', ' + str(num_nodes_current) + '\n'
#             trace_file.write(line)
#         num_nodes = num_nodes_current

#         # print(current - start)

#         # Time Condition
#         if current - start > cutoff:
#             print('Cutoff was reached')
#             break

#     end = timer()
#     # print(vc)
#     # write Solution and trace
#     solution_file.write(str(num_nodes) + '\n')
#     for num in vc:
#         solution_file.write(str(num) + ',')

#     solution_file.close()
#     trace_file.close()

#     # print(len(vc))
#     opt = 594
#     re = (len(vc)-opt)/opt
#     run_time = end - start
#     # print(run_time)
#     # print(f'Time: {run_time:.4}, VC Value: {len(vc)}, Relative Error: {re:.4}')
#     print(f'{run_time:.4},{len(vc)}')

#     return (end - start), len(vc)




