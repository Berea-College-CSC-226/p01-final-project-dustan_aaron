from mastermind import Mastermind
from RPS import RPS
from game_of_nim import GON
import tkinter as tk
import tkinter.ttk as ttk



class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Menu")
        self.root.maxsize(1000, 400)
        self.root.geometry("900x300+200+100")


        title = tk.Label(self.root, text="3 IN ONE: Games of the Year Edition", font=("Times New Roman", 30))
        title.grid(row=0, column=0, columnspan=4, sticky=tk.EW, padx=50, pady=10)

        mm_start = tk.Button(text="Mastermind", background="purple", foreground="white", command=self.mm_call)
        mm_start.grid(row=1, column=0, padx=10, pady=10)

        mm_label = tk.Label(self.root, text="Guess a random pattern of colors\nin a few amount of guesses.", font=("Times New Roman", 15))
        mm_label.grid(row=2, column=0, padx=10, pady=10)

        rps_start = tk.Button(text="Rock, Paper, Scissors", background="grey", foreground="white", command=self.rps_call)
        rps_start.grid(row=1, column=1, padx=10, pady=10)

        rps_label = tk.Label(self.root, text="Classic game of Roshambo!\nChoose rock, paper, or scissors\nto beat your opponent.", font=("Times New Roman", 15))
        rps_label.grid(row=2, column=1, padx=10, pady=10)

        gon_start = tk.Button(text="Game of Nim", background="yellow", command=self.gon_call)
        gon_start.grid(row=1, column=3, padx=10, pady=10)

        gon_label = tk.Label(self.root, text="Take turns taking balls out of a bowl.\nMake sure you take the last one!", font=("Times New Roman", 15))
        gon_label.grid(row=2, column=3, padx=10, pady=10)


        quit = tk.Button(self.root, text="Quit", command=exit)
        quit.grid(row=4, column=1, padx=10, pady=10)

    def mm_call(self):
        mm_game = Mastermind()

    def rps_call(self):
        rps_game = RPS()

    def gon_call(self):
        gon_game = GON()



def main():
    menu = Menu()
    menu.root.mainloop()

if __name__ == '__main__':
    main()