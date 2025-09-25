import pygame
from cHESS.piece_module import Piece
from cHESS.piece_module import Square

pygame.init()

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("Chess")

def is_valid_move(origin_square, piece_grabbed, destination_square): # coordinates are tuples (row, column)
    if piece_grabbed.type == 'pawn':
        if destination_square[0] == look_valid_squares(origin_square, piece_grabbed) and destination_square[1]:
            print("valid move")
        else:
            print("invalid move")
    elif piece_grabbed.type == 'rook':
        if destination_square[0] == look_valid_squares(origin_square, piece_grabbed):
            print("valid move")
        else:
            print("invalid move")
    elif piece_grabbed.type == 'knight':
        if destination_square[0] == look_valid_squares(origin_square, piece_grabbed):
            print("valid move")
        else:
            print("invalid move")
    elif piece_grabbed.type == 'bishop':
        if destination_square[0] == look_valid_squares(origin_square, piece_grabbed):
            print("valid move")
        else:
            print("invalid move")
    elif piece_grabbed.type == 'king':
        if destination_square[0] == look_valid_squares(origin_square, piece_grabbed):
            print("valid move")
        else:
            print("invalid move")
    elif piece_grabbed.type == 'queen':
        if destination_square[0] == look_valid_squares(origin_square, piece_grabbed):
            print("valid move")
        else:
            print("invalid move")

def look_valid_squares(origin_square, piece_grabbed):
    if piece_grabbed.type == 'pawn':
        valid_squares = origin_square[0]-1
        return valid_squares
    elif piece_grabbed.type == 'rook':
        valid_squares = origin_square[0]-1 and origin_square[0]-2 and origin_square[0]-3 and origin_square[0]-4 and origin_square[0]-5 and origin_square[0]-6 and origin_square[0]-7
        return valid_squares


def pixels_to_pos(pixel_coordinates): # take pixels and convert to rows and columns
    x_coord, y_coord = pixel_coordinates
    row = (y_coord // 80)
    col = (x_coord // 80)
    return row, col

def pos_to_pixels(rows_and_columns): # take rows and columns and convert to pixels
    row, col = rows_and_columns
    x = 40 + (col * 80)
    y = 40 + (row * 80)
    return x, y

all_pieces = [ # change color attribute to white = True | black = False
    Piece(False, "rook", pos_to_pixels((0,0)), "black-rook"),
    Piece(False, "knight", pos_to_pixels((0,1)), "black-knight"),
    Piece(False, "bishop", pos_to_pixels((0,2)), "black-bishop"),
    Piece(False, "queen", pos_to_pixels((0,3)), "black-queen"),
    Piece(False, "king", pos_to_pixels((0,4)), "black-king"),
    Piece(False, "bishop", pos_to_pixels((0,5)), "black-bishop"),
    Piece(False, "knight", pos_to_pixels((0,6)), "black-knight"),
    Piece(False, "rook", pos_to_pixels((0,7)), "black-rook"),

    Piece(True, "rook", pos_to_pixels((7,0)), "white-rook"),
    Piece(True, "knight", pos_to_pixels((7,1)), "white-knight"),
    Piece(True, "bishop", pos_to_pixels((7,2)), "white-bishop"),
    Piece(True, "queen", pos_to_pixels((7,3)), "white-queen"),
    Piece(True, "king", pos_to_pixels((7,4)), "white-king"),
    Piece(True, "bishop", pos_to_pixels((7,5)), "white-bishop"),
    Piece(True, "knight", pos_to_pixels((7,6)), "white-knight"),
    Piece(True, "rook", pos_to_pixels((7,7)), "white-rook"),
]

col = 0
for i in range(8):
    all_pieces.append(Piece(True, "pawn", pos_to_pixels((6,col)), "white-pawn"))
    all_pieces.append(Piece(False, "pawn", pos_to_pixels((1,col)), "black-pawn"))
    col += 1

all_squares = []
col = 0
for i in range(8):
    row = 0
    for j in range(8):
        if (i + j) % 2 == 0:
            all_squares.append(Square(True, pos_to_pixels((row, col)), "white_square"))
        else:
            all_squares.append(Square(False, pos_to_pixels((row, col)), "black_square"))

        row += 1  # move row
    col += 1  # move col

piece_grabbed = None
origin_square = None
destination_square = None

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
                    on_piece = piece.rect.collidepoint(pos)
                    if on_piece:
                        piece_grabbed = piece
                        origin_square = pixels_to_pos(piece_grabbed.rect.center) # attach every piece to its initial square

        elif event.type == pygame.MOUSEBUTTONUP:    # drop piece on square if piece is picked up and if valid move
            if piece_grabbed is not None:
                for square in all_squares:
                    on_square = square.rect.collidepoint(piece_grabbed.rect.center)
                    if on_square: # and valid_move()
                        piece_grabbed.rect.center = square.rect.center
                        piece_grabbed.position = square.position
                        destination_square = pixels_to_pos(square.position)
                        print(f'piece grabbed: {piece_grabbed.type}')
                        print(f'origin square: {origin_square}')
                        print(f'destination square: {destination_square}')
                        is_valid_move(origin_square, piece_grabbed, destination_square)
                        origin_square = destination_square
                        piece_grabbed = None
                        break
    if piece_grabbed:
        pos = pygame.mouse.get_pos()
        piece_grabbed.rect.center = pos

    pygame.display.flip()

pygame.quit()

