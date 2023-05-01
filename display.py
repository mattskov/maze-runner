from tkinter import Tk, BOTH, Canvas


class Window():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.__root = Tk()
		self.__root.title('Maze Solver') #or screenName?
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
		self.__canvas = Canvas(
			master=self.__root,
			width=width, 
			height=height,
			bg='black'
			)
		self.__canvas.pack(fill=BOTH, expand=1)
		self.is_running = False

	def refresh(self):
		self.__root.update_idletasks()
		self.__root.update()

	def wait_for_close(self):
		self.is_running = True
		while self.is_running:
			self.refresh()

	def close(self):
		self.is_running = False
		print('Closed')

	def draw_line(self, line, fill_color):
		line.draw(self.__canvas, fill_color)


class Point():
	def __init__(self, x, y):
		self.x = x # from left side of screen
		self.y = y # from top side of screen


class Line():
	def __init__(self, point_a, point_b):
		self.__point_a = point_a
		self.__point_b = point_b

	def draw(self, canvas, fill_color):
		x1 = self.__point_a.x
		y1 = self.__point_a.y

		x2 = self.__point_b.x
		y2 = self.__point_b.y

		canvas.create_line(
			x1, y1, x2, y2, fill=fill_color, width=2
		)
		canvas.pack(fill=BOTH, expand=1)