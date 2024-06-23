from window import Window
from cell import Cell

def main():
    win = Window(1000, 800)
    cell1 = Cell(20, 70, 100, 150, win, left=False)
    cell2 = Cell(25, 300, 80, 500, win, top=False)
    cell3 = Cell(150, 200, 200, 300, win)
    cell1.draw()
    cell1.move_draw(cell3, undo=True)
    cell2.draw()
    cell3.draw()
    win.wait_for_close()


main()
