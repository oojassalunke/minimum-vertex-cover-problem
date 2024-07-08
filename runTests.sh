#!/bin/bash
Files=`ls ./DATA/`

for file in $Files
	do
		if [ $file != "ExampleSolutions" ]
		then
			echo "Running tests for $file"
			python3 ./src/main.py -inst $file -alg BnB -time 1500 -seed 1
		fi
	done
