class Cell:
    """
    Cell: represent a single cell on the game board

    It saves all data(markers, states) related to a cell
    """
    def __init__(self):
        self._isMine = False #Cell is a mine or not
        self._isRevealed = False #Cell is revealed by player or not
        self._isFlagged = False #Cell is flagged by player or not
        self._minesAround = 0 #The number of mines around a cell, range is [0, 8]

class Game:
    """
    Game: represent a single game

    Game holds a board of cells, and all related states (game done or game ongoing...)
    """
    def __init__(self, rows, cols, minesNumber):
        self._rows = rows
        self._cols =cols
        self._minesNumber = minesNumber #The number of mines the board holds
        self._board = [] #The size of this board should be rows*cols
        self._mines = [] #A list of cells which are mines
        self._result = 0 #Game result [0:game ongoing, 1:player win, -1: player lose]
        self._players = []
        self._current_player = None

class Player:
    """
    Player: every player has their game history, current game status
    """
    def __init__(self, name):
        self._name = name
        self._history = [] #If game finished, add game to history
