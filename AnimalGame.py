# Author: Joshua Long
# GitHub username: prtomato
# Date: 11/24/25
# Description: This file contains the classes that are needed to run and play an abstract
# animal-themed board game. It will be tangerine vs amethyst and tangerine always starts first.
# The game takes place on a 7x7 grid and players compete to capture the opposing player's cuttlefish.


class AnimalGame:
    """
    Represents the animal-themed board game. It creates the board for the game, creates the pieces for each
    player, sets up the board, and creates the game state. It also contains a method to try to make a valid
    move and a method to print the state of the game board.
    """

    def __init__(self):
        """
        Initializes the board for the game as a list of lists, a string keeping track of whose turn
        it is, the pieces to the board game as objects from their respective classes, and the state of the game
        as a string.
        """

        # Initializing the general data members
        self._player_turn = "TANGERINE"
        self._game_state = "UNFINISHED"

        # Initializing the Tangerine player's pieces
        self._tang_okapi1 = Okapi("TANGERINE")
        self._tang_okapi2 = Okapi("TANGERINE")
        self._tang_wombat1 = Wombat("TANGERINE")
        self._tang_wombat2 = Wombat("TANGERINE")
        self._tang_kinkajou1 = Kinkajou("TANGERINE")
        self._tang_kinkajou2 = Kinkajou("TANGERINE")
        self._tang_cuttlefish = Cuttlefish("TANGERINE")

        # Initializing the Amethyst player's pieces
        self._ameth_okapi1 = Okapi("AMETHYST")
        self._ameth_okapi2 = Okapi("AMETHYST")
        self._ameth_wombat1 = Wombat("AMETHYST")
        self._ameth_wombat2 = Wombat("AMETHYST")
        self._ameth_kinkajou1 = Kinkajou("AMETHYST")
        self._ameth_kinkajou2 = Kinkajou("AMETHYST")
        self._ameth_cuttlefish = Cuttlefish("AMETHYST")

        #Initializes the lists needed
        self._tang_pieces = [self._tang_okapi1, self._tang_wombat1, self._tang_kinkajou1, self._tang_cuttlefish,
                             self._tang_kinkajou2, self._tang_wombat2, self._tang_okapi2]

        self._blank_space1 = [None for index in range(7)]
        self._blank_space2 = [None for index in range(7)]
        self._blank_space3 = [None for index in range(7)]
        self._blank_space4 = [None for index in range(7)]
        self._blank_space5 = [None for index in range(7)]

        self._ameth_pieces = [self._ameth_okapi1, self._ameth_wombat1, self._ameth_kinkajou1, self._ameth_cuttlefish,
                              self._ameth_kinkajou2, self._ameth_wombat2, self._ameth_okapi2]

        # Initializing the board
        self._board = [self._tang_pieces, self._blank_space1, self._blank_space2, self._blank_space3,
                       self._blank_space4, self._blank_space5, self._ameth_pieces]


    def get_game_state(self):
        """
        Returns the current state of the game and if anyone has won.
        """

        return self._game_state

    def make_move(self, starting_pos, ending_pos):
        """
        This method takes in an argument for the starting position of the piece the player would want
        to move and the ending position that the player wants to move it to. It will check to see if
        it is a legal move and if not return False. A legal move means it is the current players piece,
        it is able to make the move indicated, and there are no pieces in the way if the piece slides.
        If it is a legal move it will update whose turn it is and return True.
        """

        # Checks to see if the game is already over.
        if self._game_state != "UNFINISHED":
            print(self._game_state)
            return False

        # Creates data members to use for indexing the lists
        # The column is subtracting the ASCII value of whatever was passed in from the ASCII value of 'a'.
        # It will then give us an appropriate number to use for indexing.
        start_column = int(ord(starting_pos[0]) - ord('a'))

        # The row is subtracting the number passed into it by one so that it can be used to index.
        start_row = int(starting_pos[1]) - 1

        end_column = int(ord(ending_pos[0]) - ord('a'))
        end_row = int(ending_pos[1]) - 1

        # These check to see if an invalid position was given to the method.
        if start_column > 6 or start_column < 0:
            print("Invalid starting position")
            return False

        if start_row > 6 or start_row < 0:
            print("Invalid starting position")
            return False

        if end_column > 6 or end_column < 0:
            print("Invalid ending position")
            return False

        if end_row > 6 or end_row < 0:
            print("Invalid ending position")
            return False

        # Creating a data member to house what occupies the spaces
        start_space = self._board[start_row][start_column]
        end_space = self._board[end_row][end_column]

        # This checks to see if the starting space doesn't house any piece.
        if start_space is None:
            print("There is no game piece in the starting position")
            return False

        # This checks to see if the piece in the starting space belongs to the current player.
        if start_space.get_owner() != self._player_turn:
            print("That is not your piece")
            return False

        # This checks to see if the piece in the ending space belongs to the current player.
        if end_space is not None and end_space.get_owner() == self._player_turn:
            print("You cannot capture your own piece")
            return False

        # This checks to make sure the distance between the starting and ending spaces is valid given
        # the pieces direction it can move and distance in that direction.
        if start_space.get_direction() == "ORTHOGONAL":

            # This checks the alternative diagonal movement that the orthogonal pieces can make and makes
            # sure it isn't greater than one space diagonally.
            if (start_row != end_row and start_column != end_column and (abs(start_row - end_row) > 1 or
                    abs(start_column - end_column) > 1)):

                print("That piece cannot move more than 1 space in a diagonal direction")
                return False

            # This checks to see if either the row or column distance exceeds the max distance allowed for the
            # piece to move.
            if (abs(start_row - end_row) > start_space.get_distance() or
                    abs(start_column - end_column) > start_space.get_distance()):

                print(f'That piece cannot move that many spaces. It can move a max distance of '
                      f'{start_space.get_distance()}')
                return False

        else:

            # This checks the alternative orthogonal direction that the diagonal pieces can make and makes
            # sure it isn't greater than one space orthogonally.
            if (start_row == end_row or start_column == end_column and (abs(start_row - end_row) > 1 or
                    abs(start_column - end_column) > 1)):

                print("That piece cannot move more than 1 space in an orthogonal direction")
                return False

            # This checks to make sure the distance in the diagonal direction is not greater than the max
            # distance the piece can move.
            if (abs(start_row - end_row) > start_space.get_distance() or
                    abs(start_column - end_column) > start_space.get_distance()):

                print(f'That piece cannot move that many spaces. It can move a max distance of '
                      f'{start_space.get_distance()} in a diagonal direction')
                return False

        # This checks to see if the piece is sliding, so that it will return False if the path the piece will take is
        # blocked by another piece.
        if start_space.get_movement() == "SLIDING":

            seek_row = 0
            seek_column = 0

            # This creates a seek data member for going through the rows, and it determines if the row is moving
            # in a negative or positive way.
            if start_row > end_row:
                seek_row = start_row - 1
            elif start_row < end_row:
                seek_row = start_row + 1
            else:
                seek_row = start_row

            # This creates a seek data member for going through the columns, and it determines if the column is
            # moving in a negative or positive way.
            if start_column > end_column:
                seek_column = start_column - 1
            elif start_column < end_column:
                seek_column = start_column + 1
            else:
                seek_column = start_column

            while seek_row != end_row or seek_column != end_column:

                if self._board[seek_row][seek_column] is not None:
                    print("There is a piece in the pathway of your piece")
                    return False

                if start_row > end_row:
                    seek_row -= 1
                elif start_row < end_row:
                    seek_row += 1

                if start_column > end_column:
                    seek_column -= 1
                elif start_column < end_column:
                    seek_column += 1

        # This checks to see if the movement is jumping and makes sure that the distance is not less than
        # the distance required to move by the piece.
        if start_space.get_movement() == "JUMPING" and start_space.get_direction() == "ORTHOGONAL":

            # This checks to see if the movement is the alternative diagonal option which would already be
            # excluded from this.
            if (abs(start_row - end_row) < start_space.get_distance() and
                    abs(start_column - end_column) < start_space.get_distance() and (start_row == end_row or
                    start_column == end_column)):

                print(f'The piece you chose is a jumping piece and must move {start_space.get_distance()}'
                      f' spaces')
                return False

        # THis checks to see if the jumping piece moving in a diagonal direction has less than the required
        # spaces to move
        if start_space.get_movement() == "JUMPING" and start_space.get_direction() == "DIAGONAL":

            if (start_row != end_row and start_column != end_column and
                    abs(start_row - end_row) < start_space.get_distance() and
                    abs(start_column - end_column) < start_space.get_distance()):

                print(f'The piece you chose is a jumping piece and must move {start_space.get_distance()} '
                      f'spaces')
                return False

        # This checks to see if the piece being captured is the Cuttlefish piece which will end the game
        if end_space is not None and end_space.get_name() == "cuttlefish":

            if self._board[end_row][end_column].get_owner() == "TANGERINE":

                self._game_state = "AMETHYST_WON"

            else:

                self._game_state = "TANGERINE_WON"


        # These change the end space to the piece that was moved and the starting space to None
        self._board[end_row][end_column] = start_space
        self._board[start_row][start_column] = None

        # This changes the turn based on who the current turn belongs to
        if self._player_turn == "TANGERINE":
            self._player_turn = "AMETHYST"
        else:
            self._player_turn = "TANGERINE"

        return True


    def print_board(self):
        """
        This method prints what the board looks like at any given moment.
        """

        # This iterates through each list, which acts as a row
        for row in self._board:

            # This iterates through each member of the nested list, which each act as a piece to a column
            for column in row:

                # This checks if the space holds a None value so it can print a blank placeholder.
                # If it doesn't then it will print the object's name that occupies the space.
                if column is None:
                    print("[ ]", end="\t\t,\t")
                else:
                    print(column.get_name(), end="\t,\t")

            print()


    def get_player_turn(self):
        """
        Returns whose turn it currently is.
        """

        return self._player_turn

    def set_player_turn(self, player):
        """
        Sets the turn to whoever the given player is passed into the parameter player. Mainly for the
        developer to test.
        """

        self._player_turn = player



