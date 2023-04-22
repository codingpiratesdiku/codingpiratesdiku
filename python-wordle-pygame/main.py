import pygame

with open("allowed_words.txt") as f:
    all_words = f.read().splitlines()
    all_words = [word.lower() for word in all_words]


def get_words_without_letter(words, letter):
    matched = []
    for word in words:
        if letter in word:
            continue
        matched.append(word)
    return matched


def get_words_with_letter_at_position(words, letter, index):
    matched = []
    for word in words:
        if word[index] != letter:
            continue
        matched.append(word)
    return matched


def get_words_with_letter_not_at_position(words, letter, index):
    matched = []
    for word in words:
        if word[index] == letter:
            continue
        if letter not in word:
            continue
        matched.append(word)
    return matched


def history_to_info(guesses, clicks):
    not_exists = []
    nonmatch = []
    match = []
    for guess, clicks in zip(guesses, clicks):
        for i, (letter, click) in enumerate(zip(guess, clicks)):
            if click == 0:
                not_exists.append(letter)
            if click == 1:
                nonmatch.append((i, letter))
            if click == 2:
                match.append((i, letter))

    # Remove from not_exists if letter is in match or nonmatch
    for _, letter in nonmatch + match:
        if letter in not_exists:
            not_exists.remove(letter)

    return not_exists, nonmatch, match


def find_words(words, guesses, clicks):
    matched_words = words

    not_exists, nonmatch, match = history_to_info(guesses, clicks)

    for letter in not_exists:
        matched_words = get_words_without_letter(matched_words, letter)
    for i, letter in nonmatch:
        matched_words = get_words_with_letter_not_at_position(matched_words, letter, i)
    for i, letter in match:
        matched_words = get_words_with_letter_at_position(matched_words, letter, i)

    return matched_words


colors = {
    -1: (255, 255, 255),
    0: (121, 124, 126),
    1: (198, 180, 102),
    2: (121, 168, 107),
}

allowed_letters = list(range(pygame.K_a, pygame.K_z + 1)) + [
    230,
    248,
    229,
]  # Plus æ, ø, å.

cell_size = 100
gap = 5
block_size = cell_size + gap * 2
windowBgColor = (200, 200, 200)

window_width = block_size * 5
window_height = block_size * 6

pygame.init()

window = pygame.display.set_mode((window_width, window_height))
font = pygame.font.SysFont("arialunicode", 30)
pygame.display.set_caption("2048")

window.fill(windowBgColor)

running = True
c_row = 0
c_col = 0
guesses = [[""] * 5 for _ in range(6)]
clicks = [[-1] * 5 for _ in range(6)]
rects = [[pygame.Rect(0, 0, 0, 0)] * 5 for _ in range(6)]
print(rects[0][0])

while running:
    pygame.display.update()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in allowed_letters:
                if c_col < 5:
                    guesses[c_row][c_col] = event.unicode
                    clicks[c_row][c_col] = 0
                    c_col += 1
                if c_col >= 5:
                    c_row += 1
                    c_col = 0

            if event.key == pygame.K_BACKSPACE:
                if c_col > 0:
                    c_col -= 1
                    guesses[c_row][c_col] = ""
                    clicks[c_row][c_col] = -1
                else:
                    if c_row > 0:
                        c_col = 5
                        c_row -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN:     
            if event.button == 1:  # Left mouse click
                for r in range(6):
                    for c in range(5):
                        if not guesses[r][c]:
                            continue
                        if rects[r][c].collidepoint(event.pos):
                            clicks[r][c] = (clicks[r][c] + 1) % 3
        
        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
            print(find_words(all_words, guesses, clicks))
    

    # Draw board in every loop
    for r in range(6):
        y = block_size * r + gap
        for c in range(5):
            x = block_size * c + gap
            rect = pygame.draw.rect(
                window,
                colors[clicks[r][c]],
                pygame.Rect(x, y, cell_size, cell_size),
                border_radius=10,
            )
            textSurface = font.render(f"{guesses[r][c].upper()}", True, (0, 0, 0))
            textRect = textSurface.get_rect(
                center=(x + block_size / 2, y + block_size / 2)
            )
            window.blit(textSurface, textRect)
            rects[r][c] = rect
        
            if r == c_row:
                pygame.draw.rect(
                    window,
                    (0, 0, 0),
                    pygame.Rect(x, y, cell_size, cell_size),
                    3,
                    border_radius=10,
                )

