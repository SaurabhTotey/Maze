# Maze

![Animation of A* on 29 by 29 maze](./PathAnimation.gif)

## Quick Run
To get started, an A* visualization can be generated by running the `main.py` script. There are optional arguments of
maze width (integer), maze height (integer), maze seed (integer), and save location (string). Width and height must be
odd. The default values are respectively 29, 29, random, and `./PathAnimation.gif`.

## Maze Generation
Mazes can be generated with the `generate_maze.py` script. There are optional arguments of width (integer), height
(integer), seed (integer), and save location (string). Width and height must be odd. The default values are respectively
51, 51, random, and `./map.txt`. Mazes are generated with the Hunt-and-Kill algorithm. The saved mazes have `1`s in the
locations of obstacles and `0`s in the locations of free spaces.

## Path Planning
To run path planning on an already generated maze, use the `path_plan.py` script. The optional arguments are the input
file path (string), and the gif output save path (string). The default values are respectively `./map.txt` and
`./PathAnimation.gif`.
