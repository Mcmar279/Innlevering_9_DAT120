# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:16:00 2021

@author: mariu
"""

spørsmål = ["Hvor mange minutt er det i en time?", "Hva er 2+2?"]
mulige_svar = [["1: 15", "2: 30", "3: 45", "4: 60"], ["1: 15", "2: 4", "3: 96", "4: Pi"]]

class flervalgsspørsmål():
    
    def sjekk_svar(gjett):
        
        if spmNR == 0 and gjett == 4:
            return "Det er riktig"
        elif spmNR == 1 and gjett == 2:
            return "Det er riktig"
        else:
            return "Det er feil"
                
    
    def __init__(self, spmNR):
        self.tekst = spørsmål[spmNR]
        self.alternativ = mulige_svar[spmNR]
        
    def __str__(self):
        return f"{self.tekst} \nAlternativene dine er {self.alternativ}"

if __name__ == "__main__":
    spmNR = 0
    for i in range(2):
        print(flervalgsspørsmål(spmNR))
        gjett = int(input("\nHvilket tror du er riktig? "))
        print(flervalgsspørsmål.sjekk_svar(gjett))
        spmNR += 1