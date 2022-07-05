import random


class ReverseTicTacToe:
    PLAY_BOARD = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
                  'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    EMPTY_MARK = '_'
    PLAYERS_MARKS = ['O', 'X']
    WIDTH = 10
    HEIGHT = 10
    M_COMPUTER_UNITS = []

    def __init__(self):
        '''Init ReverseTicTacToe the game'''
        self.BOARD = [[self.EMPTY_MARK for MARK in range(self.WIDTH)]
                               for MARK in range(self.HEIGHT)]
        self.COMPUTER_UNITS = [(H_UNIT, W_UNIT) for H_UNIT in range(self.HEIGHT)
                                for W_UNIT in range(self.WIDTH)]
        self.WIDTH -= 1
        self.HEIGHT -= 1

    def run(self):
        '''Run the game'''
        while True:
            self.print_board()
            unit = self.i_unit()
            self.move(unit, self.PLAYERS_MARKS[1])
            if self.find_unit(unit, self.PLAYERS_MARKS[1]):
                unit, is_fail = self.computer_move()
                self.move(unit, self.PLAYERS_MARKS[0])
                if is_fail:
                    print('  /////////////////////')
                    print('You win!')
                    break
            else:
                print('  /////////////////////')
                print('You lose!')
                break

    def print_board(self):
        '''Function for print game board'''
        print('   Reversed Tic-Tac-Toe')
        print('   A B C D E F G H I J')
        print('  /////////////////////')
        i = 0
        for string in self.BOARD:
            print(i, end=' |')
            for unit in string:
                print(unit, end='|')
            print(' ')
            i += 1

    def i_unit(self):
        '''Function for user input'''
        print('  /////////////////////')
        while True:
            unit = input('Input letter and number: ').strip()
            if (len(unit) == 2 and unit[1].isdigit()
                    and unit[0].upper() in self.PLAY_BOARD
                    and 0 <= int(unit[1]) <= 9):
                unit = (int(unit[1]), self.PLAY_BOARD[unit[0].upper()])
                if self.BOARD[unit[0]][unit[1]] == self.EMPTY_MARK:
                    return unit
                else:
                    print('Error, enter the empty mark')
            else:
                print('Error, out of board')

    def move(self, unit, mark):
        '''Function that make player move'''
        self.BOARD[unit[0]][unit[1]] = mark
        if unit in self.COMPUTER_UNITS:
            del self.COMPUTER_UNITS[self.COMPUTER_UNITS.index(unit)]

    def computer_move(self):
        '''Function that make computer move'''
        while True:
            if self.COMPUTER_UNITS:
                unit = random.choice(self.COMPUTER_UNITS)
                del self.COMPUTER_UNITS[self.COMPUTER_UNITS.index(unit)]
                if self.find_unit(unit, self.PLAYERS_MARKS[0]):
                    return (unit, False)
                else:
                    self.M_COMPUTER_UNITS.append(unit)
            else:
                unit = random.choice(self.M_COMPUTER_UNITS)
                return (unit, True)

    def find_unit(self, unit, mark):
        '''Function for check players move finding unit'''
        def get_c_on_line(s_i, s_j):
            '''Find count on the line'''
            i = unit_i
            j = unit_j
            count = 0
            for x in range(4):
                if s_i == '+':
                    i += 1
                elif s_i == '-':
                    i -= 1
                if s_j == '+':
                    j += 1
                elif s_j == '-':
                    j -= 1

                if not (0 <= i <= self.HEIGHT) or not (0 <= j <= self.WIDTH):
                    break
                if self.BOARD[i][j] != mark:
                    break
                count += 1
            return count

        unit_i = unit[0]
        unit_j = unit[1]

        '''To calculate the lose one by horizontal, vertical and diagonal'''
        offsets = (
            ((0, "-"), (0, "+")),
            (("-", 0), ("+", 0)),
            (("-", "-"), ("+", "+")),
            (("+", "-"), ("-", "+")),
        )
        for offset in offsets:
            c_mark = 1 + get_c_on_line(*offset[0]) + get_c_on_line(*offset[1])
            if c_mark >= 5:
                return False

        return True


if __name__ == '__main__':
    ReverseTicTacToe().run()