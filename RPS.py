######################################################################
# Author: Dustan Webb
# Username: Dwebb28
#
# T12: Events and GUIs
#
# Purpose: Make a playable rock paper scissors game to be put in our mastery game.
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
        self.rock_button = tk.Button(self.window, text="Rock", width = 15, command=lambda: self.play("Rock"))
        self.paper_button = tk.Button(self.window, text = "Paper", width = 15, command=lambda: self.play("Paper") )
        self.scissors_button = tk.Button(self.window, text = "Scissors", width = 15, command=lambda: self.play("Scissors"))
        self.rock_button.pack()#command lambda is something I found on google in tkinter explorations that is different
#buttons that calls to the same function but has can produce a different output. With Rock paper scissors being
#same function but different output I needed to find something.
#tkinter button that calls the same function but can produce two different outputs (what I searched) google output:You
#can make a Tkinter button call the same function but produce different outputs by passing an argument to the function when creating the button.
#This is typically done using lambda or functools.partial.
        self.paper_button.pack()#packing the window in
        self.scissors_button.pack()
        self.result_label = tk.Label(self.window, text="Result:", font =("Bold", 16))
        self.result_label.pack()


    def play(self, player_choice): #now onto the fun part of making the game, the actual playing part.
        player_choice = player_choice.lower()

        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options).lower()
        if player_choice == computer_choice:
            result = "Run it back bru you trash."
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            result = "This computer will now self destruct because you beat me."
        else:# gets players input, outputs what the computer is picking.
                result = "Suck on these computer hardrive nuts."



        self.result_label.config(
        text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n\n{result}")



root = tk.Tk()
app = RPS(root)
root.mainloop()
















