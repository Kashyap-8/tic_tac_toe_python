
class Gamestate: 
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.current_player = 'x'
        self.moves_made = 0 

    def print_board (self):
        for row in range(3): 
            for col in range(3): 
                print(' ' + self.board[row][col] + ' ', end='') #no new line after cell
                if (col < 2): 
                    print('|', end='')
            print() #end of row
            if(row < 2):
                print("---|---|---")

    def make_move(self, row, col):
        if (row < 0 or row > 2 or col < 0 or col >2):
            return False
        if (self.board[row][col] != ' '): 
            return False
        self.board[row][col] = self.current_player
        self.moves_made += 1 
        return True
    
    def check_winner(self):
        #check row (Note: unlike c python let's use use chain comparisions)
        if(self.board[0][0] == self.board[0][1] == self.board[0][2] != ' '):
            return self.board[0][0]
        if(self.board[1][0] == self.board[1][1] == self.board[1][2] != ' '):
            return self.board[1][0]
        if(self.board[2][0] == self.board[2][1] == self.board[2][2] != ' '):
            return self.board[2][0]
        
        #check columns
        if(self.board[0][0] == self.board[1][0] == self.board[2][0] != ' '):
            return self.board[0][0]
        if(self.board[0][1] == self.board[1][1] == self.board[2][1] != ' '):
            return self.board[0][1]
        if(self.board[0][2] == self.board[1][2] == self.board[2][2] != ' '):
            return self.board[0][2]
        
        #check diagonals 
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] != ' '):
            return self.board[0][0]
        if(self.board[2][0] == self.board[1][1] == self.board[0][2] != ' '):
            return self.board[2][0] 
        
        if(self.moves_made == 9):
            return 'D'
        return ' '
    
    def switch_player(self): 
        if (self.current_player == 'x'):
            self.current_player = 'o'
        else:
            self.current_player = 'x'

    def game_loop(self):
        while(True):
            self.print_board()
            try:
                #the user input must be inside the try
                # Using f string format
                user_input = input(f"Player {self.current_player} enter row col eg (0 0): ")
                row, col = user_input.split()
                row, col = int(row), int(col)

            #catches bad format:
            except: 
                print("Invalid input please enter two coordinates eg. 0 0")
                continue
            #catches bad coordinate
            if not self.make_move(row, col): 
                print("Invalid move try again")
                continue

            winner = self.check_winner()
            if (winner) != ' ':
                self.print_board()
                if winner == 'D':
                    print("It's a draw")
                else:
                    print(f"we have a winner: {winner}")
                break
            self.switch_player()

if __name__ == "__main__":
    game = Gamestate()
    game.game_loop() 

