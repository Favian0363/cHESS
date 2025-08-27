    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif piece_grabbed is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in all_squares:
                    on_square = piece_grabbed.rect.collideobjects((all_squares))
                    if on_square:
                        square_on = square
        elif event.type == pygame.MOUSEBUTTONDOWN: # attach piece to cursor when 
            pos = pygame.mouse.get_pos()           # mouse button is pressed
            for piece in all_pieces:
                on_piece = piece.rect.collidepoint((pos))
                if on_piece:
                    piece_grabbed = piece
            
    if piece_grabbed:
        pos = pygame.mouse.get_pos()
        piece_grabbed.rect.center = pos
    
    if square_on:
        piece_grabbed.rect.center = square