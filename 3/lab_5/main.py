# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:28:13 2022

@author: aelbadra
"""
# This import statement imports EightQueenGameSolver from eight_queen
from eight_queen import EightQueenGameSolver

# EightQueenGameSolver.brute_force_solution()

#### Using a Brute-Force Approach to finding a solution to the 8-Queen problem. Notice the amount of time taken.
# This statement calls the brute_force_solution_2 method on EightQueenGameSolver
# EightQueenGameSolver.brute_force_solution_2()

#### Using a hill climbing approach to find a solution from an initial state very close to a goal state.
# This statement calls the hill_climbing method on EightQueenGameSolver
# EightQueenGameSolver.hill_climbing([0, 4, 7, 5, 2, 6, 1, 3])

#### Using a hill climbing approach when the initial state is that all eight queens are on the first row.
# This statement calls the hill_climbing method on EightQueenGameSolver with 0s for starting values
# EightQueenGameSolver.hill_climbing([0, 0,0,0,0,0,0,0])


#### Using a repeated hill-climbing approach. 
#### Whenever hill climbing gets stuck at a local minimum, a new initial state is generated and hill climbing 
#### is recalled until a solution is found.
# This statement calls the restarting_hill_climbing method on EightQueenGameSolver with 0s for starting values
# EightQueenGameSolver.restarting_hill_climbing([0,0,0,0,0,0,0,0])


#### Using simulated annealing
# This statement calls the simulated_annealing method on EightQueenGameSolver
EightQueenGameSolver.simulated_annealing([0, 4, 7, 5, 2, 6, 1, 3])

# charrel5
# 4/1/2023
