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
        self.root.title("Mastermind Menu")
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

    def win_lose_check(self):
        if self.try_counter == self.guesses:
            if self.guess_list == self.pattern:
                print("You won!")
            else:
                print("You lost!")
        elif self.guess_list == self.pattern:
            print("You won!")
        else:
            print("Game Continue")


    def r_button_handler(self):
        self.guess_list.append("red")
        new_peg = tk.Button(self.guess_window, background="red", width=1, height=1)
        new_peg.grid(row=0, column=self.guess_tracker+1, padx=5, pady=10)
        self.guess_tracker += 1
        self.current_guess_buttons.append(new_peg)
        if len(self.guess_list) == len(self.pattern):
            self.try_counter += 1
            self.win_lose_check()
            for i in self.current_buttons:
                i.destroy()
            self.load_pegs()
            self.game.update()
            self.guess_list.clear()
            self.guess_tracker = 0
            for i in self.current_guess_buttons:
                i.destroy()
            #print("Updated")

    def y_button_handler(self):
        self.guess_list.append("yellow")
        new_peg = tk.Button(self.guess_window, background="yellow", width=1, height=1)
        new_peg.grid(row=0, column=self.guess_tracker + 1, padx=5, pady=10)
        self.guess_tracker += 1
        self.current_guess_buttons.append(new_peg)
        if len(self.guess_list) == len(self.pattern):
            self.try_counter += 1
            self.win_lose_check()
            for i in self.current_buttons:
                i.destroy()
            self.load_pegs()
            self.game.update()
            self.guess_list.clear()
            self.guess_tracker = 0
            for i in self.current_guess_buttons:
                i.destroy()
            #print("Updated")

    def b_button_handler(self):
        self.guess_list.append("blue")
        new_peg = tk.Button(self.guess_window, background="blue", width=1, height=1)
        new_peg.grid(row=0, column=self.guess_tracker + 1, padx=5, pady=10)
        self.guess_tracker += 1
        self.current_guess_buttons.append(new_peg)
        if len(self.guess_list) == len(self.pattern):
            self.try_counter += 1
            self.win_lose_check()
            for i in self.current_buttons:
                i.destroy()
            self.load_pegs()
            self.game.update()
            self.guess_list.clear()
            self.guess_tracker = 0
            for i in self.current_guess_buttons:
                i.destroy()
            #print("Updated")

    def g_button_handler(self):
        self.guess_list.append("green")
        new_peg = tk.Button(self.guess_window, background="green", width=1, height=1)
        new_peg.grid(row=0, column=self.guess_tracker + 1, padx=5, pady=10)
        self.guess_tracker += 1
        self.current_guess_buttons.append(new_peg)
        if len(self.guess_list) == len(self.pattern):
            self.try_counter += 1
            self.win_lose_check()
            for i in self.current_buttons:
                i.destroy()
            self.load_pegs()
            self.game.update()
            self.guess_list.clear()
            self.guess_tracker = 0
            for i in self.current_guess_buttons:
                i.destroy()

            #print("Updated")

    def guess_input(self):
        self.guess_window = tk.Toplevel(self.root)
        self.guess_window.title("Input your guess")
        self.guess_window.minsize(100, 100)
        self.guess_window.geometry("250x100+500+300")
        self.guess_window.rowconfigure(0, weight=1)
        self.guess_window.columnconfigure(0, weight=1)

        self.guess_tracker = 0
        self.current_guess_buttons = []

        tk_text = tk.Text(self.guess_window, height=1, width=10)
        text = "Your guess: "
        tk_text.grid(row=0, column=0)
        tk_text.insert(tk.INSERT, text)
        tk_text.config(state=tk.DISABLED)

        r_button = tk.Button(self.guess_window, background="red", command=self.r_button_handler, width=1, height=1)
        r_button.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)

        y_button = tk.Button(self.guess_window, background="yellow", command=self.y_button_handler, width=1, height=1)
        y_button.grid(row=1, column=2, padx=5, pady=5, sticky=tk.NSEW)

        b_button = tk.Button(self.guess_window, background="blue", command=self.b_button_handler, width=1, height=1)
        b_button.grid(row=1, column=3, padx=5, pady=5, sticky=tk.NSEW)

        g_button = tk.Button(self.guess_window, background="green", command=self.g_button_handler, width=1, height=1)
        g_button.grid(row=1, column=4, padx=5, pady=5, sticky=tk.NSEW)



        """
        #Testing guesses
        guess = tk.Entry(self.guess_window)
        guess.insert(0, "Enter your guess.")
        guess.grid(row=0, column=0)
        guess.bind("<Return>", self.temp_guess_list)
        """


    def load_pegs(self):
        placement = 0
        self.current_buttons = []
        for color in self.pattern:
            if len(self.guess_list) != len(self.pattern):
                new_peg = tk.Button(self.game, background="white", width=1, height=1)
                new_peg.grid(row=0, column=placement, padx=5, pady=10)
                self.current_buttons.append(new_peg)
            else:
                if self.guess_list[placement] == color:
                    new_peg = tk.Button(self.game, background=color, width=1, height=1)
                    new_peg.grid(row=0, column=placement, padx=5, pady=10)
                    self.current_buttons.append(new_peg)
                else:
                    new_peg = tk.Button(self.game, background="white", width=1, height=1)
                    new_peg.grid(row=0, column=placement, padx=5, pady=10)
                    self.current_buttons.append(new_peg)
            placement += 1


    def game_loop(self):
        self.game = tk.Toplevel(self.root)
        self.game.title("Mastermind")
        self.game.geometry("250x50+500+200")

        self.random_pattern()
        #print(self.pattern)
        self.try_counter = 0
        self.guess_list = []
        self.load_pegs()
        self.guess_input()






def main():
    game = Mastermind()

if __name__ == '__main__':
    main()

