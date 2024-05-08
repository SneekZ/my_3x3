from numpy import array
import sys

class Game:
    __instance = None
    __turn = 0
    __start_board = array(['-'] * 9).reshape(3, 3)

    def __new__(cls):
        if cls.__instance:
            return cls.__instance
        return object.__new__(cls)

    def __init__(self):
        self.__board = self.__start_board.copy()
        self.running = True

    def __del__(self):
        print("Это была хорошая игра!")

    @classmethod
    def change_turn(cls):
        if cls.__turn == 1:
            cls.__turn = 0
        else:
            cls.__turn = 1

    def check_board_win(self):
        size, _ = self.__board.shape
        for i in range(size):
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] != '-':
                return True
            elif self.__board[0][i] == self.__board[1][i] == self.__board[2][i] != '-':
                return True
            elif self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != '-':
                return True
            elif self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != '-':
                return True
        return False

    def print_board(self):
        for i in self.__board:
            print(f"{i[0]} {i[1]} {i[2]}\n")

    def stop(self):
        self.running = False

    def new_game(self):
        print("Новая игра!")
        self.__board = self.__start_board.copy()


    def move(self, *args):
        x, y = args[0]
        self.__board[x][y] = self.__turn

    def check_move(self, *args):
        x, y = args[0]
        return self.__board[x][y] == '-'
    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value

    def get_board(self):
        return self.__board
