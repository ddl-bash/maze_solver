from line import *

class Cell():
    def __init__(self, x1, x2, y1, y2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = window
        self.visited = False
    
    def draw(self):
        Line(Point(self.x1, self.y1),Point(self.x1, self.y2)).draw(self.win, "black" if self.has_left_wall else "gray")
        Line(Point(self.x2, self.y1),Point(self.x2, self.y2)).draw(self.win, "black" if self.has_right_wall else "gray")
        Line(Point(self.x1, self.y1),Point(self.x2, self.y1)).draw(self.win, "black" if self.has_top_wall else "gray")
        Line(Point(self.x1, self.y2),Point(self.x2, self.y2)).draw(self.win, "black" if self.has_bottom_wall else "gray")
    
    def draw_move(self, other, undo=False):
        self_mid = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        other_mid = Point((other.x1 + other.x2) / 2, (other.y1 + other.y2) / 2)
        Line(self_mid, other_mid).draw(self.win, "white" if undo else "red")