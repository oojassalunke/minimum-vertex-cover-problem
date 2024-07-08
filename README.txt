Language: Python 3.10
Libraries used: networkx, dwave_networkx

The main script can be executed from the root directory using the following command:
python ./src/main.py -inst <filename> -alg [BnB|Approx|LS1|LS2] -time <cutoff in seconds> -seed <random seed>

The output, a .sol file and a .trace file are generated in the output folder.

A random seed, an integer number, needs to be provided when using local search algorithms. The approximation algorithm is not randomized and ignores the random seed. 

Data files should be placed in the root folder titled 'Data'.

The script to run the local search algorithms (LS1 and LS2) to generate the tables in the report can be executed from the root directory using the following command:
python data_tables.py

The output from the 'data_tables.py' files are stored in two .csv files in the home directory called 'L1_results' and 'L2_results'. 
