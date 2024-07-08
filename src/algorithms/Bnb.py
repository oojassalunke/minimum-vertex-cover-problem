#!/usr/bin/python
import time


class BnB:
    def __init__(self, G, T_limit, sol, tr):
        self.sol = sol
        self.tr = tr
        self.G = G
        self.T_limit = T_limit
        self.solution = set()

    def approx_alg(self, G):
        VC = set()
        EC = set()

        for i, E in enumerate(G.edges()):
            u = E[0]
            v = E[1]
            if (u, v) not in EC and (v, u) not in EC:

                VC.add(u)
                VC.add(v)
                EC = EC.union(set(G.edges([u, v])))

        return len(VC)

    # def approx_alg(self, G):

    #     cover = []
    #     while G.edges():
    #         # Pick an arbitrary edge (u, v).
    #         u, v = list(G.edges())[0]
    #         # Add u and v to the cover.
    #         cover.append(u)
    #         cover.append(v)
    #         # remove all edges incident to u and v.
    #         incident_edges = list(G.edges(u)) + list(G.edges(v))
    #         G.remove_edges_from(incident_edges)
    #     return len(cover)

    def write_output(self, trace_set):

        sol_file = open(self.sol, "w")
        sol_file.write("%d\n" % len(self.solution))
        self.solution = sorted(list(self.solution))

        for i, j in enumerate(self.solution):
            if i != len(self.solution) - 1:
                sol_file.write("%d," % j)
            else:
                sol_file.write("%d" % j)

        tr_file = open(self.tr, "w")

        for i, j in enumerate(trace_set):
            if i != len(trace_set) - 1:
                tr_file.write("%.2f, %d\n" % (j[0], j[1]))
            else:
                tr_file.write("%.2f, %d" % (j[0], j[1]))

    def max_degree_node(self, G):

        max_degree = 0
        max_degree_node = 0
        for node in G.nodes():
            if G.degree(node) > max_degree:
                max_degree = G.degree(node)
                max_degree_node = node
        return max_degree_node

    def run(self):

        start = time.time()
        current_time = time.time() - start

        bound = self.G.number_of_nodes() - 1
        UB = bound
        optimal_solution = False

        trace_set = list()
        trace_set.append([current_time, UB])

        # Run approx solution to get initial set of vertices
        while time.time() < start + self.T_limit and not optimal_solution:
            # Find vertex with maximum degree
            selected_vertex = self.max_degree_node(self.G)

            # Option 1: Select current vertex in VC and build graph with current vertex deleted
            graph_1 = self.G.copy()
            graph_1.remove_node(selected_vertex)

            # Option 2: Don't Select current vertex in VC,instead select its neighbours. We build graph_2 with neighbours of current vertex deleted
            graph_2 = self.G.copy()
            neighbors = list(graph_2.neighbors(selected_vertex))
            graph_2.remove_nodes_from(neighbors)
            graph_2.remove_node(selected_vertex)

            # Using the 2-approximation algorithm we select a lower bound as twice the optimal solution
            solution_graph_1 = self.approx_alg(graph_1) / 2
            solution_graph_2 = self.approx_alg(graph_2) / 2

            # We need to decide which graph option gives us a better solution
            if solution_graph_1 + 1 <= solution_graph_2 + len(neighbors):
                self.solution.add(selected_vertex)
                self.G.remove_node(selected_vertex)
                LB = len(self.solution) + 2 * solution_graph_1

            else:
                for vertex in neighbors:
                    self.solution.add(vertex)
                self.G.remove_nodes_from(neighbors)
                self.G.remove_node(selected_vertex)
                LB = len(self.solution) + 2 * solution_graph_2

            # Update the lower bound
            if LB < bound:
                bound = LB
                current_time = time.time() - start
                trace_set.append([current_time, LB])

            if self.G.number_of_edges() == 0:
                print("Optimal Solution has been found")
                optimal_solution = True

        if not optimal_solution:
            print("Unable to find optimal solution within cuttoff time")

        self.write_output(trace_set)
