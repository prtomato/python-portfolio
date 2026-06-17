# Author: Joshua Long
# GitHub username: prtomato
# Date: 11/29/25
# Description: This file holds tests for different aspects and methods of the AnimalGame file.

import unittest
from AnimalGame import *

class TestAnimalGame(unittest.TestCase):
    """
    This class runs multiple test cases for the AnimalGame file's classes.
    """

    def test_valid_distances(self):
        """
        This method tests the validity of the different distances that different movements can make.
        Essentially, sliding pieces can move up to their max distance, and jumping ones can only move
        the max distance.
        """

        game = AnimalGame()

        # Testing the max distance for the sliding movement of the Okapi piece from the Tangerine player.
        self.assertIs(game.make_move("a1", "a5"), True)

        # Testing the max distance for the jumping movement of the Wombat piece from the Amethyst player.
        self.assertIs(game.make_move("b7", "b6"), True)

        # Testing a distance less than the max for the sliding movement of the Okapi piece from the Tangerine player.
        self.assertIs(game.make_move("a5", "a3"), True)

        # Testing the max distance for the jumping movement of the Kinkajou piece from the Amethyst player.
        self.assertIs(game.make_move("e7", "b4"), True)

        # Testing the max distance for the sliding movement of the Cuttlefish piece from the Tangerine player.
        self.assertIs(game.make_move("d1", "f3"), True)

        # Testing a distance less than the max for the jumping movement of the Kinkajou piece from the Amethyst player.
        self.assertIs(game.make_move("b4", "d6"), False)
        game.set_player_turn("TANGERINE")

        # Testing a distance less than the max for the sliding movement of the Cuttlefish piece from the Tangerine
        # player.
        self.assertIs(game.make_move("f3", "e2"), True)

        # Testing a distance greater than the max for the jumping movement of the Wombat piece from the Amethyst
        # player.
        self.assertIs(game.make_move("b6", "b4"), False)
        game.set_player_turn("TANGERINE")

        # Testing a distance greater than the max for the sliding movement of the Cuttlefish piece from the Tangerine
        # player.
        self.assertIs(game.make_move("e2", "b5"), False)


    def test_valid_directions(self):
        """
        This method tests the validity of the different directions that different movements can make.
        The pieces that move orthogonal can move to the max amount that way but also one space diagonally.
        The pieces that move diagonally can move to the max amount that way but also one space orthogonally.
        """

        game = AnimalGame()

        # Testing the orthogonal direction the Okapi piece is supposed to move in for the Tangerine player.
        self.assertIs(game.make_move("a1", "a5"), True)

        # Testing the alternative diagonal direction the Okapi piece can move in for the Amethyst player.
        self.assertIs(game.make_move("a7", "b6"), True)

        # Testing more than the allowed distance for the alternative diagonal direction that the Okapi piece can
        # move in for the Tangerine player.
        self.assertIs(game.make_move("a5", "c3"), False)
        game.set_player_turn("AMETHYST")

        # Testing the orthogonal direction Wombat piece is supposed to move in for the Amethyst player.
        self.assertIs(game.make_move("f7", "f6"), True)

        # Testing the alternative diagonal direction the Wombat piece can move in for the Tangerine player.
        self.assertIs(game.make_move("b1", "a2"), True)

        # Testing more than the allowed distance for the alternative diagonal direction that the Wombat piece can
        # move in for the Amethyst player.
        self.assertIs(game.make_move("f6", "d4"), False)
        game.set_player_turn("TANGERINE")

        # Testing the diagonal direction the Kinkajou piece is supposed to move in for the Tangerine player.
        self.assertIs(game.make_move("c1", "f4"), True)

        # Testing the alternative orthogonal direction the Kinkajou piece can move in for the Amethyst player.
        self.assertIs(game.make_move("c7", "c6"), True)

        # Testing more than the allowed distance for the alternative orthogonal direction the Kinkajou piece can
        # move in for the Tangerine player.
        self.assertIs(game.make_move("f4", "f2"), False)
        game.set_player_turn("AMETHYST")

        # Testing the diagonal direction the Cuttlefish piece is supposed to move in for the Amethyst player.
        self.assertIs(game.make_move("d7", "f5"), True)

        # Testing the alternative orthogonal direction the Cuttlefish piece can move in for the Tangerine player.
        self.assertIs(game.make_move("d1", "d2"), True)

        # Testing more than the allowed distance for the alternative orthogonal direction the Cuttlefish piece can
        # move in for the Amethyst player.
        self.assertIs(game.make_move("f5", "f3"), False)


    def test_piece_blocking(self):
        """
        This method tests if the sliding pieces will not be allowed to move with a piece blocking their path.
        It will also test to make sure jumping pieces will not be blocked if there is a piece in their path.
        """

        game = AnimalGame()

        # Testing if the Tangerine player's Okapi blocks the movement attempted by the Amethyst player's Okapi
        # because it is trying to move past it and not capture the piece.
        self.assertIs(game.make_move("a1", "a5"), True)     # Tangerine
        self.assertIs(game.make_move("a7", "a3"), False)    # Amethyst
        game.set_player_turn("TANGERINE")

        # Testing if the Amethyst player's Kinkajou will jump over the Tangerine player's Okapi
        self.assertIs(game.make_move("a5", "e5"), True)     # Tangerine
        self.assertIs(game.make_move("c7", "f4"), True)     # Amethyst


    def test_captures(self):
        """
        This method tests the capturing of different pieces and also makes sure that the players cannot capture
        their own pieces.
        """

        game = AnimalGame()

        # Testing the Amethyst player capturing the Tangerine player's Okapi
        self.assertIs(game.make_move("a1", "a5"), True)     # Tangerine
        self.assertIs(game.make_move("a7", "a5"), True)     # Amethyst

        # Testing the Tangerine player attempting to capture their own Kinkajou piece
        self.assertIs(game.make_move("b1", "c1"), False)    # Tangerine
        game.set_player_turn("AMETHYST")

        # Testing the Tangerine player capturing the Amethyst player's Okapi
        self.assertIs(game.make_move("g7", "g4"), True)     # Amethyst
        game.set_player_turn("AMETHYST")
        self.assertIs(game.make_move("g4", "f4"), True)     # Amethyst
        self.assertIs(game.make_move("c1", "f4"), True)     # Tangerine


    def test_turn_order(self):
        """
        This method tests that the turns are being rotated successfully.
        """

        game = AnimalGame()

        # Testing if the Tangerine player chooses an invalid move, if it is still that players turn.
        self.assertEqual(game.get_player_turn(), "TANGERINE")
        self.assertIs(game.make_move("a1", "b1"), False)    # Tangerine
        self.assertEqual(game.get_player_turn(), "TANGERINE")

        # Testing if the turn is successfully passed after a valid move.
        self.assertIs(game.make_move("a1", "a2"), True)     # Tangerine
        self.assertEqual(game.get_player_turn(), "AMETHYST")


    def test_game_state(self):
        """
        This method will test if the get_game_state() method will return the proper game state at different
        moments.
        """

        game = AnimalGame()

        # Testing if it was initialized correctly
        self.assertEqual(game.get_game_state(), "UNFINISHED")

        # Testing if it remains unchanged after a piece get captured.
        self.assertIs(game.make_move("a1", "a3"), True)     # Tangerine
        self.assertIs(game.make_move("a7", "a3"), True)     # Amethyst
        self.assertEqual(game.get_game_state(), "UNFINISHED")

        # Testing if the game state successfully switches after the Tangerine player's Cuttlefish piece
        # gets captured.
        game.set_player_turn("AMETHYST")
        self.assertIs(game.make_move("a3", "d3"), True)     # Amethyst
        game.set_player_turn("AMETHYST")
        self.assertIs(game.make_move("d3", "d1"), True)     # Amethyst
        self.assertEqual(game.get_game_state(), "AMETHYST_WON")

        # Testing to see if a player can make a move after the game is over.
        self.assertIs(game.make_move("b1", "b2"), False)    # Tangerine

        # Second game to test for the game state of Tangerine winning.
        game2 = AnimalGame()

        # Testing to see if the game state reflects that the Tangerine player won and no more moves
        # can be made.
        self.assertEqual(game2.get_game_state(), "UNFINISHED")
        self.assertIs(game2.make_move("a1", "a5"), True)
        game2.set_player_turn("TANGERINE")
        self.assertIs(game2.make_move("a5", "d5"), True)
        game2.set_player_turn("TANGERINE")
        self.assertIs(game2.make_move("d5", "d7"), True)
        self.assertEqual(game2.get_game_state(), "TANGERINE_WON")
        self.assertIs(game2.make_move("a7", "a5"), False)














