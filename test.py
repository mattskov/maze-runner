import unittest
from maze import Maze


class Tests(unittest.TestCase):
	def test_maze_create_cells_10_10(self):
		num_rows = 10
		cells_per_row = 10
		maze = Maze(0, 0, num_rows, cells_per_row, 10, 10)
		self.assertEqual(
			len(maze.cells),
			num_rows,
		)
		self.assertEqual(
			len(maze.cells[0]),
			cells_per_row,
		)

	def test_maze_create_cells_20_40(self):
		num_rows = 20
		cells_per_row = 40
		maze = Maze(0, 0, num_rows, cells_per_row, 10, 10)
		self.assertEqual(
			len(maze.cells),
			num_rows,
		)
		self.assertEqual(
			len(maze.cells[0]),
			cells_per_row,
		)

	def test_maze_create_cells_1_100(self):
		num_rows = 1
		cells_per_row = 100
		maze = Maze(0, 0, num_rows, cells_per_row, 10, 10)
		self.assertEqual(
			len(maze.cells),
			num_rows,
		)
		self.assertEqual(
			len(maze.cells[0]),
			cells_per_row,
		)

	def test_maze_create_cells_100_1(self):
		num_rows = 100
		cells_per_row = 1
		maze = Maze(0, 0, num_rows, cells_per_row, 10, 10)
		self.assertEqual(
			len(maze.cells),
			num_rows,
		)
		self.assertEqual(
			len(maze.cells[0]),
			cells_per_row,
		)

	def test_maze_make_start(self):
		num_rows = 2
		cells_per_row = 2
		maze = Maze(0, 0, num_rows, cells_per_row, 100, 100)
		self.assertEqual(
			maze.cells[0][0].has_left_wall,
			False
		)
		self.assertEqual(
			maze.cells[0][0].has_right_wall,
			True
		)

	def test_maze_make_finish(self):
		num_rows = 2
		cells_per_row = 2
		maze = Maze(0, 0, num_rows, cells_per_row, 100, 100)
		self.assertEqual(
			maze.cells[num_rows-1][cells_per_row-1].has_right_wall,
			False
		)
		self.assertEqual(
			maze.cells[num_rows-1][cells_per_row-1].has_left_wall,
			True
		)

	# test will fail, bound method
	def test_maze_create_maze_recur(self):
		num_rows = 15
		cells_per_row = 25
		maze = Maze(0, 0, num_rows, cells_per_row, 100, 100)
		maze.__create_maze_recur(7, 12)
		for row in maze.cells:
			for cell in row:
				self.assertEqual(
					cell.visited,
					True
				)

	# test will fail, bound method
	def test_maze_reset_cells_visited(self):
		num_rows = 15
		cells_per_row = 25
		maze = Maze(0, 0, num_rows, cells_per_row, 100, 100)
		maze.__create_maze_recur(7, 12)
		maze.__reset_cells_visited()
		for row in maze.cells:
			for cell in row:
				self.assertEqual(
					cell.visited,
					False
				)


if __name__ == "__main__":
	unittest.main()