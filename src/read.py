from tkinter import filedialog
from atom import *
from residue import *

def generateDataFromPDB(s:str):
    data = {
        "RecordName": "",
        "SerialNumber": 0,
        "AtomName": "",
        "AltLocation": "",
        "ResidueName": "",
        "Chain": "",
        "ResidueNumber": 0,
        "InsertionCode": "",
        "X": 0.0,
        "Y": 0.0,
        "Z": 0.0,
        "Occupancy": 0.0,
        "TempFactor": 0.0,
        "Segment": "",
        "Element": "",
        "Charge": "",
    }

    data["RecordName"] = s[0:6].strip() or ""
    data["SerialNumber"] = int(s[6:11].strip()) or ""
    data["AtomName"] = s[12:16].strip() or ""
    data["AltLocation"] = s[16].strip() or ""
    data["ResidueName"] = s[17:20].strip() or ""
    data["Chain"] = s[21].strip() or ""
    data["ResidueNumber"] = int(s[22:26].strip()) or ""
    data["InsertionCode"] = s[26].strip() or ""
    data["X"] = float(s[30:38].strip()) or ""
    data["Y"] = float(s[38:46].strip()) or ""
    data["Z"] = float(s[46:54].strip()) or ""
    data["Occupancy"] = float(s[54:60].strip()) or ""
    data["TempFactor"] = float(s[60:66].strip()) or ""
    data["Segment"] = s[72:76].strip() or ""
    data["Element"] = s[76:78].strip() or ""
    data["Charge"] = s[78:80].strip() or ""

    return data

def generateDataFromServer(s:str):
    data = {
        "SerialNumber": 0,
        "AtomName": "",
        "AltLocation": "",
        "ResidueName": "",
        "Chain": "",
        "ResidueNumber": 0,
        "InsertionCode": "",
        "X": 0.0,
        "Y": 0.0,
        "Z": 0.0,
        "Occupancy": 0.0,
        "TempFactor": 0.0,
        "Segment": "",
        "Element": "",
        "Charge": "",
    }

    data["SerialNumber"] = int(s[6:11].strip()) or ""
    data["AtomName"] = s[12:16].strip() or ""
    data["AltLocation"] = s[16].strip() or ""
    data["ResidueName"] = s[17:20].strip() or ""
    data["Chain"] = s[21].strip() or ""
    data["ResidueNumber"] = int(s[22:26].strip()) or ""
    data["InsertionCode"] = s[26].strip() or ""
    data["X"] = float(s[30:38].strip()) or ""
    data["Y"] = float(s[38:46].strip()) or ""
    data["Z"] = float(s[46:54].strip()) or ""
    data["Occupancy"] = float(s[54:60].strip()) or ""
    data["TempFactor"] = float(s[60:66].strip()) or ""
    data["Segment"] = s[72:76].strip() or ""
    data["Element"] = s[76:78].strip() or ""
    data["Charge"] = s[78:80].strip() or ""

    return data

def makeAtomsFromPDB(pdb:str, atomList:list=list(), residueList:list=list()):
    split = pdb.split("\n")
    for s in split:
        
        if s[0:4] != "ATOM":
            continue
        data = generateDataFromPDB(s)
        print(data)
        

        r = getResidue(a.ResidueNumber) or Residue(
            {
                "ResidueNumber" : data["ResidueNumber"],
                "ResidueName" : data["ResidueName"]
        }, residueList)
        data["Residue"] = r
        a = Atom(data, atomList)
        r.addAtom(a)

    return atomList, residueList

        

if __name__ == "__main__":
    ls = list()
    makeAtomsFromPDB(open(filedialog.askopenfilename(),'r').read())
    #print(ls)