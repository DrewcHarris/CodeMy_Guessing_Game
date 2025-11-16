# Import tkinter
from tkinter import *

# Import the os module/library 
import os 
#import the random library
import random

# Initalize the game state variables
number_to_guess = None
number_of_guesses = 0

#Create a play again function
def reset_game():
	# Set our global variables
	global number_to_guess, number_of_guesses
	# Generate a random number and assign to a variable
	number_to_guess = random.randint(1,10)
	# Set number of guesses to zero
	number_of_guesses = 0
	# Delete result label
	result_label.config(text="")
	# Clear the entry box
	guess_entry.delete(0, END)
	# Set the submit button back to normal
	submit_button.config(state=NORMAL)
	# Hide the play again button...again
	play_again_button.pack_forget()

# Create our main game function
def check_guess():
	global number_of_guesses

	# Try / except block
	try:
		guess = int(guess_entry.get())
		number_of_guesses += 1

		# Create logic to check the guess
		if guess < number_to_guess:
			result_label.config(text="Too low! Try again!")

		elif guess > number_to_guess:
			result_label.config(text="Too high! Try again!")

		else:
			result_label.config(text=f"Correct! The number was {number_to_guess} and you guessed it in {number_of_guesses} guesses!")
			# Disable the guess button
			submit_button.config(state=DISABLED)
			# Enable the play again button
			play_again_button.pack()

	except ValueError:
		result_label.config(text="Invalid Input! Please enter a number.")
	
def setup_gui():
	# Make all our widgets global
	global result_label, guess_entry, submit_button, play_again_button

	# Creeate the window
	root = Tk()
	# Add a title
	root.title("Guessing Game")
	#Set the size of the app
	root.geometry('500x350')

	# Create a label
	instruction_label = Label(root, text="Guess a Number between 1 and 10", font=("Helvetica", 18))
	instruction_label.pack(pady=20)

	# Create an entry box
	guess_entry = Entry(root, font=("Helvetica", 18))
	guess_entry.pack(pady=10)

	# Create another label
	result_label = Label(root, text="")
	result_label.pack(pady=20)

	# Create some buttons
	submit_button = Button(root, text="Submit Guess", command=check_guess)
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?", command=reset_game)
	play_again_button.pack()

	#Hide this button
	play_again_button.pack_forget()

	# On start, reset the game
	reset_game()

	# Start the app
	root.mainloop()

# Call our main function
setup_gui()