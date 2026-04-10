import tkinter as tk

def complement_a_2():
    pass

def supp(bande):
    for i in bande:
        i.text = ""
    

def demarrer():
    nb_cases = 50
    racine = tk.Tk()
    racine.title("Turing")
    racine.geometry("2500x2500")
    label = tk.Label(racine, text="entrez vos chiffres svp :")
    label.pack(padx=20, pady=20)
    bande = []
    textes = []
    for i in range(nb_cases):
        textes.append("8")
        bande.append(tk.Entry(racine, justify="center", width = 1, fg = "#6709AF", state="readonly"))
        
    longueur = len(bande)
    entree = tk.Entry(racine, width = 20)
    entree.pack(padx=20, pady=20)
    
    bouton_complement = tk.Button(racine, text = "complément à 2", command=complement_a_2())
    bouton_complement.pack(padx=20, pady=20)
    bouton_supprimer = tk.Button(racine, text = "supprimer", command=supp(bande))
    bouton_supprimer.pack(padx=20, pady=20)
    for i in range(longueur):
        bande[i].pack( side = "left", padx=0, pady=0, fill = "x", expand = True)
        bande[i].insert(0,textes[i])


    racine.mainloop()
demarrer()