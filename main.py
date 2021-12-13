import random
import sys
import generate_maze
import path_plan

if __name__ == "__main__":
	#Default values
	width, height = 29, 29
	maze_seed = int(random.random() * 1000)
	save_location = "PathAnimation.gif"

	#Read desired user values from program arguments
	if len(sys.argv) > 2:
		width, height = int(sys.argv[1]), int(sys.argv[2])
	elif len(sys.argv) > 1:
		width, height = int(sys.argv[1]), int(sys.argv[1])
	if len(sys.argv) > 3:
		maze_seed = int(sys.argv[3])
	if len(sys.argv) > 4:
		save_location = sys.argv[4]

	#Check that width and height are indeed odd
	if width % 2 == 0 or height % 2 == 0:
		print("Cannot generate a maze with an even width or height.")
		exit()

	#Generates the maze and converts it into a readable format
	maze_object = generate_maze.Maze(width, height)
	maze = [[int(map_char) for map_char in line] for line in repr(maze_object).split("\n")]

	#Animation
	path_plan.animate_a_star(maze, save_location)
