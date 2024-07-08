# import os
import subprocess as sp
from csv import writer

# algo = ['LS1', 'LS2']

# algo = ['LS2']
# data_files = [
#     'jazz.graph', 'karate.graph', 'football.graph', 'as-22july06.graph',
#     'hep-th.graph', 'star.graph', 'star2.graph', 'netscience.graph',
#     'email.graph', 'delaunay_n10.graph', 'power.graph'
# ]


algo = ['LS1']
data_files = [
    'as-22july06.graph'
]

random_seed = list(range(70,80,10))
# print(random_seed)

for alg in algo:
    for data in data_files:
        for rnd in random_seed:
            comb = f'{alg}_{data}_{rnd}'

            run_str = f'python3 ./src/main.py -inst {data} -alg {alg} -time 600 -seed {rnd}'

            # os.system(run_str)
            output = sp.getoutput(run_str)
            # print("The exit code was: %d" % output.returncode)

            List = output.split(",")
            List.insert(0, comb)
            print (List)
            with open('result.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(List)
                f_object.close()