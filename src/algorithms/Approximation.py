import time

class Approximation:

    def __init__(self, graph, solution_file, trace_file):
        self.G = graph
        self.solution_file_name = solution_file
        self.trace_file_name = trace_file
        self.cover = []

    def run(self):
        start_time = time.time()
        # self.cover = self.approx_vertex_cover(self.G)
        self.cover = self.approx_vertex_cover_max_degree(self.G)
        end_time = time.time()
        print('Approximation: ' + str(len(self.cover)))
        print('Time: ' + str(end_time - start_time))
        self.write_solution_file()
        self.write_trace_file()

    def write_solution_file(self):
        with open(self.solution_file_name, 'w') as f:
            f.write(str(len(self.cover)) + '\n')
            f.write(' '.join(map(str, self.cover)))

    def write_trace_file(self):
        with open(self.trace_file_name, 'w') as f:
            f.write('0.0 ' + str(len(self.cover)) + '\n')

    def approx_vertex_cover(self, G):
        """Approximate vertex cover of a graph G.

        Parameters
        ----------
        G: networkx graph
            Undirected graph.

        Returns
        -------
        cover: list
            List of nodes in the vertex cover.

        Notes
        -----
        This algorithm computes a vertex cover of size at most twice the
        optimal vertex cover. It is based on the following greedy algorithm:
            1. Pick an arbitrary node.
            2. Remove all edges incident to the node.
            3. Repeat until all edges are removed.
        """
        cover = []
        while G.edges():
            # Pick an arbitrary edge (u, v).
            u, v = list(G.edges())[0]
            # Add u and v to the cover.
            cover.append(u)
            cover.append(v)
            # remove all edges incident to u and v.
            incident_edges = list(G.edges(u)) + list(G.edges(v))
            G.remove_edges_from(incident_edges)
        return cover

    def max_degree_node(self, G):
        """Find the node with maximum degree.
        
        Parameters
        ----------
        G: networkx graph
            Undirected graph.

        Returns
        -------
        n_max_d: int
            The node with maximum degree.
        """
        max_degree = 0
        max_degree_node = 0
        for node in G.nodes():
            if G.degree(node) > max_degree:
                max_degree = G.degree(node)
                max_degree_node = node
        return max_degree_node

    def approx_vertex_cover_max_degree(self, G):
        """Approximate vertex cover of a graph G using max degree Greedy algorithm.
        
        Parameters
        ----------
        G: networkx graph
            Undirected graph.

        Returns
        -------
        cover: list
            List of nodes in the vertex cover.
            
        Notes
        -----
            1. Pick the node with maximum degree.
            2. Remove all edges incident to the node.
            3. Repeat until all edges are removed.
        """
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