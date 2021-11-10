# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:39:09 2021

@author: mariu
"""

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
    
    def sjekk_svar(self, gjett, i):
        #Sjekker hva det korrekte svaret er
        sammenlign = self.korrekt_svar_tekst()
        #temporary txt fil
                
        if gjett == sammenlign:
            #i begynner 0,1,2...
            
            #øker poeng til spiller
            
            if i+1 == len(spillere):
                print("---------------------------------------------------")
                print("\nDet riktige svaret er index", sammenlign, ":", self.alternativ[sammenlign - 1], "\n")
                print("---------------------------------------------------")
            else:
                pass
            return True
        else:
            #i begynner 0,1,2...
            if i+1 == len(spillere):
                print("---------------------------------------------------")
                print("\nDet riktige svaret er index", sammenlign, ":", self.alternativ[sammenlign - 1], "\n")
                print("---------------------------------------------------")
            else:
                pass
            return False
        #i begynner 0,1,2...
#        if i+1 == len(spillere):
#                print("Det riktige svaret er index", sammenlign, ":", self.alternativ[sammenlign - 1])
#                
#        else:
#            if gjett == sammenlign:
#                return True
#            else:
#                return False

    def korrekt_svar_tekst(self):
        #legger til 1 for bedre brukervennlighet
        return int(self.riktig_svar) + 1
    
    def __str__(self):
        return f"\n{self.tekst} \nAlternativene dine er {self.alternativ}"

#rekkefølgen spillet spilles
def spillrekkefølge(objekt):
    #Printer "__str__" v
    print(objekt)
    for i in range(len(spillere)):
        
        gjett = int(input(f"Hva gjetter du? ({spillere[i]}) "))
        if objekt.sjekk_svar(gjett, i):
            #øker poeng til spiller
            spillere[i].poeng_setter()
            #riktig_liste.append(spillere[i].navn)
#            print(spillere[i], "hadde rett")
            pass
        else:
            pass    
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

class Spiller:
    def __init__(self, navn_inp, poeng=0):
        self.navn = navn_inp
        self.poengsum = poeng
        
    def poeng_setter(self):
        self.poengsum += 1
        
    def score(self):
        return self.poengsum
    
    def __str__(self):
        return f"{self.navn}"

def objekt_spiller_liste():
    spiller_liste = []
    antall = int(input("Hvor mange spillere vil du ha? "))
    for i in range(antall):
        navn_inp = str(input("Hva heter spilleren? "))
        spiller_liste.append(Spiller(navn_inp))
    return spiller_liste

if __name__ == "__main__":
    quizliste = seFil()
    #spillere er liste med spillerne
    spillere = objekt_spiller_liste()
    for i in quizliste:
        spillrekkefølge(i)
        for k in spillere:
            print("Spilleren", k.navn, "har", k.score(), "poeng")
        print("---------------------------------------------------")
    poenger = []
    vinner = []
    for u in spillere:
        poenger.append(u.score())
        if u.score() == max(poenger):
            vinner.append(u.navn)
    print("\nSpilleren/Spillerne", vinner, "vant med", max(poenger), "poeng")