class Piece:
    """
    Represents an animal piece of the board game. It will be inherited by the okapi, wombat, kinkajou, and
    cuttlefish game piece classes. It will also be used by the AnimalGame class to create each player's
    pieces. It receives arguments for the name of the piece, the direction the piece can move, the distance
    the piece can move, the type of movement it can perform, and who the owner of the piece is. It then
    makes private data members for each of these arguments as name, direction, distance, movement, and
    piece_owner. It also contains get methods for each of these data members. Since all the pieces for the game
    have the same basic data members, I wrote the get methods into this class, instead of each individual game piece's
    class.
    """

    def __init__(self, name, direction, distance, movement, piece_owner):
        """
        Initializes the game piece and has the parameters for name, direction, distance, movement, and
        piece_owner.
        """

        self._name = name
        self._direction = direction
        self._distance = distance
        self._movement = movement
        self._piece_owner = piece_owner

    def get_name(self):
        """
        Returns the name of the piece.
        """

        return self._name

    def get_direction(self):
        """
        Returns the direction that the piece can move.
        """

        return self._direction

    def get_distance(self):
        """
        Returns the distance that the piece can move.
        """

        return self._distance

    def get_movement(self):
        """
        Returns the movement that the piece makes.
        """

        return self._movement

    def get_owner(self):
        """
        Returns a string representing the owner of the piece.
        """

        return self._piece_owner


