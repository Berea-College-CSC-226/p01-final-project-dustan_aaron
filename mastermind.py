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

class Mastermind:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mastermind")
        self.root.minsize(750, 400)
        self.root.maxsize(750, 400)
        self.root.geometry("750x400+250+50")
        self.root.mainloop()

        self.pegs = 4
        settings = tk.Button(self.root, text="settings", command=self.settings())
        settings.grid(column=0, row=0)
        print(self.pegs)
        self.random_pattern()


    def peg_setting(self, event):
        self.pegs = event.widget.get()
        print(self.pegs)

    def guess_setting(self, event):
        self.guesses = event.widget.get()
        print(self.guesses)

    def settings(self):
        settings_root = tk.Toplevel(self.root)
        settings_root.title("Welcome")

        welcome_message = tk.Label(settings_root, text="Welcome to Mastermind. In this game, you must correctly guess the color combination of a number of pegs.")
        welcome_message.grid(row=0, column=0, columnspan=3)

        peg_set_label = tk.Label(settings_root, text="How many pegs do you wish to guess?")
        peg_set_label.grid(row=1, column=0, pady=10)
        peg_entry = tk.Entry(settings_root)
        peg_entry.insert(0, "4")
        peg_entry.grid(row=1, column=1, pady=10)
        peg_entry.bind("<Return>", self.peg_setting)

        guess_set_label = tk.Label(settings_root, text="How many guesses do you wish to have?")
        guess_set_label.grid(row=2, column=0, pady=10)
        guess_entry = tk.Entry(settings_root)
        guess_entry.insert(0, "3")
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

def main():
    game = Mastermind()
    print(game.pattern)
if __name__ == '__main__':
    main()

