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
            },
            "M0":{
                ("M0",1):["M0",1,"->"],
                ("M0",0):["M0",0,"->"],
                ("M0",""):["M0",0,"-"]
            },
            "A_start": {
                ("A_start", 0):["A_start", 0, "->"],
                ("A_start", 1):["A_start", 1, "->"],
                ("A_start", "+"):["A_start", "+", "->"],
                ("A_start", ""):["A0", "=", "<-"]

            },
            "A0": {
                ("A0", 0):["A0R2", "", "<-"],
                ("A0", 1):["A0R2", "", "<-"],
                ("A0", "+"):["AC", "", "->"],
                ("A0", ""):["AC", "", "->"]
            },
            "A0R2": {
                ("A0R2", 0): ["A_back0", 0, "->"],
                ("A0R2", 1): ["A_back1", 1, "->"],
                ("A0R2", "+"): ["A_back0", 0, "->"],
                ("A0R2", ""): ["A_back0", 0, "->"]
            },
            "A_back0": {
                ("A_back0", "X"): ["A0", 0, "<-"]
            },
            "A_back1": {
                ("A_back1", "X"): ["A0", 1, "<-"]
            },
            "A1": {
                ("A1", 0): ["A1R2", "X", "<-"],
                ("A1", 1): ["A1R2", "X", "<-"],
                ("A1", "+"): ["A_back1", 1, "->"],
                ("A1", ""): ["A_back1", 1, "->"]
            },
            "A1R2": {
                ("A1R2", 0): ["A_back1", 1, "->"],  # 0+0+1
                ("A1R2", 1): ["A_back0", 0, "->"],  # 1+1+1
                ("A1R2", "+"): ["A_back1", 1, "->"],
                ("A1R2", ""): ["A_back1", 1, "->"]
            },
            "AC": {
                ("AC", "X"): ["AC", "", "->"],
                ("AC", "+"): ["AC", "", "->"],
                ("AC", "="): ["Fin", "", "-"]
            }
        },
                
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