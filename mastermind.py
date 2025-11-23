######################################################################
# Author: Stephen Aaron Robinson
# Username: robinsons3
#
# Assignment: P01: Final Project
#
# Purpose: Plays a game of Mastermind with the user
#
######################################################################
import random
import tkinter as tk
import tkinter.ttk as ttk
from time import sleep


class Mastermind:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Menu")
        self.root.minsize(750, 400)
        self.root.maxsize(750, 400)
        self.root.geometry("750x400+250+50")
        self.pegs = 4
        self.guesses = 4

        title = tk.Label(self.root, text="MASTERMIND", font=("Times New Roman", 30))
        title.grid(row=0, column=0, columnspan=2, sticky=tk.EW, padx=250, pady=10)

        settings = tk.Button(self.root, text="settings", command=self.settings)
        settings.grid(column=0, row=2, padx=350, pady=5)

        game_start = tk.Button(self.root, text="Play", command=self.game_loop)
        game_start.grid(column=0, row=1, padx=350, pady=5)
        self.root.mainloop()



    def peg_setting(self, event):
        self.pegs = event.widget.get()

    def guess_setting(self, event):
        self.guesses = event.widget.get()

    def settings(self):
        settings_root = tk.Toplevel(self.root)
        settings_root.title("Welcome")
        settings_root.minsize(400, 200)
        settings_root.maxsize(600, 300)



        welcome_message = tk.Label(settings_root, text="Welcome to Mastermind. In this game, you must correctly guess the color combination of a number of pegs.")
        welcome_message.grid(row=0, column=0, columnspan=3)

        peg_set_label = tk.Label(settings_root, text="How many pegs do you wish to guess?")
        peg_set_label.grid(row=1, column=0, pady=10)
        peg_entry = tk.Entry(settings_root)
        peg_entry.insert(0, self.pegs)
        peg_entry.grid(row=1, column=1, pady=10)
        peg_entry.bind("<Return>", self.peg_setting)

        guess_set_label = tk.Label(settings_root, text="How many guesses do you wish to have?")
        guess_set_label.grid(row=2, column=0, pady=10)
        guess_entry = tk.Entry(settings_root)
        guess_entry.insert(0, self.guesses)
        guess_entry.grid(row=2, column=1, pady=10)
        guess_entry.bind("<Return>", self.guess_setting)

    def random_pattern(self):
        self.pattern = []

        for i in range(int(self.pegs)):
            color = (random.randint(0,3))
            if color == 0:
                color = ("red")
            elif color == 1:
                color = ("green")
            elif color == 2:
                color = ("blue")
            elif color == 3:
                color = ("yellow")
            self.pattern.append(color)

    def temp_guess_list(self, event):
        self.guess_list.append(event.widget.get())
        if len(self.guess_list) == self.pegs:
            self.load_pegs()
            self.guess_list.clear()
            self.game.update()


    def guess_input(self):
        self.guess_window = tk.Toplevel(self.root)
        self.guess_window.title("Input your guess")

        guess = tk.Entry(self.guess_window)
        guess.insert(0, "Enter your guess.")
        guess.grid(row=0, column=0)
        guess.bind("<Return>", self.temp_guess_list)


    def load_pegs(self):
        placement = 0
        for color in self.pattern:
            if len(self.guess_list) != self.pegs:
                new_peg = tk.Button(self.game, background="white", width=1, height=1)
                new_peg.grid(row=0, column=placement, padx=5, pady=10)
            else:
                if self.guess_list[placement] == color:
                    new_peg = tk.Button(self.game, background=color, width=1, height=1)
                    new_peg.grid(row=0, column=placement, padx=5, pady=10)
                else:
                    new_peg = tk.Button(self.game, background="white", width=1, height=1)
                    new_peg.grid(row=0, column=placement, padx=5, pady=10)
            placement += 1


    def game_loop(self):
        self.game = tk.Toplevel(self.root)
        self.game.title("Mastermind")

        self.random_pattern()


        self.guess_list = []

        self.guess_input()




def main():
    game = Mastermind()

if __name__ == '__main__':
    main()

