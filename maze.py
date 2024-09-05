from cell import Cell
from time import sleep
import random

WAIT_TIME = 0.01

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cells()
        random.seed(seed)
    
    def create_cells(self):
        global WAIT_TIME

        self.cells = []
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                x1 = self.x1 + self.cell_size_x * i
                x2 = self.x1 + self.cell_size_x * (i + 1)
                y1 = self.y1 + self.cell_size_y * j
                y2 = self.y1 + self.cell_size_y * (j + 1)
                if self.win:
                    col.append(Cell(x1, x2, y1, y2, self.win.canvas))
                else:
                    col.append("")
            self.cells.append(col)
        WAIT_TIME, temp = 0, WAIT_TIME
        for i, col in enumerate(self.cells):
            for j in range(len(col)):
                self.draw_cell(i, j)
        WAIT_TIME = temp
    
    def draw_cell(self, i, j):
        if self.win is None:
            return
        self.cells[i][j].draw()
        self.animate()
    
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(WAIT_TIME)

    def break_entrance_and_exit(self):
        i = len(self.cells) - 1
        j = len(self.cells[0]) - 1
        self.cells[0][0].has_left_wall = False
        self.draw_cell(0 ,0)
        self.cells[i][j].has_bottom_wall = False
        self.draw_cell(i, j)
    
    def break_walls_r(self, i=None, j=None):
        if i is None or j is None:
            i = self.num_cols // 10
            j = self.num_rows // 10
        self.cells[i][j].visited = True
        
        while True:
            to_visit = self.neighbors_to_visit(i, j)
            if not to_visit:
                self.draw_cell(i, j)
                return
            direction, next_i, next_j = to_visit.pop(random.choice(range(len(to_visit))))
            self.knock_down(i, j, direction)
            self.break_walls_r(next_i, next_j)
    
    def knock_down(self, i, j, direction):
        current_cell = self.cells[i][j]
        match direction:
            case "left":
                current_cell.has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
            case "right":
                current_cell.has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
            case "up":
                current_cell.has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
            case "down":
                current_cell.has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
    
    def neighbors_to_visit(self, i, j, solve=False):
        result = []
        # Check left
        if i > 0 and not self.cells[i - 1][j].visited:
            if not solve or not self.cells[i][j].has_left_wall and not self.cells[i - 1][j].has_right_wall:
                result.append(("left", i - 1, j))    
        # Check right
        if i < len(self.cells) - 1 and not self.cells[i + 1][j].visited:
            if not solve or not self.cells[i][j].has_right_wall and not self.cells[i + 1][j].has_left_wall:
                result.append(("right", i + 1, j))     
        # Check up
        if j > 0 and not self.cells[i][j - 1].visited:
            if not solve or not self.cells[i][j].has_top_wall and not self.cells[i][j - 1].has_bottom_wall:
                result.append(("up", i, j - 1))   
        # Check down
        if j < len(self.cells[i]) - 1 and not self.cells[i][j + 1].visited:
            if not solve or not self.cells[i][j].has_bottom_wall and not self.cells[i][j + 1].has_top_wall:
                result.append(("down", i, j + 1))
        
        return result
    
    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self.solve_r(0,0)
    
    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        exit_i = self.num_cols - 1
        exit_j = self.num_rows - 1
        if i == exit_i and j == exit_j:
            return True
        while True:
            to_visit = self.neighbors_to_visit(i, j, solve=True)
            if not to_visit:
                return False
            _, next_i, next_j = to_visit.pop(random.choice(range(len(to_visit))))
            self.cells[i][j].draw_move(self.cells[next_i][next_j])
            if self.solve_r(next_i, next_j):
                return True
            self.cells[i][j].draw_move(self.cells[next_i][next_j], undo=True)