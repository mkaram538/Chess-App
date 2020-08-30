class Piece:

    def __init__(self, position_row, position_column, color):
        self.row = position_row
        self.column = position_column
        self.color = color

    def return_position(self):
        return [self.row, self.column]

    def move_to(self, row, column):
        self.row = row
        self.column = column

    def path(self, requested_row, requested_column):
        position = self.return_position()
        original_row = position[0]
        original_column = position[1]
        move_list = []
        if isinstance(self, Bishop) or isinstance(self, Queen):
            distance_column = max(requested_column, original_column) - min(requested_column, original_column)
            for x in range(distance_column - 1):
                x += 1
                least_column = min(original_column, requested_column)
                least_row = min(original_row, requested_row)
                move_list.append([least_row + x, least_column + x])
        else:
            if original_row == requested_row:
                distance_between = max(requested_column, original_column) - min(requested_column, original_column)
                for x in range(distance_between - 1):
                    x += 1
                    least = min(original_column, requested_column)
                    move_list.append([original_row, least + x])
            else:
                distance_between = max(requested_row, original_row) - min(requested_row, original_row)
                for x in range(distance_between - 1):
                    x += 1
                    least = min(original_row, requested_row)
                    move_list.append([least + x, original_column])
        return move_list

    def get_color(self):
        return self.color


class Pawn(Piece):

    def __init__(self, position_row, position_column, color):
        self.row = position_row
        self.column = position_column
        self.color = color
        super().__init__(position_row, position_column, color)

    def check_move(self, requested_row, requested_column):
        if self.color == "black":
            if self.row == self.original_position():
                possible_rows = [self.row - 2, self.row - 1]
                possible_column = [self.column]
            else:
                possible_rows = [self.row - 1]
                possible_column = [self.column]
            row_value = False
            column_value = False
            for x in possible_rows:
                if requested_row == x:
                    row_value = True
            for x in possible_column:
                if requested_column == x:
                    column_value = True
            if row_value is True and column_value is True:
                return True
            else:
                return False
        if self.color == "white":
            if self.row == self.original_position():
                possible_rows = [self.row + 2, self.row + 1]
                possible_column = [self.column]
            else:
                possible_rows = [self.row + 1]
                possible_column = [self.column]
            row_value = False
            column_value = False
            for x in possible_rows:
                if requested_row == x:
                    row_value = True
            for x in possible_column:
                if requested_column == x:
                    column_value = True
            if row_value is True and column_value is True:
                return True
            else:
                return False

    def original_position(self):
        if self.color == "black":
            return 7
        if self.color == "white":
            return 2

    def return_type(self):
        return "Pawn"


class Knight(Piece):

    def __init__(self, position_row, position_column, color):
        self.row = position_row
        self.column = position_column
        self.color = color
        super().__init__(position_row, position_column, color)

    def check_move(self, requested_row, requested_column):
        possible_rows = [self.row - 2, self.row + 2, self.row - 1, self.row + 1]
        possible_column = [self.column - 1, self.column + 1, self.column + 2, self.column - 2]
        row_value = False
        column_value = False
        row_position = None
        for x in range(len(possible_rows)):
            if requested_row == possible_rows[x]:
                row_value = True
                row_position = x
        if row_position == 0 or row_position == 1:
            if requested_column == possible_column[0] or requested_column == possible_column[1]:
                column_value = True
        else:
            if requested_column == possible_column[2] or requested_column == possible_column[3]:
                return True
        if row_value is True and column_value is True:
            return True
        else:
            return False

    def return_type(self):
        return "Knight"


class Rook(Piece):

    def __init__(self, position_row, position_column, color):
        self.row = position_row
        self.column = position_column
        self.color = color
        super().__init__(position_row, position_column, color)

    def check_move(self, requested_row, requested_column):
        if (requested_row == self.row and not requested_column == self.column) or (requested_column == self.column and not requested_row == self.row):
            return True
        else:
            return False

    def return_type(self):
        return "Rook"


class Bishop(Piece):
    def __init__(self, position_row, position_column, color):
        self.row = position_row
        self.column = position_column
        self.color = color
        super().__init__(position_row, position_column, color)

    def check_move(self, requested_row, requested_column):
        row_difference = requested_row - self.row
        column_difference = requested_column - self.column
        if row_difference - column_difference == 0 or row_difference + column_difference == 0:
            return True
        else:
            return False

    def return_type(self):
        return "Bishop"


class Queen(Piece):
    def __init__(self, position_row, position_column, color):
        self.row = position_row
        self.column = position_column
        self.color = color
        super().__init__(position_row, position_column, color)

    def check_move(self, requested_row, requested_column):
        if requested_column == self.column or requested_row == self.row:
            if (requested_row == self.row and not requested_column == self.column) or (requested_column == self.column and not requested_row == self.row):
                return True
            else:
                return False
        else:
            row_difference = requested_row - self.row
            column_difference = requested_column - self.column
            if row_difference - column_difference == 0 or row_difference + column_difference == 0:
                return True
            else:
                return False

    def return_type(self):
        return "Queen"


