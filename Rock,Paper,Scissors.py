######################################################################
# Author: Dustan Webb
# Username: Dwebb28
#
# T12: Events and GUIs
#
# Purpose: Make a playable rock paper scissors game to be put in our mastery game
#
# Original code written by Dustan M. Webb
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter as tk
import random

class RPS:

    def __init__(self, window):
        self.window = window
        self.window.title("Rock, Paper, Scissors")
        self.title_lable = tk.Label(self.window, text="C'mon looser, choose your move.", font =("Bold", 16))
        self.title_lable.pack()#below this is me getting the buttons looking correct
        self.rock_button = tk.Button(self.window, text="rock", width = 15, command=lambda: self.play("rock"))
        self.paper_button = tk.Button(self.window, text = "paper", width = 15, command =lambda: self.play("paper") )
        self.scissors_button = tk.Button(self.window, text = "scissors", width = 15, command=lambda: self.play("scissors"))
        self.rock_button.pack()
        self.paper_button.pack()#packing the window in
        self.scissors_button.pack()
        self.result_label = tk.Label(self.window, text="Result:", font =("Bold", 16))
        self.result_label.pack()


    def play(self, player_choice): #now onto the fun part of making the game, the actual playing part.
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        if player_choice == computer_choice:
            "Run it back bru you trash."
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
            result = "I'm now going to blow up this computer because you won."
        else:
            result = "suck on these fat computer hardrive nuts looser."
            self.result_label.config(
                text=f"You chose: {player_choice}\n"
                     f"Computer chose: {computer_choice}\n\n{result}"
            )

root = tk.Tk()
app = RPS(root)
root.mainloop()
















