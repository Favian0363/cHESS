import pygame
from piece_module import Piece  

pygame.init()

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("Chess")
size = 1.5
x = 37
board = pygame.image.load('board.png').convert()
board = pygame.transform.scale(board,
                               (board.get_width() / 1.6,
                                board.get_height() / 1.6))


all_pieces = [
    Piece("black", "rook", (39, 38), "black-rook"),
    Piece("black", "knight", (119, 38), "black-knight"),
    Piece("black", "bishop", (199, 38), "black-bishop"),
    Piece("black", "queen", (279, 38), "black-queen"),
    Piece("black", "king", (359, 38), "black-king"),
    Piece("black", "bishop", (439, 38), "black-bishop"),
    Piece("black", "knight", (519, 38), "black-knight"),
    Piece("black", "rook", (599, 38), "black-rook"),

    Piece("white", "rook", (39, 597), "white-rook"),
    Piece("white", "knight", (119, 597), "white-knight"),
    Piece("white", "bishop", (199, 597), "white-bishop"),
    Piece("white", "queen", (279, 597), "white-queen"),
    Piece("white", "king", (359, 597), "white-king"),
    Piece("white", "bishop", (439, 597), "white-bishop"),
    Piece("white", "knight", (519, 597), "white-knight"),
    Piece("white", "rook", (599, 597), "white-rook"),
]
for i in range(8):
    all_pieces.append(Piece("white", "pawn", (x, 517), "white-pawn"))
    all_pieces.append(Piece("black", "pawn", (x, 115), "black-pawn"))
    x += 80 

piece_grabbed = None

running = True 
while running:
    
    screen.blit(board, (0, 0))
    for piece in all_pieces:
        screen.blit(piece.image, piece.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for piece in all_pieces:
                on_piece = piece.rect.collidepoint((pos))
                if on_piece:
                    piece_grabbed = piece 
    
    if piece_grabbed is not None:
        pos = pygame.mouse.get_pos()
        piece_grabbed.rect = pos   

    pygame.display.flip()

pygame.quit()

