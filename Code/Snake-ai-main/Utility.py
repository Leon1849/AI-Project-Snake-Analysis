from Constants import NO_OF_CELLS


class Node:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.h = 0
        self.g = 0
        self.f = 1000000
        self.parent = None

    def print(self):
        print(f"x: {self.x} y: {self.y}")

    def equal(self, b):
        return self.x == b.x and self.y == b.y

    def __lt__(self, other):
        return self.f < other.f
    
    def update_node(self, parent, g, h):
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h


class Grid:
    def __init__(self):
        self.grid = []

        for i in range(NO_OF_CELLS):
            col = []
            for j in range(NO_OF_CELLS):
                col.append(Node(i, j))
            self.grid.append(col)
