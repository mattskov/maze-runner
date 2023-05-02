from display import Point, Line


class Cell():
	def __init__(
		self, 
		x1, 
		y1, 
		x2, 
		y2, 
		window=None, 
		top=True, 
		right=True, 
		bottom=True, 
		left=True
	):
		self.__window = window
		self.__left = x1
		self.__top = y1
		self.__right = x2
		self.__bottom = y2
		self.has_top_wall = top
		self.has_right_wall = right
		self.has_bottom_wall = bottom
		self.has_left_wall = left
		self.visited = False
		if self.__window is not None:
			self.draw_walls()

	def draw_walls(self, border_color='grey', bg_color='black'):
		if self.__window is None:
			return

		top_left_corner = Point(self.__left, self.__top)
		top_right_corner = Point(self.__right, self.__top)
		bottom_left_corner = Point(self.__left, self.__bottom)
		bottom_right_corner = Point(self.__right, self.__bottom)
		
		top_wall = Line(top_left_corner, top_right_corner)
		if self.has_top_wall:
			self.__window.draw_line(top_wall, border_color)
		else:
			self.__window.draw_line(top_wall, bg_color)

		right_wall = Line(top_right_corner, bottom_right_corner)
		if self.has_right_wall:
			self.__window.draw_line(right_wall, border_color)
		else:
			self.__window.draw_line(right_wall, bg_color)

		bottom_wall = Line(bottom_left_corner, bottom_right_corner)
		if self.has_bottom_wall:
			self.__window.draw_line(bottom_wall, border_color)
		else:	
			self.__window.draw_line(bottom_wall, bg_color)

		left_wall = Line(top_left_corner, bottom_left_corner)
		if self.has_left_wall:
			self.__window.draw_line(left_wall, border_color)
		else:
			self.__window.draw_line(left_wall, bg_color)

	def get_center(self):
		center_x = int((self.__left + self.__right)/2)
		center_y = int((self.__top + self.__bottom)/2)
		return Point(center_x, center_y)

	def draw_move(self, to_cell, undo=False):
		this_center = self.get_center()
		to_center = to_cell.get_center()
		color = 'darkred' if undo else 'limegreen'
		move_line = Line(this_center, to_center)
		self.__window.draw_line(move_line, color)