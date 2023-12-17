import tkinter as tk
from tkinter import messagebox

def construction_morpion():
    for i in range(3):
        for j in range(3):
            morpion[i][j] =""

def afficher():
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text=morpion[i][j], width=23, height=10,bg="white", command=lambda r=i, c=j: on_click(r, c))
            button.grid(row=i, column=j)

def verif_nul():
    return all(morpion[i][j] in ['x', 'o'] for i in range(3) for j in range(3))

def mise_a_jour(row, col, c):
    morpion[row][col] = c

def verif_gagner(row, col, c):
    return all(morpion[i][i] == c for i in range(3)) or \
           all(morpion[i][col] == c for i in range(3)) or \
           all(morpion[i][2 - i] == c for i in range(3))

def verif_emplacement(row, col):
    return morpion[row][col] not in ["x", "o"]

def on_click(row, col):
    global player_turn
    if verif_emplacement(row, col):
        if player_turn % 2 == 0:
            sym = "x"
        else:
            sym = "o"

        mise_a_jour(row, col, sym)
        button = tk.Button(root, text=sym,width=5,height=3,border=0,bg="white",font="Helvetica 23 bold",fg="red")
        button.grid(row=row, column=col)

        if verif_gagner(row, col, sym):
            messagebox.showinfo("Victoire", f"Joueur {player_turn % 2 + 1} a gagné !")
            root.quit()
        elif verif_nul():
            messagebox.showinfo("Partie nulle", "La partie est nulle !")
            root.quit()

        player_turn += 1

# Les Matrices
morpion = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

# Le jeu
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")

construction_morpion()
afficher()

player_turn = 0

root.mainloop()
