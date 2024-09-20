import json
import random

class Lokalita:
    def __init__(self):
        self.bobri = [] 
        self.nory = [] 
        self.bobri_v_norach = {} 

    def nacti_bobry(self, soubor):
        with open(soubor, 'r') as f:
            self.bobri = json.load(f)

    def nacti_nory(self, soubor):
        with open(soubor, 'r') as f:
            self.nory = json.load(f)

    def prirad_nory(self):
        if len(self.nory) < len(self.bobri):
            print("Není dostatek nor pro všechny bobry!")
            return
        random.shuffle(self.nory) 
        for bobr in self.bobri:
            nora = self.nory.pop() 
            self.bobri_v_norach[bobr] = nora

    def __str__(self):
        vystup = "Bobři a jejich nory:\n"
        for bobr, nora in self.bobri_v_norach.items():
            vystup += f"{bobr} je v noře {nora}.\n"
        return vystup

bobri_data = ["Bobr A", "Bobr B", "Bobr C"]
nory_data = ["Nora 1", "Nora 2", "Nora 3"]

with open('bobri.json', 'w') as f:
    json.dump(bobri_data, f)

with open('nory.json', 'w') as f:
    json.dump(nory_data, f)

lokalita = Lokalita()

lokalita.nacti_bobry('bobri.json')
lokalita.nacti_nory('nory.json')

lokalita.prirad_nory()

print(lokalita)
