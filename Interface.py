import tkinter as tk
from tkinter import messagebox

from Machine import Machine


NB_CASES = 20


class InterfaceTuring:
    def __init__(self):
        self.racine = tk.Tk()
        self.racine.title("Machine de Turing")
        self.racine.geometry("1100x500")
        self.racine.configure(bg="#f5efe6")

        self.champs = []
        self.resultat_labels = []

        self.message_var = tk.StringVar(value="Entre des 0 et des 1 dans la bande.")
        self.info_var = tk.StringVar(value="Curseur : -")

        self._creer_interface()
        self._afficher_resultat([])

    def _creer_interface(self):
        titre = tk.Label(
            self.racine,
            text="Machine de Turing",
            font=("Helvetica", 24, "bold"),
            bg="#f5efe6",
            fg="#243447",
        )
        titre.pack(pady=(20, 8))

        sous_titre = tk.Label(
            self.racine,
            text="Simulation du complement a deux sur une bande binaire",
            font=("Helvetica", 12),
            bg="#f5efe6",
            fg="#4f6272",
        )
        sous_titre.pack()

        cadre_bande = tk.Frame(self.racine, bg="#f5efe6")
        cadre_bande.pack(pady=24)

        for index in range(NB_CASES):
            conteneur = tk.Frame(cadre_bande, bg="#f5efe6")
            conteneur.grid(row=0, column=index, padx=3)

            numero = tk.Label(
                conteneur,
                text=str(index),
                font=("Helvetica", 9),
                bg="#f5efe6",
                fg="#7a8793",
            )
            numero.pack()

            champ = tk.Entry(
                conteneur,
                width=3,
                justify="center",
                font=("Consolas", 16),
                relief="solid",
                bd=1,
            )
            champ.pack(pady=(4, 0))
            self.champs.append(champ)

        cadre_actions = tk.Frame(self.racine, bg="#f5efe6")
        cadre_actions.pack(pady=10)

        bouton_lancer = tk.Button(
            cadre_actions,
            text="Lancer",
            command=self.executer,
            bg="#2a9d8f",
            fg="white",
            activebackground="#208173",
            activeforeground="white",
            padx=18,
            pady=8,
            relief="flat",
        )
        bouton_lancer.grid(row=0, column=0, padx=8)

        bouton_exemple = tk.Button(
            cadre_actions,
            text="Exemple",
            command=self.remplir_exemple,
            bg="#457b9d",
            fg="white",
            activebackground="#35627d",
            activeforeground="white",
            padx=18,
            pady=8,
            relief="flat",
        )
        bouton_exemple.grid(row=0, column=1, padx=8)

        bouton_effacer = tk.Button(
            cadre_actions,
            text="Effacer",
            command=self.effacer,
            bg="#e76f51",
            fg="white",
            activebackground="#cf583b",
            activeforeground="white",
            padx=18,
            pady=8,
            relief="flat",
        )
        bouton_effacer.grid(row=0, column=2, padx=8)

        message = tk.Label(
            self.racine,
            textvariable=self.message_var,
            font=("Helvetica", 11),
            bg="#f5efe6",
            fg="#264653",
        )
        message.pack(pady=(8, 18))

        separateur = tk.Frame(self.racine, height=2, bg="#d8d0c4")
        separateur.pack(fill="x", padx=60, pady=(0, 18))

        titre_resultat = tk.Label(
            self.racine,
            text="Resultat",
            font=("Helvetica", 15, "bold"),
            bg="#f5efe6",
            fg="#243447",
        )
        titre_resultat.pack()

        self.cadre_resultat = tk.Frame(self.racine, bg="#f5efe6")
        self.cadre_resultat.pack(pady=18)

        info = tk.Label(
            self.racine,
            textvariable=self.info_var,
            font=("Helvetica", 11),
            bg="#f5efe6",
            fg="#4f6272",
        )
        info.pack()

    def _lire_bande(self):
        bande = []
        for champ in self.champs:
            valeur = champ.get().strip()
            if valeur == "":
                continue
            if valeur not in {"0", "1"}:
                raise ValueError("La bande doit contenir uniquement des 0, des 1 ou des cases vides.")
            bande.append(int(valeur))

        if not bande:
            raise ValueError("Ajoute au moins un symbole dans la bande.")

        return bande

    def _afficher_resultat(self, bande, position_curseur=None):
        for label in self.resultat_labels:
            label.destroy()
        self.resultat_labels.clear()

        if not bande:
            vide = tk.Label(
                self.cadre_resultat,
                text="Aucun resultat pour le moment.",
                font=("Helvetica", 11, "italic"),
                bg="#f5efe6",
                fg="#7a8793",
            )
            vide.pack()
            self.resultat_labels.append(vide)
            self.info_var.set("Curseur : -")
            return

        for index, symbole in enumerate(bande):
            texte = "_" if symbole == "" else str(symbole)
            fond = "#e9c46a" if index == position_curseur else "#ffffff"

            label = tk.Label(
                self.cadre_resultat,
                text=texte,
                width=3,
                font=("Consolas", 16, "bold"),
                relief="solid",
                bd=1,
                bg=fond,
                fg="#1d3557",
            )
            label.grid(row=0, column=index, padx=3, pady=3)
            self.resultat_labels.append(label)

        if position_curseur is None:
            self.info_var.set("Curseur : -")
        else:
            self.info_var.set(f"Curseur final : case {position_curseur}")

    def executer(self):
        try:
            bande = self._lire_bande()
            machine = Machine(bande)
            resultat = machine.complement_a_deux()
        except ValueError as erreur:
            self.message_var.set(str(erreur))
            messagebox.showerror("Erreur", str(erreur))
            return
        except Exception as erreur:
            self.message_var.set("La machine a rencontre un probleme.")
            messagebox.showerror("Erreur d'execution", str(erreur))
            return

        self._afficher_resultat(resultat, machine.curseur.indice)
        self.message_var.set("Execution terminee.")

    def remplir_exemple(self):
        self.effacer()
        exemple = "01001101"
        for index, symbole in enumerate(exemple):
            self.champs[index].insert(0, symbole)
        self.message_var.set("Exemple charge.")

    def effacer(self):
        for champ in self.champs:
            champ.delete(0, tk.END)
        self._afficher_resultat([])
        self.message_var.set("Bande effacee.")

    def lancer(self):
        self.racine.mainloop()


def demarrer():
    InterfaceTuring().lancer()


if __name__ == "__main__":
    demarrer()
