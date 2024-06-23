from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("Maze Solver")
        self.canvas = Canvas(height=height, width=width)
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
