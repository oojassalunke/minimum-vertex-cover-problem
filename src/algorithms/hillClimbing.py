# LS1
import os.path
import random as rd
from timeit import default_timer as timer
import random
import numpy as np
import dwave_networkx as dnx

# Check if vertex cover 
# def is_vertex_cover(G, cover):
#     for edge in G.edges():
#         if edge[0] not in cover and edge[1] not in cover:
#             return False
#     return True


# Hill climbing algo
def hillClimbing(graph, cutoff_time, randSeed, outPutName):   
    """Hill climbing algorithm for vertex cover problem."""
    random.seed(randSeed)
    
    trace_file = open('{}.trace'.format(outPutName), 'w')
    solution_file = open('{}.sol'.format(outPutName), 'w')
    # np.random.seed(self.seed)
    # cutoff = self.cutoff_time
    # start_time = time.time()
    G = graph
    cover = list(G.nodes())
    num_nodes = G.number_of_nodes()
    pq = list(G.nodes())
    pq.sort(key=lambda x: G.degree(x))
    start_time = timer()
    current = timer()

    # 2. Loop until the priority queue is empty or the cutoff time is reached
    while len(pq) != 0 and (current - start_time) < cutoff_time:
        # 3. Pick the node with the same degree as the first node in the priority queue
        l = []
        for node in pq:
            if G.degree(node) == G.degree(pq[0]):
                l.append(node)
            else:
                break

        # 4. Pick a random node from the list of nodes with the same degree
        node = np.random.choice(l)
        pq.remove(node)

        # 5. Remove the node from the vertex cover
        cover.remove(node)

        # 6. If the vertex cover is not valid, add the node back to the vertex cover
        if not dnx.is_vertex_cover(G, cover):
            cover.append(node)

        current = timer()
        # print('Current vertex cover: {}'.format(len(cover)))
        # print('Time: {}'.format(current - start_time), '\n')

        # Writting the trace file
        num_nodes_current = len(cover)
        if num_nodes_current < num_nodes:
            line = str(current - start_time) + ', ' + str(num_nodes_current) + '\n'
            trace_file.write(line)
        num_nodes = num_nodes_current

    end = timer()


    # write Solution and trace
    solution_file.write(str(num_nodes) + '\n')
    for num in cover:
        solution_file.write(str(num) + ',')

    # print(len(vc))
    solution_file.close()
    trace_file.close()
    # print('LS1')

    # opt = 2203
    # re = (len(cover)-opt)/opt
    run_time = end - start_time

    # print(f'Time: {run_time:.4}, VC Value: {len(vc)}, Relative Error: {re:.4}')
    print(f'{run_time:.4},{len(cover)}')

    return (end - start_time), len(cover)

# def hillClimbing(graph, cutoff_time, randSeed, outPutName):   
    # trace_file = open('{}.trace'.format(outPutName), 'w')
    # solution_file = open('{}.sol'.format(outPutName), 'w')

    # G = graph
    # num_nodes = G.number_of_nodes()
    # random.seed(randSeed)
    # start = timer()
    # vc = list(G.nodes())
    # pq = vc.copy()
    # random.shuffle(pq)
    # current = timer()
    # # print('Starting Hill Climb Algo')

    # while len(pq) != 0:
    #     # print(f'Printing time diff: {current-start}')
    #     # print('Starting while loop')
    #     node = pq[0]
    #     pq.pop(0)
    #     vc.remove(node)
    #     if (is_vertex_cover(G, vc)==False):
    #         vc.append(node)

    #     current = timer()
    #     # print(f'Time diff haylo')
        
    #     # Writting the trace file
    #     num_nodes_current = len(vc)
    #     if num_nodes_current < num_nodes:
    #         line = str(current - start) + ', ' + str(num_nodes_current) + '\n'
    #         trace_file.write(line)
    #     num_nodes = num_nodes_current

    #     # print(current - start)
    #     # Time Condition
    #     if current - start > cutoff_time:
    #         print('Cutoff was reached')
    #         break

    # end = timer()


    # # write Solution and trace
    # solution_file.write(str(num_nodes) + '\n')
    # for num in vc:
    #     solution_file.write(str(num) + ',')

    # # print(len(vc))
    # solution_file.close()
    # trace_file.close()
    # # print('LS1')
    # opt = 2203
    # re = (len(vc)-opt)/opt
    # run_time = end - start

    # # print(f'Time: {run_time:.4}, VC Value: {len(vc)}, Relative Error: {re:.4}')
    # print(f'{run_time:.4},{len(vc)}')

    # return (end - start), len(vc)


