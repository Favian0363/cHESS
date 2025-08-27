import pygame
from piece_module import Piece 
from piece_module import Square   

pygame.init()

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("Chess")
size = 1.5
x = 37

def pixels(board_position):
    row, col = board_position
    x = 40 + (col * 80)
    y = 40 + (row * 80)
    return (x, y)

all_pieces = [
    Piece("black", "rook", pixels((0,0)), "black-rook"),
    Piece("black", "knight", pixels((0,1)), "black-knight"),
    Piece("black", "bishop", pixels((0,2)), "black-bishop"),
    Piece("black", "queen", pixels((0,3)), "black-queen"),
    Piece("black", "king", pixels((0,4)), "black-king"),
    Piece("black", "bishop", pixels((0,5)), "black-bishop"),
    Piece("black", "knight", pixels((0,6)), "black-knight"),
    Piece("black", "rook", pixels((0,7)), "black-rook"),

    Piece("white", "rook", pixels((7,0)), "white-rook"),
    Piece("white", "knight", pixels((7,1)), "white-knight"),
    Piece("white", "bishop", pixels((7,2)), "white-bishop"),
    Piece("white", "queen", pixels((7,3)), "white-queen"),
    Piece("white", "king", pixels((7,4)), "white-king"),
    Piece("white", "bishop", pixels((7,5)), "white-bishop"),
    Piece("white", "knight", pixels((7,6)), "white-knight"),
    Piece("white", "rook", pixels((7,7)), "white-rook"),
]
col = 0
for i in range(8):
    all_pieces.append(Piece("white", "pawn", pixels((6,col)), "white-pawn"))
    all_pieces.append(Piece("black", "pawn", pixels((1,col)), "black-pawn"))
    col += 1

all_squares = []
y = 40
for i in range(8): 
    x = 40
    for j in range(8):  
        if (i + j) % 2 == 0:
            all_squares.append(Square("white", (x, y), "white_square"))
        else:
            all_squares.append(Square("black", (x, y), "black_square"))

        x += 80  # move column
    y += 80  # move row

piece_grabbed = None

running = True 
while running:
    
    for square in all_squares:
        screen.blit(square.image, square.rect)
    for piece in all_pieces:
        screen.blit(piece.image, piece.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if piece_grabbed is None:               # pick up piece when mouse button is pressed
                pos = pygame.mouse.get_pos()           
                for piece in all_pieces:
                    on_piece = piece.rect.collidepoint((pos))
                    if on_piece:    
                        piece_grabbed = piece
        
        elif event.type == pygame.MOUSEBUTTONUP:    # drop piece on square if piece is picked up 
            if piece_grabbed is not None:
                for square in all_squares:
                    on_square = square.rect.collidepoint(piece_grabbed.rect.center)
                    if on_square:
                        piece_grabbed.rect.center = square.rect.center
                        piece_grabbed = None
                        break

    if piece_grabbed:                           
        pos = pygame.mouse.get_pos()
        piece_grabbed.rect.center = pos

    pygame.display.flip()

pygame.quit()

