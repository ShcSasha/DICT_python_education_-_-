import random

class TicTacToe:

    def __init__(self):
        self.pole = []

    def create_pole(self):
         for i in range(3):
             row = []
             for j in range(3):
                 row.append('-')
             self.pole.append(row)

    def get_random_first_igrok(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, igrok):
        self.pole[row][col] = igrok


    def is_igrok_win(self, igrok):
        win = False
        n = len(self.pole)
        # Выигрыш по горизонтали
        for row in range(n):
            if (self.pole[row][0] == self.pole[row][1] == self.pole[row][2] == igrok):
                win = True
        # Выигрыш по вертикали
        for col in range(3):
            if (self.pole[0][col] == self.pole[1][col] == self.pole[2][col] == igrok):
                win = True
        # Выигрыш по диагонали 1
        if (self.pole[0][0] == self.pole[1][1] == self.pole[2][2] == igrok):
            win = True
        # Выигрыш по диагонали 2
        if (self.pole[0][2] == self.pole[1][1] == self.pole[2][0] == igrok):
            win = True

        return win


    def is_pole_filled(self):
        filled = True
        for row in self.pole:
            for item in row:
                if item == '-':
                    filled = False

        return filled

    def is_cell_filled(self, row, col):
        filled = False
        if (self.pole[row][col] != '-'):
                filled = True
        return filled


    def swap_igrok_turn(self, igrok):
        return 'X' if igrok == 'O' else 'O'

    def show_pole(self):
        for row in self.pole:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_pole()
        count = 0
        igrok = 'O' if self.get_random_first_igrok() == 1 else 'X'
        self.show_pole()

        while True:
            print(f"igrok {igrok} turn")

            row, col = list(
                map(int, input("Enter cells: ").split()))
            print()

            if (not self.is_cell_filled(row - 1, col - 1)):
                self.fix_spot(row - 1, col - 1, igrok)
                count += 1
                self.show_pole()
                if self.is_igrok_win(igrok):
                    print(f"Player {igrok} wins the game!")
                    break

                if self.is_pole_filled():
                    print("Match Draw!")
                    break
                igrok = self.swap_igrok_turn(igrok)
            else:
                print("That place is already filled.")
                continue

        print()

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()