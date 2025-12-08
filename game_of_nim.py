######################################################################
# Author: Stephen Aaron Robinson and Dustan M. Webb
# Username: robinsons3, webbd3
#
# Assignment:P01: including the code from:HW06: The Game of Nim
#
# Purpose: To challenge the user to The Game of Nim
#
######################################################################
import tkinter as tk
import random

class GON:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game of Nim")
        self.window.geometry("750x200+250+100")
        self.balls = 16
        self.player_win = False
        self.player_lose = False
        self.title_lable = tk.Label(self.window, text = "Welcome to the Game of Nim.\nInstructions will appear when you hit play.", font=("Arial", 30))
        self.title_lable.grid(row=0, column=0, padx=10, pady=10)
        self.play_button = tk.Button(self.window, text = "Play", width = 15, command=self.game_loop)
        self.play_button.grid(row=1, column=0, padx=10, pady=10)
        self.window.mainloop()

    def game_loop(self):
        self.instructions = tk.Toplevel(self.window)
        self.instructions.title("Game of Nim")
        self.instructions.geometry("700x300+275+100")
        self.instructions_label = tk.Label(self.instructions, text = "You have been challenged to the Game of Nim.", font=("Arial", 15))
        self.instructions_label.grid(row=0, column=0, padx=10, pady=10)
        self.instructions_label2 = tk.Label(self.instructions, text="You will select a number of balls that is greater than 15 to put in a basket.", font=("Arial", 15))
        self.instructions_label2.grid(row=1, column=0, padx=10, pady=10)
        self.instructions_label3 = tk.Label(self.instructions, text="Then you and your opponent will take turns taking out 1-4 balls each turn.", font=("Arial", 15))
        self.instructions_label3.grid(row=2, column=0, padx=10, pady=10)
        self.instructions_label4 = tk.Label(self.instructions, text="Are you ready?", font=("Arial", 15))
        self.instructions_label4.grid(row=3, column=0, padx=10, pady=10)
        self.start = tk.Button(self.instructions, text="BEGIN", command=self.ask_ball_number)
        self.start.grid(row=4, column=0, padx=10, pady=10)


    def ball_setting(self, event):
        x = int(event.widget.get())
        if x > 15:
            self.balls = x
        else:
            self.balls = 16

        self.instructions.destroy()
        self.setting.destroy()
        self.game()



    def ask_ball_number(self):
        self.setting = tk.Toplevel(self.window)
        self.setting.geometry("325x100+500+200")
        balls_set_label = tk.Label(self.setting, text="How many balls will be put in the basket?\n(If a number below 16 is input, then 16 balls will be put in.)")
        balls_set_label.grid(row=0, column=0, pady=10)

        self.not_first_turn = False

        balls_entry = tk.Entry(self.setting)
        balls_entry.insert(0, self.balls)
        balls_entry.grid(row=1, column=0, pady=10)
        balls_entry.bind("<Return>", self.ball_setting)

    def game(self):
        self.game_window = tk.Toplevel(self.window)
        self.game_window.title("Game of Nim")
        self.game_window.geometry("375x175+450+200")
        if self.not_first_turn:
            game_info = tk.Label(self.game_window, text=f"Your opponent took {self.cpu_choice} balls out.\nThere are {self.balls} balls remaining.", font=("Arial", 15))
            game_info.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        else:
            game_info = tk.Label(self.game_window, text=f"There are {self.balls} balls remaining.", font=("Arial", 15))
            game_info.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
            self.not_first_turn = True

        self.win_check("cpu")
        if self.player_lose:
            self.win_lose_screen()
            self.game_window.destroy()


        take_question = tk.Label(self.game_window, text="How many balls do you want to take out?", font=("Arial", 15))
        take_question.grid(row=1, column=0, pady=10, columnspan=4)

        take_1 = tk.Button(self.game_window, text="1", command=self.take_1_ball)
        take_1.grid(row=2, column=0, padx=10, pady=10)

        take_2 = tk.Button(self.game_window, text="2", command=self.take_2_ball)
        take_2.grid(row=2, column=1, padx=10, pady=10)

        take_3 = tk.Button(self.game_window, text="3", command=self.take_3_ball)
        take_3.grid(row=2, column=2, padx=10, pady=10)

        take_4 = tk.Button(self.game_window, text="4", command=self.take_4_ball)
        take_4.grid(row=2, column=3, padx=10, pady=10)




    def cpu_choose(self):
        if self.balls % 5 == 0:
            choice = random.randint(1, 4)
            self.balls -= choice
            self.cpu_choice = choice
        else:
            choice = self.balls % 5
            self.balls -= choice
            self.cpu_choice = choice

    def take_1_ball(self):
        self.balls -= 1
        self.win_check("player")
        if self.player_win:
            self.win_lose_screen()
            self.game_window.destroy()
        else:
            self.cpu_choose()
            self.game_window.destroy()
            self.game()

    def take_2_ball(self):
        self.balls -= 2
        self.win_check("player")
        if self.player_win:
            self.win_lose_screen()
            self.game_window.destroy()
        else:
            self.cpu_choose()
            self.game_window.destroy()
            self.game()

    def take_3_ball(self):
        self.balls -= 3
        self.win_check("player")
        if self.player_win:
            self.win_lose_screen()
            self.game_window.destroy()
        else:
            self.cpu_choose()
            self.game_window.destroy()
            self.game()

    def take_4_ball(self):
        self.balls -= 4
        self.win_check("player")
        if self.player_win:
            self.win_lose_screen()
            self.game_window.destroy()
        else:
            self.cpu_choose()
            self.game_window.destroy()
            self.game()

    def win_check(self, turn):
        if self.balls <= 0:
            if turn == "player":
                print("Player wins!")
                self.player_win = True
            elif turn == "cpu":
                print("CPU wins!")
                self.player_lose = True

    def win_lose_screen(self):
        self.results = tk.Toplevel(self.window)
        if self.player_win:
            self.results.title("Win Screen")
            self.results.geometry("220x80+500+200")
            result = tk.Label(self.results, text="YOU WIN!", font=("Arial", 30))
            result.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

            #Resets attributes incase User wants to play again
            self.player_win = False
            self.balls = 16

        if self.player_lose:
            self.results.title("Losing Screen...")
            self.results.geometry("300x80+500+200")
            result = tk.Label(self.results, text="YOU'VE LOST!", font=("Arial", 30))
            result.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

            #Resets attributes incase User wants to play again
            self.player_lose = False
            self.balls = 16



def main():
    game = GON()

if __name__ == '__main__':
    main()