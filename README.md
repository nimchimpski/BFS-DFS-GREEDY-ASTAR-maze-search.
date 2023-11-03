# maze-solver
DFS and BFS search, with option to add GreedyBest and AStar heurisics - applicable to maze .txt files
Nicely outputs a .gif animation labelled with the heuristic used. 2 of these are clickable in the main source. 'mazegreedybest.gif' and 'mazeastar.gif'

[with maze4.txt] The Astar animation shows clearly how, despite being extremely near the solution, if a node's sunk path cost is high in comparison to another unexplored node which is a long way from the goal, the further node will get selected. So for this problem a weighted discount for the sunk cost might be an improvement.




