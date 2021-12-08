import random
import sys
from itertools import chain

class MazeCell:

	def __init__(self):
		self.visited: bool = False
		self.is_walkable: bool = False

	def __repr__(self):
		return str(int(not self.is_walkable))

class Maze:

	def __init__(self, width: int, height: int):
		#Simple fields
		self.width: int = width
		self.height: int = height
		self.start_location: tuple[int, int] = (1, 1)
		self.cells: list[list[MazeCell]] = [[MazeCell() for _ in range(width)] for _ in range(height)]

		#Gets the locations of the necessarily traversable cells
		self.traversable_locations: set[tuple[int, int]] = set([self.start_location])
		new_traversable_locations = self.get_traversable_locations_adjacent_to(self.start_location)
		while len(new_traversable_locations) > 0:
			traversable_locations_to_get_adjacencies_of = []
			for new_traversable_location in new_traversable_locations:
				if new_traversable_location in self.traversable_locations:
					continue
				self.traversable_locations.add(new_traversable_location)
				traversable_locations_to_get_adjacencies_of.append(new_traversable_location)
			new_traversable_locations = list(chain.from_iterable([self.get_traversable_locations_adjacent_to(location) for location in traversable_locations_to_get_adjacencies_of]))

		#Generates the maze using the Hunt and Kill algorithm
		current_location = self.start_location
		unvisited_neighbor_locations = self.get_traversable_locations_adjacent_to(current_location)
		hunt_y = 1
		while current_location != None:
			#Random walk
			self.get_cell_at(current_location).visited = True
			self.get_cell_at(current_location).is_walkable = True
			while len(unvisited_neighbor_locations) > 0:
				new_location = unvisited_neighbor_locations[random.randrange(0, len(unvisited_neighbor_locations))]
				self.get_cell_at(new_location).visited = True
				self.get_cell_at(new_location).is_walkable = True
				location_difference = (int((new_location[0] - current_location[0]) / 2), int((new_location[1] - current_location[1]) / 2))
				intermediate_location = (current_location[0] + location_difference[0], current_location[1] + location_difference[1])
				self.get_cell_at(intermediate_location).visited = True
				self.get_cell_at(intermediate_location).is_walkable = True
				current_location = new_location
				unvisited_neighbor_locations = [location for location in self.get_traversable_locations_adjacent_to(current_location) if not self.get_cell_at(location).visited]
			#Hunt for new starting position
			current_location = None
			while hunt_y < self.height:
				for hunt_x in range(1, self.width, 2):
					hunt_location = (hunt_x, hunt_y)
					if self.get_cell_at(hunt_location).visited:
						unvisited_neighbor_locations = [location for location in self.get_traversable_locations_adjacent_to(hunt_location) if not self.get_cell_at(location).visited]
						if len(unvisited_neighbor_locations) > 0:
							current_location = unvisited_neighbor_locations[random.randrange(0, len(unvisited_neighbor_locations))]
							unvisited_neighbor_locations = [location for location in self.get_traversable_locations_adjacent_to(current_location) if not self.get_cell_at(location).visited]
							break;
				if current_location != None:
					break
				hunt_y += 2

	def __repr__(self):
		return "\n".join(["".join([repr(cell) for cell in row]) for row in self.cells])

	def is_location_valid(self, location: tuple[int, int]) -> bool:
		return 0 <= location[0] < self.width and 0 <= location[1] < self.height

	def get_traversable_locations_adjacent_to(self, location: tuple[int, int]) -> list[tuple[int, int]]:
		adjacent_locations = [
			(location[0], location[1] - 2),
			(location[0], location[1] + 2),
			(location[0] - 2, location[1]),
			(location[0] + 2, location[1])
		]
		return [adjacent_location for adjacent_location in adjacent_locations if self.is_location_valid(adjacent_location)]

	def get_cell_at(self, location: tuple[int, int]) -> MazeCell:
		return self.cells[location[1]][location[0]]

if __name__ == "__main__":
	width, height = 51, 51
	save_location = "map.txt"
	if len(sys.argv) > 2:
		width, height = sys.argv[1], sys.argv[2]
	elif len(sys.argv) > 1:
		width, height = sys.argv[1], sys.argv[1]
	if len(sys.argv) > 3:
		save_location = sys.argv[3]
	print(f"Generating a maze of width {width} and height {height} to {save_location}.")
	maze = Maze(width, height)
	print(maze)
	# TODO: visualize maze
	# TODO: save maze to argv[3]