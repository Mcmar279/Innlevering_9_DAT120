# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:43:18 2021
@author: mariu
"""


import re

spørsmål = []
mulige_svar = []
riktig_svar = []
spill_scenarioer = []
score1 = []
score2 = []

class flervalgsspørsmål:
    
    def __init__(self, spm, rkt, mlg):
        self.tekst = spm
        self.alternativ = mlg
        self.spiller1_score = 0
        self.spiller2_score = 0
    
    def sjekk_svar(self, gjett1, gjett2):
        #Sjekker hva det korrekte svaret er
        sammenlign = self.korrekt_svar_tekst()
        print("Det riktige svaret er index", sammenlign)
        if gjett1 == sammenlign and gjett2 == sammenlign:
#            self.spiller1_score += 1
#            self.spiller2_score += 1
            score1.append(1)
            score2.append(1)
            return "Begge hadde rett"
        elif gjett1 == sammenlign and gjett2 != sammenlign:
#            self.spiller1_score += 1
            score1.append(1)
            # self.spiller2_score += 0
            return "Spiller 1: Riktig \nSpiller 2: Feil"
        elif gjett1 != sammenlign and gjett2 == sammenlign:
            # self.spiller1_score += 0
#            self.spiller2_score += 1
            score2.append(1)
            return "Spiller 1: Feil \nSpiller2: Riktig"
        else:
            print("Gjett1:", gjett1)
            print("Gjett2:", gjett2)
            return "Begge hadde feil"

    def korrekt_svar_tekst(self):
        #legger til 1 for bedre brukervennlighet
        return int(rkt) + 1
    
    def __str__(self):
        return f"{self.tekst} \nAlternativene dine er {self.alternativ}"

#rekkefølgen spillet spilles
def spillrekkefølge():
    #Printer "__str__"
    print(flervalgsspørsmål(spm, rkt, mlg))
    gjett1 = int(input("\nHvilket tror du er riktig? (Spiller 1) "))
    gjett2 = int(input("\nHvilket tror du er riktig? (Spiller 2) "))
    #Sammenligner med svaret
    print(flervalgsspørsmål(spm, rkt, mlg).sjekk_svar(gjett1, gjett2))
    pass

with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as fil:
    for row in fil:
        new_list = re.split(":", row)
        spørsmål.append(new_list[0])
        spm = new_list[0]
        rkt = new_list[1].replace(" ", "")
        mlg = new_list[2].strip()
        #Liste med alle spill objekter
        spill_scenarioer.append(flervalgsspørsmål(spm, rkt, mlg))
        spillrekkefølge()

if __name__ == "__main__":
    spill = flervalgsspørsmål(spm, rkt, mlg)
#    print("Spiller 1 score:", spill.spiller1_score)
#    print("Spiller 2 score:", spill.spiller2_score)
    print("Spiller 1 score:", len(score1))
    print("Spiller 2 score:", len(score2))
    pass