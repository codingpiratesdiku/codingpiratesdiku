from maze import *
import pygame
from pygame.locals import *
import time
import colorsys
from search_algorithms import bfs_search

class SettingsWindow:
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Settings")
        
        # Colors
        self.BG = (245, 247, 250)
        self.PANEL = (255, 255, 255)
        self.BLACK = (30, 30, 30)
        self.GRAY = (200, 200, 200)
        self.BLUE = (0, 102, 255)
        self.GREEN = (0, 180, 80)
        self.DARKGRAY = (120, 120, 120)
        
        # Font
        self.font = pygame.font.SysFont("Segoe UI", 28)
        self.label_font = pygame.font.SysFont("Segoe UI", 24)
        self.button_font = pygame.font.SysFont("Segoe UI", 30, bold=True)
        
        # Input fields
        self.rows_input = "50"
        self.cols_input = "50"
        self.active_input = "rows"  # Which input is currently selected
        
        # Checkboxes
        self.print_visited = False
        self.solve = False
        
        # Layout
        self.panel_rect = pygame.Rect(60, 40, 380, 260)
        self.rows_rect = pygame.Rect(250, 70, 80, 36)
        self.cols_rect = pygame.Rect(250, 120, 80, 36)
        self.visited_rect = pygame.Rect(250, 170, 28, 28)
        self.solve_rect = pygame.Rect(250, 210, 28, 28)
        
        self.running = True
        
        self.algorithms = ["Breadth-First Search", "Depth-First Search"]
        self.selected_algorithm = 0
        
    def draw_rounded_rect(self, surface, color, rect, radius=10, width=0):
        pygame.draw.rect(surface, color, rect, width, border_radius=radius)

    def draw_checkbox(self, rect, checked):
        self.draw_rounded_rect(self.screen, self.GRAY, rect, radius=6, width=2)
        if checked:
            pygame.draw.rect(self.screen, self.GREEN, rect.inflate(-8, -8), border_radius=4)
            # Draw checkmark
            pygame.draw.line(self.screen, self.PANEL, (rect.x+7, rect.y+15), (rect.x+13, rect.y+22), 3)
            pygame.draw.line(self.screen, self.PANEL, (rect.x+13, rect.y+22), (rect.x+22, rect.y+7), 3)

    def draw(self):
        self.screen.fill(self.BG)
        self.draw_rounded_rect(self.screen, self.PANEL, self.panel_rect, radius=18)
        pygame.draw.rect(self.screen, self.GRAY, self.panel_rect, 2, border_radius=18)
        # Draw labels
        rows_label = self.label_font.render("Rows:", True, self.BLACK)
        cols_label = self.label_font.render("Columns:", True, self.BLACK)
        visited_label = self.label_font.render("Show visited cells", True, self.DARKGRAY)
        solve_label = self.label_font.render("Auto-solve", True, self.DARKGRAY)
        self.screen.blit(rows_label, (110, 75))
        self.screen.blit(cols_label, (110, 125))
        # Draw input boxes with thicker, more visible border
        border_color = (80, 120, 220) if self.active_input == "rows" else self.GRAY
        self.draw_rounded_rect(self.screen, self.PANEL, self.rows_rect, radius=8, width=0)
        pygame.draw.rect(self.screen, border_color, self.rows_rect, 4, border_radius=8)
        border_color = (80, 120, 220) if self.active_input == "cols" else self.GRAY
        self.draw_rounded_rect(self.screen, self.PANEL, self.cols_rect, radius=8, width=0)
        pygame.draw.rect(self.screen, border_color, self.cols_rect, 4, border_radius=8)
        # Draw input text
        rows_text = self.font.render(self.rows_input, True, self.BLACK)
        cols_text = self.font.render(self.cols_input, True, self.BLACK)
        self.screen.blit(rows_text, (self.rows_rect.x + 10, self.rows_rect.y + 2))
        self.screen.blit(cols_text, (self.cols_rect.x + 10, self.cols_rect.y + 2))
        # Draw checkboxes to the left of their labels
        visited_box_rect = pygame.Rect(110, 172, 28, 28)
        solve_box_rect = pygame.Rect(110, 212, 28, 28)
        self.draw_checkbox(visited_box_rect, self.print_visited)
        self.draw_checkbox(solve_box_rect, self.solve)
        self.screen.blit(visited_label, (visited_box_rect.right + 10, visited_box_rect.y + 2))
        self.screen.blit(solve_label, (solve_box_rect.right + 10, solve_box_rect.y + 2))
        self.visited_rect = visited_box_rect
        self.solve_rect = solve_box_rect
        # Draw algorithm selection
        algo_label = self.label_font.render("Algorithm:", True, self.BLACK)
        self.screen.blit(algo_label, (110, 260))
        self.radio_rects = []
        for i, name in enumerate(self.algorithms):
            y = 300 + i*36
            radio_rect = pygame.Rect(130, y, 24, 24)
            self.radio_rects.append(radio_rect)
            pygame.draw.circle(self.screen, self.GRAY, radio_rect.center, 12, 2)
            if self.selected_algorithm == i:
                pygame.draw.circle(self.screen, self.BLUE, radio_rect.center, 8)
            algo_text = self.label_font.render(name, True, self.DARKGRAY)
            self.screen.blit(algo_text, (160, y-4))
        # Draw start button
        start_rect = pygame.Rect(self.panel_rect.centerx - 70, self.panel_rect.bottom - 55, 140, 44)
        self.draw_rounded_rect(self.screen, self.BLUE, start_rect, radius=12)
        start_text = self.button_font.render("Start", True, self.PANEL)
        self.screen.blit(start_text, (start_rect.x + 32, start_rect.y + 6))
        pygame.display.flip()
        return start_rect
    
    def run(self):
        start_rect = None
        while self.running:
            start_rect = self.draw()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None, False, False, None
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check input fields
                    if self.rows_rect.collidepoint(event.pos):
                        self.active_input = "rows"
                    elif self.cols_rect.collidepoint(event.pos):
                        self.active_input = "cols"
                    # Check checkboxes
                    elif self.visited_rect.collidepoint(event.pos):
                        self.print_visited = not self.print_visited
                    elif self.solve_rect.collidepoint(event.pos):
                        self.solve = not self.solve
                    # Algorithm radio buttons
                    radio_clicked = False
                    for i, rect in enumerate(self.radio_rects):
                        if rect.collidepoint(event.pos):
                            self.selected_algorithm = i
                            radio_clicked = True
                            break
                    if not radio_clicked and start_rect.collidepoint(event.pos):
                        try:
                            size = [int(self.rows_input), int(self.cols_input)]
                            if size[0] > 0 and size[1] > 0:
                                return size, self.print_visited, self.solve, self.algorithms[self.selected_algorithm]
                        except ValueError:
                            pass
                
                if event.type == pygame.KEYDOWN:
                    if self.active_input == "rows":
                        if event.key == pygame.K_BACKSPACE:
                            self.rows_input = self.rows_input[:-1]
                        elif event.key == pygame.K_TAB:
                            self.active_input = "cols"
                        elif event.unicode.isnumeric() and len(self.rows_input) < 4:
                            self.rows_input += event.unicode
                    elif self.active_input == "cols":
                        if event.key == pygame.K_BACKSPACE:
                            self.cols_input = self.cols_input[:-1]
                        elif event.key == pygame.K_TAB:
                            self.active_input = "rows"
                        elif event.unicode.isnumeric() and len(self.cols_input) < 4:
                            self.cols_input += event.unicode
        
        return None, False, False, None

