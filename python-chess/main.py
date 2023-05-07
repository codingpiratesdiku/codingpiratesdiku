import pygame

colors = [(255, 206, 158), (209, 139, 71)]
highlight_colors = [(100, 249, 83), (0, 228, 10)]


class Square:
    def __init__(self, x, y, size):
        self.occupying_piece = None
        self.rect = pygame.Rect(x * size, y * size, size, size)
        self.highlight = False
        self.is_light_square = (x + y) % 2
        self.pos = (x, y)

    def draw(self, screen):
        if self.highlight:
            color = highlight_colors[self.is_light_square]
        else:
            color = colors[self.is_light_square]
        pygame.draw.rect(screen, color, self.rect)

        if self.occupying_piece:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            screen.blit(self.occupying_piece.img, centering_rect.topleft)


class Piece:
    def __init__(self, pos, color, board):
        self.board = board
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.has_moved = False


class Pawn(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        size = board.square_size
        img_path = "imgs/" + color[0] + "P.svg"
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.smoothscale(self.img, (size * 0.8, size * 0.8))


class Rook(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        size = board.square_size
        img_path = "imgs/" + color[0] + "R.svg"
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.smoothscale(self.img, (size * 0.75, size * 0.75))
        self.board = board


class Bishop(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        size = board.square_size
        img_path = "imgs/" + color[0] + "B.svg"
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.smoothscale(self.img, (size * 0.75, size * 0.75))
        self.board = board


class Knight(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        size = board.square_size
        img_path = "imgs/" + color[0] + "N.svg"
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.smoothscale(self.img, (size * 0.75, size * 0.75))
        self.board = board


class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        size = board.square_size
        img_path = "imgs/" + color[0] + "Q.svg"
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.smoothscale(self.img, (size * 0.75, size * 0.75))
        self.board = board


class King(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        size = board.square_size
        img_path = "imgs/" + color[0] + "K.svg"
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.smoothscale(self.img, (size * 0.75, size * 0.75))
        self.board = board


class Chessboard:
    def __init__(self, screen, square_size, colors):
        self.square_size = square_size
        self.colors = colors
        self.screen = screen
        start_pos = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.squares = self.generate_squares(start_pos)
        self.selected_square = None
        self.turn = "w"

    def generate_squares(self, pos):
        squares = []
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.square_size)
                squares.append(square)

                if not pos[y][x]:
                    continue

                col, piece = pos[y][x]

                match piece:
                    case "P":
                        square.occupying_piece = Pawn((x, y), col, self)
                    case "R":
                        square.occupying_piece = Rook((x, y), col, self)
                    case "B":
                        square.occupying_piece = Bishop((x, y), col, self)
                    case "K":
                        square.occupying_piece = King((x, y), col, self)
                    case "Q":
                        square.occupying_piece = Queen((x, y), col, self)
                    case "N":
                        square.occupying_piece = Knight((x, y), col, self)

        return squares

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if square.pos == pos:
                return square

    def draw(self):
        highlights = []
        if self.selected_square:
            highlights.append(self.selected_square)
        else:
            highlights = []
        for square in self.squares:
            if square in highlights:
                square.highlight = True
            else:
                square.highlight = False
            square.draw(self.screen)

    def handle_click(self, mx, my):
        x = mx // self.square_size
        y = my // self.square_size
        clicked_square = self.get_square_from_pos((x, y))
        clicked_piece = clicked_square.occupying_piece

        if self.selected_square:  # We've already selected a square
            clicked_square.occupying_piece = self.selected_square.occupying_piece
            self.selected_square.occupying_piece = None
            self.selected_square = None
            self.turn = "b" if self.turn == "w" else "w"
        elif clicked_piece and clicked_piece.color == self.turn:
            self.selected_square = clicked_square
        else:
            self.selected_square = None


# Setup
board_size = 512
screen = pygame.display.set_mode((board_size, board_size))
pygame.display.set_caption("Chessboard")

# Create board
chessboard = Chessboard(screen=screen, square_size=64, colors=colors)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            chessboard.handle_click(mx, my)

    chessboard.draw()
    pygame.display.flip()

pygame.quit()
