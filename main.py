from display import Window
from maze     import Maze


def main():
	screen_width = 1280
	screen_height = 750
	left_margin = 15
	top_margin = 0
	num_rows = 15
	cells_per_row = 25
	cell_width = 50 #(screen_width - (left_margin * 2)) / cells_per_row
	cell_height = 50 #(screen_height - (top_margin * 2)) / num_rows
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
	maze.start(14, 24)
	window.wait_for_close() #last, anything drawn after wont show


main()