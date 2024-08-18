import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.minsize(300, 400)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
      
        self.title_font = ("Helvetica", 16, "bold")
        self.button_font = ("Helvetica", 14)
        self.result_font = ("Helvetica", 14, "italic")

        self.choices = ["Rock", "Paper", "Scissors"]

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=self.title_font)
        self.label.grid(row=0, column=0, pady=10)

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("Rock")

        self.rock_button = tk.Radiobutton(root, text="Rock", variable=self.user_choice_var, value="Rock", font=self.button_font, indicatoron=False, width=15)
        self.rock_button.grid(row=1, column=0, padx=20, pady=5)

        self.paper_button = tk.Radiobutton(root, text="Paper", variable=self.user_choice_var, value="Paper", font=self.button_font, indicatoron=False, width=15)
        self.paper_button.grid(row=2, column=0, padx=20, pady=5)

        self.scissors_button = tk.Radiobutton(root, text="Scissors", variable=self.user_choice_var, value="Scissors", font=self.button_font, indicatoron=False, width=15)
        self.scissors_button.grid(row=3, column=0, padx=20, pady=5)

        self.play_button = tk.Button(root, text="Play", command=self.play_game, font=self.button_font, bg="#4CAF50", fg="white", width=15)
        self.play_button.grid(row=4, column=0, padx=20, pady=10)

        self.result_label = tk.Label(root, text="", font=self.result_font, fg="blue")
        self.result_label.grid(row=5, column=0, pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, font=self.button_font, bg="#2196F3", fg="white", width=15)
        self.play_again_button.grid(row=6, column=0, padx=20, pady=10)

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "You lose!"

    def reset_game(self):
        self.result_label.config(text="")
        self.user_choice_var.set("Rock")

root = tk.Tk()
app = RockPaperScissorsGame(root)

root.mainloop()
