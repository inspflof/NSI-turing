import Curseur as c


class Machine:
    def __init__(self, bande, curseur=None):
        """Initialise la machine et sa bande."""
        self.bande = list(bande)
        self.curseur = curseur if curseur is not None else c.Curseur()

    def changement_etat(self):
        """Effectue une transition de la machine."""
        if self.curseur.etat == "Fin":
            return

        table = self.curseur.renvoyer_table()
        transition = table.get((self.curseur.etat, self.curseur.lettre))
        if transition is None:
            raise KeyError(
                f"Transition introuvable pour l'etat {self.curseur.etat!r} "
                f"et la lettre {self.curseur.lettre!r}."
            )

        self.bande[self.curseur.indice] = transition[1]
        self.curseur.indice += self.curseur.deplacements[transition[2]]

        if self.curseur.indice < 0 or self.curseur.indice >= len(self.bande):
            self.arrive_bout()

        self.curseur.lettre = self.bande[self.curseur.indice]
        self.curseur.etat = transition[0]

    def update(self):
        """Applique une etape de calcul."""
        if self.curseur.indice < 0 or self.curseur.indice >= len(self.bande):
            self.arrive_bout()
        self.changement_etat()

    def arrive_bout(self):
        """Ajoute des cases vides quand le curseur sort de la bande."""
        self.bande = [""] + self.bande + [""]
        self.curseur.indice += 1

    def executer(self, etat_initial, max_steps=10000):
        self.curseur = c.Curseur(etat_initial, self.bande[self.curseur.indice], self.curseur.indice)
        steps = 0
        while self.curseur.etat != "Fin":
            if steps >= max_steps:
                raise RuntimeError(
                    f"La machine n'a pas termine apres {max_steps} etapes depuis l'etat {etat_initial!r}."
                )
            self.update()
            steps += 1
        return self.bande

    def complement_a_deux(self):
        return self.executer("E0")

    def multiplier(self):
        return self.executer("M0")

    def addition(self):
        return self.executer("A_start")


if __name__ == "__main__":
    print(Machine([1, 1, 1]).complement_a_deux())
