import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import random


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Pierre-Papier-Ciseaux")
        self.root.configure(bg='#2c3e50')

        self.choices = ['pierre', 'papier', 'ciseaux']

        self.user_label = tk.Label(root, text="Votre choix : ", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 15))
        self.user_label.grid(row=0, column=1, pady=20)

        self.buttons = {}
        for idx, choice in enumerate(self.choices):
            self.buttons[choice] = tk.Button(root, text=choice, command=lambda c=choice: self.play(c), bg='#e74c3c', fg='#ecf0f1', font=('Arial', 12))
            self.buttons[choice].grid(row=1, column=idx, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 15))
        self.result_label.grid(row=2, column=1, pady=20)

        self.reset_button = tk.Button(root, text="Rejouer", command=self.reset, bg='#16a085', fg='#ecf0f1', font=('Arial', 12))
        self.reset_button.grid(row=3, column=1, pady=10)

    def play(self, choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(choice, computer_choice)
        self.result_label.config(text=f"Ordinateur a choisi {computer_choice}. {result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "C'est un match nul !"
        elif user_choice == 'pierre' and computer_choice == 'ciseaux':
            return "Vous gagnez !"
        elif user_choice == 'papier' and computer_choice == 'pierre':
            return "Vous gagnez !"
        elif user_choice == 'ciseaux' and computer_choice == 'papier':
            return "Vous gagnez !"
        else:
            return "L'ordinateur gagne !"

    def reset(self):
        self.result_label.config(text="")

root = tk.Tk()
game = Game(root)
root.mainloop()
