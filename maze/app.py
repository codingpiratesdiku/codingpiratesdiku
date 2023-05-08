from maze import *
import pygame
from pygame.locals import *
class App:
    # Setup
    def __init__(self, size, print_visited) -> None:     
        self.print_visited = print_visited
        n, m = size
        self.maze = Maze(n, m)
        # The maze updates to always have an uneven amount, such that there are walls on the bottom and right side

        pygame.init() 
        window_width = 900
        window_height = 900
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.win_screen = pygame.image.load("./you_win.jpg")

        # Size of the cells: The maze edits the size to always be uneven such that there are walls on the edges
        self.block_width = window_width / self.maze.m
        self.block_height = window_height / self.maze.n

        # Current position
        self.pos = self.maze.entry

    # Updates the maze
    def update_maze(self) -> None:
        for y in range(self.maze.n):
            for x in range(self.maze.m):
                if x == self.pos[1] & y == self.pos[0]:
                    continue
                rect = pygame.Rect(x*self.block_width, y*self.block_height, self.block_width+1, self.block_height+1)
                if type(self.maze.grid[y][x]) == Cell: 
                    if self.print_visited:
                        if self.maze.grid[y][x].visited:
                            pygame.draw.rect(self.screen, 'pink', rect)
                        else:
                            pygame.draw.rect(self.screen, 'lightgray', rect)
                    else:
                        pygame.draw.rect(self.screen, 'lightgray', rect)
                elif type(self.maze.grid[y][x]) == Wall:
                    pygame.draw.rect(self.screen, 'black', rect)

        # print current cell
        y, x = self.pos
        rect = pygame.Rect(x*self.block_width, y*self.block_height, self.block_width+1, self.block_height+1)
        pygame.draw.rect(self.screen, 'red', rect)

    # Moves the position upwards if possible
    def move_up(self) -> None:
        i, j = self.pos
        if i-1 < 0:
            return self.pos
        if type(self.maze.grid[i-1][j]) == Cell:
            self.pos = (i-1, j)
            self.maze.grid[i-1][j].visited = True
        return self.pos
    
    # Moves the position down if possible
    def move_down(self) -> None:
        i, j = self.pos
        if i+1 >= self.maze.n:
            return
        elif type(self.maze.grid[i+1][j]) == Cell:
            self.pos = (i+1, j)
            self.maze.grid[i+1][j].visited = True

    def move_left(self) -> None:
        i, j = self.pos
        if j-1 < 0:
            return
        if type(self.maze.grid[i][j-1]) == Cell:
            self.pos = (i, j-1)
            self.maze.grid[i][j-1].visited = True

    def move_right(self) -> None:
        i, j = self.pos
        if j+1 >= self.maze.m:
            return
        if type(self.maze.grid[i][j+1]) == Cell:
            self.pos = (i, j+1)
            self.maze.grid[i][j+1].visited = True

# For some reason it doesn't render probably in the start if I don't add the following loop
    def run(self, solve):
        for _ in range(50):
            self.update_maze()
            pygame.display.flip()
        # Main loop
        if solve:
            self.solve_BFS()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.move_left()
            elif keys[pygame.K_RIGHT]:
                self.move_right()
            elif keys[pygame.K_DOWN]:
                self.move_down()
            elif keys[pygame.K_UP]:
                self.move_up()
            
            self.clock.tick(20)
            self.update_maze()
            if self.pos == self.maze.exit:
                self.screen.fill('black')
                self.screen.blit(self.win_screen, self.win_screen.get_rect())
                pygame.display.flip()
                time.sleep(3)
                self.running = False
            pygame.display.flip()

    def solve_DFS():
        """
            Hint: 
                self.maze return the Maze instance.
                self.maze.unvisited_neighbours(pos) returns all the position of all the cells you have yet to visit.
                self.move_up moves the position up if possible.
                self.move_down moves the position down if possible.
                self.move_right moves the position right if possible.
                self.move_left moves the position left if possible.
                use self.pos to set the current position
        """
        # Your code here
        pass

    def solve_BFS(self):
        queue = []
        queue.append(self.pos)
        while (self.pos != self.maze.exit) and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.pos = queue.pop(0)
            self.maze.grid[self.pos[0]][self.pos[1]].visited = True
            neighbours = self.maze.unvisited_neighbours(self.pos)
            queue += neighbours
            self.update_maze()
            pygame.display.flip()
        

if __name__ == "__main__":
    print_visited = False
    solve = False
    try:
        user_input = input("Give dimensions: <rows columns>")
        user_input = user_input.split(" ")
        assert(len(user_input) == 2)
        size = [int(x) for x in user_input]
        user_input = input("Print previously visited? (y or n): ")
        if user_input == 'y':
            print_visited = True
        user_input = input("Solve the maze for you? (y or n): ")
        if user_input == "y":
            solve = True
    except:
        size = [50, 50]
    app = App(size, print_visited)
    app.run(solve)