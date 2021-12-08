import sys

class MazeCell:
	def __init__(self):
		self.visited: bool = False
		self.is_walkable: bool = False
	def __repr__(self):
		str(int(not self.is_walkable))

class Maze:
	def __init__(self, width: int, height: int):
		self.width: int = width
		self.height: int = height
		self.start_location: tuple[int, int] = (0, 0)
		self.cells: list[list[MazeCell]] = [[MazeCell() for _ in range(width)] for _ in range(height)]
	def get_locations_adjacent_to(self, location: tuple[int, int]) -> list[tuple[int, int]]:
		adjacent_locations = [
			(location[0], location[1] - 1)
			(location[0], location[1] + 1)
			(location[0] - 1, location[1])
			(location[0] + 1, location[1])
		]
		return [adjacent_location for adjacent_location in adjacent_locations if 0 <= adjacent_location[0] < self.width and 0 <= adjacent_location[1] < self.height]
	def get_cell_at(self, location: tuple[int, int]) -> MazeCell:
		return self.cells[location[1]][location[0]]

if __name__ == "__main__":
	width, height = 50, 50
	save_location = "map.txt"
	if len(sys.argv) > 2:
		width, height = sys.argv[1], sys.argv[2]
	elif len(sys.argv) > 1:
		width, height = sys.argv[1], sys.argv[1]
	if len(sys.argv) > 3:
		save_location = sys.argv[3]
	print(f"Generating a maze of width {width} and height {height} to {save_location}.")
