import sys

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
