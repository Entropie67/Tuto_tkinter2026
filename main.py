import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple Tkinter avec grid()")
root.geometry("400x200")
root.config(bg="#f8f8f8")

# ======= Contenu =======

# Label 1
label1 = tk.Label(root, text="Nom :", font=("Helvetica", 12), bg="#f8f8f8")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry = tk.Entry(root, font=("Helvetica", 12), width=25)
entry.grid(row=0, column=1, padx=10, pady=10)

# Label 2 (affichage ou message)
label2 = tk.Label(root, text="Entrez votre nom puis cliquez :", font=("Helvetica", 10), bg="#f8f8f8", fg="#555")
label2.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Fonction appelée au clic du bouton
def on_button_click():
    name = entry.get()
    label2.config(text=f"Bonjour, {name} !", fg="green")

# Bouton
button = tk.Button(root, text="Valider", font=("Helvetica", 12), command=on_button_click)
button.grid(row=2, column=0, columnspan=2, pady=10)
# ======= Boucle principale =======
root.mainloop()
