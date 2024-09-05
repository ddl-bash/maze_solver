import tkinter

class Window():
    def __init__(self, width, height):
        self.root = tkinter.Tk()
        self.root.title("Maze Solver")
        self.canvas = tkinter.Canvas(self.root, bg="gray", height=height, width=width)
        self.canvas.pack(fill=tkinter.BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

