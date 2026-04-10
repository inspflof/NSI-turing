import tkinter as tk

def demarrer():
    racine = tk.Tk()
    racine.title("Turing")
    racine.geometry("2500x2500")
    label = tk.Label(racine, text="Turing")
    label.pack(padx=20, pady=20)
    bande = []
    for i in range(69):
        bande.append(tk.Entry(racine, text = "", width = 1, fg = "#6709AF"))
    longueur = len(bande)
    for i in bande:
        i.place(x=None, y=-1250)
    racine.mainloop()
demarrer()