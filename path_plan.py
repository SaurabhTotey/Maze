import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap, BoundaryNorm

def copy_with_change(maze: list[list[int]], location: tuple[int, int], new_value: int) -> list[list[int]]:
	return [
		[
			new_value if x == location[0] and y == location[1] else maze[y][x] for x in range(len(maze[y]))
		] for y in range(len(maze))
	]

def distance_between(from_location: tuple[int, int], to_location: tuple[int, int]) -> float:
	return math.sqrt((from_location[0] - to_location[0]) ** 2 + (from_location[1] - to_location[1]) ** 2)

def path_plan_a_star(maze: list[list[int]]) -> list[list[list[int]]]:
	pathfinding_snapshots = []
	open_list = set([(1, 1)])
	closed_list = set()
	location_to_cost = {}
	location_to_parent = {(1, 1): None}
	while len(open_list) != 0:
		current_location = min(open_list, key=lambda location: location_to_cost[location])
		open_list.remove(current_location)
		closed_list.add(current_location)
		if current_location == (17, 17):
			pass # TODO:
		neighbors = [
			(current_location[0], current_location[1] - 1),
			(current_location[0], current_location[1] + 1),
			(current_location[0] - 1, current_location[1]),
			(current_location[0] + 1, current_location[1])
		]
		neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < 19 and 0 <= neighbor[1] < 19]
		neighbors = [neighbor for neighbor in neighbors if maze[neighbor[1]][neighbor[0]] != 1]
		for neighbor in neighbors:
			if neighbor in closed_list:
				continue
			neighbor_cost = location_to_cost[current_location] + 1 + distance_between(neighbor, (17, 17))
			if neighbor in open_list and neighbor_cost > location_to_cost[neighbor]:
				continue
			location_to_cost[neighbor] = neighbor_cost
			location_to_parent[neighbor] = current_location
			open_list.add(neighbor)
	return pathfinding_snapshots

if __name__ == "__main__":
	#Read maze
	maze = None
	with open("map.txt", "r") as file:
		maze = [[int(map_char) for map_char in line.strip()] for line in file.readlines()]

	#Set plotting colors
	colors = ["white", "black", "green", "red", "gray", "yellow"]
	colormap = ListedColormap(colors)

	#Mark starts and ends
	initial_state = copy_with_change(copy_with_change(maze, (1, 1), 2), (17, 17), 3)

	#Show animation
	states = [initial_state] + path_plan_a_star(maze)
	figure = plt.figure()
	image_show = plt.imshow(maze, cmap=colormap, norm=BoundaryNorm(range(len(colors) + 1), len(colors)))
	def animation_function(frame_index):
		image_show.set_array(states[frame_index])
		return [image_show]
	animation = animation.FuncAnimation(figure, animation_function, frames=len(states))
	plt.show()
