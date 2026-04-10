import tkinter as tk

from Machine import Machine


def supp(bande):
    for case in bande:
        case.config(state="normal")
        case.delete(0, tk.END)
        case.config(state="readonly")


def afficher_bande(bande_widgets, valeurs):
    for index, case in enumerate(bande_widgets):
        case.config(state="normal")
        case.delete(0, tk.END)
        if index < len(valeurs) and valeurs[index] != "":
            case.insert(0, str(valeurs[index]))
        case.config(state="readonly")


def complement_a_2(entree, bande_widgets):
    texte = entree.get().strip()
    if not texte:
        supp(bande_widgets)
        return

    if any(caractere not in "01" for caractere in texte):
        raise ValueError("La bande du complement a 2 doit contenir uniquement des 0 et des 1.")

    resultat = Machine([int(caractere) for caractere in texte]).complement_a_deux()
    afficher_bande(bande_widgets, resultat)


def demarrer():
    nb_cases = 50
    racine = tk.Tk()
    racine.title("Turing")
    racine.geometry("2500x2500")

    label = tk.Label(racine, text="Entrez vos chiffres :")
    label.pack(padx=20, pady=20)

    bande = []
    for _ in range(nb_cases):
        case = tk.Entry(racine, justify="center", width=1, fg="#6709AF")
        case.config(state="readonly")
        bande.append(case)

    entree = tk.Entry(racine, width=20)
    entree.pack(padx=20, pady=20)

    bouton_complement = tk.Button(
        racine,
        text="complement a 2",
        command=lambda: complement_a_2(entree, bande),
    )
    bouton_complement.pack(padx=20, pady=20)

    bouton_supprimer = tk.Button(
        racine,
        text="supprimer",
        command=lambda: supp(bande),
    )
    bouton_supprimer.pack(padx=20, pady=20)

    for case in bande:
        case.pack(side="left", padx=0, pady=0, fill="x", expand=True)

    racine.mainloop()


if __name__ == "__main__":
    demarrer()
