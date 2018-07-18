class Board():
    def __init__(self):
        self.spaces = [None] * 9

    def is_empty_at(self, space):
        return self.spaces[space] is None

    def mark(self, space, symbol):
        if self.is_empty_at(space):
            self.spaces[space] = symbol
        else:
            raise ValueError("Invalid Move !")

    def is_there_a_winner(self):
        winningCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [6, 4, 2]]

        for group in winningCombos:
            if None in [e for i,e in enumerate(self.spaces) if i in group]:
                continue

            if self.spaces[group[0]] == self.spaces[group[1]] == self.spaces[group[2]]:
                # if self.spaces[group[0]] is not None:
                    return True

        return False

    def makeMove(self, letter, space):
        self.spaces[space] = letter


    def isSpaceFree(self, space):
        return self.spaces[space] == ' '


    def is_the_game_board_Full(self):
        for i in range(0, 8):
            if isSpaceFree(self, i):
                return False
        return True

    def new_board():


        board = []
        for square in range(0,8):
            board.append(" ")
        return board



    def draw(self):

        #ttt_board var could be changed to just self.spaces
        nones_to_spaces = [ " " if s is None else s for s in self.spaces]
        return """
-------
|{}|{}|{}|
-------
|{}|{}|{}|
-------
|{}|{}|{}|
-------
        """.strip().format(*nones_to_spaces)
