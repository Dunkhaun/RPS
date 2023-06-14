import tkinter as tk
from tkinter import messagebox
import random


class RPSGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")

        self.options = ['Rock', 'Paper', 'Scissors']
        self.difficulty_options = ['Easy', 'Medium', 'Hard']
        self.difficulty = 'Easy'

        self.user_wins = 0
        self.computer_wins = 0
        self.draws = 0

        self.create_difficulty_menu()
        self.create_buttons()
        self.create_counter_labels()

    def create_difficulty_menu(self):
        difficulty_menu = tk.Menu(self.window)
        difficulty_menu.add_command(label="Easy", command=lambda: self.set_difficulty('Easy'))
        difficulty_menu.add_command(label="Medium", command=lambda: self.set_difficulty('Medium'))
        difficulty_menu.add_command(label="Hard", command=lambda: self.set_difficulty('Hard'))

        menu_bar = tk.Menu(self.window)
        menu_bar.add_cascade(label="Difficulty", menu=difficulty_menu)

        self.window.config(menu=menu_bar)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def create_buttons(self):
        for option in self.options:
            button = tk.Button(
                self.window,
                text=option,
                width=10,
                command=lambda option=option: self.play_game(option)
            )
            button.pack(pady=10)

    def create_counter_labels(self):
        counter_frame = tk.Frame(self.window)
        counter_frame.pack(pady=10)

        tk.Label(counter_frame, text="Wins:").pack(side=tk.LEFT)
        self.user_wins_label = tk.Label(counter_frame, text="0")
        self.user_wins_label.pack(side=tk.LEFT, padx=5)

        tk.Label(counter_frame, text="Draws:").pack(side=tk.LEFT)
        self.draws_label = tk.Label(counter_frame, text="0")
        self.draws_label.pack(side=tk.LEFT, padx=5)

        tk.Label(counter_frame, text="Losses:").pack(side=tk.LEFT)
        self.computer_wins_label = tk.Label(counter_frame, text="0")
        self.computer_wins_label.pack(side=tk.LEFT, padx=5)

    def play_game(self, user_choice):
        computer_choice = self.get_computer_choice()

        result = ""

        if user_choice == computer_choice:
            result = "It's a draw!"
            self.draws += 1
        elif (
                (user_choice == 'Rock' and computer_choice == 'Scissors')
                or (user_choice == 'Paper' and computer_choice == 'Rock')
                or (user_choice == 'Scissors' and computer_choice == 'Paper')
        ):
            result = "You win!"
            self.user_wins += 1
        else:
            result = "Computer wins!"
            self.computer_wins += 1

        self.update_counter_labels()
        messagebox.showinfo("Result", f"User: {user_choice}\nComputer: {computer_choice}\n\n{result}")

    def get_computer_choice(self):
        if self.difficulty == 'Easy':
            return random.choice(self.options)
        elif self.difficulty == 'Medium':
            return random.choice(self.options[:-1])
        elif self.difficulty == 'Hard':
            return random.choice(self.options)

    def update_counter_labels(self):
        self.user_wins_label.config(text=str(self.user_wins))
        self.draws_label.config(text=str(self.draws))
        self.computer_wins_label.config(text=str(self.computer_wins))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = RPSGame()
    game.run()