class App:
    # Setup
    def __init__(self, size, print_visited, algorithm) -> None:     
        self.print_visited = print_visited
        self.algorithm = algorithm
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
                if x == self.pos[1] and y == self.pos[0]:
                    continue
                rect = pygame.Rect(x*self.block_width, y*self.block_height, self.block_width+1, self.block_height+1)
                cell = self.maze.grid[y][x]
                if type(cell) == Cell:
                    if getattr(cell, 'solution_path', False):
                        pygame.draw.rect(self.screen, (0, 200, 0), rect)  # green
                    elif getattr(cell, 'search_color', None) is not None:
                        pygame.draw.rect(self.screen, cell.search_color, rect)
                    elif self.print_visited and cell.visited:
                        pygame.draw.rect(self.screen, 'pink', rect)
                    else:
                        pygame.draw.rect(self.screen, 'lightgray', rect)
                elif type(cell) == Wall:
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

    def run(self, solve):
        for _ in range(50):
            self.update_maze()
            pygame.display.flip()
        # Main loop
        if solve:
            import time as _time
            while True:
                start = _time.time()
                if self.algorithm == "Breadth-First Search":
                    self.solve_BFS()
                elif self.algorithm == "Depth-First Search":
                    self.solve_DFS()
                elapsed = _time.time() - start
                run_again = self.show_popup(self.algorithm, f"Solved in {elapsed:.2f} seconds")
                if not run_again:
                    break
                # Regenerate maze and rerun
                self.maze = Maze(self.maze.n, self.maze.m)
                self.pos = self.maze.entry
                for y in range(self.maze.n):
                    for x in range(self.maze.m):
                        cell = self.maze.grid[y][x]
                        if hasattr(cell, 'search_color'):
                            cell.search_color = None
                        if hasattr(cell, 'solution_path'):
                            cell.solution_path = False
                        if hasattr(cell, 'visited'):
                            cell.visited = False
                self.update_maze()
                pygame.display.flip()
            # After auto-solve, keep the solved maze visible until the user closes the window
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                self.clock.tick(20)
                self.update_maze()
                pygame.display.flip()
            return
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

    def solve_DFS(self):
        from search_algorithms import dfs_search
        def visualize_callback(pos):
            self.pos = pos
            self.update_maze()
            pygame.display.flip()
        parent, color_map = dfs_search(self.maze, self.maze.entry, self.maze.exit, visualize_callback)
        if self.pos == self.maze.exit:
            path = []
            cur = self.pos
            while cur is not None:
                y, x = cur
                self.maze.grid[y][x].solution_path = True
                self.maze.grid[y][x].search_color = None
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            for _ in range(60):
                self.update_maze()
                pygame.display.flip()
                self.clock.tick(30)

    def solve_BFS(self):
        import time as _time
        def visualize_callback(pos):
            self.pos = pos
            self.update_maze()
            pygame.display.flip()
        parent, color_map = bfs_search(self.maze, self.maze.entry, self.maze.exit, visualize_callback)
        # Trace back the solution path
        if self.pos == self.maze.exit:
            path = []
            cur = self.pos
            while cur is not None:
                y, x = cur
                self.maze.grid[y][x].solution_path = True
                self.maze.grid[y][x].search_color = None  # Override with green
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            # Show the solved maze with the path
            for _ in range(60):
                self.update_maze()
                pygame.display.flip()
                self.clock.tick(30)

    def show_popup(self, title, message):
        popup_width, popup_height = 400, 200
        popup = pygame.Surface((popup_width, popup_height))
        popup.fill((245, 247, 250))
        pygame.draw.rect(popup, (200, 200, 200), popup.get_rect(), 2, border_radius=16)
        font = pygame.font.SysFont("Segoe UI", 28, bold=True)
        msg_font = pygame.font.SysFont("Segoe UI", 24)
        title_surf = font.render(title, True, (30, 30, 30))
        msg_surf = msg_font.render(message, True, (30, 30, 30))
        ok_rect = pygame.Rect(popup_width//2 + 10, popup_height - 60, 100, 40)
        again_rect = pygame.Rect(popup_width//2 - 130, popup_height - 60, 120, 40)  # wider button
        running = True
        result = False
        while running:
            self.screen.blit(popup, ((self.screen.get_width()-popup_width)//2, (self.screen.get_height()-popup_height)//2))
            popup.blit(pygame.Surface((popup_width, popup_height)), (0,0))
            popup.fill((245, 247, 250))
            pygame.draw.rect(popup, (200, 200, 200), popup.get_rect(), 2, border_radius=16)
            popup.blit(title_surf, (popup_width//2 - title_surf.get_width()//2, 30))
            popup.blit(msg_surf, (popup_width//2 - msg_surf.get_width()//2, 80))
            pygame.draw.rect(popup, (0, 102, 255), ok_rect, border_radius=10)
            pygame.draw.rect(popup, (0, 180, 80), again_rect, border_radius=10)
            ok_text = font.render("OK", True, (255,255,255))
            again_text = font.render("Run Again", True, (255,255,255))
            popup.blit(ok_text, (ok_rect.x + (ok_rect.width - ok_text.get_width())//2, ok_rect.y + 5))
            popup.blit(again_text, (again_rect.x + (again_rect.width - again_text.get_width())//2, again_rect.y + 5))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    rel_x = mouse_x - (self.screen.get_width()-popup_width)//2
                    rel_y = mouse_y - (self.screen.get_height()-popup_height)//2
                    if ok_rect.collidepoint(rel_x, rel_y):
                        running = False
                        result = False
                    if again_rect.collidepoint(rel_x, rel_y):
                        running = False
                        result = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        running = False
                        result = False
        return result

if __name__ == "__main__":
    settings = SettingsWindow()
    result = settings.run()
    if result:
        size, print_visited, solve, algorithm = result
        app = App(size, print_visited, algorithm)
        app.run(solve)
    pygame.quit()