from window import Window
from maze import Maze

win = Window(800, 600)

maze = Maze(50,50,25,35,20,20,win)
maze.break_entrance_and_exit()
maze.break_walls_r()
maze.reset_cells_visited()
maze.solve()

win.wait_for_close()