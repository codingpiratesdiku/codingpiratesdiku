import colorsys
from collections import deque

def bfs_search(maze, entry, exit_pos, visualize_callback=None):
    queue = deque()
    queue.append(entry)
    parent = {entry: None}
    color_map = {}
    color_idx = 0
    def get_branch_color(idx):
        h = (idx * 0.13) % 1.0
        rgb = colorsys.hsv_to_rgb(h, 0.7, 1.0)
        return tuple(int(255 * c) for c in rgb)
    maze.grid[entry[0]][entry[1]].search_color = get_branch_color(color_idx)
    color_map[entry] = color_idx
    while queue:
        pos = queue.popleft()
        cell = maze.grid[pos[0]][pos[1]]
        cell.visited = True
        neighbours = maze.unvisited_neighbours(pos)
        for n in neighbours:
            if n not in parent:
                parent[n] = pos
                color_idx += 1
                color_map[n] = color_idx
                maze.grid[n[0]][n[1]].search_color = get_branch_color(color_idx)
                queue.append(n)
        if visualize_callback:
            visualize_callback(pos)
        if pos == exit_pos:
            break
    return parent, color_map

def dfs_search(maze, entry, exit_pos, visualize_callback=None):
    stack = [entry]
    parent = {entry: None}
    color_map = {}
    color_idx = 0
    def get_branch_color(idx):
        h = (idx * 0.13) % 1.0
        rgb = colorsys.hsv_to_rgb(h, 0.7, 1.0)
        return tuple(int(255 * c) for c in rgb)
    maze.grid[entry[0]][entry[1]].search_color = get_branch_color(color_idx)
    color_map[entry] = color_idx
    while stack:
        pos = stack.pop()
        cell = maze.grid[pos[0]][pos[1]]
        cell.visited = True
        neighbours = maze.unvisited_neighbours(pos)
        for n in neighbours:
            if n not in parent:
                parent[n] = pos
                color_idx += 1
                color_map[n] = color_idx
                maze.grid[n[0]][n[1]].search_color = get_branch_color(color_idx)
                stack.append(n)
        if visualize_callback:
            visualize_callback(pos)
        if pos == exit_pos:
            break
    return parent, color_map

# Template for new algorithms
# def your_algorithm_search(maze, entry, exit_pos, visualize_callback=None):
#     ...
#     return parent, color_map 