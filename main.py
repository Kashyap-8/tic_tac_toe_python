
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
    