class Okapi(Piece):
    """
    Represents the Okapi animal piece of the board game. It inherits from the Piece class and will be used
    by the AnimalGame class to create the Okapi pieces for each player.
    """

    def __init__(self, piece_owner):
        """
        Initializes the Okapi animal piece of the board game. It takes a string parameter for the owner of the
        piece, and it will pass the name, the directions it can move, the distance it can move, and the type of
        movement it does to the parent class.
        """

        # The order of arguments is name, direction, distance, movement, and piece_owner
        # Their types are string, string, int, string, and string respectively
        super().__init__("okapi", "ORTHOGONAL", 4, "SLIDING", piece_owner)


class Wombat(Piece):
    """
    Represents the Wombat animal piece of the board game. It inherits from the Piece class and will be used by
    the AnimalGame class to create the Wombat pieces for each player.
    """

    def __init__(self, piece_owner):
        """
        It takes in a string parameter for the owner of the piece. It then passes the data for the name,
        direction, distance, movement type and the owner to the parent class.
        """

        # The order of arguments is name, direction, distance, movement, and piece_owner
        # Their types are string, string, int, string, and string respectively
        super().__init__("wombat", "ORTHOGONAL", 1, "JUMPING", piece_owner)


class Kinkajou(Piece):
    """
    Represents the kinkajou animal piece of the board game. It inherits from the Piece class and will be used by
    the AnimalGame class to create the kinkajou pieces for each player.
    """

    def __init__(self, piece_owner):
        """
        It initializes the kinkajou pieces for the board game. It takes in a string parameter for the owner of the
        piece. It then passes the data for the name, direction, distance, movement type and the owner to the parent
        class.
        """

        # The order of arguments is name, direction, distance, movement, and piece_owner
        # Their types are string, string, int, string, and string respectively
        super().__init__("kinkajou", "DIAGONAL", 3, "JUMPING", piece_owner)


class Cuttlefish(Piece):
    """
    Represents the cuttlefish piece of the board game. It inherits from the Piece class and will be used by the
    AnimalGame class to create the cuttlefish pieces for each player.
    """

    def __init__(self, piece_owner):
        """
        Initializes the cuttlefish pieces for the board game. It takes in a string parameter for the owner of the
        piece. It then passes the data for the name, direction, distance, movement type and the owner to the parent
        class.
        """

        # The order of arguments is name, direction, distance, movement, and piece_owner
        # Their types are string, string, int, string, and string respectively
        super().__init__("cuttlefish", "DIAGONAL", 2, "SLIDING", piece_owner)



