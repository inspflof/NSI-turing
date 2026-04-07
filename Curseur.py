class Curseur():
    def __init__(self,etat=None,lettre="", indice=0):
        self.etat=etat
        self.lettre=lettre
        self.indice = indice
        self.tables = {"E0":{("E0",1):["E0",0,"->"],
                          ("E0",0):["E0",1,"->"],
                          ("E0",""):["E1","","<-"]},
                    "E1":{("E1",0):["Fin",1,"-"],
                          ("E1",1):["E1",0,"<-"],
                          ("E1",""):["Fin","","-"]}}
        self.deplacements = {"->": 1,
                                "<-": -1,
                                "-":0}
    

    def renvoyer_table(self):
        if self.etat == "Fin":
            return "Stop"
        else:
            return self.tables[self.etat]