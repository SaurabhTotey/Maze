import matplotlib.pyplot as plt

if __name__ == "__main__":
	maze = None
	with open("map.txt", "r") as file:
		maze = [[int(map_char) for map_char in line.strip()] for line in file.readlines()]
	plt.imshow(maze, cmap="Greys")
	plt.show()
