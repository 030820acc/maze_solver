import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_zero_rows(self):
        num_cols = 5
        num_rows = 0
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_cols
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows
        )

    def test_break_start_and_end(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze._break_entry_and_exit()
        self.assertEqual(
            maze._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            maze._cells[-1][-1].has_bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()