import tkinter as tk

#####################################
# Création de la fenêtre principale #
#####################################

root = tk.Tk()
root.title("Exemple Tkinter")
root.geometry("800x400")
root.config(bg="#f8f8f8")


#################################
# Frame pour la partie en clair #
#################################

frame1 = tk.Frame ( root , bg = "green")
frame1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="new")
# Label 1
label1 = tk.Label(frame1, text="Message en clair :", font=("Helvetica", 12), bg="#f8f8f8")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry = tk.Entry(frame1, font=("Helvetica", 12), width=25)
entry.grid(row=0, column=1, padx=10, pady=10)

#################################
# Frame pour la partie chiffrée #
#################################

frame2 = tk.Frame ( root , bg = "red")
frame2.grid(row=2, column=0,columnspan=3, padx=10, pady=10, sticky="ew")

entry2 = tk.Entry(frame2, font=("Helvetica", 12), width=25)
entry2.grid(row=0, column=1, padx=10, pady=10)

# Label 2 (affichage ou message)
label2 = tk.Label(frame2, text="Message chiffré :", font=("Helvetica", 10), bg="#f8f8f8", fg="#555")
label2.grid(row=0, column=0, padx=10, pady=10, sticky="e")

######################################
# Fonction appelée au clic du bouton #
######################################
def on_button_click():
    result = chiffrement(entry.get())
    entry2.delete(0, tk.END)
    entry2.insert(tk.END, result)

def chiffrement(chaine):
    # bla bla 
    return chaine

# Bouton
button = tk.Button(root, text="Valider", font=("Helvetica", 12), command=on_button_click)
button.grid(row=3, column=2, columnspan=2, pady=10)
# ======= Boucle principale =======
root.mainloop()
