from display import Window
from maze     import Maze


def main():
	screen_width = 1280
	screen_height = 750
	left_margin = 15
	top_margin = 0
	num_rows = 30
	cells_per_row = 50
	cell_width = (screen_width - (left_margin * 2)) / cells_per_row
	cell_height = (screen_height - (top_margin * 2)) / num_rows
	window = Window(screen_width, screen_height)

	maze = Maze(
		left_margin,
		top_margin,
		num_rows,
		cells_per_row,
		cell_width,
		cell_height,
		window
	)
	maze.start(29, 49)
	window.wait_for_close() #last, anything drawn after wont show


main()