import pygame

pygame.init()

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("Chess")

size = 1.5

board = pygame.image.load('board.png').convert()

board = pygame.transform.scale(board,
                               (board.get_width() / 1.6,
                                board.get_height() / 1.6))

blackBishop = pygame.image.load('black-bishop.png').convert_alpha()
blackBishop_rect = blackBishop.get_rect()
blackBishop = pygame.transform.scale(blackBishop,
                                     (blackBishop.get_width() / size,
                                      blackBishop.get_height() / size))

blackKing = pygame.image.load('black-king.png').convert_alpha()
blackKing_rect = blackKing.get_rect()
blackKing = pygame.transform.scale(blackKing,
                                     (blackKing.get_width() / size,
                                      blackKing.get_height() / size))

blackKnight = pygame.image.load('black-knight.png').convert_alpha()
blackKnight_rect = blackKnight.get_rect()
blackKnight = pygame.transform.scale(blackKnight,
                                     (blackKnight.get_width() / size,
                                      blackKnight.get_height() / size))

blackPawn = pygame.image.load('black-pawn.png').convert_alpha()
blackPawn_rect = blackPawn.get_rect()
blackPawn = pygame.transform.scale(blackPawn,
                                     (blackPawn.get_width() / size,
                                      blackPawn.get_height() / size))

blackQueen = pygame.image.load('black-queen.png').convert_alpha()
blackQueen_rect = blackQueen.get_rect()
blackQueen = pygame.transform.scale(blackQueen,
                                     (blackQueen.get_width() / size,
                                      blackQueen.get_height() / size))

blackRook = pygame.image.load('black-rook.png').convert_alpha()
blackRook_rect = blackRook.get_rect()
blackRook = pygame.transform.scale(blackRook,
                                     (blackRook.get_width() / size,
                                      blackRook.get_height() / size))

whiteBishop = pygame.image.load('white-bishop.png').convert_alpha()
whiteBishopR_rect = whiteBishop.get_rect(topleft=(397, 555))
whiteBishopL_rect = whiteBishop.get_rect(topleft=(157, 555))
whiteBishop = pygame.transform.scale(whiteBishop,
                                     (whiteBishop.get_width() / size,
                                      whiteBishop.get_height() / size))

whiteKing = pygame.image.load('white-king.png').convert_alpha()
whiteKing_rect = whiteKing.get_rect(topleft=(317, 555))
whiteKing = pygame.transform.scale(whiteKing,
                                     (whiteKing.get_width() / size,
                                      whiteKing.get_height() / size))

whiteKnight = pygame.image.load('white-knight.png').convert_alpha()
whiteKnightR_rect = whiteKnight.get_rect(topleft=(477, 555))
whiteKnightL_rect = whiteKnight.get_rect(topleft=(77, 555))
whiteKnight = pygame.transform.scale(whiteKnight,
                                     (whiteKnight.get_width() / size,
                                      whiteKnight.get_height() / size))

whitePawn = pygame.image.load('white-pawn.png').convert_alpha()
whitePawn_rect = whitePawn.get_rect()
whitePawn = pygame.transform.scale(whitePawn,
                                     (whitePawn.get_width() / size,
                                      whitePawn.get_height() / size))

whiteQueen = pygame.image.load('white-queen.png').convert_alpha()
whiteQueen_rect = whiteQueen.get_rect(topleft=(237, 555))
whiteQueen = pygame.transform.scale(whiteQueen,
                                     (whiteQueen.get_width() / size,
                                      whiteQueen.get_height() / size))

whiteRook = pygame.image.load('white-rook.png').convert_alpha()
whiteRookR_rect = whiteRook.get_rect(topleft=(-3, 555))
whiteRookL_rect = whiteRook.get_rect(topleft=(557, 555))
whiteRook = pygame.transform.scale(whiteRook,
                                     (whiteRook.get_width() / size,
                                      whiteRook.get_height() / size))

running = True 
while running:

    screen.blit(board, (0, 0))
    screen.blit(blackRook, (557, -3))
    screen.blit(blackKnight, (477, -3))
    screen.blit(blackBishop, (397, -3))
    screen.blit(blackKing, (317, -3))
    screen.blit(blackQueen, (237, -3))
    screen.blit(blackBishop, (157, -3))
    screen.blit(blackKnight, (77, -3))
    screen.blit(blackRook, (-3, -3))
    x = -3
    for i in range(1,9):
        screen.blit(blackPawn, (x, 75))
        x += 80
    screen.blit(whiteRook, (whiteRookL_rect))
    screen.blit(whiteKnight, (whiteKnightL_rect))
    screen.blit(whiteBishop, (whiteBishopL_rect))
    screen.blit(whiteQueen, (whiteQueen_rect))
    screen.blit(whiteKing, (whiteKing_rect))
    screen.blit(whiteBishop, whiteBishopR_rect)
    screen.blit(whiteKnight, (whiteKnightR_rect))
    screen.blit(whiteRook, (whiteRookR_rect))
    x = -3
    for i in range(1,9):
        screen.blit(whitePawn, (x, 475))
        x += 80

    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
