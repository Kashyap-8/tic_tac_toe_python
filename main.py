
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
                if col < 2: 
                    print('|', end='')
            print() #end of row
            if row < 2:
                print("---|---|---")

    def make_move(self, row, col):
        if  row < 0 or row > 2 or col < 0 or col >2:
            return False
        if  self.board[row][col] != ' ': 
            return False
        self.board[row][col] = self.current_player
        self.moves_made += 1 
        return True
    
    def check_winner(self):
        #check row (Note: unlike c python let's use use chain comparisions)
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != ' ':
            return self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2] != ' ':
            return self.board[1][0]
        if self.board[2][0] == self.board[2][1] == self.board[2][2] != ' ':
            return self.board[2][0]
        
        #check columns
        if self.board[0][0] == self.board[1][0] == self.board[2][0] != ' ':
            return self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1] != ' ':
            return self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2] != ' ':
            return self.board[0][2]
        
        #check diagonals 
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
            return self.board[2][0] 
        
        if self.moves_made == 9:
            return 'D'
        return ' '
    
    def switch_player(self): 
        if  self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'

    def game_loop(self):
        while True:
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
            if not self.make_move (row, col): 
                print("Invalid move try again")
                continue

            winner = self.check_winner()
            if  winner != ' ':
                self.print_board()
                if winner == 'D':
                    print("It's a draw")
                else:
                    print(f"we have a winner: {winner}")
                break
            self.switch_player()


if __name__ == "__main__":
    game = Gamestate()
    # game.game_loop() 






# pygame libraries: https://www.pygame.org/docs/

import pygame
# game loop on pygame 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock() #clock to keep track of time?
pygame.display.set_caption("tic tac toe") # title

#constants for the pygame window
WIDTH, HEIGHT = 1280, 720 
#cell size
cell_width = WIDTH // 3 
cell_height = HEIGHT // 3 
#color for the grid
BLACK = (0, 0, 0)
#grid border width
LINE_WIDTH = 3

# constants for the draw_board (shapes: 'x' or 'o')
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)
size = 80 
radius = 80


def draw_board(screen, game): 

    for row in range(3): 
        for col in range(3): 
            cell = game.board[row][col]
            
            center_x = col * cell_width  + cell_width  // 2   
            center_y = row * cell_height + cell_height // 2 
            if cell == 'x':
                #diagonal
                # top left to bottom right
                pygame.draw.line(screen, X_COLOR, (center_x - size, center_y - size), (center_x + size, center_y + size), LINE_WIDTH)
                # top right to bottom left
                pygame.draw.line(screen, X_COLOR, (center_x + size, center_y - size), (center_x - size, center_y + size), LINE_WIDTH)
            elif cell == 'o':
                #circle 
                pygame.draw.circle(screen, O_COLOR, (center_x, center_y), radius, LINE_WIDTH)

    # vertical grid lines
    pygame.draw.line(screen, BLACK, (cell_width, 0), (cell_width, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (cell_width * 2, 0), (cell_width * 2, HEIGHT), LINE_WIDTH) 

    # horizontal grif lines (note that the parameters are flipped)
    pygame.draw.line(screen, BLACK, (0, cell_height), (WIDTH, cell_height), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, cell_height * 2), (WIDTH, cell_height * 2), LINE_WIDTH)

running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("grey")
    
    #call draw board function
    draw_board(screen, game)

    pygame.display.flip()

    clock.tick(60) #limits fps to 60 (60Hz)

pygame.quit()

