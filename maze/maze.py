import numpy as np
import random
import time
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Wall:
    def __init__(self) -> None:
        self.visited = True #Visited always true, so I don't have to check for cell or wall when checking unvisted neighbours
        self.val = u"\u2588"
class Cell:
    def __init__(self, visited=False) -> None:
        self.visited = visited
        self.val = " "
        self.searching = False  # For BFS/DFS visualization
        self.solution_path = False  # For final path visualization
        self.search_color = None  # Color for search branch
class Maze:
    def __init__(self, n: int, m: int, output=False):
        # Make sure there is an uneven amount of rows and columns such that it ends with a wall
        if (not n % 2):
            n += 1
        if (not m % 2):
            m += 1
        self.n = n
        self.m = m
        self.grid = []
        self.entry = (0,0)
        self.exit = (0,0)
        self.generate_maze(output)
    
    def unvisited_neighbours(self, pos: tuple, gap=1) -> list:
        x, y = pos
        lst = []
        if x-gap >= 0: # Checks the position is within the bounds
            if (not self.grid[x-gap][y].visited):
                lst.append((x-gap, y))
        if x+gap < self.n:
            if (not self.grid[x+gap][y].visited):
                lst.append((x+gap, y))
        if y-gap >= 0:
            if (not self.grid[x][y-gap].visited):
                lst.append((x, y-gap))
        if y+gap < self.m:
            if (not self.grid[x][y+gap].visited):
                lst.append((x, y+gap))
        return lst

    def remove_wall(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 - x2 > 0:
            self.grid[x1-1][y1] = Cell()
        elif x1 - x2 < 0:
            self.grid[x1+1][y1] = Cell()
        elif y1 - y2 > 0:
            self.grid[x1][y1-1] = Cell()
        elif y1 - y2 < 0:
            self.grid[x1][y1+1] = Cell()

    def reset_visited(self):
        for i in range(self.n):
            for j in range(self.m):
                if type(self.grid[i][j]) == Cell:
                    self.grid[i][j].visited = False
    
    def generate_maze(self, output):
        # Create a maze, where there is walls all around, and there is a cell on every other cell
        for i in range(self.n):
            line = []
            if i % 2:
                for j in range(self.m):
                    if j % 2:
                        line.append(Cell())
                    else:
                        line.append(Wall())
            else:
                line = [Wall() for x in range(self.m)]
            self.grid.append(line)

        # Find a random cell to start the DFS algorithm
        row, col = 0, 0
        while type(self.grid[row][col]) is not Cell:
            row, col = (random.randint(1, self.n-1), random.randint(1, self.m-1))
        self.grid[row][col].visited = True

        lst = [(row, col)] # DFS queue

        while len(lst) > 0: # Depth first backtrace algorithm to create the maze
            if output: # Prints the iterative process, if so desired
                self.print_maze(sleep=0.01)
            curr = lst.pop()
            neighbours = self.unvisited_neighbours(curr, gap=2) # Find the unvisited neighbours
            if neighbours:
                lst.append(curr)
                chosen = neighbours[random.randint(0, len(neighbours)-1)] # Choose a random neighbour
                self.remove_wall(curr, chosen) # Remove the wall between the two
                self.grid[chosen[0]][chosen[1]].visited = True
                lst.append(chosen)

        self.reset_visited()

        # Below we find a random entry and exit on opposing sides, until there is a neighbour for both.
        while ((len(self.unvisited_neighbours(self.entry)) == 0) | (len(self.unvisited_neighbours(self.exit)) == 0)):
            rand = random.randint(0, 1)
            if rand:
                col = random.randint(1, self.m-2)
                self.entry = (0, col)
                if col >= (self.m/2): # if the entry point is on the right side of the maze, we want the exit to be on the left side.
                    rand1 = random.randint(0, 1) # Random whether the exit is on the left wall or the bottom wall given the entry is right side of the top.
                    if rand1:
                        row = random.randint(int(self.n/2), self.n - 2)
                        self.exit = (row, self.m-1)
                    else:
                        col = random.randint(1, int(self.m/2))
                        self.exit = (self.n-1, col)
                else:
                    rand1 = random.randint(0, 1) # Random whether the exit is on the right wall or bottom, given the entry is on the left side of the top.
                    if rand1:
                        row = random.randint(int(self.n/2), self.n - 2)
                        self.exit = (row, self.m-1)
                    else:
                        col = random.randint(int(self.m/2), self.m-2)
                        self.exit = (self.n-1, col)
            else:
                row = random.randint(1, self.n-2)
                self.entry = (row, 0)
                if row >= (self.n/2): # if entry is on the bottom half of the maze
                    rand1 = random.randint(0, 1) # Random whether the exit is on the right wall or the top wall given the entry is on the bottom side of the left wall.
                    if rand1:
                        row = random.randint(1, int(self.n/2))
                        self.exit = (row, self.m-1)
                    else:
                        col = random.randint(int(self.m/2), self.m-2)
                        self.exit = (0, col)
                else:
                    rand1 = random.randint(0, 1) # Random whether the exit is on the right wall or bottom, given the entry is on the top side of the left wall.
                    if rand1:
                        row = random.randint(int(self.n/2), self.n - 2)
                        self.exit = (row, self.m-1)
                    else:
                        col = random.randint(int(self.m/2), self.m-2) 
                        self.exit = (self.n-1, col)
        # Make the entry and exit cells
        self.grid[self.entry[0]][self.entry[1]] = Cell()
        self.grid[self.entry[0]][self.entry[1]].visited = True
        self.grid[self.exit[0]][self.exit[1]] = Cell()
        self.reset_visited()
        if output:
            self.print_maze()

    def print_maze(self, sleep=0.1):
        time.sleep(sleep)
        print("\033[H\033[J", end="") # clear the cmd
        for i in range(self.n):
            line = ""
            for j in range(self.m):
                line += (self.grid[i][j].val)
            print(line)

if __name__ == '__main__':
    maze = Maze(50, 50, output=True)
    maze.print_maze()
