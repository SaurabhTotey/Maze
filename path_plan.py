import math
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap, BoundaryNorm

def copy_with_change(maze: list[list[int]], location: tuple[int, int], new_value: int) -> list[list[int]]:
	return [
		[
			new_value if x == location[0] and y == location[1] else maze[y][x] for x in range(len(maze[y]))
		] for y in range(len(maze))
	]

def distance_between(from_location: tuple[int, int], to_location: tuple[int, int]) -> float:
	return math.sqrt((from_location[0] - to_location[0]) ** 2 + (from_location[1] - to_location[1]) ** 2)

def path_plan_a_star(maze: list[list[int]], start_location: tuple[int, int], end_location: tuple[int, int]) -> list[list[list[int]]]:
	pathfinding_snapshots = []
	previous_snapshot = copy_with_change(maze, (-1, -1), 0)
	open_list = set([start_location])
	closed_list = set()
	location_to_cost = {start_location: 0}
	location_to_parent = {start_location: None}
	while len(open_list) != 0:
		current_location = min(open_list, key=lambda location: location_to_cost[location])
		previous_snapshot = copy_with_change(previous_snapshot, current_location, 5)
		pathfinding_snapshots += [previous_snapshot]
		open_list.remove(current_location)
		closed_list.add(current_location)
		if current_location == end_location:
			while current_location != start_location:
				previous_snapshot = copy_with_change(previous_snapshot, current_location, 7)
				pathfinding_snapshots += [previous_snapshot]
				current_location = location_to_parent[current_location]
			pathfinding_snapshots += [copy_with_change(previous_snapshot, start_location, 7)]
			return pathfinding_snapshots
		neighbors = [
			(current_location[0], current_location[1] - 1),
			(current_location[0], current_location[1] + 1),
			(current_location[0] - 1, current_location[1]),
			(current_location[0] + 1, current_location[1])
		]
		neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(maze[0]) and 0 <= neighbor[1] < len(maze)]
		neighbors = [neighbor for neighbor in neighbors if maze[neighbor[1]][neighbor[0]] != 1]
		for neighbor in neighbors:
			if neighbor in closed_list:
				continue
			neighbor_cost = location_to_cost[current_location] + 1 + distance_between(neighbor, end_location)
			if neighbor in open_list and neighbor_cost > location_to_cost[neighbor]:
				continue
			pathfinding_snapshots += [copy_with_change(previous_snapshot, neighbor, 4)]
			location_to_cost[neighbor] = neighbor_cost
			location_to_parent[neighbor] = current_location
			open_list.add(neighbor)
		previous_snapshot = copy_with_change(previous_snapshot, current_location, 6)
	return pathfinding_snapshots

def animate_a_star(maze: list[list[int]], output_location: str):
	#Set plotting colors
	colors = ["white", "black", "green", "red", "cyan", "pink", "gray", "yellow"]
	colormap = ListedColormap(colors)

	#Gets starts and ends
	maze_height = len(maze)
	maze_width = len(maze[0])
	start_location = (1, 1)
	end_location = (maze_width - 2, maze_height - 2)

	#Show and Save animation
	states = [maze] + path_plan_a_star(maze, start_location, end_location)
	figure = plt.figure()
	image_show = plt.imshow(maze, cmap=colormap, norm=BoundaryNorm(range(len(colors) + 1), len(colors)))
	def animation_function(frame_index):
		image_show.set_array(states[frame_index])
		return [image_show]
	animation = FuncAnimation(figure, animation_function, frames=len(states), interval=64, repeat=False)
	plt.show()
	matplotlib.rcParams["animation.convert_path"] = r"/usr/bin/convert"
	animation.save(output_location, writer="imagemagick")

if __name__ == "__main__":
	#Default values
	maze_file = "map.txt"
	animation_save_location = "PathAnimation.gif"

	#Read desired user values from program arguments
	if len(sys.argv) > 1:
		maze_file = sys.argv[1]
	if len(sys.argv) > 2:
		animation_save_location = sys.argv[2]

	#Read maze and generate the animation
	maze = None
	with open(maze_file, "r") as file:
		maze = [[int(map_char) for map_char in line.strip()] for line in file.readlines()]
	animate_a_star(maze, animation_save_location)
