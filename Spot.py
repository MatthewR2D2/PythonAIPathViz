import pygame

class spot:
    def __init__(self, x, y, screen, row, cols, w, h):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1
        self.screen = screen
        self.row = row
        self.cols = cols
        self.w = w
        self.h = h

    def show(self, color, st):
        if self.closed == False :
            pygame.draw.rect(self.screen, color, (self.i * self.w, self.j * self.h, self.w, self.h), st)
            pygame.display.update()

    def path(self, color, st):
        pygame.draw.rect(self.screen, color, (self.i * self.w, self.j * self.h, self.w, self.h), st)
        pygame.display.update()

    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        if i < self.cols-1 and grid[self.i + 1][j].obs == False:
            self.neighbors.append(grid[self.i + 1][j])
        if i > 0 and grid[self.i - 1][j].obs == False:
            self.neighbors.append(grid[self.i - 1][j])
        if j < self.row-1 and grid[self.i][j + 1].obs == False:
            self.neighbors.append(grid[self.i][j + 1])
        if j > 0 and grid[self.i][j - 1].obs == False:
            self.neighbors.append(grid[self.i][j - 1])
