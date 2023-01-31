from atom import *

def getResidue(residueNumber:int, store:list):
    for res in store:
        if res.ResidueNumber == residueNumber:
            return res



class Residue:
    def __init__(self, data:dict, store:list):
        self.ResidueNumber = data["ResidueNumber"]
        self.ResidueName = data["ResidueName"]
        self.Atoms = []

        store.append(self)

    def addAtom(self, atom:Atom):
        self.Atoms.append(atom)
