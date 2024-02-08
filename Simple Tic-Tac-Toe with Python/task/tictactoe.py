class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        print("---------")
        for row in self.board:
            print(f"| {' '.join(row)} |")
        print("---------")

    def get_user_input(self):
        while True:
            try:
                coordinates = input().split()
                i, j = map(int, coordinates)
            except ValueError:
                print("You should enter numbers!")
                continue

            if 1 <= i <= 3 and 1 <= j <= 3:
                if self.board[i - 1][j - 1] == ' ':
                    return i - 1, j - 1
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def start_game(self):
        current_player = 'X'
        while True:
            self.print_board()
            i, j = self.get_user_input()
            self.board[i][j] = current_player

            if self.check_winner(current_player):
                self.print_board()
                print(f"{current_player} wins!")
                break

            if all(cell != ' ' for row in self.board for cell in row):
                self.print_board()
                print("Draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
