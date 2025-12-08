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
    def __init__(self, window):
        self.window = window
        self.window.title("Game of Nim")
        self.title_lable = tk.Label(self.window, text = "Welcome to the game of nim the instruction will appear when you hit play")






def ask_ball_number():
        num = int(input("How many balls will be put in the basket?\n"))
        while num <= 15:
            print("The number of balls needs to be higher than 15.")
            num = int(input("How many balls will be put in the basket?\n"))
        return num

def cpu_choose(num):
    if num % 5 == 0:
        choice = random.randint(1, 4)
        return choice
    else:
        choice = num % 5
        return choice

def user_choose():
    choice = int(input("\nHow many balls will you take out?\n"))
    while choice < 1 or choice > 5:
        if choice < 1:
            print("You need to take at least 1.")
            choice = int(input("How many balls will you take out?\n"))
        elif choice > 5:
            print("You can only take up to 4.")
            choice = int(input("How many balls will you take out?\n"))
    return choice

def remove_balls(num_balls, num_remove):
    num_balls = num_balls - num_remove
    return num_balls


def main():
    print("You have been challenged to the Game of Nim.")
    print("You will select a number of balls that is greater than 15 to put in a basket.")
    print("Then you and your opponent will take turns taking out 1-4 balls each turn.")
    print("Are you ready?")
    balls_left = ask_ball_number()
    print("You have the pleasure of going first. Choose wisely.")

    while balls_left > 0:
        user_turn = True
        balls_left = remove_balls(balls_left, user_choose())
        if balls_left == 1:
            print(f"There is now {balls_left} ball in the basket.")
        else:
            print(f"There are now {balls_left} balls in the basket.")
        if balls_left > 0:
            user_turn = False
            cpu_choice = cpu_choose(balls_left)
            balls_left = remove_balls(balls_left, cpu_choice)
            if cpu_choice == 1:
                print(f"Your opponent took 1 ball out of the basket.\nThere are {balls_left} balls left.")
            else:
                if balls_left == 1:
                    print(f"Your opponent took {cpu_choice} balls out of the basket.\nThere is {balls_left} ball left.")
                else:
                    print(f"Your opponent took {cpu_choice} balls out of the basket.\nThere are {balls_left} balls left.")
    if user_turn:
        print("You took the last ball, you have won!")
    else:
        print("Your opponent took the last ball, you have lost...")


if __name__ == '__main__':
    main()