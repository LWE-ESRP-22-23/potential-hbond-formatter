from residue import *

def findAtom(data:dict, store:list):
    for a in store:
        possible = True
        for test in data:
            if a[test] != data[test]:
                possible = False
                break

        if possible:
            print(a)
            return a

class Atom:
    def __init__(self, data:dict, store:list):
        self.SerialNumber = data["SerialNumber"]
        self.AtomName = data["AtomName"]
        self.AltLocation = data["AltLocation"]
        self.ResidueName = data["ResidueName"]
        self.Chain = data["Chain"]
        self.ResidueNumber = data["ResidueNumber"]
        self.InsertionCode = data["InsertionCode"]
        self.X = data["X"]
        self.Y = data["Y"]
        self.Z = data["Z"]
        self.Occupancy = data["Occupancy"]
        self.TempFactor = data["TempFactor"]
        self.Segment = data["Segment"]
        self.Element = data["Element"]
        self.Charge = data["Charge"]
        self.Residue = data["Residue"]

        store.append(self)

    def setResidue(self, res:Residue):
        self.Residue = res