class King(Piece):
    def __init__(self, position_row, position_column, color):
        self.row = position_row
        self.column = position_column
        self.color = color
        super().__init__(position_row, position_column, color)

    def check_move(self, requested_row, requested_column):
        possible_rows = [self.row + 1, self.row, self.row - 1]
        possible_column = [self.column - 1, self.column, self.column + 1]
        row_value = False
        column_value = False
        for x in range(len(possible_rows)):
            if requested_row == possible_rows[x]:
                row_value = True
        for x in possible_column:
            if requested_column == x:
                column_value = True
        if row_value is True and column_value is True:
            return True
        else:
            return False

    def return_type(self):
        return "King"


class Board(object):

    def __init__(self, white_positions, black_positions):
        self.white = white_positions
        self.black = black_positions

    def change_positions(self, new_white_positions, new_black_positions):
        self.white = new_white_positions
        self.black = new_black_positions

    def check_path(self, piece, requested_row, requested_column):
        piece_type = piece.return_type()
        if piece_type == "Knight":
            if piece.check_move(requested_row, requested_column):
                return True
        else:
            path = piece.path(requested_row, requested_column)
            for q in path:
                for p in self.black:
                    if q == p:
                        return False
                for n in self.white:
                    if q == n:
                        return False
            return True


white = []
black = []


pawn_1 = Pawn(2, 1, "white")
pawn_2 = Pawn(2, 2, "white")
pawn_3 = Pawn(2, 3, "white")
pawn_4 = Pawn(2, 4, "white")
pawn_5 = Pawn(2, 5, "white")
pawn_6 = Pawn(2, 6, "white")
pawn_7 = Pawn(2, 7, "white")
pawn_8 = Pawn(2, 8, "white")
rook_1 = Rook(1, 1, "white")
rook_2 = Rook(1, 8, "white")
knight_1 = Knight(1, 2, "white")
knight_2 = Knight(1, 7, "white")
bishop_1 = Bishop(1, 3, "white")
bishop_2 = Bishop(1, 6, "white")
queen_1 = Queen(1, 4, "white")
king_1 = King(1, 5, "white")
white.append(pawn_1)
white.append(pawn_2)
white.append(pawn_3)
white.append(pawn_4)
white.append(pawn_5)
white.append(pawn_6)
white.append(pawn_7)
white.append(pawn_8)
white.append(rook_1)
white.append(rook_2)
white.append(knight_1)
white.append(knight_2)
white.append(bishop_1)
white.append(bishop_2)
white.append(queen_1)
white.append(king_1)

pawn_9 = Pawn(7, 1, "black")
pawn_10 = Pawn(7, 2, "black")
pawn_11 = Pawn(7, 3, "black")
pawn_12 = Pawn(7, 4, "black")
pawn_13 = Pawn(7, 5, "black")
pawn_14 = Pawn(7, 6, "black")
pawn_15 = Pawn(7, 7, "black")
pawn_16 = Pawn(7, 8, "black")
rook_3 = Rook(8, 1, "black")
rook_4 = Rook(8, 8, "black")
knight_3 = Knight(8, 2, "black")
knight_4 = Knight(8, 7, "black")
bishop_3 = Bishop(8, 3, "black")
bishop_4 = Bishop(8, 6, "black")
queen_2 = Queen(8, 4, "black")
king_2 = King(8, 5, "black")
black.append(pawn_9)
black.append(pawn_10)
black.append(pawn_11)
black.append(pawn_12)
black.append(pawn_13)
black.append(pawn_14)
black.append(pawn_15)
black.append(pawn_16)
black.append(rook_3)
black.append(rook_4)
black.append(knight_3)
black.append(knight_4)
black.append(bishop_3)
black.append(bishop_4)
black.append(queen_2)
black.append(king_2)

board1 = Board(0, 0)
check_mate = False

white_position = []
black_position = []

while check_mate is False:
    for p in white:
        white_position.append(p.return_position())
    for q in black:
        black_position.append(q.return_position())
    board1 = Board(white_position, black_position)
    piece_color = input("What color is the piece?: ")
    piece_current_row = int(input("What row is the current piece in?: "))
    piece_current_column = int(input("What column is the current piece in?: "))
    piece_requested_row = int(input("What row would you like to move the piece to?: "))
    piece_requested_column = int(input("What column would you like to move the piece to?: "))
    counter = 0
    piece_position = None
    if piece_color == "white":
        for x in white_position:
            if x == [piece_current_row, piece_current_column]:
                piece_position = counter
                break
            else:
                counter += 1
    counter = 0
    if piece_color == "black":
        for y in black_position:
            if y == [piece_current_row, piece_current_column]:
                piece_position = counter
                break
            else:
                counter += 1
    piece = None
    if piece_color == "white":
        piece = white[piece_position]
    if piece_color == "black":
        piece = black[piece_position]
    move_check = piece.check_move(piece_requested_row, piece_requested_column)
    check_path = board1.check_path(piece, piece_requested_row, piece_requested_column)
    if move_check and check_path:
        piece.move_to(piece_requested_row, piece_requested_column)
        print("That is a good move!")
    elif move_check is False:
        print("That piece can not move to the space!")
    else:
        print("There is a piece in the way!")
    #check for checkmate: if the white king is in question, we can check the possibility for every black piece
    #to move into the space that the king is in. Transitioning this into a checkmate clause would require me to check
    #all the other open spaces around the king. and then when finding the pieces that are endangering the king,
    #I would need to check if the pieces around the king could move to block the path of the piece.

    #capturing pieces, find what other piece is in the position using the same functionality for finding what piece
    #was requested, then simply removing that piece from the other color's list














