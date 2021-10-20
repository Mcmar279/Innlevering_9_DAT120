# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:16:00 2021

@author: mariu
"""

import re

spørsmål = []
mulige_svar = []
riktig_svar = []



with open("C:/Users/mariu/Documents/Git Repository/Innlevering_9_DAT120/sporsmaalsfil.txt", "r", encoding="UTF-8") as fil:
    for row in fil:
        new_list = re.split(":", row)
#        print(new_list)
        spørsmål.append(new_list[0])
        riktig_svar.append(new_list[1].replace(" ",""))
        mulige_svar.append((new_list[2]).strip())
class flervalgsspørsmål():
    
    def sjekk_svar(gjett1, gjett2, spiller1_score, spiller2_score):
        if gjett1 == riktig_svar[spmNR] and gjett2 == riktig_svar[spmNR]:
            spiller1_score += 1
            spiller2_score += 1
            return "Begge hadde rett"
        elif gjett2 == riktig_svar[spmNR] and gjett1 != riktig_svar[spmNR]:
            spiller2_score += 1
            return "Spiller 1: Feil \nSpiller2: Riktig"
        elif gjett1 == riktig_svar[spmNR] and gjett2 != riktig_svar[spmNR]:
            spiller1_score += 1
            return "Spiller 1: Riktig \nSpiller 2: Feil"
        else:
            return "Begge hadde feil"
    
    def korrekt_svar_tekst(self):
        return str(riktig_svar[self])
    
    def __init__(self, spmNR):
        self.tekst = spørsmål[spmNR]
        self.alternativ = mulige_svar[spmNR]
        
    def __str__(self):
        return f"{self.tekst} \nAlternativene dine er {self.alternativ}"

if __name__ == "__main__":
    spmNR = 0
    spiller1_score = 0
    spiller2_score = 0
    for i in range(len(spørsmål)):
        print(flervalgsspørsmål(spmNR))
        gjett1 = str(input("\nHvilket tror du er riktig? (Spiller 1) "))
        gjett2 = str(input("\nHvilket tror du er riktig? (Spiller 2) "))
        print("Det riktige svaret er:", flervalgsspørsmål.korrekt_svar_tekst(spmNR))
        print(flervalgsspørsmål.sjekk_svar(gjett1, gjett2, spiller1_score, spiller2_score))
        spmNR += 1
    print("Spiller 1 score:", spiller1_score)
    print("Spiller 2 score:", spiller2_score)

#for k in range(len(mulige_svar[spmNR])):
#            for element in mulige_svar[spmNR]:
#                print(mulige_svar[spmNR].index(element),":", element)