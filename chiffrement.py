import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple Tkinter avec grid()")
root.geometry("600x400")
root.config(bg="#f8f8f8")

###############################
#        Fenêtre 1            #
###############################
fenetre1 = tk.Frame (root , bg = "#F5279F")
fenetre1.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
# Label
titre1 = tk.Label(fenetre1, text="Message en clair", font=("Helvetica", 12), bg="#f8f8f8")
titre1.grid(row=0, column=1, padx=10, pady=10, sticky="n")
# Label
label1 = tk.Label(fenetre1, text="Message :", font=("Helvetica", 12), bg="#f8f8f8")
label1.grid(row=1, column=0, padx=10, pady=10, sticky="e")
# Entry
entry = tk.Entry(fenetre1, font=("Helvetica", 12), width=25)
entry.grid(row=1, column=1, padx=10, pady=10)

###############################
#        Fenêtre 2            #
###############################
fenetre2 = tk.Frame (root , bg = "red" , width = 320 , height = 240 )
fenetre2.grid(row=1, column=0,columnspan=3, padx=20, pady=20, sticky="nsew")

# Label 2 (affichage ou message)
label2 = tk.Label(fenetre2, text="Entrez votre nom puis cliquez :", font=("Helvetica", 10), bg="#f8f8f8", fg="#555")
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