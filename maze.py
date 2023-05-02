from random   import seed, randrange
from time     import sleep
from cell     import Cell
from display  import Point, Line


class Maze():
	def __init__(
		self, 
		left_margin, 
		top_margin, 
		num_rows, 
		cells_per_row, 
		cell_width, 
		cell_height, 
		window=None,
		random_seed=None
	):
		self.__left = left_margin
		self.__top = top_margin
		self.__num_rows = num_rows
		self.__cells_per_row = cells_per_row
		self.__cell_width = cell_width
		self.__cell_height = cell_height
		self.__window = window
		self.cells = []
		self.__create_cells()
		self.__make_start_and_finish()
		if random_seed is not None:
			seed(random_seed)

	def __create_cells(self):
		x = self.__left
		y = self.__top
		for i in range(self.__num_rows):
			new_row = []
			for j in range(self.__cells_per_row):
				new_cell = Cell(
					x, 
					y, 
					x+self.__cell_width, 
					y+self.__cell_height, 
					self.__window
				)
				new_row.append(new_cell)
				x += self.__cell_width
			self.cells.append(new_row)
			x = self.__left
			y += self.__cell_height
			self.__animate()

	def __animate(self):
		if self.__window is None:
			return
		self.__window.refresh()
		#sleep(1/25)

	def __make_start_and_finish(self):
		start_cell = self.cells[0][0]
		start_cell.has_left_wall = False
		start_cell.draw_walls()

		finish_cell = self.cells[self.__num_rows-1][self.__cells_per_row-1]
		finish_cell.has_right_wall = False
		finish_cell.draw_walls()

		self.__animate()

	def __create_maze_recur(self, i=14, j=24):
		current_cell = self.cells[i][j]
		current_cell.visited = True
		for n in range(2):
			directions = []

			if i > 0:
				if self.cells[i-1][j].visited == False:
					directions.append('up')
			if j < self.__cells_per_row-1:
				if self.cells[i][j+1].visited == False:
					directions.append('right')
			if i < self.__num_rows-1:
				if self.cells[i+1][j].visited == False:
					directions.append('down')
			if j > 0:
				if self.cells[i][j-1].visited == False:
					directions.append('left')

			if len(directions) == 0:
				current_cell.draw_walls()
				return

			direction = directions[randrange(len(directions))]

			if direction == 'up':
				current_cell.has_top_wall = False
				current_cell.draw_walls()
				self.cells[i-1][j].has_bottom_wall = False
				self.cells[i-1][j].draw_walls()
				self.__animate()
				self.__create_maze_recur(i-1, j)
			elif direction == 'right':
				current_cell.has_right_wall = False
				current_cell.draw_walls()
				self.cells[i][j+1].has_left_wall = False
				self.cells[i][j+1].draw_walls()
				self.__animate()
				self.__create_maze_recur(i, j+1)
			elif direction == 'down':
				current_cell.has_bottom_wall = False
				current_cell.draw_walls()
				self.cells[i+1][j].has_top_wall = False
				self.cells[i+1][j].draw_walls()
				self.__animate()
				self.__create_maze_recur(i+1, j)
			elif direction == 'left':
				current_cell.has_left_wall = False
				current_cell.draw_walls()
				self.cells[i][j-1].has_right_wall = False
				self.cells[i][j-1].draw_walls()
				self.__animate()
				self.__create_maze_recur(i, j-1)

	def __reset_cells_visited(self):
		for row in self.cells:
			for cell in row:
				cell.visited = False

	def __solve(self, i=0, j=0, from_cell=None):
		line_color = 'limegreen'

		if from_cell is None:
			start_cell_center = self.cells[0][0].get_center()
			start_edge_point = Point(0, start_cell_center.y)
			start_line = Line(start_edge_point, start_cell_center)
			self.__window.draw_line(start_line, line_color)

		if i == self.__num_rows-1 and j == self.__cells_per_row-1:
			end_cell_center = self.cells[self.__num_rows-1][self.__cells_per_row-1].get_center()
			end_edge_point = Point(self.__window.width, end_cell_center.y)
			end_line = Line(end_cell_center, end_edge_point)
			self.__window.draw_line(end_line, line_color)
			print('\nSolved!')
			return True

		self.__animate()
		cell = self.cells[i][j]
		cell.visited = True
		solved = False

		# right
		if j < self.__cells_per_row-1 and not cell.has_right_wall:
			if self.cells[i][j+1].visited == False:
				cell.draw_move(self.cells[i][j+1])
				self.__animate()
				solved = self.__solve(i, j+1, cell)
				if solved:
					return True
		# down
		if i < self.__num_rows-1 and not cell.has_bottom_wall:
			if self.cells[i+1][j].visited == False:
				cell.draw_move(self.cells[i+1][j])
				self.__animate()
				solved = self.__solve(i+1, j, cell)
				if solved:
					return True
		# up
		if i > 0 and not cell.has_top_wall:
			if self.cells[i-1][j].visited == False:
				cell.draw_move(self.cells[i-1][j])
				self.__animate()
				solved = self.__solve(i-1, j, cell)
				if solved:
					return True
		# left
		if j > 0 and not cell.has_left_wall:
			if self.cells[i][j-1].visited == False:
				cell.draw_move(self.cells[i][j-1])
				self.__animate()
				solved = self.__solve(i, j-1, cell)
				if solved:
					return True
		if not solved:
			cell.draw_move(from_cell, True)
		return False

	def start(self, i=14, j=24):
		self.__create_maze_recur(i, j)
		self.__reset_cells_visited()
		self.__solve()