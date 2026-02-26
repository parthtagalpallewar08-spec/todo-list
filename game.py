import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x450")
root.config(bg="lightblue")

# Variables to track score
user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 😢"
        computer_score += 1
    
    winner_text.set(result)
    score_text.set(f"Your Score: {user_score}  |  Computer Score: {computer_score}")

# Function to reset game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_text.set("")
    winner_text.set("")
    score_text.set("Your Score: 0  |  Computer Score: 0")

# UI Elements
title_label = tk.Label(root, text="Rock Paper Scissors", 
                       font=("Arial", 18, "bold"), bg="lightblue")
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", 
                             font=("Arial", 12), bg="lightblue")
instruction_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result Display
result_text = tk.StringVar()
winner_text = tk.StringVar()
score_text = tk.StringVar()

result_label = tk.Label(root, textvariable=result_text, 
                        font=("Arial", 12), bg="lightblue")
result_label.pack(pady=10)

winner_label = tk.Label(root, textvariable=winner_text, 
                        font=("Arial", 14, "bold"), bg="lightblue")
winner_label.pack(pady=5)

score_label = tk.Label(root, textvariable=score_text, 
                       font=("Arial", 12), bg="lightblue")
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

# Initialize score
score_text.set("Your Score: 0  |  Computer Score: 0")

root.mainloop()