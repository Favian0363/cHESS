import pygame
from piece_module import Piece  

pygame.init()

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("Chess")
size = 1.5
board = pygame.image.load('board.png').convert()
board = pygame.transform.scale(board,
                               (board.get_width() / 1.6,
                                board.get_height() / 1.6))

all_pieces = [
    Piece("black", "rook", (-3, -3), "black-rook"),
    Piece("black", "knight", (77, -3), "black-knight"),
    Piece("black", "bishop", (157, -3), "black-bishop"),
    Piece("black", "queen", (237, -3), "black-queen"),
    Piece("black", "king", (317, -3), "black-king"),
    Piece("black", "bishop", (397, -3), "black-bishop"),
    Piece("black", "knight", (477, -3), "black-knight"),
    Piece("black", "rook", (557, -3), "black-rook"),
    Piece("black", "pawn", (-3, 75), "black-pawn"),

    Piece("white", "rook", (-3, 555), "white-rook"),
    Piece("white", "knight", (77, 555), "white-knight"),
    Piece("white", "bishop", (157, 555), "white-bishop"),
    Piece("white", "queen", (237, 555), "white-queen"),
    Piece("white", "king", (317, 555), "white-king"),
    Piece("white", "bishop", (397, 555), "white-bishop"),
    Piece("white", "knight", (477, 555), "white-knight"),
    Piece("white", "rook", (557, 555), "white-rook"),
    Piece("white", "pawn", (-3, 477), "white-pawn")
]

running = True 
while running:

    screen.blit(board, (0, 0))

    for piece_image, piece_rect in all_pieces:
        screen.blit(piece_image, (piece_rect))

    # screen.blit(black_rook_L.image, (black_rook_L.rect))
    # screen.blit(black_knight_L.image, (black_knight_L.rect))
    # screen.blit(black_bishop_L.image, (black_bishop_L.rect))
    # screen.blit(black_queen.image, (black_queen.rect))
    # screen.blit(black_king.image, (black_king.rect))
    # screen.blit(black_bishop_R.image, (black_bishop_R.rect))
    # screen.blit(black_knight_R.image, (black_knight_R.rect))
    # screen.blit(black_rook_R.image, (black_rook_R.rect))
    # screen.blit(black_pawn.image, (black_pawn.rect))

    # screen.blit(white_rook_L.image, (white_rook_L.rect))
    # screen.blit(white_knight_L.image, (white_knight_L.rect))
    # screen.blit(white_bishop_L.image, (white_bishop_L.rect))
    # screen.blit(white_queen.image, (white_queen.rect))
    # screen.blit(white_king.image, (white_king.rect))
    # screen.blit(white_bishop_R.image, (white_bishop_R.rect))
    # screen.blit(white_knight_R.image, (white_knight_R.rect))
    # screen.blit(white_rook_R.image, (white_rook_R.rect))
    # screen.blit(white_pawn.image, (white_pawn.rect))
    

    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
