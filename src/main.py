# Initialization

from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import request
import atom
import contact
import excel
import read



url = "https://swift.cmbi.umcn.nl/cgi/GenericCGI.py"

# Ask

minDist = float(input("Please enter the minimum HBond distance: "))
minAngle = float(input("Please enter the minimum HBond angle: "))

print("Please select the PDB file:")
pdb_file = filedialog.askopenfilename()

print("Please select the desired save location:")
save_file = asksaveasfile(initialfile = "{loc}_Output.xlsx".format(loc = pdb_file[pdb_file.rindex("/") + 1:pdb_file.rindex(".pdb")]), defaultextension=".xlsx", filetypes=[("Excel","*.xlsx*")]).name
atoms = read.makeAtomsFromPDB(open(pdb_file,"r"))

# Interpret

def isHead(string):
    if string.find("<-->") > -1:
        return True
    else:
        return False


data = request.requestServer(pdb_file).split("\n")
del data[0:8], data[len(data) - 1]

nextExp = []
for i in range(len(data)):
    
    if isHead(data[i]):
        if len(nextExp) > 1:
            excel.addExport(nextExp.copy())
            nextExp.clear()
        elif len(nextExp) > 0:
            nextExp.clear()

        data[i] = data[i].replace("(", " ")
        data[i] = data[i].replace(")", " ")
        split = data[i].split(" ")
        for n in range(len(split) - 1, -1, -1):
            if split[n] == "":
                del split[n]
                continue
            
            hasR = split[n].find("\r")
            if hasR > -1:
                split[n] = split[n].replace("\r", "")
        print(split)

        read.generateDataFromPDB(data[i])

        out = "{0} {1} ({2}) {4}...{6} {7} ({8}) {10}".format(*split)
        nextExp.append(out)
    else:
        if len(nextExp) > 1:
            excel.addExport(nextExp.copy())
            nextExp.clear()
            nextExp.append("")
        
        data[i] = data[i].replace("(", " ")
        data[i] = data[i].replace(")", " ")
        split = data[i].split(" ")
        
        for n in range(len(split) - 1, -1, -1):
            if split[n] == "":
                del split[n]
                continue
            
            hasR = split[n].find("\r")
            if hasR > -1:
                split[n] = split[n].replace("\r", "")
        dist = float(split[3])

        if dist < minDist:
            continue

        nextExp.append(split[3])


excel.save(save_file)

print(f"Formatted HBonds have been saved to {save_file}")