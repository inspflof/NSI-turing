import tkinter as tk

def demarrer():
    racine = tk.Tk()
    racine.title("Turing")
    racine.geometry("2500x2500")
    label = tk.Label(racine, text="Turing")
    label.pack(padx=20, pady=20)
    bande = []
    for i in range(69):
        bande[i-34] = tk.Entry(racine, text = "", width = 1, fg = "#6709AF")
    racine.mainloop()
demarrer()