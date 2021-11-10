# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:43:18 2021
@author: mariu
"""


import re

score1 = []
score2 = []

class flervalgsspørsmål:
    
    def __init__(self, spm, rkt, mlg):
        self.tekst = spm
        self.alternativ = mlg
        self.riktig_svar = rkt
    
    def sjekk_svar(self, gjett1, gjett2):
        #Sjekker hva det korrekte svaret er
        sammenlign = self.korrekt_svar_tekst()
        print("Det riktige svaret er index", sammenlign, ":", self.alternativ[sammenlign - 1])
        if gjett1 == sammenlign and gjett2 == sammenlign:
            score1.append(1)
            score2.append(1)
            return "Begge hadde rett"
        elif gjett1 == sammenlign and gjett2 != sammenlign:
            score1.append(1)
            return "Spiller 1: Riktig \nSpiller 2: Feil"
        elif gjett1 != sammenlign and gjett2 == sammenlign:
            score2.append(1)
            return "Spiller 1: Feil \nSpiller2: Riktig"
        else:
            print("Gjett1:", gjett1)
            print("Gjett2:", gjett2)
            return "Begge hadde feil"

    def korrekt_svar_tekst(self):
        #legger til 1 for bedre brukervennlighet v
        return int(self.riktig_svar) + 1
    
    def __str__(self):
        return f"{self.tekst} \nAlternativene dine er {self.alternativ}"

#rekkefølgen spillet spilles
def spillrekkefølge(objekt):
    #Printer "__str__" v
    print(objekt)
    gjett1 = int(input("\nHvilket tror du er riktig? (Spiller 1) "))
    gjett2 = int(input("\nHvilket tror du er riktig? (Spiller 2) "))
    #Sammenligner med svaret
    print(objekt.sjekk_svar(gjett1, gjett2))
    pass

def seFil():
    spill_scenarioer = []
    with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as fil:
        for row in fil:
            new_list = re.split(":", row)
            spm = new_list[0]
            rkt = new_list[1].replace(" ", "")
            
            #newlist[2] er en streng
            a = new_list[2].replace("[", "")
            a = a.replace("]", "")
            a = a.replace("\n","")
            a = a.replace(" ", "")
            mlg = a.split(",")
            
            #Liste med alle spill objekter v
            spill_scenarioer.append(flervalgsspørsmål(spm, rkt, mlg))
    return spill_scenarioer

if __name__ == "__main__":
    quizliste = seFil()
    for i in quizliste:
        spillrekkefølge(i)
    print("Spiller 1 score:", len(score1))
    print("Spiller 2 score:", len(score2))