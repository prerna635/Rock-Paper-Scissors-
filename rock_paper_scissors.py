import tkinter as tk
import random

# Choices
choices = ['Rock', 'Paper', 'Scissors']

# Score counters
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update display
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

# GUI Window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")
window.resizable(False, False)

# Heading
tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 18, "bold")).pack(pady=10)

# Instruction
tk.Label(window, text="Choose your option:", font=("Arial", 12)).pack()

# Buttons for choices
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Labels to show choices and result
user_choice_label = tk.Label(window, text="", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(window, text="", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Score label
score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

# Reset button
tk.Button(window, text="Reset Game", font=("Arial", 11), command=reset_game).pack(pady=10)

# Run the app
window.mainloop()
