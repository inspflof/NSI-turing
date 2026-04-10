import tkinter as tk

def demarrer():
    nb_cases = 50
    racine = tk.Tk()
    racine.title("Turing")
    racine.geometry("2500x2500")
    label = tk.Label(racine, text="enttrez vos chiffres svp :")
    label.pack(padx=20, pady=20)
    bande = []
    for i in range(nb_cases):
        bande.append(tk.Entry(racine, text = " ", width = 1, fg = "#6709AF", state="readonly"))
    longueur = len(bande)
    entree = tk.Entry(racine, width = 20)
    entree.pack(padx=20, pady=20)
    for i in range(longueur):
        bande[i].pack(side="left", padx=0, pady=0, expand=True)
    racine.mainloop()
demarrer()