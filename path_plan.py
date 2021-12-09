import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

if __name__ == "__main__":
	#Read maze
	maze = None
	with open("map.txt", "r") as file:
		maze = [[int(map_char) for map_char in line.strip()] for line in file.readlines()]
	
	#Set plotting colors
	colors = ["white", "black", "green", "red"]
	colormap = ListedColormap(colors)

	#Mark starts and ends
	maze[1][1] = 2
	maze[17][17] = 3

	#Testing
	plt.imshow(maze, cmap=colormap, norm=BoundaryNorm(range(len(colors) + 1), len(colors)))
	plt.show()
