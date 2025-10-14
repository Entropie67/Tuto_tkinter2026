import tkinter as tk

# --- Fonction pour gérer les clics ---
def on_click(val):
    """Ajoute la valeur cliquée dans l'entrée"""
    entry.insert(tk.END, val)

# --- Fonction pour calculer le résultat ---
def calculate():
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))


# --- Fenêtre principale ---
root = tk.Tk()
root.title("Calculatrice")

entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=5)

# --- Liste des boutons ---
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# --- Génération automatique des boutons ---
row, col = 1, 0
for b in buttons:
    # Si c’est le bouton "=", on appelle calculate()
    if b == '=':
        action = calculate
    else:
        # sinon, on ajoute la valeur du bouton
        action = lambda x=b: on_click(x)

    tk.Button(root, text=b, width=5, height=2, font=("Arial", 16),
              command=action).grid(row=row, column=col, padx=2, pady=2)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# --- Bouton "C" pour effacer ---
tk.Button(root, text="C", width=5, height=2, font=("Arial", 16),
          command=lambda: entry.delete(0, tk.END)).grid(row=row, column=0, columnspan=4, pady=5)

root.mainloop()
