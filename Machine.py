import Curseur as c


class Machine:
    def __init__(self, bande, curseur=None):
        """Initialise la machine avec une bande et un curseur."""
        self.bande = list(bande)
        self.curseur = curseur if curseur is not None else c.Curseur()

    def changement_etat(self):
        """Applique la transition correspondant a l'etat et au symbole courant."""
        table = self.curseur.renvoyer_table()
        stock = table[(self.curseur.etat, self.curseur.lettre)]
        self.bande[self.curseur.indice] = stock[1]
        self.curseur.indice += self.curseur.deplacements[stock[2]]
        self.curseur.lettre = self.bande[self.curseur.indice]
        self.curseur.etat = stock[0]

    def update(self):
        """Execute une etape de la machine."""
        if self.curseur.indice == len(self.bande) or self.curseur.indice == 0:
            self.arrive_bout()
        self.changement_etat()

    def arrive_bout(self):
        """Ajoute des cases vides aux extremites lorsque le curseur atteint un bord."""
        self.bande.append("")
        self.bande = [""] + self.bande
        self.curseur.indice += 1

    def complement_a_deux(self):
        self.curseur = c.Curseur("E0", self.bande[self.curseur.indice], self.curseur.indice)
        while self.curseur.etat != "Fin":
            self.update()
        return self.bande

    def multiplier(self):
        self.curseur = c.Curseur("M0", self.bande[self.curseur.indice], self.curseur.indice)
        while self.curseur.etat != "Fin":
            self.update()
        return self.bande


if __name__ == "__main__":
    exemple = Machine([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    exemple.complement_a_deux()
    print(exemple.bande)
