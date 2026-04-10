import tkinter as tk
racine = tk.Tk()
racine.title("Turing")
racine.geometry("2500x2500")

def ajouter_texte(texte, bande):
    t = []
    for i in range(len(texte)):
        t.append(texte[0])
        del(texte[0])
    tj = 0
    while len(tj) > 0:
        if bande[tj].get() == "":
            bande[tj].insert(0,t[0])
            del(t[0])



def complement_a_2():
    print("Je complémente à 2")

def supp(bande):
    for i in range(len(bande)):
        bande[i].delete(0,1)
        print("Je m'enlève")
    racine.update()
    print("What?")
    

def demarrer():
    nb_cases = 50
    
    label = tk.Label(racine, text="entrez vos chiffres svp :")
    label.pack(padx=20, pady=20)
    bande = []
    textes = []
    for i in range(nb_cases):
        textes.append("8")
        bande.append(tk.Entry(racine, justify="center", width = 1, fg = "#6709AF"))
        
    longueur = len(bande)
    entree = tk.Entry(racine, width = 20)
    entree.pack(padx=20, pady=20)
    
    bouton_complement = tk.Button(racine, text = "complément à 2", command=lambda : complement_a_2())
    bouton_complement.pack(padx=20, pady=20)
    bouton_supprimer = tk.Button(racine, text = "supprimer", command=lambda : supp(bande))
    bouton_supprimer.pack(padx=20, pady=20)
    for i in range(longueur):
        bande[i].pack( side = "left", padx=0, pady=0, fill = "x", expand = True)
        bande[i].insert(0,textes[i])


    

demarrer()

racine.mainloop()