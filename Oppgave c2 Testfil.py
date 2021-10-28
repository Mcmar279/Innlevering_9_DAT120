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

class flervalgsspørsmål:
    
    def __init__(self, spm, rkt, mlg):
        self.tekst = spm
        self.alternativ = mlg
        self.spiller1_score = 0
        self.spiller2_score = 0
    
    def sjekk_svar():
        return True

    def korrekt_svar_tekst(self):
        return int(rkt) + 1
    
    def __str__(self):
        return f"{self.tekst} \nAlternativene dine er {self.alternativ}"


with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as fil:
    for row in fil:
        new_list = re.split(":", row)
        spørsmål.append(new_list[0])
        spm = new_list[0]
        rkt = new_list[1].replace(" ", "")
        mlg = new_list[2].strip()
        spill_scenarioer.append(flervalgsspørsmål(spm, rkt, mlg))
        
if __name__ == "__main__":
#    for i in range(len(spørsmål)):
##        spill = flervalgsspørsmål(spm, rkt, mlg)
##        gjett1 = int(input("\nHvilket tror du er riktig? (Spiller 1) "))
##        gjett1 = gjett1 - 1
##        gjett1 = str(gjett1)
##        gjett2 = int(input("\nHvilket tror du er riktig? (Spiller 2) "))
##        gjett2 = gjett2 - 1
##        gjett2 = str(gjett2)
##        print("Det riktige svaret er:", spill.korrekt_svar_tekst())
#        print(spill.sjekk_svar(gjett1, gjett2))
#        spmNR += 1
#    print("Spiller 1 score:", spill.spiller1_score)
#    print("Spiller 2 score:", spill.spiller2_score)
    print(spill_scenarioer[0])
    pass