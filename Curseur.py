class Curseur():
    def __init__(self,etat=None,lettre="", indice=0):
        self.etat=etat
        self.lettre=lettre
        self.indice = indice
        self.tables = {
            "E0":{
                ("E0",1):["E0",0,"->"],
                ("E0",0):["E0",1,"->"],
                ("E0",""):["E2","","<-"]
            },
            "E1":{
                ("E1",0):["Fin",1,"-"],
                ("E1",1):["E1",0,"<-"],
                ("E1",""):["Fin","1","-"]
            },
            "E2":{
                ("E2",0):["Fin",1,"-"],
                ("E2",1):["E1",0,"<-"],
                ("E2",""):["E2","","<-"]
            }
        }
                
        self.deplacements = {"->": 1,
                                "<-": -1,
                                "-":0}
    
    def renvoi_all(self):
        print(self.etat,self.lettre,self.indice)

    def renvoyer_table(self):
        if self.etat == "Fin":
            return "Stop"
        else:
            return self.tables[self.etat]