from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title = "Maze Solver"
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, color):
        line.draw(self.canvas, color)

    def redraw(self):
        self.root_widget.update()
        self.root_widget.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, color):
        canvas.create_line(
            self.point_one.x, 
            self.point_one.y,
            self.point_two.x,
            self.point_two.y,
            fill=color,
            width=2
        )


def main():
    win = Window(800, 600)
    point_a = Point(50, 50)
    point_b = Point(100, 100)
    line_a = Line(point_a, point_b)
    win.draw_line(line_a, "black")
    win.wait_for_close()


main()
