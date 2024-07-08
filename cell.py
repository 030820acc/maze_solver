# from line import Line
# from point import Point

# class Cell:
#     def __init__(self, x1, x2, y1, y2, window, top=True, bottom=True, left=True, right=True):
#         self.has_left_wall = left
#         self.has_right_wall = right
#         self.has_top_wall = top
#         self.has_bottom_wall = bottom
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2
#         self._top_left = Point(x1, y1)
#         self._top_right = Point(x2, y1)
#         self._bottom_right = Point(x2, y2)
#         self._bottom_left = Point(x1, y2)
#         self._top = Line(self._top_left, self._top_right)
#         self._bottom = Line(self._bottom_left, self._bottom_right)
#         self._right = Line(self._top_right, self._bottom_right)
#         self._left = Line(self._top_left, self._bottom_left)
#         self._window = window

#     def draw(self):
#         canvas = self._window.canvas
#         if self.has_top_wall != False:
#             self._window.draw_line(self._top, "black")
#         if self.has_bottom_wall:
#             self._window.draw_line(self._bottom, "black")
#         if self.has_left_wall:
#             self._window.draw_line(self._left, "black")
#         if self.has_right_wall:
#             self._window.draw_line(self._right, 'black')

#     def move_draw(self, to_cell, undo=False):
#         self_center = Point((self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2)
#         other_center = Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y2 + to_cell._y1) / 2)
#         new_line = Line(self_center, other_center)
#         if undo:
#             self._window.draw_line(new_line, "red")
#         else:
#             self._window.draw_line(new_line, "black")
from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)