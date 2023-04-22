import random

import pygame

BG_COLORS = {
    0: (250, 250, 250),
    2: (238, 228, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 201, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

def rotate_90(matrix):
    new_matrix = []
    for i in range(3, -1, -1):
        row = []
        for j in range(4):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix

def rotate_180(matrix):
    return rotate_90(rotate_90(matrix))

def rotate_270(matrix):
    return rotate_90(rotate_180(matrix))

def stack(matrix):
    new_matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][pos] = matrix[i][j]
                pos += 1
    return new_matrix

def combine(matrix):
    new_matrix = matrix.copy()
    for i in range(4):
        for j in range(3):
            if matrix[i][j] != 0 and matrix[i][j] == matrix[i][j+1]:
                new_matrix[i][j] *= 2
                new_matrix[i][j+1] = 0
    return new_matrix

def stack_combine_stack(matrix):
    return stack(combine(stack(matrix)))


def move_left(matrix):
    return stack_combine_stack(matrix)

def move_down(matrix):
    matrix = rotate_270(matrix)
    matrix = stack_combine_stack(matrix)
    matrix = rotate_90(matrix)
    return matrix

def move_up(matrix):
    matrix = rotate_90(matrix)
    matrix = stack_combine_stack(matrix)
    matrix = rotate_270(matrix)
    return matrix

def move_right(matrix):
    matrix = rotate_180(matrix)
    matrix = stack_combine_stack(matrix)
    matrix = rotate_180(matrix)
    return matrix


matrix = [
    [0, 0, 0, 0],
    [0, 2, 0, 2],
    [0, 2, 0, 0],
    [0, 2, 0, 0]
]

cell_size = 100
gap = 5
block_size = cell_size + gap * 2
windowBgColor = (187, 173, 160)

window_width = block_size * 4
window_height = window_width


pygame.init()

window = pygame.display.set_mode((window_width, window_height))
font = pygame.font.SysFont("Comic Sans MS", 30)
pygame.display.set_caption("2048")

window.fill(windowBgColor)
running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                matrix = move_up(matrix)
            elif event.key == pygame.K_DOWN:
                matrix = move_down(matrix)
            elif event.key == pygame.K_LEFT:
                matrix = move_left(matrix)
            elif event.key == pygame.K_RIGHT:
                matrix = move_right(matrix)
            elif event.key == pygame.K_ESCAPE:
                running = False
            
            new_i = random.randint(0, 3)
            new_j = random.randint(0, 3)
            while matrix[new_i][new_j] != 0:
                new_i = random.randint(0, 3)
                new_j = random.randint(0, 3)
            matrix[new_i][new_j] = 2
        
        # Draw board
        for r in range(4):
            rectY = block_size * r + gap
            for c in range(4):
                rectX = block_size * c + gap
                cell_value = matrix[r][c]

                pygame.draw.rect(
                    window,
                    BG_COLORS[cell_value],
                    pygame.Rect(rectX, rectY, cell_size, cell_size)
                )

                if cell_value != 0:
                    textSurface = font.render(f"{cell_value}", True, (0, 0, 0))
                    textRect = textSurface.get_rect(center=(rectX + block_size/2, rectY + block_size/2))
                    window.blit(textSurface, textRect)



pygame.display.update()

