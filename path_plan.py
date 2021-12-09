import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap, BoundaryNorm

def copy_with_change(maze: list[list[int]], location: tuple[int, int], new_value: int) -> list[list[int]]:
	return [
		[
			new_value if x == location[0] and y == location[1] else maze[y][x] for x in range(len(maze[y]))
		] for y in range(len(maze))
	]

def path_plan_a_star(maze: list[list[int]]) -> list[list[list[int]]]:
	return [copy_with_change(maze, (13, 13), 4), copy_with_change(maze, (13, 13), 2), copy_with_change(maze, (13, 13), 5)]

if __name__ == "__main__":
	#Read maze
	maze = None
	with open("map.txt", "r") as file:
		maze = [[int(map_char) for map_char in line.strip()] for line in file.readlines()]

	#Set plotting colors
	colors = ["white", "black", "green", "red", "gray", "yellow"]
	colormap = ListedColormap(colors)

	#Mark starts and ends
	maze[1][1] = 2
	maze[17][17] = 3

	#Show animation
	states = [maze] + path_plan_a_star(maze)
	figure = plt.figure()
	image_show = plt.imshow(maze, cmap=colormap, norm=BoundaryNorm(range(len(colors) + 1), len(colors)))
	def animation_function(frame_index):
		image_show.set_array(states[frame_index])
		return [image_show]
	animation = animation.FuncAnimation(figure, animation_function, frames=len(states))
	plt.show()
