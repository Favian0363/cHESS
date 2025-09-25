import pygame

size = 1.5

class Piece:
    def __init__(self, is_white, type_name, position, image):
        self.is_white = is_white
        self.type = type_name
        self.position = position
        self.image = pygame.image.load(f'{image}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect(center=position)

    def is_valid_move(self):
        pass

class Square:
    def __init__(self, is_white, position, image):
        self.is_white = is_white
        self.position = position
        self.image = pygame.image.load(f'{image}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                     (self.image.get_width() / 1.6,
                                      self.image.get_height() / 1.6))
        self.rect = self.image.get_rect(center=position)

class Rook(Piece):
    def is_valid_move(self):
        pass
    pass # moves any number of squares horizontally or vertically

class Knight(Piece):
    def is_valid_move(self):
        pass
    pass # moves two squares in a straight direction, and then one square perpendicular to that

class Bishop(Piece):
    def is_valid_move(self):
        pass
    pass # moves any number of squares diagonally

class King(Piece):
    def is_valid_move(self):
        pass
    pass # moves one square in any direction

class Queen(Piece):
    def is_valid_move(self):
        pass
    pass # moves any number of squares diagonally, horizontally, or vertically

class Pawn(Piece):
    def is_valid_move(self,):
        pass
    pass # moves one square forward
         # on first move, it can move two squares forward
         # captures diagonally

