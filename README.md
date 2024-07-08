# Minimum Vertex Cover Project

## Project Overview
This repository contains a project aimed at solving the Minimum Vertex Cover (MVC) problem using different approaches. The MVC problem is an NP-complete problem with applications in computer science, computational biology, and supply chain optimization. We implement and compare the performance of an exact algorithm, an approximation algorithm, and two local search algorithms.

## Table of Contents
- [Introduction](#introduction)
- [Problem Definition](#problem-definition)
- [Related Work](#related-work)
- [Algorithms](#algorithms)
  - [Branch and Bound](#branch-and-bound)
  - [Approximation Algorithm](#approximation-algorithm)
  - [Local Search: Hill Climbing](#local-search-hill-climbing)
  - [Local Search: Simulated Annealing](#local-search-simulated-annealing)
- [Empirical Evaluation](#empirical-evaluation)
  - [Branch and Bound](#branch-and-bound-1)
  - [Approximation Algorithm](#approximation-algorithm-1)
  - [Local Search](#local-search)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction
The Minimum Vertex Cover (MVC) problem involves finding a set of vertices in a graph such that each edge is incident to at least one vertex in the set. This problem has numerous applications across various fields, making it crucial to develop efficient algorithms for its solution.

## Problem Definition
Given a graph \(G = (V, E)\), a vertex cover is a subset \(C \subseteq V\) such that every edge in \(E\) is incident to at least one vertex in \(C\). The goal is to find the smallest possible vertex cover.

## Related Work
The MVC problem has been extensively studied, with numerous algorithms developed for its solution. These range from exact methods to heuristics and approximation algorithms. Recent studies focus on improving the performance and accuracy of these methods.

## Algorithms
### Branch and Bound
Branch and bound is an exact algorithm that guarantees an optimal solution given sufficient computational time. It explores the search space by selecting nodes with the highest degree and deciding their inclusion in the vertex cover using a 2-approximation algorithm.

### Approximation Algorithm
The approximation algorithm provides a solution within a factor of 2 of the optimal solution. It works by iteratively adding vertices to the cover until all edges are covered.

### Local Search: Hill Climbing
Hill climbing is a local search algorithm that iteratively removes vertices from the cover to find a minimum vertex cover. It is prone to getting stuck in local optima but is efficient for smaller graphs.

### Local Search: Simulated Annealing
Simulated annealing is a probabilistic algorithm that avoids local optima by occasionally accepting worse solutions. It gradually reduces the probability of accepting worse solutions as iterations progress, aiming to converge on a global optimum.

## Empirical Evaluation
### Branch and Bound
The branch and bound algorithm was tested on various graph sizes, demonstrating high accuracy but increased computational time for larger graphs.

### Approximation Algorithm
The approximation algorithm was faster but less accurate compared to branch and bound. An improved version using a maximum degree greedy heuristic showed better performance.

### Local Search
Hill climbing and simulated annealing were evaluated for their efficiency and accuracy. Simulated annealing provided better accuracy, while hill climbing was faster.

## Discussion
The choice of algorithm depends on the required accuracy and available computational resources. Exact algorithms provide the best accuracy but are computationally expensive, while approximation and local search algorithms offer a trade-off between cost and accuracy.

## Conclusion
This project implemented and compared five different algorithms for solving the MVC problem. The exact branch and bound algorithm provided the highest accuracy, while local search algorithms offered a good balance between cost and accuracy for large graphs.

## References
1. Delbot, F., & Laforest, C. (2010). Analytical and experimental comparison of six algorithms for the vertex cover problem. Journal of Experimental Algorithmics, 15, 1-1.
2. Filiol, E., Franc, E., Gubbioli, A., Moquet, B., & Roblot, G. (2007). Combinatorial optimisation of worm propagation on an unknown network. International Journal of Computer Science, 2(2), 124-130.
3. Mustafa, W. (2021). Shrink: an efficient construction algorithm for minimum vertex cover problem. Information Sciences Letters, 10(2), 9.
4. Veytsman, B. (2016). LATEX Class for Association for Computing Machinery.
5. Wang, L., Hu, S., Li, M., & Zhou, J. (2019). An exact algorithm for minimum vertex cover problem. Mathematics, 7(7), 603.
