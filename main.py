import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()

# Titre de la fenêtre
root.title("Ma première fenêtre Tkinter")

# Taille de la fenêtre (largeur x hauteur)
root.geometry("400x300")

# Optionnel : couleur de fond
root.config(bg="#f0f0f0")

# Label d'exemple
label = tk.Label(root, text="Bonjour, Tkinter !", font=("Helvetica", 16), bg="#f0f0f0")
label.pack(pady=50)

# Boucle principale (affichage)
root.mainloop()
