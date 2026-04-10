import Curseur as c


class Machine():
    def __init__(self,bande, curseur=c.Curseur()):
        """méthode qui initie la machine"""
        self.bande=bande
        self.curseur = curseur


    def changement_etat(self):
        """méthode qui effectue les changements en fonction de la table de transition table"""
        if self.curseur.etat!="Fin":
            table=self.curseur.renvoyer_table()
            stock=table[(self.curseur.etat,self.curseur.lettre)]
            self.bande[self.curseur.indice]=stock[1]
            self.curseur.indice += self.curseur.deplacements[stock[2]]
            self.curseur.lettre=self.bande[self.curseur.indice]
            self.curseur.etat=stock[0]



    def update(self):
        """fonction appelée à chaque étapes de l'exécution de la machine"""
        if self.curseur.indice >= len(self.bande) or self.curseur.indice == 0:
            self.arrive_bout()
        self.changement_etat()
        



    
    def arrive_bout(self):
        """fonction qui ajoute des strings vides au début et à la fin de la bande quand le curseur arrive au bout """
        self.bande=[""]+self.bande+[""]
        self.curseur.indice += 1


    def complement_a_deux(self):
        self.curseur=c.Curseur("E0",self.bande[self.curseur.indice])
        while self.curseur.etat!="Fin":
            self.update()

    def multiplier(self):
        self.curseur=c.Curseur("M0",self.bande[self.curseur.indice])
        while self.curseur.etat!="Fin":
            self.update()

e=Machine([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
f=Machine([0,1,0,0,1,1,0,1])
# e.complement_a_deux()
# print(e.bande)
f.multiplier()
print(f.bande)
