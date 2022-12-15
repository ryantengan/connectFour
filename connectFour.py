import tkinter as tk

window = tk.Tk()

c = tk.Canvas(window, width = 440, height = 370, bg = "blue")

class Connect_Four:

    def __init__(self):
        self.grid = [[' ' for columns in range(7)] for rows in range(6)]
        self.grid_display = [[' ' for columns in range(7)] for rows in range(6)]
        self.turn = 0
        self.player = 0
        self.player_token = None
        self.game_active = True
        self.player_won = False
        self.create_board_display()
        self.switch_token()
        self.select_column()

    def create_board_display(self):
        offset = 55
        r = 25
        for column in range(1,8):
            for row in range(1,7):
                x_inital = offset * column - r
                y_initial = offset * row - r
                x_final = offset * column + r
                y_final = offset * row + r
                token_slot = c.create_oval(x_inital, y_initial, x_final, y_final, fill = "black")
                self.grid_display[row - 1][column - 1] = token_slot
                c.pack()

    def switch_token(self):
        if self.player_won == False:
            self.turn += 1
            if self.turn % 2 == 1:
                self.player = 1
                self.player_token = "O"
                self.player_color = "red"
            else:
                self.player = 2
                self.player_token = "X"
                self.player_color = "yellow"

    def declare_victor(self):
        c.delete('all')
        c.config(bg = self.player_color)
        if self.player_color == 'red':
            c.create_text(220, 185, text = "Red player wins!", font = ('Arial', 30))
        else:
            c.create_text(220, 185, text = "Yelllow player wins!", font = ('Arial', 30))

    def select_column(self):
        window.bind('<Key>', self.drop_token)

    def drop_token(self, event):
        if self.player_won == False:
            invalid_column_choice = False
            valid_columns_list = [str(valid_column) for valid_column in range(1,8)]
            column_choice = event.char
            if column_choice in valid_columns_list:
                column = int(column_choice) - 1
                for row in range(5,-1,-1):
                    if self.grid[row][column] == ' ':
                        self.grid[row][column] = self.player_token
                        c.itemconfig(self.grid_display[row][column], fill = self.player_color)
                        break
                    if row - 1 == -1:
                        invalid_column_choice = True
                for row in self.grid:
                    print(row)
                print("\n")
            elif invalid_column_choice == True or column_choice not in valid_columns_list:
                print("Invalid column choice!")
                self.turn -= 1
                self.select_column()
            self.check_for_completion()
            self.switch_token()
        else:
            self.declare_victor()

    def check_for_completion(self):
        self.count_horizontal()
        self.count_vertical()
        self.count_diagonal()
    
    def count_horizontal(self):
        horizontal_streak = 0
        for row in self.grid:
            for column in row:
                if column == self.player_token:
                    horizontal_streak += 1
                    if horizontal_streak == 4:
                        self.player_won = True
                else:
                    horizontal_streak = 0

    def count_vertical(self):
        vertical_count = 0
        for column in range(len(self.grid[1])):
            if vertical_count == 4:
                self.player_won = True
                break
            else:
                vertical_count = 0
                for row in range(len(self.grid)):
                    if row == len(self.grid) and vertical_count < 4:
                        vertical_count = 0
                        break
                    if self.grid[row][column] == self.player_token:
                        vertical_count += 1
                        if vertical_count == 4:
                            self.player_won = True
                            break
                    else:
                        vertical_count = 0
    
    def count_diagonal(self):
        for baseRow in range(5):
            for baseColumn in range(7):
                rowNumber = baseRow
                columnNumber = baseColumn
                right_diagonal_streak = 0
                left_diagonal_count = 0
                for row in range(6):
                    if right_diagonal_streak == 4:
                        self.player_won = True
                        break
                    if columnNumber == len(self.grid[row]) or rowNumber == len(self.grid):
                        break
                    else:
                        if self.grid[rowNumber][columnNumber] == self.player_token:
                            right_diagonal_streak += 1
                        else:
                            token_count = 0
                        rowNumber += 1
                        columnNumber += 1
                if right_diagonal_streak < 4:
                    rowNumber = baseRow
                    columnNumber = baseColumn
                    for row in range(6):
                        if left_diagonal_count == 4:
                            self.player_won = True
                            break
                        if columnNumber < 0 or rowNumber == len(self.grid):
                            break
                        else:
                            if self.grid[rowNumber][columnNumber] == self.player_token:
                                left_diagonal_count += 1
                            else:
                                left_diagonal_count = 0
                            rowNumber += 1
                            columnNumber -= 1

board = Connect_Four()
window.mainloop()