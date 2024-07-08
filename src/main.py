#!/usr/bin/python
# CSE 6140 Fall 2022 Project: Main Script

import os
import sys

import networkx as nx

from algorithms.Approximation import Approximation
from algorithms.Bnb import BnB
from algorithms.greedy import greedy
from algorithms.hillClimbing import hillClimbing


class Main:

    def __init__(self, args):

        self.filename = args[2]
        self.method = args[4]

        self.cutoff = float(args[6])
        self.seed = args[8]

        self.G = nx.Graph()

    def run(self):
        # self.check()
        self.read_graph()
        self.call_appropriate_algorithm()

    def read_graph(self):
        with open('./DATA/' + self.filename, 'r') as f:
            for i, line in enumerate(f):
                if i > 0 and len(line.split()) != 0:
                    self.G.add_edges_from([(i, int(j)) for j in line.split()])
                    self.G.add_node(i)

    def call_appropriate_algorithm(self):
        instance = self.filename.split('.')[0]
        if self.method == 'BnB':
            sol = './output/BnB/' + instance + '_BnB_' + str(int(
                self.cutoff)) + '.sol'
            tr = './output/BnB/' + instance + '_BnB_' + str(int(
                self.cutoff)) + '.trace'
            solver = BnB(self.G, self.cutoff, sol, tr)
            solver.run()
        elif self.method == 'Approx':
            sol = './output/Approx/' + instance + '_Approx.sol'
            tr = './output/Approx/' + instance + '_Approx.trace'
            solver = Approximation(self.G, sol, tr)
            solver.run()
        elif self.method == 'LS1':
            output = './output/LS1/' + instance + '_LS1HC_' + str(
                int(self.cutoff)) + '_' + str(self.seed)
            hillClimbing(self.G, self.cutoff, self.seed, output)
        elif self.method == 'LS2':
            output = './output/LS2/' + instance + '_LS2G_' + str(
                int(self.cutoff)) + '_' + str(self.seed)
            greedy(self.G, self.cutoff, self.seed, output)

    def check(self):
        # check if minimum number of arguments have been supplied
        if len(sys.argv) < 7:
            print('Error: not enough input arguments')
            exit(1)

        if self.method not in ['BnB', 'Approx', 'LS1', 'LS2']:
            print('Error: incorrect algorithm type')
            exit(1)

        if self.method != 'BnB' and len(sys.argv) < 8:
            print('Error: random seed not supplied')
            exit(1)

        if self.cutoff < 600:
            print('Error: cutoff time is too short')
            if self.method == 'BnB':
                print('Setting cutoff time to 1200 for BnB')
                self.cutoff = 1200
            else:
                print('Setting cutoff time to 600')
                self.cutoff = 600

        if os.path.isfile('./DATA/' + self.filename) is False:
            print('Error: cannot find input file')
            exit(1)


if __name__ == '__main__':
    main = Main(sys.argv)
    main.run()
