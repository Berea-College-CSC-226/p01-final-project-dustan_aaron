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

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.title_Lable = tk.Label(self.window, text="C'mon looser, choose your move.", font =("Bold", 16))
        self.title_Lable.pack()#below this is me getting the buttons looking correct
        self.rock_button = tk.Button(self.window, text="Rock", width = 17, command=lambda: self.play("Rock"))
        self.paper_button = tk.Button(self.window, text = "Paper", width = 17, command=lambda: self.play("Paper") )
        self.scissors_button = tk.Button(self.window, text = "Scissors", width = 17, command=lambda: self.play("Scissors"))
        self.rock_button.pack()#command lambda is something I found on google in tkinter explorations that is different
#buttons that calls to the same function but has can produce a different output. With Rock paper scissors being
#same function but different output I needed to find something.
#tkinter button that calls the same function but can produce two different outputs (what I searched) google output:You
#can make a Tkinter button call the same function but produce different outputs by passing an argument to the function when creating the button.
#This is typically done using lambda or functools.partial.
        self.paper_button.pack()#packing the window in
        self.scissors_button.pack()
        self.result_Label = tk.Label(self.window, text="Result:", font=("Bold", 15), width=45)
        self.window.configure(bg="purple")
        self.title_Lable.config(bg="purple", fg="white")
        self.rock_button.config(bg="blue", fg="black")
        self.paper_button.config(bg="white", fg="black")
        self.scissors_button.config(bg="red", fg="black")
        self.result_Label.config(bg="purple", fg="white")
        #I searched up how to put a color in tkinter because I forgot how to, if this is not how the book shows this was what the first thing I seen online.
        self.result_Label.pack()
        self.window.mainloop()

    def play(self, player_choice): #now onto the fun part of making the game, the actual playing part.
        player_choice = player_choice.lower()
#Very tricky, this is honestly where I had the most trouble, for some reason it would only print the Computer wins result.
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options).lower()
        if player_choice == computer_choice:
            result = "Run it back bru you trash."
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            result = "Even if you beat me, you still trash."

        else:# gets players input, outputs what the computer is picking.
                result = "Suck on these computer hardrive nuts."



        self.result_Label.config(
        text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n\n{result}")


def main():
    rps = RPS()

if __name__ == "__main__":
    main()


















